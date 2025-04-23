class String:
    def __init__(self, value=""):
        self.value = value

    def __iadd__(self, other):
        """Overloads the += operator to concatenate strings."""
        if isinstance(other, String):
            self.value += other.value
        elif isinstance(other, str):
            self.value += other
        else:
            raise TypeError("Can only concatenate String or str objects.")
        return self

    def toLower(self):
        """Converts the string to lowercase."""
        self.value = self.value.lower()

    def toUpper(self):
        """Converts the string to uppercase."""
        self.value = self.value.upper()

    def __str__(self):
        """Returns the string representation."""
        return self.value



s1 = String("Hello")
s2 = String("World")


s1 += " "
s1 += s2
print("After concatenation:", s1)

s1.toLower()
print("To lowercase:", s1)


s1.toUpper()
print("To uppercase:", s1)
