import os

def convertpdf(filename):

    os.system('pdftohtml {} static/results.html'.format(filename))
