def charfromnum(num):
    if 1 <= num <= 26:
        return chr(num + 64)
    else:
        raise Exception('no good number')


def column(dividend):
    outstr = str()
    while dividend:
        if dividend <= 26:
            return charfromnum(dividend) + outstr
        dividend, charin = dividend // 26, dividend % 26
        if not charin:
            outstr = charfromnum(26) + outstr
            dividend -= 1
        else:
            outstr = charfromnum(charin) + outstr
    return outstr


def columnrec(dividend, outstr):
    if not outstr:
        outstr = str()
    if not dividend:
        return outstr
    if dividend <= 26:
        return charfromnum(dividend) + outstr
    quotient, charin = dividend // 26, dividend % 26
    if not charin:
        outstr = charfromnum(26) + outstr
        quotient -= 1
    else:
        outstr = charfromnum(charin) + outstr
    return columnrec(quotient, outstr)


print(column(52))
