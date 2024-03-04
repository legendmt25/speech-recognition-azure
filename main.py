import speech_recognition
from speech_recognition import AudioData
from pyfirmata import Arduino, SERVO
from time import sleep
import env

recognizer = speech_recognition.Recognizer()
microphone = speech_recognition.Microphone(device_index=1)

def getCommand(audio: AudioData) -> tuple[str, float]:
  return recognizer.recognize_azure(audio, key=env.AZURE_SPEECH_RECOGNITION_KEY, location=env.AZURE_SPEECH_RECOGNITION_LOCATION);

port = "COM6"
servoPin = 10
board = Arduino(port)

board.digital[servoPin].mode = SERVO

def handleLightsOn() -> None:
  print("Lights are on")
  for i in range(0, 45):
    rotate(servoPin, i)

allCommands = {
  'lights on': handleLightsOn
}

def rotate(pin: int, angle: int):
  board.digital[pin].write(angle)
  sleep(0.015)

with microphone as source:
  recognizer.adjust_for_ambient_noise(source)

  print("Say something")

  while True:
    audio = recognizer.listen(source)
    
    command = getCommand(audio)
    
    try:
      for definedCommand, handler in allCommands.items():
        if definedCommand in command[0].lower():
          handler()
          continue
      
      print("UNKNOWN COMMAND: " + command)
    except:
      print("Except: Error happened.")