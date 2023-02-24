def to_fikonspråket(text):
    res = ""
    for word in text.split():
        if len(word) <= 2:
            res += word + "ikon" + " "
        else:
            res += word[0] + "ikon" + word[2:] + " "
    return res.strip()
