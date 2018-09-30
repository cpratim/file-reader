def converttxt(filename):
    html_data = """
    <html>
        <head>
            <title>
            Text File
            </title>
        <head>
        <body>
        <p>
    """
    with open(filename, 'r') as f:
        contents= f.readlines()
    for line in contents:
        html_data += line + '<br>'

    html_data += '</p></body></html>'

    with open('static/results.html', 'w') as f:
        f.write(html_data)
