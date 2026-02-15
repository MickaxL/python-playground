#beginner project : pawword generator
import random
import string

start = input("Choose the difficlty of the password :"
"\n1) Easy (no MAJ, no num)" 
"\n2) Medium (Lower/Upper + num)"
"\n3) Hard (MAJ,Lower,Upper and special caractere like #|&)   Your choice : ")

longueur = int(input("how long is the psswd ?"))

if start == "1":
    caracteres = string.ascii_lowercase

elif start == "2":
    caracteres = string.ascii_lowercase + string.ascii_uppercase + string.digits

elif start == "3":
    caracteres = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation


password = ""

for i in range(longueur):
    caractere = random.choice(caracteres)
    password = password + caractere

print("Your password :", password)
