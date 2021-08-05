
def pivots(high, low, close):

    pivot = (high + low + close) / 3
    r1 = 2 * pivot - low
    r2 = pivot + (high-low)
    r3 = r1 + (high - low)
    s1 = 2 * pivot - high
    s2 = pivot - (high - low)
    s3 = s1 - (high - low)

    pivot = round(pivot, 6)
    r1 = round(r1, 6)
    r2 = round(r2, 6)
    r3 = round(r3, 6)
    s1 = round(s1, 6)
    s2 = round(s2, 6)
    s3 = round(s3, 6)

    return pivot


def testing_pivot(opener, high, low, close, pivot):

    if pivot < opener:

        if pivot > high or pivot > low or pivot > close:

            print('Der Pivot wurde von oben nach unten durchbrochen.')

        else:

            print('Der Pivot wurde nicht durchbrochen.')

    elif pivot > opener:

        if pivot < high or pivot < low or pivot < close:

            print('Der Pivot wurde von unten nach oben durchbrochen.')

        else:

            print('Der Pivot wurde nicht durchbrochen.')

