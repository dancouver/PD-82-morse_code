# create dictionary for morse code
# encode = {"A": ".-", ...... }
encode = {"A": ".-",
          "B": "-...",
          "C": "-.-.",
          "D": "-..",
          "E": ".",
          "F": "..-.",
          "G": "--.",
          "H": "....",
          "I": "..",
          "J": ".---",
          "K": "-.-",
          "L": ".-..",
          "M": "--",
          "N": "-.",
          "O": "---",
          "P": ".--.",
          "Q": "--.-",
          "R": ".-.",
          "S": "...",
          "T": "-",
          "U": "..-",
          "V": "...-",
          "W": ".--",
          "X": "-..-",
          "Y": "-.--",
          "Z": "--..",
          "0": "-----",
          "1": ".----",
          "2": "..---",
          "3": "...--",
          "4": "....-",
          "5": ".....",
          "6": "-....",
          "7": "--...",
          "8": "---..",
          "9": "----."}
# convert the name
carry_on = True
while carry_on:
    input_name = input("Enter the name: ").upper()
    output_name = ""
    invalid_name = False
    # go through each letter
    for letter in input_name:
        if letter in encode:
            output_name += encode[letter]  # convert the letter and add to the output
        else:
            invalid_name = True
        if invalid_name:
            print("Invalid input")
            # stop the encoding
            break
    if not invalid_name:
        # only print decoded names with all valid characters
        print(output_name)

    carry_on = input("Do you want to continue? (y/n) ").upper() == "Y"
