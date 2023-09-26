import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setup(dac, GPIO.OUT, initial=GPIO.HIGH)
pwm = GPIO.PWM(24, 1000)
pwm.start(0)
try:
    while True:
        dutycycle = int(input())
        pwm.ChangeDutyCycle(dutycycle)
        print("{:.2f}".format(dutycycle * 3.3 / 100))
finally:
    GPIO.output(24, 0)
    GPIO.output(dac, 0)
    GPIO.cleanup()