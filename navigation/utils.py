import string
from django.utils.text import slugify
from transliterate import slugify as t_slugify


def add_slug(title):
    flag = 0
    alph = list(string.ascii_letters)
    alph.append(" ")
    for l in title:
        if l not in alph:
            flag = 1
            break
    if flag == 0:
        return slugify(title)
    else:
        return t_slugify(title)
