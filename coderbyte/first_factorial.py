# challenge: https://coderbyte.com/information/First%20Factorial

def FirstFactorial(num):

  # code goes here
  f = 1
  for n in range(1, num+1):
    f *= n
  return f

# keep this function call here 
print FirstFactorial(raw_input())
