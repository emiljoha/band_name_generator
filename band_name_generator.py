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
# You need personal api_key and secret from flickr to use api You need
# to get your own and write a config.py file to get the flickr
# image.
try:
    from config import api_key, secret
    get_album_art = True
except ImportError:
    get_album_art = False
    print('No album art will be downloaded as no api keys are found')

print('Band name: %s' % wiki.random(1).title())
quote = wikiquotes.random_quote(author='Aristotle', raw_language="english")
album_name = quote.split(' ')[-4:]
album_name = ' '.join(album_name)
print('First Album: %s' % album_name)

if get_album_art is True:
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
    print(url)
