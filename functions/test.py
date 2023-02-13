
def addIterest(balance, rate):
  newBalance = balance * (1 + rate)
  balance = newBalance
  
  return newBalance

def test():
  amount = 1000
  rate = 0.05
  amount = addIterest(amount, rate)
  print(amount)
  
  
test()
  