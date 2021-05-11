integer = 11
float = 3.141
string = "Texto"
print("Mi texto {:d}".format(integer)) # :d decimal
print("Mi texto {:x}".format(integer)) # :d hexadecimal
print("Mi texto {:b}".format(integer)) # :d binario
print("Mi texto {:f}".format(float)) # :d float
print("Mi texto {:s}".format(string)) # :d string

sentence = "Mi nombre es {name} y tengo un {what}".format(
    name = "Andres",
    what = "curso"
)

print(sentence) 