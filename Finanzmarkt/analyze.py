import pandas as pd
# ps = pw/gw*100
# KeyError


class WeeklyCurrencyPivot:

    def __init__(self, openers, highs, lows, closes):

        self.openers = openers
        self.highs = highs
        self.lows = lows
        self.closes = closes

        self.trues = 0
        self.falses = 0
        self.gesamt = 0

        self.analyzer(self.openers, self.highs, self.lows, self.closes)
        self.ps = self.probability_calculation(gw=self.gesamt, pw=self.trues)
        self.resulting()

    def resulting(self):

        print('\nDie Gesamtzahl bewerteter Weeklypivots liegt bei:', self.gesamt)
        print(f'\nDavon sind {self.trues} Weeklypivots durchbrochen worden.')
        print(f'\n{self.falses} Weeklypivots wurden nicht durchbrochen.')
        print(f'\nSomit liegt die zukünftige Wahrscheinlichkeit bei {self.ps}% dass der Weeklypivot durbrochen wird.')
        print('Anhand der historischen Daten.')

    def analyzer(self, opener, high, low, close):

        datas = {'Openers': opener, 'Highs': high, 'Lows': low, 'Closes': close}
        num0 = 0
        num1 = 1

        df = pd.DataFrame(data=datas, columns=['Openers', 'Highs', 'Lows', 'Closes'])

        while True:

            try:

                piv = self.make_pivot(df.loc[num0, 'Highs'], df.loc[num0, 'Lows'], df.loc[num0, 'Closes'])
                self.testing_pivot(df.loc[num1, 'Openers'], df.loc[num1, 'Highs'], df.loc[num1, 'Lows'],
                                   df.loc[num1, 'Closes'], pivot=piv)

            except KeyError:

                break

            num0 += 1
            num1 += 1

    def make_pivot(self, high, low, close):

        pivot = (high + low + close) / 3
        pivot = round(pivot, 6)
        return pivot

    def testing_pivot(self, opener, high, low, close, pivot):

        self.gesamt += 1

        if pivot < opener:

            if pivot > high or pivot > low or pivot > close:

                self.trues += 1

            else:

                self.falses += 1

        elif pivot > opener:

            if pivot < high or pivot < low or pivot < close:

                self.trues += 1

            else:

                self.falses += 1

    def probability_calculation(self, gw, pw):

        ps = round(pw / gw * 100, 2)
        return ps
