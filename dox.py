import pypandoc
from tidylib import tidy_document

def convertdox(filename):
    out = pypandoc.convert_file(filename, "html")
    out, err = tidy_document(out)

    with open("static/results.html", "w") as f:
        f.write(out)
