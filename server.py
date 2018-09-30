from flask import Flask, render_template, request, send_from_directory, redirect
from random import randint
from xslxtohtml import convertxslx
from txttohtml import converttxt
from dox import convertdox
from werkzeug import secure_filename
from pdftohtml import convertpdf
import os
import urllib.request

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/handlefile', methods=['GET', 'POST'])
def handlefile():
    if request.method == 'POST':
        file = request.files['file']
        name=secure_filename(file.filename)
        file.save(name)
        if name.endswith('xlsx'):
            convertxslx(name)
            os.remove(name)
            return redirect('static/results.html')
        elif name.endswith('docx'):
            convertdox(name)
            os.remove(name)
            return redirect('static/results.html')
        elif name.endswith('txt'):
            converttxt(name)
            os.remove(name)
            return redirect('static/results.html')
        elif name.endswith('pdf'):
            convertpdf(name)
            os.remove(name)
            return redirect('static/results.html')
        return render_template('lsuccess.html')


if __name__ == '__main__':
    try:

        app.run()
    except:
        app.run(port=6969)
