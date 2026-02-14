def count_words(words):
    words_list=words.split()
    count=len(words_list)
    return count

def count_characters(words):
    words=words.lower()
    words_count={}
    for ch in words:
        if ch in words_count:
            words_count[ch]+=1;
        else:
            words_count[ch]=1;
    return words_count

def sort_on(store):
    return store["num"]

def sort_dictionary(store):
    sorted_list=[]
    for ch in store:
        sorted_list.append({"char": ch, "num": store[ch]})
    sorted_list.sort(reverse=True,key=sort_on)
    return sorted_list