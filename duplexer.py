import os
import sys

from pypdf import PdfReader, PdfWriter
from pypdf.errors import PdfReadError

def main():
    filenames = sys.argv[1:]

    if len(filenames) == 0:
        print('duplexer: no files specified')

    readers = []

    for filename in filenames:
        if not os.path.isfile(filename):
            print(f'duplexer: file "{filename}" does not exist.')
            sys.exit(1)

        try:
            readers.append(PdfReader(filename))
        except PdfReadError:
            print(f'duplexer: unable to read "{filename}" as pdf.')
            sys.exit(1)

    (first, second) = duplex(readers)

    filename_combined = ':'.join([os.path.splitext(filename)[0] for filename in filenames])
    filename_first = f'print first, {filename_combined}.pdf'
    filename_second = f'print second, {filename_combined}.pdf'

    with open(filename_first, 'wb') as file:
        first.write(file)
        print(f'duplexer: wrote "{filename_first}".')
    with open(filename_second, 'wb') as file:
        second.write(file)
        print(f'duplexer: wrote "{filename_second}".')

    sys.exit(0)


def duplex(readers : [PdfReader]):
    merger = PdfWriter()

    for reader in readers:
        merger.append_pages_from_reader(reader)

    reader = merger
    num_pages = len(reader.pages)

    if num_pages < 2:
        print('duplexer: pdf does not need duplexing.')
        sys.exit(0)

    first = PdfWriter()
    second = PdfWriter()

    odd_pages = reader.pages[0::2]
    even_pages = reader.pages[1::2]

    for page in odd_pages:
        first.add_page(page)

    if num_pages % 2 != 0:
        last_page = even_pages[-1]
        width = last_page.mediabox.width
        height = last_page.mediabox.height

        second.add_blank_page(width, height)

    for page in reversed(even_pages):
        second.add_page(page)

    return first, second


if __name__ == "__main__":
    main()