

class SpecialRequest:

    def __init__(self, key, grw=None, prw=None, prs=None):

        self.fehlermeldung = 'Irgendwas ist schief gegangen, bitte wiederholen Sie die Eingabe.'
        self.stop = '\nDrücken Sie "q" um das Programm zu beenden.'
        self.key = key
        self.grw = grw
        self.prw = prw
        self.prs = prs

        if key == 'gw':

            self.gw_plus_minus_gleich_pw(gw=grw, pw=prw)

        elif key == 'pw':

            self.gw_plus_minus_gleich_pw(gw=grw, pw=prw)

        elif key == 'ps':

            self.hundert_minus_ps(ps=prs)

    def gw_plus_minus_gleich_pw(self, gw, pw):

        print(self.stop)

        while True:

            quest = input('\nWollen Sie den Prozentwert vom Grundwert abziehen, dazurechnen oder es so '
                          'belassen? (+/-/=/q) ')

            if quest == '+':

                gesamt = gw+pw
                print(f'\nZuzüglich dem Prozentwert "{pw}" beträgt der Grundwert: "{gesamt}"')
                break

            elif quest == '-':

                gesamt = gw-pw
                print(f'\nAbzüglich dem Prozentwert "{pw}" beträgt der Grundwert: "{gesamt}"')
                break

            elif quest == '=':

                print(f'\nOk es bleibt alles wie es ist Grundwert: "{gw}", Prozentwert: "{pw}"')
                break

            elif quest == 'q':

                break

            else:

                print(self.fehlermeldung)
                continue

    def hundert_minus_ps(self, ps):

        print(self.stop)

        while True:

            quest = input('Wollen Sie den Prozentsatz von 100 abziehen oder so belassen? (-/=/q) ')

            if quest == '-':

                gesamt = 100-ps
                print(f'\nAbzüglich des Prozentsatzes: {ps}% von 100% beträgt der neue Prozentsatz: {gesamt}%')
                break

            elif quest == '=':

                print(f'\nOk der Prozentsatz bleibt so wie er ist: {ps}%')
                break

            elif quest == 'q':

                break

            else:

                print(self.fehlermeldung)
                continue
