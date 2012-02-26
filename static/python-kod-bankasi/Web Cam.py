from VideoCapture import Device
import time, string

## Specify the amount of seconds to wait between individual captures.
interval = 2

## If you get horizontal stripes or other errors in the captured picture
## (especially at high resolutions), try setting showVideoWindow=0.
cam = Device(devnum=0, showVideoWindow=1)
#cam = Device(devnum=1, showVideoWindow=1)

## Using the separate programs "setPropertiesDev0/1.pyw" before capturing
## works better for some devices.
## On the other hand, some devices don't remember their state, so the
## properties have to be set at every program start.
cam.displayCapturePinProperties()
#cam.displayCaptureFilterProperties()

print "press 'ctrl + c' to terminate"

i = 0
quant = interval * .1
starttime = time.time()
while 1:
    lasttime = now = int((time.time() - starttime) / interval)
    #print i
    cam.saveSnapshot('C:\\Windows\\Temp\\' + string.zfill(str(i), 4) + '.jpg', timestamp=3, boldfont=1)
    i += 1
    while now == lasttime:
        now = int((time.time() - starttime) / interval)
        time.sleep(quant)
