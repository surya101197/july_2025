from gtts import gTTS

file=open("recent123.txt",mode='r')
reader=file.read()
Text_To_Speech_tts=gTTS(reader)
Text_To_Speech_tts.save("recent123.mp3")
file.close()