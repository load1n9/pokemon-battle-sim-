from ../main import Battle
try:
  a = int(input("first pokemon id: "))
  b = int(input("second pokemon id: "))
  test = Battle(a,b)
  for x in test.data["msg"]:
     print(x)
  print(test.data["pokemon"]," won")
except:
  print("something went wrong")
