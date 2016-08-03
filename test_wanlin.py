import zxing
from PIL import Image
import picamera

#only have to set up reader once
reader = zxing.BarCodeReader("/home/pi/Documents/zxing/zxing")

#to take picture from RaPi
camera = picamera.PiCamera()
camera.awb_mode = u'auto'
camera.brightness=60
camera.resolution=(320,180)

#other camera properties
#camera.zoom=(0.3,0.3,0.5,0.5)

def main():
    filename = "test_01"
    decode(filename)

def decode(name):
    
    ctr = 1
    r_w=160
    r_h=90
    while(ctr < 6):
        camera.resolution=(r_w*ctr,r_h*ctr)
        print camera.resolution
        camera.capture(name+".png")
        barcode = reader.decode(name+".png")
        if barcode is not None:
            print("decoded: "+barcode.data)
            print("points: "+str(barcode.points).strip("[]"))
            #print(ctr)
            im = Image.open(name+".png")
            #print(camera.resolution[0])
            box = (0,0,camera.resolution[0]-1,camera.resolution[1]-1)
            region = im.crop(box)
            region.save(name+"_crop1"+".png","PNG")
            #print(box)
            print("try detect on cropped image")
            barcode_reg = reader.decode(name+"_crop1"+".png")
            print(barcode_reg)
            break
        else:
            ctr += 1
    if ctr == 6:
        print("data matrix not found")

main()

