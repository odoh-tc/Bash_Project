def get_single_digit(number):
    if len(number) == 1 and number.isdigit():
          return True
    else:
          return False

while True:
   num = input("Enter a number: ")
   if get_single_digit(num):
       print("Valid single digit")
       break
   else:
       print("Not Valid single digit")

print("single digit you enter is: " + num)
