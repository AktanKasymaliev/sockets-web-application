
def render_to_string(htmlfile):
    directory = "templates/" + htmlfile
    with open(directory, "r") as html:
        txt = html.read()
    return str(txt)
