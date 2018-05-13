import random
random.seed()

global remain
global stats
stats = {}

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

def probe1(st1,harder=0,skill=0,silent=False,stats=stats):# {{{
    global remain
    v1 = w20_1()
    s1 = (st1 if type(st1) == int else stats[st1])
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

def probe3(st1,st2,st3,harder=0,skill=0,silent=False,stats=stats):# {{{
    global remain 
    v1,v2,v3 = w20_c(3)
    s1 = (st1 if type(st1) == int else stats[st1])
    s2 = (st2 if type(st2) == int else stats[st2])
    s3 = (st3 if type(st3) == int else stats[st3])
    skarder = skill - harder
    if not silent:
        print("%s %2d / %2d"%(st1,v1,s1))
        print("%s %2d / %2d"%(st2,v2,s2))
        print("%s %2d / %2d"%(st3,v3,s3))
    num20 = ( (v1 == 20) + (v2 == 20) + (v3 == 20) )
    if 1 < num20:
        if not silent:
            print("Probe nicht bestanden")
            if 3 == num20: print("Spektakulärer Patzer")
        return False
    d1 = s1 - v1
    d2 = s2 - v2
    d3 = s3 - v3
    num1 = ( (v1 == 1) + (v2 == 1) + (v3 == 1) )
    if skarder < 0:
        if num1 < 2 and \
                ( d1 + skarder < 0 or d2 + skarder < 0 or d3 + skarder < 0 ):
            if not silent: print("Probe nicht bestanden")
            return False
        else:
            if not silent:
                print("Probe bestanden mit 1 übrig")
                if num1 == 3: print("Spektakulärer Erfolg")
            return True
    rem = skarder + min(0,d1) + min(0,d2) + min(0,d3)
    remain = rem
    if rem >= 0:
        if not silent:
            print("Probe bestanden mit %d übrig"%(max(1,rem)))
            if num1 == 3: print("Spektakulärer Erfolg")
        return True
    else:
        if num1 > 1:
            if not silent:
                print("Probe bestanden mit 1 übrig")
                if num1 == 3: print("Spektakulärer Erfolg")
            return True
        if not silent: print("Probe nicht bestanden")
        return False
# }}}

def probe(st,harder=0,skill=0,silent=False,nonstop=False,stats=stats):# {{{
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

def wahrscheinlich(st1,st2,st3,harder=0,skill=0,silent=False,# {{{
        stats=stats):
    skarder = skill - harder
    s1 = (st1 if type(st1) == int else stats[st1])
    s2 = (st2 if type(st2) == int else stats[st2])
    s3 = (st3 if type(st3) == int else stats[st3])
    if skarder <= 0:
        prob = ( s1 + skarder ) * ( s2 + skarder ) * ( s3 + skarder ) / 8000
    else:
        prob = 0
        for w1 in range(1,21):
            for w2 in range(1,21):
                for w3 in range(1,21):
                    num1  = (w1 ==  1) + (w2 ==  1) + (w3 ==  1)
                    if num1 > 1:
                        prob = prob + 1
                        continue
                    num20 = (w1 == 20) + (w2 == 20) + (w3 == 20)
                    if num20 > 1: continue
                    d1 = s1 - w1
                    d2 = s2 - w2
                    d3 = s3 - w3
                    rem = skarder + min(0,d1) + min(0,d2) + min(0,d3)
                    if rem >= 0: prob = prob + 1
        prob = prob / 8000
    if not silent:
        print("Wahrscheinlichkeit des Bestehens: {0} %".format(
            round(100 * prob, 8)))
    return prob
# }}}

# MU = "mu"
# KL = "kl"
# IN = "in"
# CH = "ch"
# FF = "ff"
# GE = "ge"
# KO = "ko"
# KK = "kk"
