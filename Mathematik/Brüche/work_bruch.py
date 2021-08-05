import numpy as np
from bruch_formeln import FormelnBruch
from time import sleep as sl


class WorkspaceBruchrechnung(FormelnBruch):

    def __init__(self):

        self.fehlermeldung = 'Irgendwas ist schiefgegangen, wiederholen Sie bitte diese Eingabe.'
        self.stop = 'Drücken Sie "q" um zu beenden.'
        self.prompt_aufforderung = '\nBitte geben Sie Zähler und Nenner nacheinander, mit Minuszeichen falls '\
                                   'vorhanden, vor den Zählern ein.\nDie Ganzen werden zum Schlusss abgefragt, '\
                                   'dort bitte auch auf die Vorzeichen achten.\n'

        self.prompt_ganzen = 'Wenn Sie "q" drücken werden dann noch die Ganzen abgefragt.\n'

        print('\n"f-g" Um unechte Brüche in gemischte Zahlen umzuwandeln.')
        print('"g-f" Um gemischte Zahlen in ein unechten Bruch umzuwandeln')
        print('"zus" Um verschiedene Brüche zusammen zu rechnen.')
        print('"mult" Um mehrere Brüche miteinander zu multiplizieren.')
        print('"div" Um Brüche zu dividieren.')
        print('"erw" Um Brüche zu erweitern.')
        print('"k" Um einfach Brüche zu kürzen.\n')

        while True:

            print(self.stop)

            frage = input('action? (f-g/g-f/zus/mult/div/erw/k/q) ')

            if frage == 'zus':

                self.zusammen_rechnung()

            elif frage == 'f-g':

                self.unechte_bruch_gemischte_zahl()

            elif frage == 'g-f':

                self.gemischte_zahl_unechte_bruch()

            elif frage == 'k':

                self.kuerzen()

            elif frage == 'mult':

                self.multiplikation_bruch()

            elif frage == 'div':

                self.division_bruch()

            elif frage == 'erw':

                self.bruch_erweitern()

            elif frage == 'q':

                break

            else:

                print('Ihre Eingabe konnte leider nicht zugeordnet werden, bitte versuchen Sie es nochmal.')
                continue

    def bruch_erweitern(self):

        while True:

            print(self.stop)

            zahler = self.quest_zaehler()
            nenner = self.quest_nenner()

            factor = input('Um welche Zahl soll erweitert werden? ')

            if factor == 'q':

                break

            try:

                factor = int(factor)

            except ValueError:

                print(self.fehlermeldung)
                continue

            else:

                zahler *= factor
                nenner *= factor

                print('Das ist der neue Zähler:', zahler)
                print('Das ist der neue Nenner:', nenner)

    def unechte_bruch_gemischte_zahl(self):

        print('\nBitte geben Sie nun Zähler und Nenner ein,\num den unechten Bruch in eine gemischte Zahl '
              'umzuwandeln.\n')

        print(self.stop)

        while True:

            zaeh = input('Zähler: ')

            if zaeh == 'q':

                break

            nen = input('Nenner: ')

            if nen == 'q':

                break

            try:
                zaeh = int(zaeh)
                nen = int(nen)

            except ValueError:
                print(self.fehlermeldung)
                sl(1)
                continue

            dezimal = self.get_dezimal(zaehler=zaeh, nenner=nen)
            ganzen = self.get_ganzen(dezimal)
            neue_zaeh = self.get_zaehler(dezi=dezimal, nenner=nen)

            print('Die Ganzen sind:', ganzen)
            print('Der Zähler ist:', neue_zaeh)
            print('Der Nenner ist:', nen)

            frage = input('Wollen Sie noch kürzen? (n/y) ')

            if frage == 'y':

                self.kuerzen(neue_zaeh, nen)

            print('----------------------------------')
            print('Neue Rechnung!')
            print()

    def gemischte_zahl_unechte_bruch(self):

        print(self.stop)

        while True:

            ganzen = input('Wie viele Ganzen? ')

            if ganzen == 'q':

                break

            zaehler = input('Zähler: ')

            if zaehler == 'q':

                break

            nenner = input('Nenner: ')

            if nenner == 'q':

                break

            try:

                ganzen = int(ganzen)
                zaehler = int(zaehler)
                nenner = int(nenner)

            except ValueError:

                print(self.fehlermeldung)
                continue

            else:

                neue_zahler = ganzen*nenner+zaehler
                print('Das ist der Zähler:', neue_zahler)
                print('Das ist der Nenner: ', nenner)

            frage = input('Wollen Sie noch kürzen? (n/y) ')

            if frage == 'y':

                self.kuerzen(neue_zahler, nenner=nenner)

            print('----------------------------------')
            print('Neue Rechnung!')
            print()

    def division_bruch(self):

        print(self.prompt_aufforderung)

        bruch1 = 0
        bruch2 = 0

        zahler1 = self.quest_zaehler()
        nenner1 = self.quest_nenner()
        ganzen = self.quest_ganzen()
        print('-----------------------------')
        bruch1 += self.get_dezimal(zahler1, nenner1)
        bruch1 += ganzen

        zahler2 = self.quest_zaehler()
        nenner2 = self.quest_nenner()
        ganzen2 = self.quest_ganzen()
        print('-----------------------------')
        bruch2 += self.get_dezimal(zahler2, nenner2)
        bruch2 += ganzen2

        dezimal = bruch1/bruch2
        bruch_gesamt = self.get_fraction(dezimal)

        print('Der Bruch lautet:', bruch_gesamt)

    def multiplikation_bruch(self):

        dezimal = 1
        ganzen = 0
        nenner_gesamt = []

        print(self.prompt_aufforderung)
        print(self.prompt_ganzen)

        while True:

            zahler = input('Zähler: ')

            if zahler == 'q':

                break

            nenner = input('Nenner: ')

            if nenner == 'q':

                break

            print('---------------------------------')

            try:

                zahler = int(zahler)
                nenner = int(nenner)

            except ValueError:

                print(self.fehlermeldung)
                continue

            else:

                if nenner not in nenner_gesamt:

                    nenner_gesamt.append(nenner)

                else:

                    continue

                dezi = zahler/nenner
                dezimal *= dezi

        while True:

            ganz = input('Ganzen: ')

            if ganz == 'q':

                break

            try:

                ganz = int(ganz)

            except ValueError:

                print(self.fehlermeldung)
                continue

            else:

                ganzen += ganz
                dezimal += ganz

        kgv_nenner = np.lcm.reduce(nenner_gesamt)
        zahler = self.get_zaehler(dezi=dezimal, nenner=kgv_nenner)

        print('Die Ganzen sind:', ganzen)
        print('Die Zähler sind:', zahler)
        print('Der Nenner ist:', kgv_nenner)
        print()

        frage = input('Wollen Sie noch kürzen? (n/y) ')

        if frage == 'y':

            self.kuerzen(zaehler=zahler, nenner=kgv_nenner)

    def zusammen_rechnung(self):

        nenner_gesamt = []
        dezimal = 0
        ganzen = 0

        print(self.prompt_aufforderung)
        print(self.prompt_ganzen)

        while True:

            zahler = input('Zähler: ')

            if zahler == 'q':

                break

            nenner = input('Nenner: ')

            if nenner == 'q':

                break

            print('--------------------------------------')

            try:

                zahler = int(zahler)
                nenner = int(nenner)

            except ValueError:

                print(self.fehlermeldung)
                continue

            else:

                dezi = zahler/nenner
                dezimal += dezi

                if nenner not in nenner_gesamt:

                    nenner_gesamt.append(nenner)

                else:

                    continue

        print(self.stop)

        while True:

            ganz = input('Ganze: ')

            if ganz == 'q':

                break

            else:

                ganz = int(ganz)
                ganzen += ganz

        dezimal += ganzen
        ganzen = self.get_ganzen(dezimal)
        kgv_nenner = np.lcm.reduce(nenner_gesamt)
        orig_zahler = self.get_zaehler(dezimal, kgv_nenner)

        print('Die Ganzen sind:', ganzen)
        print('Die Zähler sind:', orig_zahler)
        print('Der Nenner ist:', kgv_nenner)
        print()

        frage = input('Wollen Sie noch kürzen? (n/y) ')

        if frage == 'y':

            self.kuerzen(zaehler=orig_zahler, nenner=kgv_nenner)
