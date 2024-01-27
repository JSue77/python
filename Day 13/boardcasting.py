import gtts

#text = "언제나 응원해 화이팅!"
#gtts.gTTS(text, lang= 'ko').save('fighting.mp3')

#text = "I'm always rooting for you! Fighting"
#gtts.gTTS(text, lang='en').save('ff.mp4')


text = input("텍스트 입력:")
gtts.gTTS(text, lang='ko').save('text.mp4')