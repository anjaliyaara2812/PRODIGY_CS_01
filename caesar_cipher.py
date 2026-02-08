def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


print("Caesar Cipher Program")
message = input("Enter your message: ")
shift = int(input("Enter shift value: "))

encrypted_text = encrypt(message, shift)
print("Encrypted Text:", encrypted_text)

decrypted_text = decrypt(encrypted_text, shift)
print("Decrypted Text:", decrypted_text)
