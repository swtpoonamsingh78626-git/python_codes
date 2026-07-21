# DICTIONARY METHODS :-

i = {
    "name":"yashvi",
    "age":"10",
    "is_young":"True"
}
print(i.keys())# gets you the keys.
print(i.values())# gets you the values.
print(i.items())# gets you the items.
print(i.get("age"))# gets you the item you want.
i.update({"age":"11"})# updates a key pair.
print(i)
print(list(i.keys()))
print(list(i.values()))
print(set(i.values()))
print(set(i.keys()))
print(len(i))
