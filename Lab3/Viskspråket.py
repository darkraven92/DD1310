def to_viskspraket(input_string):
    vowels = "aeiouyåäöAEIOUYÅÄÖ"  # Lista med alla vokaler
    output_string = ""  # Tom sträng för att lagra översättningen
    for char in input_string:
        if char not in vowels:
            output_string += char
    return output_string

  to_viskspraket("Får jag viska ditt namn?")
