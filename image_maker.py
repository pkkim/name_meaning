from hashlib import sha256
from os.path import isfile
from PIL import (Image,
                 ImageFont,
                 ImageDraw)


class ImageMaker:

    # image constants
    IMG_TEMPLATE = 'static/images/nameplate.png'
    IMG_FORMAT = 'static/images/cached/{}.png'
    size = (800, 600)
    name_1_center = (276, 168)
    name_2_center = (533, 168)
    name_size = 32
    name_font = ImageFont.truetype("static/fonts/Impact.ttf", name_size)
    meaning_1_center = (276, 450)
    meaning_2_center = (533, 450)
    meaning_size = 32
    meaning_font = ImageFont.truetype("static/fonts/Impact.ttf", meaning_size)
    text_color = '#131576'
    _debug = True

    @classmethod
    def get_image(cls, name, meaning):
        hashkey = name + meaning
        hashed = sha256(hashkey).hexdigest()
        filename = cls.IMG_FORMAT.format(hashed)
        if (not cls._debug) and isfile(filename):
            return filename, hashed
        else:
            return cls._make_image(name, meaning, filename), hashed

    @classmethod
    def _make_image(cls, name, meaning, dest):
        name_split = len(name) / 2
        name_1, name_2 = name[:name_split], name[name_split:]

        meaning_1, meaning_2 = meaning.split('_')

        name_texts = [
            (name_1, cls.name_1_center, cls.name_size),
            (name_2, cls.name_2_center, cls.name_size),
        ]
        meaning_texts = [
            (meaning_1, cls.meaning_1_center, cls.meaning_size),
            (meaning_2, cls.meaning_2_center, cls.meaning_size),
        ]

        img = Image.open(cls.IMG_TEMPLATE)
        draw = ImageDraw.Draw(img)

        for text in name_texts:
            text_width, text_height = draw.textsize(text[0], font=cls.name_font)
            text_pos = (text[1][0] - text_width / 2,
                        text[1][1] - text_height / 2)

            draw.text(text_pos, text[0], font=cls.name_font, fill=cls.text_color)
        for text in meaning_texts:
            text_width, text_height = draw.textsize(text[0], font=cls.meaning_font)
            text_pos = (text[1][0] - text_width / 2,
                        text[1][1] - text_height / 2)

            draw.text(text_pos, text[0], font=cls.meaning_font, fill=cls.text_color)
        img.save(dest)
        return dest
