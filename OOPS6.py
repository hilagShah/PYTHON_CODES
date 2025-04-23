class Date:
    def __init__(self, day, month, year):
        self.date = [day, month, year]

    def __eq__(self, other):
        """Overloads the == operator to compare two Date objects."""
        if not isinstance(other, Date):
            return NotImplemented
        return self.date == other.date

    def display(self):
        print(f"{self.date[0]:02d}-{self.date[1]:02d}-{self.date[2]}")


d1 = Date(20, 4, 2025)
d2 = Date(20, 4, 2025)
d3 = Date(21, 4, 2025)

print("Date 1:", end=" ")
d1.display()
print("Date 2:", end=" ")
d2.display()
print("Date 3:", end=" ")
d3.display()


print("\nIs Date 1 equal to Date 2?", d1 == d2)  
print("Is Date 1 equal to Date 3?", d1 == d3)    
