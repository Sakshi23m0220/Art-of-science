def encrypt(plaintext, key):
    ciphertext = ""
    for char in plaintext:
        char = char.lower()  # Convert to lowercase
        if char != ' ':
            index = letter.find(char)
            if index == -1:
                ciphertext += char
            else:
                new_index = (index + key) % 26  # Calculate the new index
                ciphertext += letter[new_index]
        else:
            ciphertext += ' '  # Preserve spaces

    return ciphertext

def decrypt(ciphertext, key):
    return encrypt(ciphertext, -key)  # Decryption is just encryption with a negative key

letter = "abcdefghijklmnopqrstuvwxyz"

print('*** CAESAR CIPHER PROGRAM ***')
print()

user_input = input("Enter 'e' for encryption or 'd' for decryption: ").strip().lower()

if user_input == 'e':
    print('*** ENCRYPT ***')
    key = int(input("Enter key (1 through 26): ").strip())

    # Ask for the text file
    filename = input("Enter the name of the text file (1800 to 1900 words): ")
    try:
        with open('C:\\Users\\rahul\\PycharmProjects\\week1\\Sample.txt') as file:
            text = file.read().strip()
            encrypted_text = encrypt(text, key)
            print("Encrypted text:", encrypted_text)

            # Write encrypted text to a file
            with open("output.txt", "w") as output_file:
                output_file.write(encrypted_text)
    except FileNotFoundError:
        print("File not found.")

elif user_input == 'd':
    print('*** DECRYPT ***')
    key = int(input("Enter key (1 through 26): ").strip())

    # Ask for the text file
    filename = input("Enter the name of the text file (1800 to 1900 words): ")
    try:
        with open(filename, 'r') as file:
            text = file.read().strip()
            decrypted_text = decrypt(text, key)
            print("Decrypted text:", decrypted_text)

            # Write decrypted text to a file
            with open("output.txt", "w") as output_file:
                output_file.write(decrypted_text)
    except FileNotFoundError:
        print("File not found.")

else:
    print("Invalid choice. Please enter 'e' for encryption or 'd' for decryption.")

