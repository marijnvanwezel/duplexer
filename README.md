# Duplexer

Super simple Python utility to manually prepare PDF files for duplex printing.

## Prerequisites

To use the utility, make sure you have Python 3 and `pypdf` installed.

1. To install Python, follow [these instructions](https://wiki.python.org/moin/BeginnersGuide/Download).
2. To install `pypdf`, type:
   ```commandline
   pip install pypdf
   ```

## Usage

To use the utility, follow the steps below:

1. Invoke the utility with one or more filenames, like so:
   ```commandline 
   python3 duplexer.py my_pdf1.pdf my_pdf2.pdf my_pdf3.pdf
   ```
2. Print the outputted PDF prefixed with `print first`.
3. Go to your printer, reinsert (and possibly flip) the pages it just printed.
4. Print the outputted PDF prefixed with `print second`.
5. Done!
