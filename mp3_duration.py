from mutagen.mp3 import MP3


def mp3_duration(mp3File):
    audio = MP3(mp3File)
    return audio.info.length
