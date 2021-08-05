import numpy as np
from fractions import Fraction as frac
from mathe_formeln import Formeln


class FormelnBruch(Formeln):

    def dividieren(self, dividend, divisor):

        produkt = dividend/divisor

        return produkt

    def quest_zaehler(self):

        while True:

            zaehler = input('Zähler: ')

            if zaehler == 'q':

                break

            try:

                zaehler = int(zaehler)

            except ValueError:

                print('Irgendwas ist schief gelaufen, wiederholen Sie bitte diese Eingabe.')
                continue

            else:

                return zaehler

    def quest_nenner(self):

        while True:

            nenner = input('Nenner: ')

            if nenner == 'q':

                break

            try:

                nenner = int(nenner)

            except ValueError:

                print('Irgendwas ist schief gelaufen, wiederholen Sie bitte diese Eingabe.')
                continue

            else:

                return nenner

    def quest_ganzen(self):

        ganze = input('Ganzen: ')

        try:

            ganze = int(ganze)

        except ValueError:

            print('Irgendwas ist schief gelaufen, wiederholen Sie bitte diese Eingabe.')

        else:

            return ganze

    def get_fraction(self, dezi):

        ganzen = 0

        while dezi > 1:

            dezi -= 1
            ganzen += 1

            if dezi < 1:

                break

        bruch = frac(dezi).limit_denominator(100)
        print('Die Ganzen sind:', ganzen)

        return bruch

    def get_dezimal(self, zaehler, nenner):

        """Erstellt aus dem Zähler und dem Nenner eine Dezimalzahl.\nEs spielt dabei keine Rolle ob es sich um einen
        echten oder unechten Bruch handelt."""

        dezi = zaehler/nenner

        return dezi

    def get_ganzen(self, dezi):

        """Tut aus einer Dezimalzahl nur die Ganzen herausziehen und wiedergeben."""

        ganzen = 0

        while dezi > 1:

            dezi -= 1
            ganzen += 1

            if dezi < 1:
                break

        return ganzen

    def get_zaehler(self, dezi, nenner):

        """Durch die Subtraktion der Ganzen in einem Dezimalbruch, wenn vorhanden, wird der übrige Wert mit dem\n
        vorhandenen Nenner multipliziert, um den Zähler der gemischten Zahl herauszufinden und wieder zu geben."""

        while dezi > 1:

            dezi -= 1

            if dezi < 1:

                break

        neue_zaehler = dezi*nenner
        return round(neue_zaehler)

    def kuerzen(self, zaehler=None, nenner=None):

        fehler_meldung = 'Irgendwas ist schiefgegangen, wiederholen Sie bitte diese Eingabe.'
        print('Drücken Sie "q" um zu beenden.')

        if zaehler and nenner:

            zaehler = int(zaehler)
            nenner = int(nenner)

            kgv = np.lcm(zaehler, nenner)

            for num_a in range(1, 1000):

                if num_a * nenner == kgv:

                    neue_zaehler = num_a

                    if neue_zaehler == zaehler:

                        continue

                    else:

                        print('Das ist der neue Zähler:', neue_zaehler)
                        break

            for num_b in range(1, 1000):

                if num_b * zaehler == kgv:

                    neue_nenner = num_b

                    if neue_nenner == nenner:

                        continue

                    else:

                        print('Das ist der neue Nenner:', neue_nenner)
                        break

        else:

            while True:

                zaehler = input('Zähler: ')

                if zaehler == 'q':

                    break

                nenner = input('Nenner: ')

                if nenner == 'q':

                    break

                try:

                    zaehler = int(zaehler)
                    nenner = int(nenner)

                except ValueError:

                    print(fehler_meldung)
                    continue

                kgv = np.lcm(zaehler, nenner)

                for num_a in range(1, 1000):

                    if num_a * nenner == kgv:

                        neue_zaehler = num_a

                        if neue_zaehler == zaehler:

                            continue

                        else:

                            print('Das ist der neue Zähler:', neue_zaehler)
                            break

                for num_b in range(1, 1000):

                    if num_b * zaehler == kgv:

                        neue_nenner = num_b

                        if neue_nenner == nenner:

                            continue

                        else:

                            print('Das ist der neue Nenner:', neue_nenner)
                            break