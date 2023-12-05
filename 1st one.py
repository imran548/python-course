# from PIL import Image
# file = "tree.jpg"
# img = Image.open(file)
# bw= img.convert("RGBA")
# bw.show()
# bw.save('tree1.png')

from PIL import Image
# img = Image.open("tree.jpg")
# data = img.getdata()
# print(list(data))
# print(img.size)
# new_img = img.resize((360,240))
# new_img.show()
# new_img.save("resize.jpg")

# width, height =img.size
# new_height = int(height*0.8)
# new_width = int(width*0.8)
# new_resize = img.resize((new_width,new_height))
# new_resize.show()
# new_resize.save("newresize.png")


#Croping in python
# from PIL import Image
# img = Image.open("tree.jpg")
# cropped = img.crop((90,55,300,320))
# cropped.show()
#
# width,hight = img.size
# new_crop_image = img.crop((30,30,width-100,hight-100))
# new_crop_image.show()


#bulk_image_resize
# import os
# images = os.listdir("F:\PYTHON\python with awal vai\image manupulation")
# print(images)
# for image in images:
#     file = Image.open("F:\PYTHON\python with awal vai\image manupulation/"+image)
#     h,w = file.size
#     new_h = int(h*0.8)
#     new_w = int(w*0.8)
#     resize = file.resize((new_w,new_h))
#     resize.save("size/" +image)


#Create random colour
import random
from PIL import Image
# number = random.randint(0,255)
# number1 = random.randint(0,255)
# number2 = random.randint(0,255)
# img = Image.new("RGB",(700,700),(number,number1,number2))
# img.show()

# i= 0
# while i < 100:
#     number = random.randint(0, 255)
#     number1 = random.randint(0, 255)
#     number2 = random.randint(0, 255)
#     img = Image.new("RGB", (700, 700), (number, number1, number2))
#     img.save("size/"+str(i)+'.jpg')
#     i+=1


#Image pasting

# from PIL import Image
# img1 = Image.open("F:\PYTHON\python with awal vai\size/1.jpg")
# img2 = Image.new("RGB", (600,600))
# img1_resize = img1.resize((150,150))
# img2.paste(img1_resize,(225,225))
# img2.show()

#text to image

from PIL import Image, ImageFont, ImageDraw
text = "I am writing"
img =  Image.open("F:\PYTHON\python with awal vai\size/1.jpg")
font = ImageFont.truetype("AmericanChristmas_PERSONAL_USE_ONLY.otf",159)
draw = ImageDraw.Draw(img)
w,h = img.size
draw.text((w-200,h-200),text, font= font, fill="Red")
img.show()




