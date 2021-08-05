
def wert_abfrage(name):

    print('Drücken Sie "q" um zu beenden.')

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


zahl_x = wert_abfrage('x')
zahl_y = wert_abfrage('y')

print('Das ist Zahl "x":', zahl_x)
print('Das ist Zahl "y":', zahl_y)

