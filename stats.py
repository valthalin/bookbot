def get_num_words(txtdata):
    word_array = txtdata.split()
    return len(word_array)

def get_num_chars(txtdata):
    out_dict = {}
    alpha = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split()
    txtdata = txtdata.lower()
    for char in alpha:
        out_dict[char] = 0

    for character in txtdata:
        if character in alpha:
            out_dict[character] += 1
    
    return out_dict