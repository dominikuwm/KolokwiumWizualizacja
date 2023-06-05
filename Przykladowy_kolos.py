class Wielomian:
    def __init__(self, wspolczynniki):
        self.wspolczynniki = wspolczynniki

    def __str__(self):
        wyrazy = []
        stopien = len(self.wspolczynniki) - 1
        for potega, wspolczynnik in enumerate(self.wspolczynniki):
            if wspolczynnik != 0:
                if potega == stopien:
                    wyrazy.append(str(wspolczynnik))
                else:
                    if potega == stopien - 1:
                        wyrazy.append(f"{wspolczynnik}x")
                    else:
                        wyrazy.append(f"{wspolczynnik}x^{stopien - potega}")
        return " + ".join(wyrazy)

    def __add__(self, other):
        if len(self.wspolczynniki) > len(other.wspolczynniki):
            nowe_wspolczynniki = self.wspolczynniki.copy()
            for i in range(len(other.wspolczynniki)):
                nowe_wspolczynniki[i] += other.wspolczynniki[i]
        else:
            nowe_wspolczynniki = other.wspolczynniki.copy()
            for i in range(len(self.wspolczynniki)):
                nowe_wspolczynniki[i] += self.wspolczynniki[i]
        return Wielomian(nowe_wspolczynniki)

    def __sub__(self, other):
        if len(self.wspolczynniki) > len(other.wspolczynniki):
            nowe_wspolczynniki = self.wspolczynniki.copy()
            for i in range(len(other.wspolczynniki)):
                nowe_wspolczynniki[i] -= other.wspolczynniki[i]
        else:
            nowe_wspolczynniki = [-wspolczynnik for wspolczynnik in other.wspolczynniki]
            for i in range(len(self.wspolczynniki)):
                nowe_wspolczynniki[i] += self.wspolczynniki[i]
        return Wielomian(nowe_wspolczynniki)

    def stopien(self):
        return len(self.wspolczynniki) - 1

w1 = Wielomian([1, -2, 2])
w2 = Wielomian([3, 1, -2, 1])

print("w1:", w1)  # Output: w1: 1x^2 - 2x^1 + 2
print("w2:", w2)  # Output: w2: 3x^3 + x^2 - 2x^1 + 1

w3 = w1 + w2
print("w3:", w3)  # Output: w3: 3x^3 + 2x^2 - 4x^1 + 3

w4 = w1 - w2
print("w4:", w4)  # Output: w4: -3x^3 -

## zad 2
lista_slow = ['apple', 'banana', 'pomergranate', 'plum', 'orange', 'melon', 'cherry', 'watermelon']

dlugosci_slow = [len(slowo) for slowo in lista_slow if 'u' in slowo or 'o' in slowo]

print(dlugosci_slow)
 ## zad 3
def calculate_power_product(n, *args):
    power_product = 1
    for num in args:
        power_product *= num ** n
    return power_product
result = calculate_power_product(2, 1, 2, 3, 4, 5)
print(result)  # Output: 14400

result = calculate_power_product(3, 2, 3, 4)
print(result)  # Output: 13824
## zad 4
def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def fibonacci_iterative(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n+1):
            a, b = b, a + b
        return b
#zad 5
wyraz = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."

# Usunięcie spacji i innych symboli
wyraz = ''.join(c for c in wyraz if c.isalnum())

# Wyświetlenie co czwartej litery w odwrotnym porządku
print(wyraz[::-4])
#zad 6
def print_unique_values(lst):
    unique_values = list(set(lst))
    for value in unique_values:
        print(value)

