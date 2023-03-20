import os

from gtts import gTTS
# from playsound import playsound

# 경로를 .py파일의 실행경로로 이동, 현재 경로로 이동
os.chdir(os.path.dirname(os.path.abspath(__file__)))

file_path = '나의_텍스트.txt'
with open(file_path, 'rt', encoding='UTF-8') as f:
    read_file = f.read()

text = "안녕하세요. 파이썬과 40개의 작품들 입니다."

tts = gTTS(text=read_file, lang='ko')
tts.save("myText.mp3")

# It seems that cannot play sound at cloud env.
# playsound("myText.mp3")
