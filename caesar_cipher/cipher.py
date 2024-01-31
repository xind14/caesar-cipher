from is_english import count_words


def encrypt(plaintext, shift):
    encrypted_text = ""


    number_of_characters = 26
    base_character = "A"

    for char in plaintext:
        base_code = ord(base_character)
        current_code = ord(char)
        current_position = current_code - base_code
        shifted_position = (current_position + shift) % number_of_characters
        shifted_char = base_code + shifted_position
        encrypted_text += chr(shifted_char)

    return encrypted_text


def decrypt(encoded, shift):
    return encrypt(encoded, -shift)


if __name__ == "__main__":
    pins = [
        "AAAA",
        "BBBB",
        "ABCD",
        "ABAB",
    ]

    for i, pin in enumerate(pins):
        shift = i + 1
        print("plain pin", pin)
        print("shift by", shift)
        encrypted_pin = encrypt(pin, shift)
        print("encrypted_pin", encrypted_pin)
        decrypted_pin = decrypt(encrypted_pin, shift)
        print("decrypted_pin", decrypted_pin)
        print()