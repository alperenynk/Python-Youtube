# Dictionary = a collection of {key:value} pairs
#              ordered and changeable. No duplicates

capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Türkiye": "Ankara",
            "Russia": "Moscow"}

print(capitals.get("USA"))
for key in capitals.keys():
    print(key)
for value in capitals.values():
    print(value)
for key, value in capitals.items():
    print(f"{key}: {value}")
for item in capitals.items():
    print(item)

# print(dir(capitals))
# print(help(capitals))
