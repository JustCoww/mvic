#!/usr/bin/python3
from wand.image import Image
from wand.drawing import Drawing
from PIL import Image as PImage, ImageDraw as PImageDraw, ImageFont as PImageFont
from os.path import expanduser

# Variables
cover = input('Insert the cover image location: ')
song_name = input("What's the song name? ")
artist_name = input("What's the name of the artist? ")
cover = Image(filename=cover)
cover.convert('png')
folder = expanduser('~') + '/.local/bin/vic/'
text_colors = (255, 255, 255)
font_folder = folder + 'fonts/'
W, H = (7680, 317)

# Background
bg = cover.clone()
bg.level(0.1, 20, gamma = 5)
bg.blur(sigma = 6)
bg.resize(7680, 4320)

# Cover
cv = cover.clone()
cv.resize(2500, 2500)

# Thumbnail
thumb = bg.clone()
thumb.composite(cv, gravity='center')
thumb.resize(1920, 1080)
thumb.save(filename='thumb.png')

# Main Text
text_base = PImage.new(mode='RGBA', size=(W, H), color=(255, 0, 0, 0))
text = PImageDraw.Draw(text_base)
font = PImageFont.truetype(str(font_folder + 'Roboto-Bold.ttf'), 279)
w, h = text.textsize(song_name, font=font)
text.text( ( (W-w)/2, (H-h)/2 ), song_name, fill=text_colors, font=font, align='center')
text_base.save(folder + 'song.png')

# Artist Text
text_base = PImage.new(mode='RGBA', size=(W, H), color=(255, 0, 0, 0))
text = PImageDraw.Draw(text_base)
font = PImageFont.truetype(str(font_folder + 'Roboto-Light.ttf'), 186)
w, h = text.textsize(artist_name, font=font)
text.text( ( (W-w)/2, (H-h)/2 ), artist_name, fill=text_colors, font=font, align='center')
text_base.save(folder + 'artist.png')

# Video image
sr = Image(filename = folder + 'slowedreverb.png')
video = bg.clone()
song = Image(filename = folder + 'song.png')
artist = Image(filename = folder + 'artist.png')
video.composite(sr, gravity='center')
video.composite(cv, left= 2591, top=659)
video.composite(song, left= 1, top=3240)
video.composite(artist, left= 1, top=3610)
video.save(filename='video.png')
