from datetime import datetime
import locale

def main():
    print(jour_semaine()) 


def jour_semaine():
    date= input('entre une date stp')
    date = datetime.strptime(date, "%d/%m/%Y")
    locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')
    return date.strftime('%A')


if __name__ == "__main__":
    main()

