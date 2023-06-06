
# #WAP to create a billing system (product, price, auality,total,all_total) for the function
name = input("Please enter your name:   ")
print("Namaskar "+name+" ji")

   
def calculate_bill():
    all_total = 0
    num_product = int(input("Enter the number of products: "))
    for i in range(num_product):
        product = input("Enter product name: ")
        price = int(input("Enter product price: "))
        quantity = int(input("Enter product quantity: "))
        total = price * quantity
        print("You buy product total price:  "+ str(total)+"\n\n")
        all_total += total
    print("You buys in the total price: "+"\n"+str(all_total))
calculate_bill()


