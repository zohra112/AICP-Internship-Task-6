#Main menu
print("\t\t\t\t    Main Menu\n")
print("\t\t-----------------------------------------------\n")
print("\t\t  SYMBOLS\t  ITEMS\t  WEIGHTS\t  PRICES\n")
print("\t\t-----------------------------------------------\n")
print("\t\t     C\t    Cement\t  24.9KG to 25.1KG\t  3$\n")
print("\t\t     S\t    Sand\t  49.5KG to 50.1KG\t  2$\n")
print("\t\t     G\t    Gravel\t  49.5KG to 50.1KG\t  2$\n")
print("\t\t-----------------------------------------------\n\n")

c_sack = int(input("\t\tEnter the number of cement sacks: "))
g_sack = int(input("\t\tEnter the number of gravel sacks: "))
s_sack = int(input("\t\tEnter the number of sand sacks: "))

actual_price = (c_sack * 3) + (g_sack * 2) + (s_sack * 2)
total_order = c_sack + g_sack + s_sack

rej = 0
total_weight = 0

for count in range(1, total_order + 1):
    print()
    content = input("\t\tEnter the content of a sack, C for cement, G for gravel, and S for sand: ").upper()
    weight = 0

    if content == 'C':
        while True:
            weight = float(input("\t\tEnter weight of cement sack between 24.9KG and 25.1KG: "))
            if 24.9 <= weight <= 25.1:
                break
            else:
                print("\t\tSack is underweight or overweight")
    elif content in ['G', 'S']:
        while True:
            weight = float(input(f"\t\tEnter weight of {content} sack between 49.0KG and 50.1KG: "))
            if 49.0 <= weight <= 50.1:
                break
            else:
                print(f"\t\t{content} sack is underweight or overweight")
    else:
        print("\t\tThe entered content is incorrect")

    total_weight += weight

print()
print(f"\t\tThe total weight of the order is: {total_weight}")
print(f"\t\tThe number of sacks rejected are: {rej}")

sp = 0
sp_price = 0

while c_sack >= 1 and g_sack >= 2 and s_sack >= 2:
    sp += 1
    c_sack -= 1
    g_sack -= 2
    s_sack -= 2

if sp >= 1:
    sp_price = sp * 10
    print(f"\t\tTotal special packs are: {sp}")
    print(f"\t\tPrice of special packs in dollars is: ${sp_price}")

    discount_price = (c_sack * 3) + (g_sack * 2) + (s_sack * 2) + sp_price
    print(f"\t\tThe actual price of the order is: ${actual_price}")
    print(f"\t\tThe discounted price of the order is: ${discount_price}")

    total_discount = actual_price - discount_price
    print(f"\t\tTotal discount in the order is: ${total_discount}")
else:
    print(f"\t\tPrice of the regular order in dollars is: ${actual_price}")
  
#Written by Zohra Batool
