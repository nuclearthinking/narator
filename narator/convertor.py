import logging
import subprocess
from tempfile import NamedTemporaryFile

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
        NamedTemporaryFile('r+b') as result,
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
            '-ab',
            '16k',
            '-f',
            'mp3',
            result.name,
        ]
        try:
            command_result = subprocess.run(command, check=True)
            if command_result.stderr:
                logger.error('Error while converting file to mp3, details: %s', result.stderr)
                raise Exception(f"Can't convert file to mp3, details: {result.stderr}")
        except subprocess.CalledProcessError as e:
            logger.error('Error while converting file to mp3, details: %s', e.stderr)
            raise Exception(f"Can't convert file to mp3, details: {e.stderr}")
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
        NamedTemporaryFile('r+b') as result,
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
            command_result = subprocess.run(command, check=True)
            if command_result.stderr:
                logger.error('Error while converting file to wav, details: %s', result.stderr)
                raise Exception(f"Can't convert file to wav, details: {result.stderr}")
        except subprocess.CalledProcessError as e:
            logger.error('Error while converting file to wav, details: %s', e.stderr)
            raise Exception(f"Can't convert file to wav, details: {e.stderr}")
        return result.read()


def concat_audio_fragments(first_fragment: bytes, second_fragment: bytes, delay: int = 500) -> None:
    """ffmpeg -i input1.wav -filter_complex "[0:a]adelay=1000|1000[out1];[1:a]adelay=1000|1000[out2];[out1][out2]concat=n=2:v=0:a=1[a]" -map "[a]" output.wav"""
    with (
        NamedTemporaryFile('w+b', suffix='.wav') as source1,
        NamedTemporaryFile('w+b', suffix='.wav') as source2,
        NamedTemporaryFile('r+b', suffix='.wav') as result,
    ):
        source1.write(first_fragment)
        source2.write(second_fragment)

        command = [
            'ffmpeg',
            f'-i {source1.name}',
            f'-i {source2.name}',
            '-filter_complex',
            f'"[0:a]adelay={delay}|{delay}[out1];[1:a]adelay={delay}|{delay}[out2];[out1][out2]concat=n=2:v=0:a=1[a]"',
            '-map',
            '[a]',
            result.name,
        ]
        try:
            command_result = subprocess.run(command, check=True)
            if command_result.stderr:
                logger.error('Error while converting file to wav, details: %s', result.stderr)
                raise Exception(f"Can't convert file to wav, details: {result.stderr}")
        except subprocess.CalledProcessError as e:
            logger.error('Error while converting file to wav, details: %s', e.stderr)
            raise Exception(f"Can't convert file to wav, details: {e.stderr}")
        return result.read()
