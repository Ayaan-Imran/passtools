import getpass
import sys
import hashlib
import secrets
import os

__doc__ = "Passtools is a package that allows you to use tools with which you can do all kinds of stuff with passwords"
__version__ = "0.1.0"
__author__ = "Ayaan Imran Saleem"

def passhash(prompt:str, hash_type:str="sha256", hash_strength:int=1):
    if hash_type == "sha256":
        hash = ""
        for _ in range(hash_strength):
            hash = hashlib.sha256(bytes(prompt, "utf-8")).hexdigest()

    elif hash_type == "sha1":
        hash = ""
        for _ in range(hash_strength):
            hash = hashlib.sha1(bytes(prompt, "utf-8")).hexdigest()

    elif hash_type == "sha224":
        hash = ""
        for _ in range(hash_strength):
            hash = hashlib.sha224(bytes(prompt, "utf-8")).hexdigest()

    elif hash_type == "sha384":
        hash = ""
        for _ in range(hash_strength):
            hash = hashlib.sha384(bytes(prompt, "utf-8")).hexdigest()

    elif hash_type == "sha512":
        hash = ""
        for _ in range(hash_strength):
            hash = hashlib.sha512(bytes(prompt, "utf-8")).hexdigest()

    elif hash_type == "md5":
        hash = prompt
        for _ in range(hash_strength):
            hash = hashlib.md5(bytes(hash, "utf-8")).hexdigest()

    return hash

def passask(prompt:str="password: ", do_hash:bool=True, hashtype="sha256", hashstrength:int=1):
    if not sys.stdin.isatty():
        password = input(prompt)

        if do_hash == True:
            password = passhash(password, hash_type=hashtype, hash_strength=hashstrength)

    else:
        password = getpass.getpass(prompt)

        if do_hash == True:
            password = passhash(password, hash_type=hashtype, hash_strength=hashstrength)

    return password

def passgen(length:int = 10, caplock="mix"):
    # Define the letter, numbers and symbols
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "h", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
               "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O",
               "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    symbols = ["@", "#", "%", "!", "*", ">", "<", "$"]

    # Check if length parameter is valid
    if length < 1:
        raise ValueError("Length is too short. It has to be greater than 0")

    # Create generator instance
    generartor = secrets.SystemRandom()

    # Create the random string
    result = ""
    turn = "letter"
    for _ in range(length):
        if turn == "letter":
            result += generartor.choice(letters)

            if caplock == True:
                result = result.upper()
            elif caplock == False:
                result = result.lower()

            turn = "number"

        elif turn == "number":
            result += str(generartor.randint(0, 11))
            turn = "symbol"

        elif turn == "symbol":
            result += generartor.choice(symbols)
            turn = "letter"

    # Shuffle the randomized string
    result = list(result)  # generator.shuffle() takes a list, not str
    for _ in range(10):
        generartor.shuffle(result)

    # Join the result back
    final_result = ""
    for i in result:
        final_result += i

    # Return the result
    return final_result

def passhashcracker(hash:str, wordlist:str, hash_type:str):
    """
    Function to crack hashes using brute force
    :param hash: Hash to crack
    :param wordlist: Text file which contains passwords that you think might be the password
    :param hash_type: The hash type of the hash provided in this function. Hash types included: sha256, sha1, sha224, sha384, sha512, md5
    :return: A tuple with this syntax (Boolean, cracked hash)
    """

    if hash_type == "sha256":
        cracked_hash = ""
        cracked = False

        with open(wordlist, "r") as wordlist_file:
            for password in wordlist_file.readlines(): # Get each password from each line
                password = password.strip("\n")
                hashed_password = hashlib.sha256(bytes(password, "utf-8")).hexdigest()

                if hashed_password == hash: # Compare the hashed password with the hash. If they match, then we have cracked it
                    cracked_hash = password # Save the cracked password
                    cracked = True # Tell the program that the hash has been cracked
                    break # Get out of the loop because the hash is cracked

    elif hash_type == "sha1":
        cracked_hash = ""
        cracked = False

        with open(wordlist, "r") as wordlist_file:
            for password in wordlist_file.readlines():  # Get each password from each line
                password = password.strip("\n")
                hashed_password = hashlib.sha1(bytes(password, "utf-8")).hexdigest()

                if hashed_password == hash:  # Compare the hashed password with the hash. If they match, then we have cracked it
                    cracked_hash = password  # Save the cracked password
                    cracked = True  # Tell the program that the hash has been cracked
                    break  # Get out of the loop because the hash is cracked

    elif hash_type == "sha224":
        cracked_hash = ""
        cracked = False

        with open(wordlist, "r") as wordlist_file:
            for password in wordlist_file.readlines():  # Get each password from each line
                password = password.strip("\n")
                hashed_password = hashlib.sha224(bytes(password, "utf-8")).hexdigest()

                if hashed_password == hash:  # Compare the hashed password with the hash. If they match, then we have cracked it
                    cracked_hash = password  # Save the cracked password
                    cracked = True  # Tell the program that the hash has been cracked
                    break  # Get out of the loop because the hash is cracked

    elif hash_type == "sha384":
        cracked_hash = ""
        cracked = False

        with open(wordlist, "r") as wordlist_file:
            for password in wordlist_file.readlines():  # Get each password from each line
                password = password.strip("\n")
                hashed_password = hashlib.sha384(bytes(password, "utf-8")).hexdigest()

                if hashed_password == hash:  # Compare the hashed password with the hash. If they match, then we have cracked it
                    cracked_hash = password  # Save the cracked password
                    cracked = True  # Tell the program that the hash has been cracked
                    break  # Get out of the loop because the hash is cracked

    elif hash_type == "sha512":
        cracked_hash = ""
        cracked = False

        with open(wordlist, "r") as wordlist_file:
            for password in wordlist_file.readlines():  # Get each password from each line
                password = password.strip("\n")
                hashed_password = hashlib.sha512(bytes(password, "utf-8")).hexdigest()

                if hashed_password == hash:  # Compare the hashed password with the hash. If they match, then we have cracked it
                    cracked_hash = password  # Save the cracked password
                    cracked = True  # Tell the program that the hash has been cracked
                    break  # Get out of the loop because the hash is cracked

    elif hash_type == "md5":
        cracked_hash = ""
        cracked = False

        with open(wordlist, "r") as wordlist_file:
            for password in wordlist_file.readlines():  # Get each password from each line
                password = password.strip("\n")
                hashed_password = hashlib.md5(bytes(password, "utf-8")).hexdigest()

                if hashed_password == hash:  # Compare the hashed password with the hash. If they match, then we have cracked it
                    cracked_hash = password  # Save the cracked password
                    cracked = True  # Tell the program that the hash has been cracked
                    break  # Get out of the loop because the hash is cracked

    return (cracked, cracked_hash)

def hashfile(filename:str, hash_type:str="sha256"):
    """
    Function to hash a file
    :param filename: Name of a valid filename
    :param hash_type: Hash type. Available hash types: sha256, sha1, sha224, sha384, sha512, md5
    :return: The hash of the file in string data type
    """

    if hash_type == "sha256":
        hash = hashlib.sha256()

        with open(filename, "rb") as target_file:
            chunk = 0
            while chunk != b"":
                chunk = target_file.read(1024)
                hash.update(chunk)

    elif hash_type == "sha1":
        hash = hashlib.sha1()

        with open(filename, "rb") as target_file:
            chunk = 0
            while chunk != b"":
                chunk = target_file.read(1024)
                hash.update(chunk)

    elif hash_type == "sha224":
        hash = hashlib.sha224()

        with open(filename, "rb") as target_file:
            chunk = 0
            while chunk != b"":
                chunk = target_file.read(1024)
                hash.update(chunk)

    elif hash_type == "sha384":
        hash = hashlib.sha384()

        with open(filename, "rb") as target_file:
            chunk = 0
            while chunk != b"":
                chunk = target_file.read(1024)
                hash.update(chunk)

    elif hash_type == "sha512":
        hash = hashlib.sha512()

        with open(filename, "rb") as target_file:
            chunk = 0
            while chunk != b"":
                chunk = target_file.read(1024)
                hash.update(chunk)

    elif hash_type == "md5":
        hash = hashlib.md5()

        with open(filename, "rb") as target_file:
            chunk = 0
            while chunk != b"":
                chunk = target_file.read(1024)
                hash.update(chunk)

    return hash.hexdigest()
