# pip install SpeechRecognition
# Pip install PyAudio

import speech_recognition as sr

# 마이크로 부터 음성 듣기
r=sr.Recognizer() #객체 만들기
with sr.Microphone() as source:
  print("듣고 있어요.") # 약간의 지연이 발생 될 수 있어 이 문장 출력 후에 말하면 됨.
  audio=r.listen(source=source) #마이크로 부터 음성 듣기

# 파일로부터 음성 파일 불러오기 (wav, aiff, flac 가능) mp3는 불가
# r=sr.Recognizer()
# with sr.AudioFile("sample.wav") as source:
#   audio=r.record(source=source)

# 아래 작업은 똑 같음

try:
  # 구글 API로 인식(하루 50회 제한)
  # 영어 문장
  # text=r.recognize_google(audio_data=audio,language="en-US")
  # print(text) # hello 테스트 잘 처리됨

  # 한글 문장
  text=r.recognize_google(audio_data=audio,language="ko")
  print(text) # hello 테스트 잘 처리됨
  # pass


except sr.UnknownValueError:
  print("인식 실패") # 음성인식 실패한 경우
except sr.RequestError as e:
  print("요청 실패 : {0}".format(e)) # API Key 오류, 네트워크 단절 등
