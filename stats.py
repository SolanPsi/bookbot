def get_num_words(text):
        word_count = text.split()
        return len(word_count)

def get_char_count(character):
	characters = character.lower()
	strings = {}
	for char in characters:
		if char in strings:
			strings[char] += 1
		else:
			strings[char] = 1
	return strings

def sort_on(dict):
    return dict["count"]

def chars_dict_to_sorted_list(char_count_dict):
    chars_list = []
    
    for char, count in char_count_dict.items():
        chars_list.append({"char": char, "count": count})
    
    chars_list.sort(reverse=True, key=sort_on)
    
    return chars_list
