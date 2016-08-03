import zxing
from PIL import Image
import picamera

#only have to set up reader once
reader = zxing.BarCodeReader("/home/pi/Documents/zxing/zxing")

#to input filname directly
#filename = raw_input("Please type full file path: ")
#barcode = reader.decode(filename)


#to take picture from RaPi
camera = picamera.PiCamera()
filename = "test_01.jpg"
camera.capture(filename)
ctr = 0

while(ctr < 20):
    barcode = reader.decode(filename)
    if barcode is not None:
        print("decoded: "+barcode.data)
        print("points: "+str(barcode.points).strip("[]"))
        print(ctr)
        break
    else:
        ctr += 1
if ctr == 20:
    print("data matrix not found")


#barcode = reader.decode(filename)
#print(barcode)

#if barcode is not None:
#    print("decoded: "+barcode.data)
#    print("points: "+str(barcode.points).strip("[]"))
#else:
#    print("data matrix not found")
