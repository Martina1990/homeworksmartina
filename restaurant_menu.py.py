restaurant_menu = {}

while True:
    dish = raw_input("Enter a dish: ")
    price = raw_input("Enter a price for %s: " % dish)
    print "Your dish is: " + dish + " " + price

    restaurant_menu[dish] = price

    new_dish = raw_input("Would you like to enter another dish? (yes/no): ").strip().lower()

    if new_dish == "no":
        break

print "Menu of the Day: %s" % restaurant_menu

with open("menu.txt", "w+") as restaurant_menu_file:
    for dish in restaurant_menu:
        restaurant_menu_file.write("%s: %s Euro\n" % (dish, restaurant_menu[dish]))