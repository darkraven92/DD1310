def to_rovarspraket(input_string):
    consonants = "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ"  # Lista med alla konsonanter
    output_string = ""  # Tom sträng för att lagra översättningen
    for char in input_string:
        if char in consonants:
            output_string += char + "o" + char.lower()  # Fördubbla konsonanten och stoppa in 'o'
        else:
            output_string += char
    return output_string

to_rovarspraket("Att vara eller att inte vara")

