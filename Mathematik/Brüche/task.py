import work_bruch
import work_prozent
import work_dreisatz


class WorkMathe:

    def __init__(self):

        with open('stuff.txt', encoding='utf-8') as f:
            content = f.read()
            print(content)

        quest = input('Geben Sie hier Ihre Antwort ein: ')

        if quest == 'pr':

            work_prozent.WorkspaceProzent()

        elif quest == 'br':

            work_bruch.WorkspaceBruchrechnung()

        elif quest == 'dr':

            work_dreisatz.PropAntiProp()


while True:

    frage = input('Wollen Sie was berechnen?(n/y) ')

    if frage == 'n':

        break

    else:

        berechnung = WorkMathe()

# Bei f-g und g-f Kürzungsmöglichkeit geben.
