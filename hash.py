import hashlib



myText = None

def menu():
    myText = input("Insira a frase que o hash precisa ser validada: ")
    SHA256 = hashlib.sha256(myText.encode('utf-8')).hexdigest()
    MD5 = hashlib.md5(myText.encode('utf-8')).hexdigest()
    print("\"" +myText + "\" - " + SHA256 + " - " + MD5)




    

menu()
