apparel_type = input("What is the type of your item? ")
color = input("What is the color of your item? ")
quantity = int(input("How many of this item do you wish to purchase? "))
value = float(input("What is the value of one item? "))
total_cost = quantity * value

print(f"You have selected the {color} {apparel_type}.")
print(f"You will be purchasing {quantity} {apparel_type}(s) at a cost of ${value} each.")
print(f"The total price is ${total_cost}.")