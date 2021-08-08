# importing the necessary classes from modules
from gpiozero import Button, LED
from picamera import PiCamera
from datetime import datetime
from signal import pause
from time import sleep


camera = PiCamera()  # create object and initializing itself
sleep(2)  # allow camera time to adjust
camera.resolution = (1024, 768)  # set camera resolution(width, height)
camera.image_effect = "film"
timestamp = datetime.now()

imagebutton = Button(23)
red = LED(17)
red.source = imagebutton.values

previewbutton = Button(24)
previewbutton.when_pressed = camera.start_preview
previewbutton.when_released = camera.stop_preview
white = LED(27)
white.source = previewbutton.values

videobutton = Button(25)
blue = LED(22)
blue.source = videobutton.values


def capture():
    image_file_name = "/home/pi/Pictures"+ str(timestamp) + ".jpg"
    camera.capture(image_file_name)  # capture is a function
    sleep(2)
    print("Done")  # visual cue picture has been taken

imagebutton.when_pressed = capture

def video():
    video_file_name = "/home/pi/Video"+ str(timestamp) + ".h264"
    print("Start recording...")  # visual cue video started
    camera.start_recording(video_file_name)
    camera.wait_recording(15)  # continue recording for amount of seconds
    camera.stop_recording()
    print("Done recording")  # visual cue video stopped

videobutton.when_pressed = video

try:
    while True:
        print('Active')  # visually see that script is jogging
        sleep(1)

except KeyboardInterrupt:  # CTRL + C stop the script
    quit()

pause()  # looping the scripting
