from PIL import Image

image = Image.new("RGB",(500,500),(255,255,255))
im = image.load()
(width, height) = image.size

for i in range(0, width):
    for j in range(0, height):
        color = (i+j)*255//(width+height)
        im[i,j] = (0,0,color)

image.save("pix.jpg")