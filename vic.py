#!/usr/bin/python3
def thumbnail(cover):

    from PIL import Image, ImageEnhance, ImageFilter
    from math import trunc

    # Import
    tb = Image.open(cover)
    cv = Image.open(cover)

    # Cover
    x, y = (626, 626)
    cv = cv.resize((x, y), resample=0, box=None)
    
    # Thumb Resize
    X, Y = (1920, 1080)
    tb = tb.resize((X, Y), resample=0, box=None)
    
    # Blur and brightness
    tb = ImageEnhance.Brightness(tb).enhance(0.3)
    tb = tb.filter(ImageFilter.GaussianBlur(6))
    tb = tb.copy()

    # Mix into file
    center = (trunc((X-x)/2), trunc((Y-y)/2))
    tb.paste(cv, center)
    tb.save('thumb.png', quality=95)
    
    return print('Thumbnail image: Done')
    
def video(cover, song, artist):

    from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageFilter
    from math import trunc

    x, y = (2500, 2500) # Cover size
    X, Y = (7680, 4320) # Background size

    # Import cover
    bg = Image.open(cover)
    cv = Image.open(cover)
    # Cover
    cv = cv.resize((x, y), resample=0, box=None)
    # Thumb Resize
    bg = bg.resize((X, Y), resample=0, box=None)
    # Blur and brightness
    bg = ImageEnhance.Brightness(bg).enhance(0.3)
    bg = bg.filter(ImageFilter.GaussianBlur(6))
    bg = bg.copy()
    # Paste cover into the background
    center = (trunc((X-x)/2), trunc((Y-y)/2))
    bg.paste(cv, ( trunc((X-x)/2 ), 659))

    ### Text
    text = ImageDraw.Draw(bg)
    # Fonts
    font_folder = 'fonts/'
    roboto_bold = ImageFont.truetype(font_folder + 'Roboto-Bold.ttf', 279)
    roboto_light = ImageFont.truetype(font_folder + 'Roboto-Light.ttf', 186)
    # Get the size of the final texts
    s_x, x_y = text.textsize(song, font=roboto_bold)
    a_x, a_y = text.textsize(artist, font=roboto_light)
    # Write text in the middle
    text.text(((X-s_x)/2, 3240), song, fill=(255, 255, 255), font=roboto_bold, align='center')
    text.text(((X-a_x)/2, 3640), artist, fill=(255, 255, 255), font=roboto_light, align='center')

    # Export final file
    bg.save('video.png', quality=95)

    return print('Video image: Done')
