enter = int(raw_input("Please enter a number between 1 and 100: "))
print enter

for number in range(1, enter+1):        #verstehe nicht warum hier "for number" und nicht "for enter" zu verwenden ist
    if number%3 == 0 and number%5 == 0: #und warum bei range "1" am Anfang steht, damit es funktioniert.
        print "fizzbuzz"
    elif number%3 == 0:
        print "fizz"
    elif number%5 == 0:
        print "buzz"
    else:
        print number