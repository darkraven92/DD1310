def to_bebisspråket(text):
    vowels = "aeiouyåäö"
    res = ""
    for word in text.split():
        res += word[:word.find(any(c for c in word.lower() if c in vowels))+1]*3 + " "
    return res.strip()
