from caesar_cipher.is_english_word import count_words
# from is_english_word import count_words

def encrypt(plaintext, shift):
    encrypted_text = ""


    number_of_characters = 26

    for char in plaintext:
        if char.isalpha():
            base_code = ord('a') if char.islower() else ord('A')
            current_code = ord(char)
            current_position = current_code - base_code
         
            shifted_position = (current_position + shift) % number_of_characters
            shifted_char = base_code + shifted_position
            encrypted_text += chr(shifted_char)
        else:
            encrypted_text += char
    return encrypted_text


def decrypt(encoded, shift):
    return encrypt(encoded, -shift)

def crack(encoded):
    for shift in range(26):
        plaintext = decrypt(encoded, shift)
        word_count = len(plaintext.split())
        if count_words(plaintext) == word_count:
            return plaintext

    return ''


if __name__ == "__main__":
    cipher = encrypt("Is this wOrKINg. AYO 28? Testing", 7)
    print(cipher)
    print (decrypt(cipher, 7))
    crack(cipher)