def using_brute(text: str):
    words_list = text.split()
    hashtable = dict()
    for i in range(0, len(words_list)):
        word = words_list[i]
        if word not in hashtable:
            hashtable[word] = 0
            for j in range(i, len(words_list)):
                if words_list[j] == word:
                    hashtable[word] += 1
    return hashtable

def using_memo(text: str):
    words_list = text.split()
    hashtable = dict()
    for word in words_list:
        hashtable[word] = hashtable.get(word, 0) + 1
    
    return hashtable

    pass