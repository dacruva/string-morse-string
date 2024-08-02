MORSE_CODE_DICT = {  # Use all-caps for constants
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', ' ': '/'
}

# Reverse the dictionary for decoding
MORSE_CODE_REVERSE_DICT = {value: key for key, value in MORSE_CODE_DICT.items()}


def string_to_morse(text):
    return "".join(MORSE_CODE_DICT.get(char, '') for char in text.upper())  # Concise conversion


def morse_to_string(morse):
    return "".join(MORSE_CODE_REVERSE_DICT.get(code, '') for code in morse.split())


def main():
    while True:
        choice = input("Encode or Decode Morse Code (Type e to encode / d to decode / q to quit: ")

        if choice == 'e':
            text = input("Type your message to be coded: ")
            coded_message = string_to_morse(text)
            print(f"Message coded: {coded_message}")
        elif choice == 'd':
            morse = input("Type your morse code to decode: ")
            decoded_message = morse_to_string(morse)
            print(f"Message decoded: {decoded_message}")
        elif choice == 'q':
            break
        else:
            print("Invalid option, Please enter 'e', 'd' or 'q' ")


if __name__ == "__main__":
    main()
