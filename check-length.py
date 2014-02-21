from mutagen.mp3 import MP3

audio = MP3("test-data/MakingFriends_Episode11_Janice.mp3")
len = audio.info.length
print int(round(len))
