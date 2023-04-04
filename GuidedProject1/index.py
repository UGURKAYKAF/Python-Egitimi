# my_name = "ugur"
# my_surname = "kaykaf"
# my_age = 21
# ID_number = 123456789
# where_i_live = "İstanbul"
# health_i_insurance = True 
# my_mationality = "Turkey"
# print (f"My name is {my_name} {my_age} I am {str(my_age)} years old, I live in {where_i_live}")

item_list = ['Laptop', 'Headset', 'Second monitor', 'Mousepad', 'USB Driver', 'External Driver']
mandatory_item_list = item_list[0:3]
optional_item_list = item_list[3:6]
print(item_list)
print(mandatory_item_list)
print(optional_item_list)

limit = 5000
price_sheet = {
    'Laptop':1500,
    'Headset':100,
    'Second monitor':200,
    'Mousepad':50,
    'USB Driver':70,
    'External driver':250
}
cart = []
def add_to_cart (item,quantity):
    cart.append((item,quantity))
    item_list.remove(item)

def create_invoice():
    total_amount_inc_tax = 0
    for item,quantity in cart:
        price = price_sheet[item]
        tax = 0.18 * price
        total = (tax + price) * quantity
        total_amount_inc_tax += total
        print('Item:',item,'\t','Price:',price,'\t','Quantity:',quantity,'\t','Tax:',tax,'\t','Total:',total,'\n')
    
    print("After the taxes are applied the total amount is:",'\t',total_amount_inc_tax)
    
    return total_amount_inc_tax

def checkout():
    global limit
    total_amount = create_invoice()
    if limit==0:
        print("You don't have any budget")
    elif total_amount > limit:
        print("The amount you have to pay is aboce the spending limit. You have to drop some items.")
    else:
        limit -= total_amount
        print(f"The total amount (inc1, taxes) you've paid is {total_amount}. You've {limit} dollars left")

add_to_cart("Laptop",1)
add_to_cart("Headset",8)
add_to_cart("Second monitor",1)
add_to_cart("Mousepad",1)
add_to_cart("USB Driver",2)
add_to_cart("External dirver",4)
checkout()