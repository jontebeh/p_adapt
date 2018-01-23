from urllib.request import urlopen
import create_change_list
import variables as var
var.replace_str = create_change_list.create_change_list_by_txt()

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
            if end_index < begin_index:
                p_to_p_text[end_index] = ""
            p_to_p_text = p_to_p_text[:begin_index] + p_to_p_text[end_index + len(begin):]
            #print(p_to_p_text)
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

def find_sentence(p_to_p_text):
    sentence_list = []
    new_sentence = True
    while True:
        try:
            point_index = p_to_p_text.index(".")
            new_sentence = True
            try:
                double_point_index = p_to_p_text.index(":")
                if double_point_index < point_index:
                    p_to_p_text = p_to_p_text[double_point_index + 1:]
                    new_sentence = False
            except:
                pass
            if new_sentence == True:
                if p_to_p_text[0] == " ":
                    p_to_p_text = p_to_p_text[1:]
                    point_index-=1
                try:
                    int(p_to_p_text[:point_index])
                except:
                    if len(p_to_p_text[:point_index])>10:
                        sentence_list.append(p_to_p_text[:point_index])
                p_to_p_text = p_to_p_text[point_index+1:]
        except:
            return sentence_list
            break
        
def sentence_in_words(sentence):
    words = []
    while True:
        try:
            space_index = sentence.index(" ")
            if space_index == 0:
                sentence[0] = ''
            else:
                word = sentence[:space_index]
                sentence = sentence[space_index+1:]
                words.append(word)
        except:
            words.append(sentence)
            if len(words) < 5:
                return words, 0
            else:
                return words, 1
    
    
    