import string_html as st

def __main__():
    source_code = st.get_html_code("https://de.wikipedia.org/wiki/Basler_AG")
    p_texte = []
    while source_code != "":
        p_text, source_code = st.p_to_p(source_code)
        p_text = st.del_scribt(p_text)
        p_texte.append(p_text)
    
    for tx in p_texte:
        tx = st.str_replace(tx,"\xc3\xa4", "ae")
        tx = st.str_replace(tx,"\xc3\xbc", "ue")
        tx = st.str_replace(tx,"\xc3\xb6", "oe")
        tx = st.str_replace(tx,"\n", "<br>")
        print(str(tx))
    
__main__()
