

def word_in_txt(sentence):
    counter = 0
    for word in sentence:
        try:
            file = open("words\\"+str(word+".txt"), "r")
            w_info = file.read()
            file.close()
            w_c = int(w_info[w_info.index('<wc="')+5:w_info.index('"/wc>')])
            s_b = int(w_info[w_info.index('<sb="')+5:w_info.index('"/sb>')])
            s_e = int(w_info[w_info.index('<se="')+5:w_info.index('"/se>')])
            
            n_w = w_info[w_info.index("<nw>"):w_info.index("</nw>")]
            n_w_list = []
            
            while True:
                try:
                    n_w_id = n_w[n_w.index('<id="')+5:n_w.index('"/id>')]
                    n_w_c = int(n_w[n_w.index('<c="')+4:n_w.index('"/c>')])
                    n_w_list.append((n_w_id, n_w_c))
                    n_w = n_w[n_w.index('/c>')+3:]
                except:
                    break
                
            w_c += 1
            if counter == 0:
                s_b+=1
            if counter + 1 == len(sentence):
                s_e += 1
            if counter + 1 < len(sentence):
                found_n_w = False
                for n_w_e in n_w_list:
                    if sentence[counter+1]==n_w_e[0]:
                        n_w_e[1] += 1
                        found_n_w = True
                if found_n_w == False:
                    n_w_list.append((sentence[counter+1],1))
            '''    
            print(w_c)
            print(s_b)
            print(s_e)
            print(n_w_list)
            '''
            end_script = write_word_script(word, w_c, s_b, s_e, n_w_list)
            
        except:
            w_c = 1
            s_b = 0
            s_e = 0
            if counter == 0:
                s_b+=1
            if counter + 1 == len(sentence):
                s_e += 1
            if counter + 1 < len(sentence):
                n_w_list = [(sentence[counter+1],1)]
            end_script = write_word_script(word, w_c, s_b, s_e, n_w_list)
            
        file = open(str("words\\"+word+".txt"), "w+")
        file.write(end_script)
        file.close()
        counter += 1

def write_word_script(word, w_c, s_b, s_e, n_w_list):
    word_script = '<id="'+word+'">\n'
    w_c_sript = '<wc="'+str(w_c)+'"/wc>\n'
    s_b_sript = '<sb="'+str(s_b)+'"/sb>\n'
    s_e_sript = '<se="'+str(s_e)+'"/se>\n'
    n_w_script = '<nw>\n'
    for n_w_e in n_w_list:
        n_w_script += '<id="'+n_w_e[0]+'"/id>\n'
        n_w_script += '<c="'+str(n_w_e[1])+'"/c>\n'
    n_w_script += '</nw>'
    end_script = word_script+w_c_sript+s_b_sript+s_e_sript+n_w_script
    return end_script
