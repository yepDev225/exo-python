
import sys
import os

def main():
    product = init_db()
    run = True
    print(product)
    while run:
        try:
            option= int(input("tapez 1 pour ajouter \n2 pour supprimer \n3 pour modifier \npour tout autre valeur nous quitteront le programme \n"))
        except ValueError:
            save_in_file(product)
            sys.exit("good bye!")
        except KeyboardInterrupt:
            save_in_file(product)
            sys.exit("good bye!")
        else:
            if option == 1:
                prod = add_item()
                product.update(**prod)
                print(product)
            elif option == 2:
                product = delete_item(product)
                print(product)
            elif option == 3:
                product  = edit(product)
            else:
                save_in_file(product)
                sys.exit("good bye!")


def add_item():
    print("____ ajout de produit _____")
    name= input("nom: ")
    qte = input("quantité: ")

    return {name:qte}


def delete_item(product):
    print("____ suppression de produit _____")
    name= input("nom: ")
    try:
        del product[name]
    except KeyError:
        print("ce produit n'existe pas!")
    else:
        print("suppression avec succes")
        return product


def edit(product):
    print("____ modification de produit _____")
    name= input('nom : ')
    qte= input('valeur : ')
    try:
        product[name]=qte 
    except KeyError:
        print('produit introuvable')
    else:
        print("modification reussite!")
        return product

def init_db():
    final_product ={}
    product = ""
    if os.path.exists("db.txt"):
        with open("db.txt", "r") as file:
            product += str(file.read())
        product = product.split(",")
        for item in product:
            if item.strip() != "":
                final_product[item.split(":")[0]] = int(item.split(":")[1])
    return final_product


def save_in_file(product):
    with open("db.txt", "w") as file:
        for cle, val in product.items():
            file.write(cle+":"+str(val)+",")

if __name__ == "__main__":
    main()



