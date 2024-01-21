import RPi.GPIO as GPIO
import time


fsr_pin = 17

def setup():

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(fsr_pin, GPIO.IN)

def detect_pressure():

    if GPIO.input(fsr_pin) == GPIO.HIGH:
        print("압력이 감지되었습니다.")
    else:
        print("압력이 감지되지 않았습니다.")

def cleanup():

    GPIO.cleanup()

setup()

try:
    while True:
        detect_pressure()
        time.sleep(1)
except KeyboardInterrupt:
    print("프로그램을 종료합니다.")
finally:
    cleanup()
