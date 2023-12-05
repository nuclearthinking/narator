import logging
import subprocess
from tempfile import NamedTemporaryFile

from pydub import AudioSegment

logger = logging.getLogger(__name__)


def convert_to_mp3(file: bytes) -> bytes:
    """
    The ffmpeg command arguments used:

        -y overwrites the output file if it already exists.
        -i specifies the input file, in this case source.name.
        -vn disables video recording, meaning only the audio will be processed.
        -ar sets the audio sampling rate to 44100 Hz.
        -b:a sets the audio bitrate to 16k (16 kilobits per second).
        -f specifies the output format, in this case mp3.

    """
    with (
        NamedTemporaryFile('w+b') as source,
        NamedTemporaryFile('w+b', suffix='.mp3') as result,
    ):
        source.write(file)
        segment = AudioSegment.from_wav(source.name)
        segment.export(result.name, format='mp3')
        return result.read()


def convert_to_wav(file: bytes) -> bytes:
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
            '-ab',
            '16k',
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


def _to_segment(audio_data: bytes) -> AudioSegment:
    with NamedTemporaryFile('w+b', suffix='.wav') as t_wav:
        t_wav.write(audio_data)
        return AudioSegment.from_wav(t_wav.name)


def _from_segment(segment: AudioSegment) -> bytes:
    with NamedTemporaryFile('w+b', suffix='.wav') as t_wav:
        segment.export(t_wav.name, format='wav')
        return t_wav.read()


def concat_audio_fragments(*fragments: bytes, delay: int = 500) -> bytes:
    if len(fragments) == 1:
        return fragments[0]
    result = _to_segment(fragments[0])
    for fragment in fragments[1:]:
        result = result.append(_to_segment(fragment), delay)
    return _from_segment(result)


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


def modify_mp3_metadata(mp3_bytes, title, artist) -> bytes:
    """
    The ffmpeg command arguments used:

        -y overwrites the output file if it already exists.
        -i specifies the input file, in this case source.name.
        -metadata title="Title",artist="Artist" sets the metadata for the output file.
        -f specifies the output format, in this case mp3.

    :param mp3_bytes:
    :param title:
    :param artist:
    :return: modified mp3 data
    """

    with (
        NamedTemporaryFile(suffix='.mp3') as temp_mp3_file,
        NamedTemporaryFile(suffix='.mp3') as modified_mp3_file,
    ):
        temp_mp3_file.write(mp3_bytes)

        ffmpeg_command = [
            'ffmpeg',
            '-y',
            '-i',
            temp_mp3_file.name,
            '-metadata',
            f'title={title}',
            '-metadata',
            f'artist={artist}',
            '-metadata',
            f'album={artist}',
            '-f',
            'mp3',
            modified_mp3_file.name,
        ]
        try:
            command_result = subprocess.run(
                ffmpeg_command,
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
        return modified_mp3_file.read()


def add_mp3_cover_art(mp3_bytes, cover_bytes) -> bytes:
    with (
        NamedTemporaryFile(suffix='.mp3') as temp_mp3_file,
        NamedTemporaryFile(suffix='.mp3') as modified_mp3_file,
        NamedTemporaryFile(suffix='.jpg') as cover,
    ):
        temp_mp3_file.write(mp3_bytes)
        cover.write(cover_bytes)
        ffmpeg_command = [
            'ffmpeg',
            '-y',
            '-i',
            temp_mp3_file.name,
            '-i',
            cover.name,
            '-c',
            'copy',
            '-map',
            '0',
            '-map',
            '1',
            modified_mp3_file.name,
        ]
        try:
            command_result = subprocess.run(
                ffmpeg_command,
                check=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            if command_result.stderr:
                logger.error('Error while applying cover to mp3, details: %s', command_result.stderr)
                raise Exception(f"Can't apply cover to mp3, details: {command_result.stderr}")
        except subprocess.CalledProcessError as e:
            logger.error('Error while applying cover to mp3, details: %s', e.stderr)
            raise Exception(f"Can't apply cover to mp3, details: {e.stderr}")
        return modified_mp3_file.read()
