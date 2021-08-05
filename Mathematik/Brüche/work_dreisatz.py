from mathe_formeln import Formeln


class PropAntiProp(Formeln):

    def __init__(self):

        self.fehlermeldung = 'Irgendwas ist schiefgegangen, wiederholen Sie bitte diese Eingabe.'
        self.stop = 'Drücken Sie "q" um zu beenden.\n'

        with open('dreisatz.txt', encoding='utf-8') as f:

            content = f.read()
            print(content)

        while True:

            quest = input('Wie möchten Sie fortfahren? (a/p/q) ')

            if quest == 'a':

                self.anti_prop()

            elif quest == 'p':

                self.prop()

            elif quest == 'q':

                break

            else:

                print('Ihre Eingabe konnte leider nicht zugeordnet werden, bitte versuchen Sie es nochmal.')
                continue

    def anti_prop(self):

        print('Hier werden Sie aufgefordert Werte für eine antiproportionale Dreisatzrechnung einzugeben.\n')

        while True:

            try:

                zahl_x = self.wert_abfrage('x')
                zahl_y = self.wert_abfrage('y')
                zahl_f = self.wert_abfrage('f')

            except ValueError:

                print(self.fehlermeldung)
                continue

            print('Es wird nun die Zahl "x" auf den Wert von Zahl "f" gleichgesetzt und die Zahl "y" '
                  'dementsprechend dividiert.\n')

            try:

                self.anti_proportionalitaet(zahl_x, zahl_y, zahl_f)

            except TypeError:

                print('Da Sie in einen der Werte "q" eingegeben haben wird das Programm beendet.\n')
                break

            quest = input('Wiederholen? (n/y) ')

            if quest == 'y':

                continue

            else:

                break

    def prop(self):

        print('Hier werden Sie aufgefordert Werte für eine proportionale Dreisatzrechnung einzugeben.\n')

        while True:

            try:

                zahl_x = self.wert_abfrage('x')
                zahl_y = self.wert_abfrage('y')
                zahl_f = self.wert_abfrage('f')

            except ValueError:

                print(self.fehlermeldung)
                continue

            print('Es wird nun die Zahl "x" auf den Wert von Zahl "f" gleichgesetzt und die Zahl "y" mit erweitert.\n')

            try:

                self.proportionalitaet(zahl_x, zahl_y, zahl_f)

            except TypeError:

                print('Da Sie in einen der Werte "q" eingegeben haben wird das Programm beendet.\n')
                break

            quest = input('Wiederholen? (n/y) ')

            if quest == 'y':

                continue

            else:

                break

    def wert_abfrage(self, name):

        print(self.stop)

        while True:

            wert = input(f'Geben Sie eine Zahl für "{name}" ein: ')
            wert = wert.replace(',', '.')

            if wert == 'q':

                break

            try:

                wert = int(wert)

            except ValueError:

                wert = float(wert)
                return wert

            else:

                return wert
