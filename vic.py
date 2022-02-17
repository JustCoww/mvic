#!/usr/bin/python3
from wand.image import Image
from wand.drawing import Drawing
from PIL import Image as PImage, ImageDraw as PImageDraw, ImageFont as PImageFont
from os.path import expanduser
from os import system as cmd
from sys import argv as arg
cover = input('Insert the cover image location: ')
song_name = input("What's the song name? ")
artist_name = input("What's the name of the artist? ")
cover = Image(filename = cover)
cover.convert('png')
cache = expanduser('~') + '/.cache/vic/'

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
thumb.composite(cv, gravity = 'center')
thumb.resize(1920, 1080)
thumb.save(filename = 'thumb.png')



##### Text

text_colors = (255, 255, 255)
font_folder = cache + 'fonts/'
W, H = (7680, 317)

# Main Text
text_base = PImage.new(mode = 'RGBA', size = (W, H), color = (255, 0, 0, 0))
text = PImageDraw.Draw(text_base)
font = PImageFont.truetype(str(font_folder + 'Roboto-Bold.ttf'), 279)
w, h = text.textsize(song_name, font=font)
text.text( ((W-w)/2, (H-h)/2) , song_name, fill = text_colors, font=font, align='center')
text_base.save(cache + 'song.png')

# Artist Text
text_base = PImage.new(mode = 'RGBA', size = (W, H), color = (255, 0, 0, 0))
text = PImageDraw.Draw(text_base)
font = PImageFont.truetype(str(font_folder + 'Roboto-Light.ttf'), 186)
w, h = text.textsize(artist_name, font=font)
text.text( ((W-w)/2, (H-h)/2) , artist_name, fill = text_colors, font=font, align='center')
text_base.save(cache + 'artist.png')

#####



# Video image
slowedreverb = Image(filename = cache + 'slowedreverb.png')
video = bg.clone()
text_main = Image(filename = cache + 'song.png')
text_artist = Image(filename = cache + 'artist.png')
video.composite(slowedreverb, gravity = 'center')
video.composite(text_artist, left = 1, top = 3610)
video.composite(text_main, left = 1, top = 3240)
video.composite(cv, left = 2591, top = 659)
video.save(filename = 'video.png')

cmd('rm ~/.cache/vic/artist.png')
cmd('rm ~/.cache/vic/song.png')
