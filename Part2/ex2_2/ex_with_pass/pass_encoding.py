from simplecrypt import decrypt, DecryptionException

encrypted = open("encrypted.bin", "rb").read()
passwords = open("passwords.txt").readlines()

for password in passwords:
    password = password[:-1]
    try:
        s = decrypt(password, encrypted).decode("utf-8")
    except DecryptionException:
        continue

    print(s)
