import logging
import subprocess
from tempfile import NamedTemporaryFile
from concurrent.futures import ThreadPoolExecutor, wait

from pydub import AudioSegment

logger = logging.getLogger(__name__)


def _to_segment(audio_data: bytes, format_: str = 'wav') -> AudioSegment:
    with NamedTemporaryFile('w+b', suffix=f'.{format_}') as t_wav:
        t_wav.write(audio_data)
        return AudioSegment.from_file(t_wav.name, format=format_)


def _from_segment(segment: AudioSegment, format_: str = 'wav', **kwargs) -> bytes:
    with NamedTemporaryFile('w+b', suffix='.wav') as t_wav:
        segment.export(t_wav.name, format=format_, **kwargs)
        return t_wav.read()


def convert_to_mp3(data: bytes) -> bytes:
    segment = _to_segment(data)
    return _from_segment(segment, format_='mp3')


def convert_to_wav(file: bytes, bitrate: str = '16k') -> bytes:
    """
    The ffmpeg command arguments used:

        -y overwrites the output file if it already exists.
        -hide_banner hides ffmpeg banner output
        -i specifies the input file, in this case source.name.
        -vn disables video recording, meaning only the audio will be processed.
        -ar sets the audio sampling rate to 44100 Hz.
        -ac sets the number of audio channels to 1.
        -ab sets the audio bitrate to 16k (16 kilobits per second).
        -f specifies the output format, in this case wav.

    """
    if bitrate is None:
        bitrate_cmd = []
    else:
        bitrate_cmd = ['-ab', bitrate]
    with (
        NamedTemporaryFile('w+b') as source,
        NamedTemporaryFile('w+b', suffix='.wav') as result,
    ):
        source.write(file)
        source.flush()
        command = [
            'ffmpeg',
            '-hide_banner',
            '-y',
            '-i',
            source.name,
            '-vn',
            '-ar',
            '44100',
            '-ac',
            '1',
            *bitrate_cmd,
            '-f',
            'wav',
            result.name,
        ]
        try:
            command_result = subprocess.run(
                command,
                check=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            if command_result.stderr:
                logger.error('Error while converting file to wav, details: %s', command_result.stderr)
                raise Exception(f"Can't convert file to wav, details: {command_result.stderr}")
        except subprocess.CalledProcessError as e:
            logger.error('Error while converting file to wav, details: %s', e.stderr)
            raise Exception(f"Can't convert file to wav, details: {e.stderr}")
        return result.read()


def concat_audio_fragments(*fragments: bytes, delay: int = 0, format_: str = 'wav') -> bytes:
    if len(fragments) == 1:
        return fragments[0]
    result = _to_segment(fragments[0], format_=format_)
    for fragment in fragments[1:]:
        result = result.append(
            AudioSegment.silent(duration=delay, frame_rate=result.frame_rate),
            crossfade=0,
        )
        result = result.append(_to_segment(fragment, format_=format_), crossfade=0)
    return _from_segment(result, format_=format_)


def apply_filters(wav_bytes):
    with (
        NamedTemporaryFile(suffix='.wav') as temp_audio_file,
        NamedTemporaryFile(suffix='.wav') as adjusted_audio,
    ):
        temp_audio_file.write(wav_bytes)

        filters = [
            'compand=points=-80/-105|-62/-80|-15.4/-15.4|0/-12|20/-7.6:soft-knee=6',
            'loudnorm=I=-16:LRA=11:TP=-2.5',
            # 'highpass=f=200',
            # 'lowpass=f=3000',
            # 'bass=frequency=100:gain=-50',
            # 'anlmdn=s=7:p=0.002:r=0.002:m=15:o=o',
            # 'bandreject=frequency=200:width_type=h:width=200',
            # 'volume=volume=2',
        ]

        ffmpeg_command = [
            'ffmpeg',
            '-y',
            '-i',
            temp_audio_file.name,
            '-af',
            ','.join(filters),
            '-f',
            'wav',
            adjusted_audio.name,
        ]

        try:
            command_result = subprocess.run(
                ffmpeg_command,
                check=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            if command_result.returncode != 0:
                logger.error('Error while converting file to wav, details: %s', command_result.stderr)
                raise Exception(f"Can't convert file to wav, details: {command_result.stderr}")
        except subprocess.CalledProcessError as e:
            logger.error('Error while converting file to wav, details: %s', e.stderr)
            raise Exception(f"Can't convert file to wav, details: {e.stderr}")
        return adjusted_audio.read()


def apply_filters_multithreaded(wav_bytes: list[bytes]) -> list[bytes]:
    return _do_in_parallel(apply_filters, wav_bytes)


def convert_to_mp3_multithreaded(wav_bytes: list[bytes]) -> list[bytes]:
    return _do_in_parallel(convert_to_mp3, wav_bytes)


def _do_in_parallel(func, data, threads=10):
    def _run(item, position):
        return func(item), position

    result = []
    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = []
        for i, wav in enumerate(data):
            futures.append(executor.submit(_run, wav, i))
        done, not_done = wait(futures)
        if not_done:
            raise Exception(f'Filed to execute {func}.')
        for future in done:
            result.append(future.result())
    sorted_result = sorted(result, key=lambda x: x[1])
    return [s[0] for s in sorted_result]


def modify_mp3_metadata(mp3_bytes: bytes, title: str, artist: str, cover: bytes) -> bytes:
    # TODO: change segments to direct ffmpeg command Command:['ffmpeg', '-y', '-f', 'wav', '-i', '/tmp/tmphkezski9', '-i', '/tmp/tmpjr7gztak.jpg', '-map', '0', '-map', '1', '-c:v', 'mjpeg', '-c', 'copy', '-metadata', 'title=376 - 380', '-metadata', 'artist=Lord of the Mysteries (Web Novel)', '-metadata', 'album=Lord of the Mysteries (Web Novel)',
    # '-id3v2_version', '4', '-f', 'mp3', '/tmp/tmp8yqnvf4y'] using '-c copy' parameter to skip unnecesary encoding
    with NamedTemporaryFile(suffix='.jpg') as cover_file:
        cover_file.write(cover)

        segment = _to_segment(mp3_bytes, format_='mp3')
        return _from_segment(
            segment,
            format_='mp3',
            tags={
                'title': title,
                'artist': artist,
                'album': artist,
            },
            cover=cover_file.name,
        )
