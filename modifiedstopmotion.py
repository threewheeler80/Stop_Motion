#importing the necessary modules
from datetime import datetime
from gpiozero import Button, LED
from picamera import PiCamera
from time import sleep
from signal import pause

imagebutton = Button(23)
red = LED(17)
previewbutton = Button(24)
white = LED(27)
videobutton = Button(25)
blue = LED(22)
camera = PiCamera()
running = True
camera.resolution = (1024, 768)#use this to set the resolution
white.source = previewbutton.values
red.source = imagebutton.values
blue.source = videobutton.values
previewbutton.when_pressed = camera.start_preview
previewbutton.when_released = camera.stop_preview
timestamp = datetime.now()

def picture():
    camera.capture('pic'+str(timestamp)+'.jpg')
sleep(2) #give the camera two seconds
imagebutton.when_pressed = picture #execute the picture function

def video():
    camera.start_recording('vid'+str(timestamp)+'.h264')
    camera.wait_recording(15)
    camera.stop_recording
sleep(2)
videobutton.when_pressed = video #execute the video function

try:
    while running:
        print('Active') #displaying 'Active' to the shell
        sleep(1)

#we detect Ctrl+C then quit the program
except KeyboardInterrupt:
    camera.stop_preview()
    running = False

pause()#keep the script alive
