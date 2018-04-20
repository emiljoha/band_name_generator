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

print('Band name: %s' % wiki.random(1).title())
quote = wikiquotes.random_quote(author='Aristotle', raw_language="english")
album_name = quote.split(' ')[-4:]
album_name = ' '.join(album_name)
print('First Album: %s' % album_name)
