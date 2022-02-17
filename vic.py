from wand.image import Image
from wand.drawing import Drawing
from os import system as cmd
if input('want to download slowed reverb png? y/n') == 'y':
    cmd('mkdir ~/.cache/vic')
    cmd('curl https://raw.githubusercontent.com/JustCoww/videoimagecreator/main/slowedreverb.png -o ~/.cache/vic/slowedreverb.png')
cover = input('Insert the cover image location: ')
song_name = input("What's the song name? ")
cover = Image(filename = cover)
cover.convert('png')

# Background
bg = cover.clone()
bg.level(0.1, 10, gamma = 5)
bg.blur(sigma = 6)
bg.resize(7680, 4320)
# Cover
cv = cover.clone()
cv.resize(2500, 2500)

# Text
draw = Drawing()
draw.font = '~/.cache/vic/fonts/Roboto-Bold.ttf'
draw.font_size = 139
draw.text(bg.width / 2, bg.height / 2, song_name )
draw(bg)

# Thumbnail
thumb = bg.clone()
thumb.resize(1920, 1080)
thumb.composite(cv, gravity = 'center')
thumb.save(filename = 'thumb.png')

# Video image
video = bg.clone()
video.composite(cv, left = 2591, top = 659)
video.save(filename = 'video.png')
