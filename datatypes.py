"""
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType

"""

x = 5
print(type(x))

a = "abu shahma"
print(type(a))

b =  1j
print(type(b))

c = ["apple", "banana", "cherry"]
print(type(c))

d = ("apple", "ananas", "papaya")
print(type(d))

e = range(6)
print(type(e))

f = {"name", "john", "age", "36"}
print(type(f))

g = frozenset({"apple", "banana", "cherry"})
print(type(g))

h = True
print(type(h))

i = b"hello"
print(type(i))

j = bytearray(5)
print(type(j))

k = memoryview(bytes(5))
print(type(k))

l = None
print(type(l))