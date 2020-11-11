from picamera import PiCamera, Color
from time import sleep

camera = PiCamera()
camera.rotation = 180
camera.resolution = (2592, 1944)
camera.framerate = 15

camera.start_preview(alpha=150)
camera.annotate_text_size = 60
camera.annotate_background = Color('blue')
camera.annotate_foreground = Color('yellow')

# Try different brightness settings
#for i in range(100):
#    camera.annotate_text = "Brightness: %s" % i
#    camera.brightness = i
#    sleep(0.1)

# Try different contrast settings
#for i in range(100):
#    camera.annotate_text = "Contrast: %s" % i
#    camera.contrast = i
#    sleep(0.1)

# Try different camera effects
#for effect in camera.IMAGE_EFFECTS:
#    camera.image_effect = effect
#    camera.annotate_text = "Effect: %s" % effect
#    sleep(5)

# Try different exposure modes
#for mode in camera.EXPOSURE_MODES:
#    camera.exposure_mode = mode
#    camera.annotate_text = "Exposure mode: %s" % mode
#    sleep(5)

# Try different white balances
#for white in camera.AWB_MODES:
#    camera.awb_mode = white
#    camera.annotate_text = "White balance: %s" % white
#    sleep(5)

camera.image_effect = 'none'
camera.exposure_mode = 'auto'
camera.awb_mode = 'auto'
camera.annotate_text = "Hello world!"

for i in range(3):
    sleep(2)
    camera.capture('/home/rich/Pictures/image%s.jpg' % i)

camera.resolution = (1920, 1080)
camera.framerate = 30
camera.start_recording('/home/rich/Pictures/video.h264')
camera.wait_recording(15)
camera.stop_recording()

camera.stop_preview()