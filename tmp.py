import os
from slugify import slugify

s = 'Very / Unsafe / file\nname hähä \n\r'
clean_basename = slugify(s)
# clean_extension = slugify(os.path.splitext(s)[1][1:])
# if clean_extension:
#     clean_filename = '{}.{}'.format(clean_basename, clean_extension)
# elif clean_basename:
#     clean_filename = clean_basename
# else:
#     clean_filename = 'none' # only unclean characters
#
print(clean_basename)