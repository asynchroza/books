import os
from glob import glob
from dotenv import load_dotenv
from socket import gethostname
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

load_dotenv()

def send_book_to_mail(path_to_book):

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(os.getenv('EMAIL'), os.getenv('PASSWORD'))
    msg = MIMEMultipart()

    msg['Subject'] = 'Book'
    msg['From'] = os.getenv('EMAIL')
    msg['To'] = os.getenv('TO')
    with open(path_to_book, "rb") as f:
        attach = MIMEApplication(f.read(),_subtype="pdf")
        attach.add_header('Content-Disposition','attachment',filename=str(path_to_book))
        msg.attach(attach)
        server.send_message(msg)
        print('A book has been sent - path: {}\n'.format(path_to_book))


def write_in_readme():
    result = [y for x in os.walk(os.path.dirname(os.path.realpath(__file__))) for y in glob(os.path.join(x[0], '*.pdf'))]

    with open('readme.md', 'w') as readme:
        readme.write(
            '<h3>PDF Books</h3>\n'
        )
        for path in result:
            send_book_to_mail(path)
            book_name = os.path.basename(path)
            book_name_url = book_name.replace(' ', '%20')
            book_name = book_name.replace('.pdf', '')

            base_dir = os.path.join(os.path.basename(os.path.dirname(path)), os.path.basename(path))
            base_dir = ''.join(base_dir[0:base_dir.find('/')])
            readme.write(
                '<li><a href=\'https://github.com/asynchroza/books/blob/main/{}/{})\'>{}</a> - {}</li>\n'.format(base_dir, book_name_url, book_name, base_dir)
            )

        readme.close()

if __name__ == '__main__':
    write_in_readme()