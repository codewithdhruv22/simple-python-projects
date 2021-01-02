#CONVERT PNG TO JPEG IMAGE EASILY

#pip install pillow

from PIL import Image

img = Image.open("car.png")
jpeg_img = img.convert('RGB')
jpeg_img.save("codewithdhurv.jpeg")
