import wikipedia as wiki
import wikiquotes

print('Band name: %s' % wiki.random(1).title())
quote = wikiquotes.random_quote(author='Aristotle', raw_language="english")
album_name = quote.split(' ')[-4:]
album_name = ' '.join(album_name)
print('First Album: %s' % album_name)
