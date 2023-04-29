# Do not modify these lines
__winc_id__ = '62311a1767294e058dc13c953e8690a4'
__human_name__ = 'casting'

# Add your code after this line
leek_price = 2
order_leek = 'leek 4'
x = order_leek[order_leek.find('4'):6] # x is number extracted from string
int_x = int(x)
sum_total = leek_price*int_x

broccoli_price = 2.34
order_broccoli = 'broccoli 1.6'
y = order_broccoli[order_broccoli.find('1.6'):(order_broccoli.find('6'))+1]  # y is number extracted from string
int_y = float(y)
""" This time we do not use int function to convert the string to number,
becasue we will get a decimal number and this cant be an integer"""
sum_total_broc = round(broccoli_price*float(y),2) # round number to 2 decimal points


print(f"Leek is {leek_price} euro per kilo.")
print(sum_total)
print(f"1.6kg broccoli costs {sum_total_broc}e")

