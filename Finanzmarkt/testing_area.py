import pandas as pd
from analyze import WeeklyCurrencyPivot


df = pd.read_csv('EURUSD.csv')
df.dropna(inplace=True)

filt = (df['Date'] >= '2020-01-01')
df = df.loc[filt]
filt = (df['Date'] <= '2021-01-01')
df = df.loc[filt]

dates = [d for d in df['Date']]
openers_filtered = [o for o in df['Open']]
highs_filtered = [h for h in df['High']]
lows_filtered = [i for i in df['Low']]
close_filtered = [c for c in df['Close']]

WeeklyCurrencyPivot(openers_filtered, highs_filtered, lows_filtered, close_filtered)

print(f'\nDer gewählte Zeitraum liegt von {dates[0]} bis {dates[-1]}.')

