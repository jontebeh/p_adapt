from urllib.request import urlopen

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

def del_scribt(p_to_p_text):
    while True:
        try:
            begin_index = p_to_p_text.index('<')
            end_index = p_to_p_text.index('>')
            p_to_p_text = p_to_p_text[:begin_index] + p_to_p_text[end_index + 1:]
        except:
            break
    return p_to_p_text

def str_replace(main_str, search_for, replace_with):
    new_str = ""
    while True:
        try:
            search_index = main_str.index(search_for)
            new_str = new_str + main_str[:search_index] + replace_with
            main_str = main_str[search_index + len(search_for):]
        except:
            new_str += main_str
            break
    return new_str