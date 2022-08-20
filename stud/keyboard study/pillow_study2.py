from PIL import Image

image = Image.open("sample1.png")

im = image.load()

(width, height) = image.size

for i in range(0,width):
    if(im[i,i] != (255,255,255)):
        color = im[i,i]

for i in range(0,width):
    for j in range(0,height):
        if(im[i,j] != (255,255,255) and im[i,j] != color):
            im[i,j] = (255-color[0],255-color[1],255-color[2])

image.save("result.jpg")