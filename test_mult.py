import zxing
from PIL import Image

reader = zxing.BarCodeReader("/Users/wanlinxie/Documents/projects/aisleNet/zxing")

#s = 80, 6/10, i= s/2
#s = 70, 3/10, i= s/2
#s = 70, 9/10, i= s/3
#s = 70, 8/10, i = s/4

def main():
    filename = "mult_1"
    im = Image.open(filename+".png")
    lst = []

    #print("uncropped image decode: ")
    #decode(filename)

    ctr = 1
    side=70
    x=side/2
    while(x < 639): #camera.resolution[0]
        y=side/2
        while(y < 359): #camera.resolution[1]
            box = (x-side/2,y-side/2,x+side/2,y+side/2)
            region = im.crop(box)
            region.save(filename+"_crop"+".png","PNG")
            tmp = decode(filename+"_crop") #tmp is barcode object or None
            if tmp is not None:
                lst.append(tmp.data)
                region.save(filename+"_crop"+str(ctr)+".png","PNG")
                ctr += 1
            y += side/4
        x += side/4
            
    
    print(lst)
 

def decode(name):
    barcode = reader.decode(name+".png")
    if barcode is not None:
        print("decoded: "+barcode.data)
        print("points: "+str(barcode.points).strip("[]"))
    return barcode

main()
