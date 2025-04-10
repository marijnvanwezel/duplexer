# duplexer

Super simple Python utility to manually prepare PDF files for duplex printing.

## Prerequisites

The following software should be installed on your system:

- [Python 3](https://www.python.org/)
- [pypdf](https://pypdf.readthedocs.io/en/stable/)

## Installation

Follow the steps below to install `duplexer`:

1. Clone this repository and navigate to it:
   ```commandline
   git clone https://github.com/marijnvanwezel/duplexer.git
   cd duplexer
   ```
2. Make the Python script executable:
   ```commandline
   chmod +x duplexer.py
   ```
3. Move the script into `/usr/local/bin`:
   ```commandline
   mv duplexer.py /usr/local/bin/duplexer
   ```

## Usage

To use the utility, follow the steps below:

1. Invoke the utility with one or more filenames, like so:
   ```commandline 
   duplexer my_pdf1.pdf my_pdf2.pdf my_pdf3.pdf
   ```
2. Print the PDF `first.pdf`;
3. Go to your printer;
4. Reinsert the pages, and (depending on the model of your printer), flip the pages;
5. Go back to your computer;
6. Print the PDF `second.pdf`.
