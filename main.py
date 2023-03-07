print("Welcome to the roolarcoster")
Height=int(input("Enter the Height in cm:"))
if Height >120:
  print("you can ride")
  Age=int(input("Enter the age "))
  if Age ==18:
    print("You can pay $12")
  elif Age ==12:
    print("You can pay $5")
  elif Age >22:
    print("You can pay $15")
  else:
    print("You can pay $7")
else:
  print("Sorry you can't ride")



