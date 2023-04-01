# Zadanie 2. Napisz funkcję sprawdzającą czy podane liczby są
# liczbami pierwszymi w szybszy sposób niż w przykładzie. (jakim przykladzie?)
# Do funkcji można przekazać dowolną liczbę argumentów (liczby). Liczby 0 i 1 nie są liczbami pierwszymi. (10%)




def isPrime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            return False
    return True

def arePrime(*numbers):
    wynik = " "
    for number in numbers:
        if not isPrime(number):
            wynik =str(number)+" is not prime"
        else:
            wynik =str(number)+" is  prime"

        print(wynik)

arePrime(3,4,5,6,7,8,9)


