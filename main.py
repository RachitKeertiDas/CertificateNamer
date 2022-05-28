import math
import csv
from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color

print("Hello World")


people = [
    {"name":"John Doe","position":"First"}
    ,{"name":"Ronald Roe","position":"Second"}
]

cert_file = 'Participation.jpg'
cert_font = 'URW Chancery L'
font_size = 40


for person in people:
    with Image(filename=cert_file) as image:
        draw=Drawing()

        draw.font_family= cert_font
        draw.font_size= font_size
        draw.stroke_color=Color('black')
        draw.text(x=(870-math.floor(len(person["name"])*8)),y=416,body=person["name"])
        draw.draw(image)
        image.format="png"

        image.save(filename=person["name"]+person["position"]+".png")

