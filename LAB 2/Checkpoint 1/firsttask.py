def decrypt_caesar(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():  # check if the character is an alphabet
            shifted = ord(char) - shift
            if char.islower():
                if shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted < ord('A'):
                    shifted += 26
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char
    return decrypted_text

def main():
    # Given ciphertext
    ciphertext = "odroboewscdrolocdcwkbdmyxdbkmdzvkdpybwyeddrobo"

    # Perform brute force decryption by trying all possible shifts
    for shift in range(26):
        decrypted_text = decrypt_caesar(ciphertext, shift)
        print(f"Shift {shift}: {decrypted_text}")

if __name__ == "__main__":
    main()