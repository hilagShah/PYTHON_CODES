grocery_prices = {'apple' : 160,'banana' : 40,'orange' : 100,'pineapple' : 60,'mango' : 200}

customers = {
'veer' : {'apple' : 2,'banana' : 3,'orange' : 1,'pineapple' : 1,'mango' : 10},
'hemang' : {'apple' : 3,'banana' : 9,'orange' : 1,'pineapple' : 4,'mango' : 20},
'shivam' : {'apple' : 6,'banana' : 7,'orange' : 1,'pineapple' : 8,'mango' : 10}
}


for customer,items in customers.items():
    total_bill = 0
    for item,quantity in items.items():
        total_bill += grocery_prices[item]*quantity
    print(customer,':',total_bill)
