class Train:

    def __init__(self, cars):
        self.cars = cars

    def __iter__(self):
        for i in range(self.cars):
            yield f'car #{i+1}'


t = Train(10)

for car in t:
    print(car)

print(f'Imprimindo da lista {list(t)[3]}')

print(t.__dict__)

a = 'MA'
print(a[0])

countries = {'BR': 'Brasil', 'CN': 'China'}
print(countries['BR'])

print(countries.get('NA', 'Nao Encontrei'))

a, b, c = [10, 20, 30]

a, b, c, *rest = [10, 20, 30, 40, 50]
print(a, b, c, rest)



nome = 'Marcos'

s = nome[:1]
print(s)
s = nome[:2]
print(s)
s = nome[:3]
print(s)
s = nome[:4]
print(s)
s = nome[:5]
print(s)
s = nome[:6]
print(s)


e = {n for n in range(10) if n % 2 == 0}
print(e)
