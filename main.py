

def demandez_age(nom_personne):
    age_int = 0
    while age_int  == 0:
        age_str = input(nom_personne+" Quel est votre age ? ")
        try:
            age_int = int(age_str)
        except:
            print("ERREUR: Vous devez entrer un nombre pour l'age")
    return age_int

def afficher_information_personne(nom,age):
    print()
    print("Vous vous appelez " + nom + " et vous avez " + str(age) + " ans.")
    print(" l'an prochain vous aurez " + str(age + 1) + " ans")

    if age==17:
        print("Vous etes presque majeur")
    elif age == 18:
        print("Tout juste majeur : Felicitation")
    elif age<10:
        print("vous etes enfants")
    elif age>60:
        print("vous etes senior")


    elif age>=18 :
        print("vous etes majeur ")
    else:
        print("vous etes mineur ")


def demandez_nom():
    reponse_nom = ""
    while reponse_nom == "":
        reponse_nom= input("quel est votre nom ")
    return reponse_nom

nom1=demandez_nom()
nom2=demandez_nom()

age1=demandez_age(nom1)
age2=demandez_age(nom2)

afficher_information_personne(nom1,age1)
afficher_information_personne(nom2,age2)



