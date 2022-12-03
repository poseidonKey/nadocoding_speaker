# pip install gTTS
# pip install playsound==1.2.2

from gtts import gTTS
from playsound import playsound

# 영어의 경우
# text="Imagine that you have just arrived at a hotel after a tiring 7-hour overnight flight."
# file_name="sample.mp3"
# tts_en=gTTS(text=text,lang="en")
# tts_en.save(file_name)
# playsound(sound=file_name)

# 한글문장
# text="파이썬을 배우면 이런 것도 할 수 있어요."
# file_name="sample_ko.mp3"
# tts_en=gTTS(text=text,lang="ko")
# tts_en.save(file_name)

# playsound(sound=file_name)

with open("sample.txt", "r", encoding="utf8") as f:
    text = f.read()

file_name = "sample_ko_file.mp3"
tts_en = gTTS(text=text, lang="ko", slow=False) # slow 세부 변화 없음.
# 아래 사이트 참고
# https://scribblinganything.tistory.com/522?category=918711
tts_en.save(file_name)

playsound(sound=file_name)
