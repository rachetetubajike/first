

def demandez_nom():
    reponse_nom = ""
    while reponse_nom == "":
        reponse_nom= input("quel est votre nom? ")
    return reponse_nom
nom=demandez_nom()
print("")
print("Bonjour ", nom, " et bonne chance! "," "
                                            "voici la premiere question:", " "
                                                                           ""
                                                                           "Quelle est la capitale de la France ? ")

print("""
A. Lyon
B. Paris
C. Marseille
D. Lille""")
print("")
reponse=input("Tape ta réponse : ")

print(nom,"vous avez avait repondu ", reponse )

if reponse.lower()=="paris":
    print("Felicitation !")
else:
    print("Mauvaise réponse! ")

