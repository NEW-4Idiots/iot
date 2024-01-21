import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522


GPIO.setmode(GPIO.BOARD)


reader = SimpleMFRC522()

try:
    print("카드를 리더기에 태그하세요.")
    while True:

        id, text = reader.read()
        print("카드 ID: {}".format(id))
        print("텍스트: {}".format(text))
finally:

    GPIO.cleanup()