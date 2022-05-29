import math
import os
import csv
from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color

print("Starting Printing Certificates")

people = [
    {"name":"John Doe","position":"First"}
    ,{"name":"Ronald Roe","position":"Second"}
]

cert_file = 'Participation.jpg'
cert_font = 'URW Chancery L'
font_size = 40
print_position = False

with open('names.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    people = [row for row in reader]


def process_name(filename):
    #Replace spaces, dot and @
    filename = filename.replace(" ","")
    filename = filename.replace(".","[dot]")
    filename = filename.replace("@","[at]")
    return filename


for person in people:
    with Image(filename=cert_file) as image:
        draw=Drawing()

        draw.font_family = cert_font
        draw.text_alignment = 'center'
        draw.font_size = font_size
        draw.stroke_color = Color('black')
        draw.text(x=870,y=416,body=person["name"])
        if print_position:
            draw.text(x=230,y=236,body=person["position"])
        draw.draw(image)
        image.format = "png"

        image.save(filename=process_name(person["name"]+person["position"])+".png")
