# Yusuf Al zoubi 

upc = input("Please enter the UPC-A barcode: ")            #Asking user for input
while not upc.isdigit():
    print ("Error: UPC-A must contain only digits.")       #Determine the input must be only digits
    upc = input("Please enter the UPC-A barcode: ")        #Asking the user for another input 

if len(upc) != 12:                                         #Determine the length of the input
    print ("Error, the UPC-A barcode must be 12 digits")
    upc = input("Please enter the UPC-A barcode: ")        #Asking the user for another input 

digits = []
for x in upc:                                              #Convert strings to integers
    digits.append(int(x))

odd_positions = digits[0::2]                               #Slicing the list to get the odd positions
sum_odds = sum(odd_positions)
odd_x_3 = sum_odds * 3
even_positions = digits[1:-1:2]                             #:-1: means without the last value (check digit)
'''chick_digit = even_positions[-1]'''
result = odd_x_3 + sum(even_positions)
reminder = result%10                                        #calculate the reminder
check_digit = digits[-1]

if reminder == 0:                                           
    check_digit = 0
else:
    check_digit = 10 - reminder

if check_digit == digits[-1]:                               #compare the calculated check digit with the provided one 
    print(f"The UPC-A {upc} is valid ✅")
else:
    print(f"The UPC-A {upc} is invalid ❌")


