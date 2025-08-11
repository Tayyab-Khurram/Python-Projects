def encrypt(msg, key):
    encrypted = []
    for m in msg:
        ascii = ord(m)
        xor = ascii ^ key
        ans = chr(xor)
        encrypted.append(ans)
    return ''.join(encrypted)


def decrypt(msg, key):
    decrypted = []
    for m in msg:
        ascii = ord(m)
        dexor = ascii ^ key
        ans = chr(dexor)
        decrypted.append(ans)
    return ''.join(decrypted)


def getInput():
    while True: 
        print("What do you want to perform?\n1. Encryption\n2. Decryption\n3. Exit")
        try: 
            user_input = int(input("\nEnter your choice [1/2/3]: ")) 
            if user_input in [1, 2, 3]: 
                break 
            else:
                print("\nInvalid choice. Please enter 1, 2, or 3.\n")
        except ValueError: 
            print("\nInvalid Input. Please enter a number.\n")
    return user_input


if __name__ == "__main__":

    while 1:
        
        choice = getInput()
        
        if choice == 1:
            user_string1 = input("Enter your message: ").strip()
            try:
                user_key1 = int(input("Enter the private key [e.g:123]: "))
                result1 = encrypt(user_string1, user_key1)
                print("\nEncrypted Message:",result1,"\n")
            except ValueError:
                print("\nInvalid key!\n")
            
        elif choice == 2:
            user_string2 = input("Enter the encrypted message: ").strip()
            try:
                user_key2 = int(input("Enter the private key used for encryption: "))
                result2 = decrypt(user_string2, user_key2)
                print("\nDecrypted Message:",result2,"\n")
            except ValueError:
                print("\nInvalid key!\n") 
            
        elif choice == 3:
            print("\n** Exitting **\n")
            exit()
