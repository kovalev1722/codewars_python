def encode(st):
    global vowels
    for key in vowels:
        st = st.replace(key, vowels.get(key))
    return st
    
def decode(st):
    global vowels
    keys = list(vowels.keys())
    print(keys)
    for value in vowels.values():
        st = st.replace(value, keys[int(value) - 1])
    return st

vowels = {'a': '1',
          'e': '2',
          'i': '3',
          'o': '4', 
          'u': '5', 
          'y': '6'}

print(encode('hx2sf6lgczp2c4llfxlfhpj'))

def good_encode(s, t=str.maketrans("aeiou", "12345")):
    return s.translate(t)
    
def good_decode(s, t=str.maketrans("12345", "aeiou")):
    return s.translate(t)