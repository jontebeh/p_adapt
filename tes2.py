from urllib.request import urlopen
#import cgi

file = open("test.txt", "w")
def get_html_code(source_link):
    response = urlopen(source_link)
    page_source = response.read()
    return str(page_source)
code = str(get_html_code("https://de.wikipedia.org/wiki/Basler_AG"))
#code = cgi.escape(code, quote=False)
#code = code.rstrip()
code = code.replace('\\n', 'jo')
file.write(code)
file.close()
#print(code.index("\n"))