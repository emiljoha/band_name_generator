# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import wikipedia as wiki
import wikiquotes
import flickrapi
import urllib.request as download
from PIL import Image, ImageDraw, ImageFont
import os
# You need personal api_key and secret from flickr to use api You need
# to get your own and write a config.py file to get the flickr
# image.
from config.secret_config import api_key, secret, domain, port


def get_band_name():
    band_name = wiki.random(1).title()
    return band_name


def get_album_name():
    quote = wikiquotes.random_quote(author='Aristotle', raw_language="english")
    album_name = quote.split(' ')[-4:]
    album_name = ' '.join(album_name)
    return album_name


def get_album_art_url():
    # See if keys to get album art from flick is present
    if api_key == '<api key here>' or secret == '<secret here>':
        print('No album art will be downloaded.')
        print('No api keys found in config.py')
        print('visit https://www.flickr.com/services/api/misc.api_keys.html')
        print('To get keys to insert into config.py')
        return None
    else:
        flickr = flickrapi.FlickrAPI(api_key, secret)
        recent_photos_lxml = flickr.photos.getRecent(per_page=3)
        third_photo_info = recent_photos_lxml[0][2]
        farm = third_photo_info.get('farm')
        server = third_photo_info.get('server')
        photo_id = third_photo_info.get('id')
        photo_secret = third_photo_info.get('secret')
        # https://farm{farm-id}.staticflickr.com/{server-id}/{id}_{secret}.jpg
        url = 'https://farm%s.staticflickr.com/%s/%s_%s.jpg' % (farm,
                                                                server,
                                                                photo_id,
                                                                photo_secret)
        return url


def format_file_name(band_name):
    filename = []
    for c in band_name:
        if c not in {'.', ' ', '(', ')', '\'', '\"', '\`'}:
            filename.append(c)
    filename = ''.join(filename)
    filename = 'albums/%s.JPEG' % filename
    return filename


def create_album(cover_picture_url, band_name, album_name):
    filename = format_file_name(band_name)
    if not os.path.isdir('albums'):
        os.makedirs('albums')
    download.urlretrieve(cover_picture_url, filename=filename)
    img = Image.open(filename)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("fonts/NOVASOLID.ttf", 30)
    band_name_text_size = draw.textsize('By %s' % band_name, font)
    album_name_text_size = draw.textsize(album_name, font)
    band_name_text_pos = (0*img.size[1]/4, 3*img.size[1]/4)
    album_name_text_pos = (0*img.size[1]/4, img.size[1]/4)
    band_name_rectangle = band_name_text_pos + (band_name_text_pos[0] + band_name_text_size[0],
                                                band_name_text_pos[1] + band_name_text_size[1])
    draw.rectangle(list(band_name_rectangle), fill='white', outline=None)
    album_name_rectangle = album_name_text_pos + (album_name_text_pos[0] + album_name_text_size[0],
                                                  album_name_text_pos[1] + album_name_text_size[1])
    draw.rectangle(album_name_rectangle, fill='white', outline=None)
    draw.text(album_name_text_pos, album_name, font=font,
              fill='red')
    draw.text(band_name_text_pos, 'By %s' % band_name,
              font=font, fill='red')
    img.save(filename, "JPEG", quality=300)
    return filename


def get_new_album():
    band_name = get_band_name()
    album_name = get_album_name()
    cover_picture_url = get_album_art_url()
    filename = create_album(cover_picture_url, band_name, album_name)
    url = 'http://%s:%s/%s' % (domain, port, filename)
    return {'band_name': band_name,
            'album_name': album_name,
            'cover_picture_url': cover_picture_url,
            'url': url}


def generate_album():
    band_name = get_band_name()
    album_name = get_album_name()
    print('Band name: %s' % band_name)
    print('First Album: %s' % album_name)
    cover_picture_url = get_album_art_url()
    filename = create_album(cover_picture_url, band_name, album_name)
    # os.system('xdg-open %s' % filename)
    print(filename)


if __name__ == '__main__':
    generate_album()
