def read_word_list(file_path):
    """
    Reads a text file and returns a list of words.
    """
    with open(file_path, encoding='utf-8') as file:
        word_list = [word.strip() for word in file.readlines()]
    return word_list

if __name__ == '__main__':
    word_list = read_word_list('ordlista')
    print(f"Number of words in list: {len(word_list)}")
    print(f"First word: {word_list[0]}")
    print(f"Length of first word: {len(word_list[0])}")
