def get_num_words(text):
    words = text.split()
    return len(words)

def get_count_chars(text):
    counter = {}
    for word in text:
        string = word.lower()
        for char in string:
            if char not in counter:
                counter[char] = 1
            else:
                counter[char] += 1
    return counter

def sort_on(items):
    return items["num"]

def get_sorted_report(dict):
    list = []

    for key in dict:
        if key.isalpha():
            list.append({"char": key, "num": dict[key]})
        
    list.sort(reverse=True, key=sort_on)

    return list
