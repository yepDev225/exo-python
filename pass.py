
def main():
    mot_de_passe=input('entre un mot de passe')
    if len(mot_de_passe)<8:
        print(' mot de passe court')
        return False
    maj=any(caractere.isupper() for caractere in mot_de_passe)
    min=any(caractere.islower() for caractere in mot_de_passe)
    nbre=any(caractere.isdigit() for caractere in mot_de_passe)
    spec=any(caractere in "@;,:_-" for caractere in mot_de_passe)


    if maj and min and nbre and spec:
        print("mot de passe cree avec succes")
    else:
        print('mot non securiser')

        
if __name__ == "__main__":
    main()