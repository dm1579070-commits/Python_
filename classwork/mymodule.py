PI=3.14159265358979
VERSION="1.0.0"
_secret="Это скрытая константа"

def circle_area(r): return PI * r ** 2
def circle_len(r):  return 2 * PI * r
def _helper():      return PI/2

def sphere_volume(r):  
    """ Объем шара вычисляется так= 4/3 * ПИ *r**3"""
    return (4/3)* PI*r**3


if __name__=="__main__":
    print(f"[{VERSION}] Самопроверка mymodule:")
    print("  S(r=2) =", circle_area(2))
    print("  L(r=2) =", circle_len(2))
    print("  Объем шара =", sphere_volume(2))

    #ДОП. ЗАДАНИЕ ПОВЫШЕННОЙ СЛОЖНОСТИ в MYMODULE.PY

