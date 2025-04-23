names = {"Alice", "Andrew", "Ava", "Ben", "Bella", "Brian", "Amanda", "Bob"}

a_names = {name for name in names if name.startswith('A')}
b_names = {name for name in names if name.startswith('B')}

print("Names starting with A:", a_names)
print("Names starting with B:", b_names)
