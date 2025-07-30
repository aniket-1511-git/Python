'''
Scenario:
Simulate adding/removing items and computing the bill in an online store.
What you’ll learn:
Real-world application of classes
Encapsulation and methods
Task:
Design a ShoppingCart class with add, remove, and total methods.
Example:
Add "Book" (2 × 200) and "Pen" (5 × 20); show total.
Expected Output:
500
'''
class ShoppingCart:
    def __init__(self):
        self.items = {}  

    def add(self, i, q, p):
        if i in self.items:
            current_qty, current_price = self.items[i]
            self.items[i] = (current_qty + q, p)
        else:
            self.items[i] = (q, p)

    def remove(self, i):
        if i in self.items:
            del self.items[i]
        else:
            print(f"{i} not in cart.")

    def total(self):
        total = 0
        for i, (q, p) in self.items.items():
            total += q * p
        return total
    
c1 = ShoppingCart()
c1.add("Book", 2, 200)
c1.add("Pen", 5, 20)
print("Total:", c1.total())  

    