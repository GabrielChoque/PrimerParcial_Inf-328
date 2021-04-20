def isOp(res):
    if res != "": 
        return (res in "+-*/")
    else: 
        return False

def pri(res):
    if res in "+-": 
        return 0
    if res in "*/": 
        return 1
    
def isNum(res):
    if res != "": 
        return (res in "0123456789.")
    else: 
        return False

def calc(cal, n1, n2):
    if cal == "+": 
        return str(float(n1) + float(n2))
    if cal == "-": 
        return str(float(n1) - float(n2))
    if cal == "*": 
        return str(float(n1) * float(n2))
    if cal == "/": 
        return str(float(n1) / float(n2))

def Infix(expr):
    expr = list(expr)
    pilaC = list()
    pilaN = list()
    pilaN.append("0")
    n = ""
    while len(expr) > 0:
        res = expr.pop(0)
        if len(expr) > 0: 
            d = expr[0]
        else: 
            d = ""
        if isNum(res):
            n = n + res
            if not isNum(d):
                pilaN.append(n)
                n = ""
        elif isOp(res):
            while True:
                if len(pilaC) > 0: 
                    top = pilaC[-1]
                else: top = ""
                if isOp(top):
                    if not pri(res) > pri(top):
                        n2 = pilaN.pop()
                        op = pilaC.pop()
                        n1 = pilaN.pop()
                        pilaN.append(calc(op, n1, n2))
                    else:
                        pilaC.append(res)
                        break
                else:
                    pilaC.append(res)
                    break
        elif res == "(":
            pilaC.append(res)
        elif res == ")":
            while len(pilaC) > 0:
                res = pilaC.pop()
                if res == "(":
                    break
                elif isOp(res):
                    n2 = pilaN.pop()
                    n1 = pilaN.pop()
                    pilaN.append(calc(res, n1, n2))

    while len(pilaC) > 0:
        res = pilaC.pop()
        if res == "(":
            break
        elif isOp(res):
            n2 = pilaN.pop()
            n1 = pilaN.pop()
            pilaN.append(calc(res, n1, n2))
    return pilaN.pop()



def setFormat1(pos):
    m = str(pos).split(".")
    if m[1] == "0":
        return int(m[0])
    return pos
def setFormat2(pos):
    m = pos.split(".")
    if m[1] == "0":
        return m[0]
    return pos