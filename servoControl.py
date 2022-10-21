import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

pinky_pin = 8;
ring_pin = 10;
middle_pin = 12;
pointer_pin = 16;
thumb_pin = 18;

#setup finger pins as outputs
GPIO.setup(pinky_pin, GPIO.OUT)
GPIO.setup(ring_pin, GPIO.OUT)
GPIO.setup(middle_pin, GPIO.OUT)
GPIO.setup(pointer_pin, GPIO.OUT)
GPIO.setup(thumb_pin, GPIO.OUT)

#50Hz PWM 
pwm_pinky = GPIO.PWM(pinky_pin, 50)
pwm_ring = GPIO.PWM(ring_pin, 50)
pwm_middle = GPIO.PWM(middle_pin, 50)
pwm_pointer = GPIO.PWM(pointer_pin, 50)
pwm_thumb = GPIO.PWM(thumb_pin, 50)

#start
pwm_pinky.start(0);
pwm_ring.start(0);
pwm_middle.start(0);
pwm_pointer.start(0);
pwm_thumb.start(0);

# pwm_**.ChangeDutyCycle(x) 
# x = 5, -90 deg (left)
# x = 7.5, 0 deg (middle)
#x = 10, 90 deg (right)

# assuming fingers up/open = 5% duty
# and fingers down/closed = 10% duty

def init_():
    setRestPosition();


def setRestPosition():
    pwm_pinky.ChangeDutyCycle(5)
    pwm_ring.ChangeDutyCycle(5)
    pwm_middle.ChangeDutyCycle(5)
    pwm_pointer.ChangeDutyCycle(5)
    pwm_thumb.ChangeDutyCycle(5)

#all closed
def setFistPosition():
    pwm_pinky.ChangeDutyCycle(10)
    pwm_ring.ChangeDutyCycle(10)
    pwm_middle.ChangeDutyCycle(10)
    pwm_pointer.ChangeDutyCycle(10)
    pwm_thumb.ChangeDutyCycle(10)

def exec_loop():
    setRestPosition()
    time.sleep(2.5)
    setFistPosition()
    time.sleep(2.5)


def main():
    print("starting up")
    setRestPosition() #start all fingers at rest
    
    while True:
        exec_loop()

if __name__ == "__main__":
    main()