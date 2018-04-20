# Wikipedia band name generator

Use the only truly scientific way to generate bandnames and first album titles.

Draws a random wikipedia article and uses the title as the band name. The first album name is choosen as the last 4 words of a random Aristotle quote.

# Installation
```shell
git clone https://github.com/emiljoha/band_name_generator.git
virtualenv --python=python3 band_name_generator
cd band_name_generator
. bin/activate
pip install -r requirements.py
```
# Usage
Navigate to installation directory band_name_generator and execute:
```shell
. bin/activate
```
if virtual enviroment not already on then to generate a band name and album name:
```shell
python band_name_generator.py
```
Behold endless source of band names and titles for your first album