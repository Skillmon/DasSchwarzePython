import random
random.seed()

global remain

def w6(num=1):# {{{
    a = []
    for i in range(num):
        a.append(random.randint(1,6))
    return a
# }}}
def w6_1(): return random.randint(1,6)
def w6_c(num=1): return [ random.randint(1,6) for i in range(num) ]
def w20(num=1):# {{{
    # list comprehension is faster for num >= 3
    a = []
    for i in range(num):
        a.append(random.randint(1,20))
    return a
    # return [ random.randint(1,20) for i in range(num) ]
# }}}
def w20_1(): return random.randint(1,20)
def w20_c(num=1): return [ random.randint(1,20) for i in range(num) ]

# Meljow Stats (leider hier noch nötig, gute Lösung für Proben etc. gesucht)
# stats={"mu":13,"kl":14,"in":13,"ch":14,"ff":12,"ge":13,"ko":13,"kk":12}

def set_stats(newstats):# {{{
    global stats
    stats = newstats
# }}}

def probe1(st1,harder=0,skill=0,silent=False):# {{{
    global remain
    v1 = w20_1()
    s1 = stats[st1]
    if not silent: print("%s %2d / %2d"%(st1,v1,s1))
    skarder = skill - harder
    rem = s1 + skarder - v1
    remain = rem
    if v1 == 20:
        if not silent: print("Probe nicht bestanden")
        return False
    if rem >= 0:
        if not silent:
            print("Probe bestanden",end="")
            if skarder > 0: print(" mit %d übrig"%(min(skarder,rem)),end="")
            print("")
        return True
    else:
        if not silent: print("Probe nicht bestanden")
        return False
# }}}

def probe3(st1,st2,st3,harder=0,skill=0,silent=False):# {{{
    global remain 
    v1,v2,v3 = w20_c(3)
    s1 = stats[st1]
    s2 = stats[st2]
    s3 = stats[st3]
    skarder = skill - harder
    if not silent:
        print("%s %2d / %2d"%(st1,v1,s1))
        print("%s %2d / %2d"%(st2,v2,s2))
        print("%s %2d / %2d"%(st3,v3,s3))
    if v1 == 20 or v2 == 20 or v3 == 20:
        if not silent: print("Probe nicht bestanden")
        return False
    d1 = s1 - v1
    d2 = s2 - v2
    d3 = s3 - v3
    if skarder < 0:
        if d1 + skarder < 0 or d2 + skarder < 0 or d3 + skarder < 0:
            if not silent: print("Probe nicht bestanden")
            return False
        else:
            if not silent: print("Probe bestanden")
            return True
    rem = skarder + min(0,d1) + min(0,d2) + min(0,d3)
    remain = rem
    if rem >= 0:
        if not silent:
            print("Probe bestanden",end="")
            if skarder > 0: print(" mit %d übrig"%(rem),end="")
            print("")
        return True
    else:
        if not silent: print("Probe nicht bestanden")
        return False
# }}}

def probe(st,harder=0,skill=0,silent=False,nonstop=False):# {{{
    global remain
    if type(st) == str or type(st) == int: st = (st,)
    skarder = skill - harder
    failed = False
    if skarder < 0:
        for stat in st:
            if type(stat) == str:
                s = stats[stat]
                if not silent: print(stat,end=" ")
            else:
                s = stat
                if not silent: print("  ",end=" ")
            v = w20_1()
            if not silent: print("%2d / %2d - %2d"%(v, s, abs(skarder)))
            if s + skarder < v or v == 20:
                if not nonstop:
                    if not silent: print("Probe nicht bestanden")
                    return False
                else: failed = True
        if failed:
            if not silent: print("Probe nicht bestanden")
            return False
        else:
            if not silent: print("Probe bestanden")
            remain = 0
            return True
    else:
        rem = skarder
        for stat in st:
            if type(stat) == str:
                s = stats[stat]
                if not silent: print(stat,end=" ")
            else:
                s = stat
                if not silent: print("  ",end=" ")
            v = w20_1()
            if not silent: print("%2d / %2d"%(v, s))
            if s + rem < v or v == 20:
                if not nonstop:
                    if not silent: print("Probe nicht bestanden")
                    return False
                else: failed = True
            else: rem = rem + min(0, s - v)
        if failed:
            if not silent: print("Probe nicht bestanden")
            return False
        else:
            remain = rem
            if not silent:
                print("Probe bestanden",end="")
                if skarder > 0: print(" mit %d übrig"%(rem),end="")
                print("")
            return True
# }}}

def wahrscheinlich(st1,st2=False,st3=False,harder=0,skill=0,silent=False,# {{{
        tries=1e5):
    skarder = skill - harder
    if skarder <= 0:
        prob = ( stats[st1] + skarder ) / 20
        if st2: prob = prob * ( stats[st2] + skarder ) / 20
        if st3: prob = prob * ( stats[st3] + skarder ) / 20
    else:
        prob = 0
        for i in range(int(tries)):
            prob = prob + probe(
                    st1,st2=st2,st3=st3,harder=harder,skill=skill,silent=True)
        prob = prob / tries
        if tries <= 1e7: prob = round(prob, 2)
        if not silent and tries <= 1e7: print("Ungefähre ",end="")
    if not silent:
        print("Wahrscheinlichkeit des Bestehens: {0} %".format(
            round(100 * prob, 3)))
    return round(prob, 5)
# }}}

# MU = "mu"
# KL = "kl"
# IN = "in"
# CH = "ch"
# FF = "ff"
# GE = "ge"
# KO = "ko"
# KK = "kk"
