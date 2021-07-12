def multiply(n1, n2):
    return n1*n2

def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def divide(n1,n2):
    return n1 / n2

def exponent(n1, n2):
    return n1**n2 

def pemdas(n1,n2,n3,n4,n5,n6):
    result = 0 
    result += exponent(n1, n2)
    result = multiply(result, n3)
    result = divide(result, n4)
    result = add(result, n5)
    result = subtract(result, n6)

    return result 

print(pemdas(1,2,3,4,5,6))

def poodas(n1,n2,n3,n4,n5,n6):
    result = ((((n1**n2)*n3)/n4)+n5)-n6
    return result

print(poodas(1,2,3,4,5,6))




# total of items
# apply sales tax
# apply membership fee
# apply discount

### UNREFACTORED
def order_summary(item_prices):

    sales_tax_rate = .08
    sub_total = 0

    for price in item_prices:
        sub_total += price

    sales_tax_total = float(sub_total * sales_tax_rate)
    grand_total = float(sub_total + sales_tax_total)

    sub_total = "$ {:.2f}".format(sub_total)
    grand_total = "$ {:.2f}".format(grand_total)
    sales_tax_total = "$  {:.2f}".format(sales_tax_total)

    return (f"""
        **** Order Summary ****\n  
        Item(s) Subtotal:  {sub_total}
        Sales Tax:         {sales_tax_total}
        --------------
        Grand Total:       {grand_total}""")    

print(order_summary([20,20]))



### HELPER FUNCTIONS

def calculate_subtotal(item_prices):
    total = 0
    for price in item_prices:
        total += price
    return float(total)

def calculate_sales_tax(total):
    sales_tax_rate = .08
    sales_tax_total = total * sales_tax_rate
    return float(sales_tax_total)

def display_order_summary(item_prices):
    sub_total = calculate_subtotal(item_prices)
    sales_tax_total = calculate_sales_tax(sub_total) 
    grand_total = sub_total + sales_tax_total

    sub_total = "$ {:.2f}".format(sub_total)
    grand_total = "$ {:.2f}".format(grand_total)
    sales_tax_total = "$  {:.2f}".format(sales_tax_total)

    return (f"""
        **** Order Summary ****\n  
        Item(s) Subtotal:  {sub_total}
        Sales Tax:         {sales_tax_total}
        --------------
        Grand Total:       {grand_total}""")  

# print(order_summary([20,20]))