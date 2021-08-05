from special_task import SpecialRequest


class Formeln:

    def prozent_rechnung(self, gw, pw, ps):

        """\ngw:Grundwert, pw=Prozentwert, ps=Prozentsatz\n\nDie Formel erfordert 2 beliebige Werte \nmit denen es den
        dritten ausrechnet."""

        if gw == 0:
            gw = pw/ps*100
            gw = round(gw, 2)
            print('Der Grundwert ist:', gw)
            SpecialRequest(key='gw', grw=gw, prw=pw)

        elif pw == 0:
            pw = gw/100*ps
            pw = round(pw, 2)
            print('Der Prozentwert ist:', pw)
            SpecialRequest(key='pw', grw=gw, prw=pw)

        elif ps == 0:
            ps = pw/gw*100
            ps = round(ps, 2)
            print(f'Der Prozentsatz ist: {ps}%')
            SpecialRequest(key='ps', prs=ps)

    def zinsrechnung(self, kapital, ps, laufzeit=1, key=None):

        prompt = 'Mit Zinseszinsberechnung? (n/y) '

        if key == 'm':

            quest = input(prompt)

            if quest == 'y':

                z = 0

                for number in range(1, laufzeit+1):

                    rechnung = (kapital * ps) / 100
                    z = rechnung
                    print('Zins:', z)
                    kapital += rechnung

                print('Der letzte Zinseszins ist:', z)
                print('Das neue Kapital:', kapital)

            else:

                z = (kapital * laufzeit * ps) / (100 * 12)
                print('Der Zins beträgt:', round(z, 2))
                print('Das neue Kapital beträgt:', round(kapital + z, 2))

        elif key == 'd':

            quest = input(prompt)

            if quest == 'y':

                z = 0

                for number in range(1, laufzeit+1):

                    rechnung = (kapital * ps) / 100
                    z = rechnung
                    print('Zins:', z)
                    kapital += rechnung

                print('Der letzte Zinseszins ist:', z)
                print('Das neue Kapital:', kapital)

            else:

                z = (kapital * laufzeit * ps) / (100 * 360)
                print('Der Zins beträgt:', round(z, 2))
                print('Das neue Kapital beträgt:', round(kapital + z, 2))

        else:

            quest = input(prompt)

            if quest == 'y':

                z = 0

                for number in range(1, laufzeit + 1):

                    rechnung = (kapital * ps) / 100
                    z = rechnung
                    print('Zins:', z)
                    kapital += rechnung

                print('Der letzte Zinseszins ist:', z)
                print('Das neue Kapital:', kapital)

            else:

                z = (kapital * laufzeit * ps) / 100
                print('Der Zins beträgt:', round(z, 2))
                print('Das neue Kapital beträgt:', round(kapital + z, 2))

    def proportionalitaet(self, x, y, factor):

        for number in range(1, 1000):

            if x / number == 1:
                x /= number
                y /= number
                break

        x *= factor
        y *= factor

        print(round(x, 2))
        print(round(y, 2))

    def anti_proportionalitaet(self, x, y, factor):

        for number in range(1, 1000):

            if x / number == 1:
                x /= number
                y *= number
                break

        x *= factor
        y /= factor

        print(round(x, 2))
        print(round(y, 2))

    def list_sum(self):

        liste = []

        print('Drücken Sie "q" um die Eingabe zu beenden.')

        while True:

            value = input('Geben Sie eine Zahl ein: ')
            value = value.replace(',', '.')

            if value == 'q':

                zahl = sum(liste)
                return round(zahl, 2)

            try:

                value = int(value)
                liste.append(value)

            except ValueError:

                value = float(value)
                liste.append(value)



