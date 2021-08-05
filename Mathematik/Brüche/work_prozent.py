from mathe_formeln import Formeln


class WorkspaceProzent(Formeln):

    def __init__(self):

        self.fehlermeldung = 'Irgendwas ist schiefgegangen, wiederholen Sie bitte diese Eingabe.'
        self.stop = 'Drücken Sie "q" um zu beenden.\n'

        with open('prozent.txt', encoding='utf-8') as f:

            content = f.read()
            print(content)

        while True:

            print(self.stop)

            quest = input('action? (w/ls/z/q) ')

            if quest == 'w':

                self.einfache_prozentrechnung()

            elif quest == 'ls':

                self.prozent_liste()

            elif quest == 'z':

                self.zinsen()

            elif quest == 'q':

                break

            else:

                print('Ihre Eingabe konnte leider nicht zugeordnet werden, bitte versuchen Sie es nochmal.')
                continue

    def zinsen(self):

        prompt = '\n"m" für Monate.\n"d" für Tage.\n"w" für weiter mit Defaultwert Jahre.\n'

        print(prompt)

        while True:

            print(self.stop)

            zeitraum = input('Um welchen Zeitraum handelt es sich? ')

            if zeitraum == 'q':

                break

            if zeitraum == 'w':

                zeitraum = None

            kap = input('Kapital: ')

            if kap == 'q':

                break

            prozentsatz = input('Prozentsatz: ')

            if prozentsatz == 'q':

                break

            dauer = input('Dauer in ganzen Zahlen: ')

            if dauer == 'q':

                break

            kap = kap.replace(',', '.')
            prozentsatz = prozentsatz.replace(',', '.')

            try:

                dauer = int(dauer)
                kap = float(kap)
                prozentsatz = float(prozentsatz)

            except ValueError:

                print(self.fehlermeldung)
                continue

            else:

                self.zinsrechnung(kapital=kap, ps=prozentsatz, key=zeitraum, laufzeit=dauer)

    def prozent_liste(self):

        print(self.stop)

        while True:

            print('\nWerte für den Grundwert eingeben.\n')
            grundwert = self.list_sum()
            print('\nWerte für den Prozentwert eingeben.\n')
            prozentwert = self.list_sum()

            prozentsatz = input('Prozentsatz: ')

            prozentsatz = prozentsatz.replace(',', '.')

            if prozentsatz == 'q':

                break

            try:

                prozentsatz = float(prozentsatz)

            except ValueError:

                print('Irgendwas ist schief gelaufen, bitte wiederholen Sie die Eingaben.')
                continue

            else:

                self.prozent_rechnung(grundwert, prozentwert, prozentsatz)

    def einfache_prozentrechnung(self):

        while True:

            print(self.stop)

            grundwert = input('Grundwert: ')

            if grundwert == 'q':

                break

            prozentwert = input('Prozentwert: ')

            if prozentwert == 'q':

                break

            prozentsatz = input('Prozentsatz: ')

            if prozentsatz == 'q':

                break

            grundwert = grundwert.replace(',', '.')
            prozentwert = prozentwert.replace(',', '.')
            prozentsatz = prozentsatz.replace(',', '.')

            try:

                grundwert = float(grundwert)
                prozentwert = float(prozentwert)
                prozentsatz = float(prozentsatz)

            except ValueError:

                print(self.fehlermeldung)
                continue

            else:

                self.prozent_rechnung(grundwert, prozentwert, prozentsatz)