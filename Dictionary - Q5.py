grocery_prices = {'apple' : 160,'banana' : 40,'orange' : 100,'pineapple' : 60,'mango' : 200}
grocery_quantity = {'apple' : 2,'banana' : 3,'orange' : 1,'pineapple' : 1,'mango' : 10}

total_bill = 0
for items in grocery_quantity:
    if items in grocery_prices:
        total_bill += grocery_prices[items]*grocery_quantity[items]

print(total_bill)
