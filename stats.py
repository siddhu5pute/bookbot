def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    char_count = {}
    lowered_text = text.lower()
    
    for char in lowered_text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
            
    return char_count

def sort_char_count(char_count):
    char_list = [{"char": char, "num": count} for char, count in char_count.items()]
    char_list.sort(reverse=True, key=lambda d: d["num"])
    return char_list


