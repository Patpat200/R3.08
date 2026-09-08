
def grandNombre (r1: int, r2 : int) -> int:
    if r1 > r2:
        return r1
    else:
        return r2

print(grandNombre(2, 1))


def ceuil(a : int, b : int) -> bool:
    if b > a:
        return False
    else:
        return True

print(ceuil(2, 10))


def grandList (*args) -> int:
    max = args[0]
    for i in args:
        if i > max:
            max = i

    return max

print(grandList(1,2,6,8,4,2,9,3,4,1))

def mini(*args) -> int:
    b =3
    total = 0
    for i in args:
        if i < b:
            total += 1
    return total

print(mini(1,2,6,8,4,2,9,3,4,1))

