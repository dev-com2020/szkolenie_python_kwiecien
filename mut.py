def zmien_string(string):
    return string + "a"


string = "słow"

print(zmien_string(string))
print(zmien_string(string))
print(zmien_string(string))

s = ""

for i in range(10):
    s = s + "a"
# to jest zły pomysł, tworzy nam 11 sztuk zmiennej a

l = []

def zmien_liste(lista):
    return lista.append(1)

zmien_liste(l)
zmien_liste(l)
zmien_liste(l)
print(l)

