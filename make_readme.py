import os
from glob import glob

result = [y for x in os.walk(os.path.dirname(os.path.realpath(__file__))) for y in glob(os.path.join(x[0], '*.pdf'))]

with open('readme.md', 'w') as readme:
    readme.write(
        '<h3>PDF Books</h3>\n'
    )
    for path in result:
        book_name = os.path.basename(path)
        book_name_url = book_name.replace(' ', '%20')
        book_name = book_name.replace('.pdf', '')

        base_dir = os.path.join(os.path.basename(os.path.dirname(path)), os.path.basename(path))
        base_dir = ''.join(base_dir[0:base_dir.find('/')])
        readme.write(
            '<li><a href=\'https://github.com/asynchroza/books/blob/main/{}/{})\'>{}</a> - {}</li>\n'.format(base_dir, book_name_url, book_name, base_dir)
        )

    readme.close()
