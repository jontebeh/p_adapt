def str_replace(main_str, search_for, replace_with):
    new_str = ""
    #search_index = -1
    while True:
        try:
            search_index = main_str.index(search_for)
            new_str = new_str + main_str[:search_index] + replace_with
            main_str = main_str[search_index + len(search_for):]
        except:
            new_str += main_str
            break
    return new_str

main_str = input("main ")
search_for = input("search ")
replace_with = input("replace ")
main_str = str_replace(main_str, search_for, replace_with)
print(main_str)