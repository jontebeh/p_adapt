
def create_change_list_by_txt():
    file = open("change_list.txt", "r")
    text = file.read()
    lines = []
    result = [('\\n','')]
    sub_result = ("","")
    while True:
        try:
            line_end = text.index("\n")
            lines.append(text[:line_end])
            text = text[line_end+1:]
        except:
            break
    
    for line in lines:
        space = line.index(" => ")
        word1 = line[:space]
        word2 = line[space+4:]
        sub_result = (word1, word2)
        result.append(sub_result)
    return result