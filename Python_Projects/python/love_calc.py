print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")


combine_name = name1 + name2
lower_case = combine_name.lower()

t = lower_case.count("t")
r = lower_case.count("r")
u = lower_case.count("u")
e = lower_case.count("e")

true = t + r + u + e

l = lower_case.count("l")
o = lower_case.count("o")
v = lower_case.count("v")
e = lower_case.count("e")

love = l + o + v + e

score1 = int(str(true) + str(love))

if (score1 < 10) or (score1 > 90):
  score = str(score1)
  print("Your score is " + score + ", you go together like coke and mentos.")
elif (score1 >= 40) and (score1 <= 50):
  score = str(score1)
  print("Your score is " + score + ", you are alright together.")
else:
  score = str(score1)
  print("Your score is " + score + ".")
