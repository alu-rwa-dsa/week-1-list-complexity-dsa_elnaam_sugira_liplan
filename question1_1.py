

def rmwht(s):
    nw = s.strip()
    while '  ' in nw:
        nw = nw.replace('  ', ' ')
    return nw
