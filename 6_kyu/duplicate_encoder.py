def duplicate_encode(word):
    update_word = str()
    word = word.lower()
    for char in word:
        if word.count(char) > 1:
            update_word = update_word + ')'
        else:
            update_word = update_word + '('
    return update_word
    
print(duplicate_encode("Success"))
#print(duplicate_encode(")xy!zO wv@IyxQGvnSQzJQRIRuzSHyFdyuS"))
                       #())()((()(())(()((()((((())(()(())(
                       #())()((()())))()()))()))))))()(()))
                       #())()((()())))()()))()))))))()(()))