from narator.convertor import concat_audio_fragments, clean_audio, convert_to_mp3

chapters = [
    open('550.wav', 'rb').read(),
    open('551.wav', 'rb').read(),
    open('552.wav', 'rb').read(),
]

start = chapters[0]

for chapter in chapters[1:]:
    start = concat_audio_fragments(start, chapter, 1000)

cleaned_result = clean_audio(start)

mp3_result = convert_to_mp3(cleaned_result)

with open('538-549.mp3', 'wb') as result_file:
    result_file.write(cleaned_result)

