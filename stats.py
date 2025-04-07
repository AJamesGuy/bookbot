def get_book_text(fpath):
    with open(fpath) as f:
        content = f.read()
    return content

def count_words(content):
    count = 0
    words = content.split()
    for word in words:
        count += 1
    return count

def count_symbols(content):
    counts = {}
    for symbol in content:
        if symbol == symbol.upper():
            symbol = symbol.lower()
        if symbol not in counts:
            counts[symbol] = 1
        else:
            counts[symbol] += 1
    return counts

def custom_sort(counts):
    for k in counts:
        return counts[k]

def sorted_counts(counts):
    count_list = []
    for k, v in counts.items():
        if k.isalpha() != True:
            continue
        count_list.append({k : v})
    count_list.sort(reverse=True, key=custom_sort)    
    return count_list