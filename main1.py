
import sys

def main():

    product = {}

    run = True
    while run:
        try:
            option= int(input("tapez 1 pour ajouter \n2 pour supprimer \n3 pour modifier \npour tout autre valeur nous quitteront le programme \n"))
        except ValueError:
            sys.exit("good bye!")
        except KeyboardInterrupt:
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


if __name__ == "__main__":
    main()
