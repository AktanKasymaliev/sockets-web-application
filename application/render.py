import io

def render_to_string(htmlfile):
    directory = "templates/" + htmlfile
    with io.open(directory, encoding='utf-8') as html:
        txt = html.read()
    return str(txt)
