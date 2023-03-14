a = float(input("Podaj liczbe: "))
b = float(input("Podaj 2 liczbe: "))
c = input("Podaj operacje: '+', '-',  '/',  '*' : ")

match c:
    case "+":
        d = float(a+b)
        print(round(d,3))
    case "-":
        d = float(a-b)
        print(round(d,3))
    case "/":
        d = float(a/b)
        print(round(d,3))
    case "*":
        d = float(a*b)
        print(round(d,3))
    case _:
        print("Zle podane dane")
