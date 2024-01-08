#Food Ordering app
li = []
menu = {
    'samosa': 2.50,
    'paneer tikka': 8.99,
    'chicken tikka masala': 12.99,
    'naan': 2.00,
    'butter chicken': 13.99,
    'aloo gobi': 9.50,
    'chana masala': 8.50,
    'rogan josh': 11.99,
    'palak paneer': 10.50,
    'dal makhani': 9.99,
    'biryani': 14.50,
    'tandoori chicken': 11.99,
    'mango lassi': 4.50,
    'gulab jamun': 3.50,
    'raita': 2.50,
    'pakora': 5.50,
    'chicken korma': 12.50,
    'papadum': 1.99,
    'vegetable biryani': 10.99,
    'fish curry': 14.99,
    'matar paneer': 10.99,
    'malai kofta': 11.50,
    'dosa': 9.99,
    'idli': 7.50,
    'vada': 6.99,
    'rasgulla': 3.99,
    'jalebi': 4.50,
    'pav bhaji': 8.99,
    'kheer': 4.99,
    'chole bhature': 9.50,
    'chicken 65': 11.99,
    'mutton curry': 15.50,
    'pani puri': 6.50,
    'samosa chaat': 7.99,
    'chicken biryani': 13.50,
    'lamb rogan josh': 14.50,
    'mango kulfi': 3.99,
    'shahi paneer': 11.99,
    'gajar halwa': 5.50,
}

def order_item():
    order = None
    while order !="done":
        order = input("What do you want? (If completed, type \"done\") ").strip().lower()
        li.append(order)
def get_my_bill():
    my_bill = 0
    for item in li[:-1]:
        my_bill = my_bill+menu[item]
    return my_bill
def display_order():
    for item in li[:-1]:
        print(item.title())
print("Welcome to indian restaurant!")
print("How can we help today?\nOrder(O) \nFeedback(F) \nExit(E)")
choice = input("Choose the option: ").strip().upper()
match choice:
    case "O":
        print("*** Menu ***")
        for i in menu:
            print(i,":",menu[i])
        print("xxxxxxxxxxxxxxxxxxxxxxx")
        #Function to order item
        order_item()
        get_my_bill()
        print("\n**** Your Order ****")
        display_order()
        confirm = None
        while confirm != "y":
            confirm = input("Confirm order? (Y/N) ").strip().lower()
            if confirm == "n":
                display_order()
                delete_item = input("Enter food-item to delete: ").strip().lower()
                li.remove(delete_item)
                display_order()
        payment = get_my_bill()
        print("Total Bill : $.",payment)
    case "F":
        print("Customer feedbacks are always valuable for us! We keep getting better just for you!")
        input("Share your experience: ")
        print("Thank you for sharing it.")
    case "E":
        print("Thank you! visit again")