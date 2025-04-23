names_set = set()

names_set.update(["Alice", "Bob", "Charlie", "David", "Emma"])

names_set.discard("Charlie")
names_set.add("Chris")

names_set.discard("Bob")
names_set.discard("Emma")

print(names_set)
