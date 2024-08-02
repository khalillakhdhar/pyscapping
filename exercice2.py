contacts=[]

def ajouter_contact():
    nom=input("Entrer le nom: ")
    numero=input("Entrer le numéro de téléphone: ")
    contact={"nom":nom,"numero":numero}
    contacts.append(contact)
while True:
    ajouter_contact()
    continuer=input("appuyer sur n pour arrêter et n'importe quelle touche pour continuer")
    if continuer.lower()== 'n':
        break

print("Liste des contacts:")
for contact in contacts:
    print(f"Nom :{contact['nom']},Numéro:{contact['numero']} ")