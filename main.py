def main():
    path = 'books/frankenstein.txt'
    text = get_book_text(path)
    numb = word_count(text)
    chardict = char_dict(text)
    charlist = sorted_list(chardict)
    print(f'------------------------------------------------------')
    print(f'                    wow much nice')
    print(f'------------------------------------------------------')
    print(f'There is {numb} words in this book')
    print(f'------------------------------------------------------')
    for item in charlist:
        print(f"Char {item['key']} was found {item['num']} times")
    print(f'------------------------------------------------------')
    
def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_count(text):
    words = text.split()
    word_c = 0
    for word in words:
        word_c += 1
    return word_c

def lower_casing(text):
    my_text_lower = text.lower()
    return my_text_lower

def char_dict(text):
    chars = {}
    for char in text:
        low = char.lower()
        if low.isalpha():
            if low in chars:
                chars[low] += 1
            else:
                chars[low] = 1
    return chars
    
    
def sort(k):
    return k['num']

def sorted_list(chars):
    sorted = []
    for c in chars:
        sorted.append({'key':c,'num':chars[c]})
    sorted.sort(reverse=True,key=sort)
    return sorted

            
    
    






main()