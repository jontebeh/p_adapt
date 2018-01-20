import string_html as st

def __main__():
    source_code = st.get_html_code("https://de.wikipedia.org/wiki/Basler_AG")
    p_texte = []
    while source_code != "":
        p_text, source_code = st.p_to_p(source_code)
        p_text = st.del_in_script(p_text)
        p_text = st.replace_script(p_text)
        p_texte.append(p_text)
    
    for tx in p_texte:
        print(tx)
    
__main__()
