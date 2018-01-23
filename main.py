import string_html as st
import word_to_txt as w_to_txt
site_link = "https://de.wikipedia.org/wiki/Basler_AG"
def __main__():
    source_code = st.get_html_code(site_link)
    all_sentences = []
    all_words = []
    while source_code != "":
        p_text, source_code = st.p_to_p(source_code)
        #print("p-p")
        p_text = st.del_in_script(p_text)
        #print("del")
        p_text = st.replace_script(p_text)
        #print(p_text)
        #print("\n")
        if p_text != "":
            sentences_in_p = st.find_sentence(p_text)
            for sentence in sentences_in_p:
                all_sentences.append(sentence)
            #print("done")
    #print(all_sentences)
    print("=====================================================")
    for tx in all_sentences:
        print(tx)
    print("=====================================================")
    
    for sentence in all_sentences:
        words = []
        words, sentence_state = st.sentence_in_words(sentence)
        if sentence_state == 1:
            all_words.append(words)
    for word_sentence in all_words:
        print(word_sentence)
        w_to_txt.word_in_txt(word_sentence)
    
    
__main__()
