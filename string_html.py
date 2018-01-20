from urllib.request import urlopen
import variables as var

def get_html_code(source_link):
    response = urlopen(source_link)
    page_source = response.read()
    return str(page_source)

def p_to_p(source_code):
    try:
        p_index = source_code.index('<p>')
        p_end_index = source_code.index('</p>')
        p_to_p_text = source_code[p_index + 3:p_end_index]
        new_source_code = source_code[p_end_index + 4:]
        return p_to_p_text, new_source_code
    except:
        return "",""

def del_script(p_to_p_text, begin, end):
    while True:
        try:
            begin_index = p_to_p_text.index(begin)
            end_index = p_to_p_text.index(end)
            p_to_p_text = p_to_p_text[:begin_index] + p_to_p_text[end_index + len(begin):]
        except:
            break
    return p_to_p_text

def del_in_script(p_to_p_text):
    for sub_del in var.del_str:
        p_to_p_text = del_script(p_to_p_text, sub_del[0], sub_del[1])
    return p_to_p_text

def replace_script(p_to_p_text):
    for sub_repl in var.replace_str:
        p_to_p_text = p_to_p_text.replace(sub_repl[0], sub_repl[1])
    return p_to_p_text
