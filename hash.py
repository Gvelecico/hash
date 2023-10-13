import hashlib





def menu():
    global myText 
    global SHA256_Validation
    global MD5_Validation
    myText = input(str("Insira a frase que o hash precisa ser validada: \n" ))
    SHA256_Validation =  input(str("Insira a hash no padrão SHA256 para ser validada \n"))
    MD5_Validation =  input(str("Insira a hash no padrão MD5 para ser validada \n"))




def hash(myText, SHA256_Validation, MD5_Validation):
    SHA256 = hashlib.sha256(myText.encode('utf-8')).hexdigest()
    MD5 = hashlib.md5(myText.encode('utf-8')).hexdigest()

    print("\"" + myText + "\" - " + SHA256 + " - " + MD5 + "\n")
    
    if SHA256 == SHA256_Validation and MD5 == MD5_Validation:
        print("Hash correto em ambos padrões\n")
    elif SHA256 == SHA256_Validation:
        print("Hash correto no padrão SHA256\n")
    elif MD5 == MD5_Validation:
        print("Hash correto no padrão MD5\n")
    else:
        print("Nenhuma validação correta\n")
            
        
loop = 1
    
while loop == 1:
    menu()
    hash(myText, SHA256_Validation, MD5_Validation)
    choice = input("Para testar outra frase, digite 1. Para sair, digite 0: ")   
    if choice != '1':
        loop = 0
