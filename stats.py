import sys
def get_num_words(text):
    list_of_words = text.split()
    num_words = len(list_of_words)
    return f"Found {num_words} total words"

def character_count(text):
    heat_map = {}

    for l in text:
        if not l.isalpha():
            continue
        l = l.lower()
        if l not in heat_map:
            heat_map[l] = 1 
        else :
            heat_map[l] +=1
    
    return heat_map

def get_book_text(name):
    file_content = ""
    with open(name) as f:
         file_content = f.read()
    return file_content



def analyze_book(bkn: str) :
    print(f"""============ BOOKBOT ============
Analyzing book found at {bkn}..."""
    )
    text = get_book_text(bkn)
    print("----------- Word Count ----------")
    print(get_num_words(text))
    print("--------- Character Count -------")
    heat_map = character_count(text)
    for k,v in heat_map.items():
        print(f"{k}: {v}")
    