import itertools

def PlusMinus(num):
  # code goes here

  str_num = str(num)
  arr = [int(dig) for dig in str_num]
  signs = list(itertools.product("-+", repeat=len(arr)-1))
  final_signs = []

  for s in signs:
    total = arr[0]
    for i in range(len(arr) - 1):
      if s[i] == '+':
        total += arr[i+1]
      else:
        total -= arr[i+1]
      if total == 0:
        if final_signs:
          if s.count('-') > final_signs.count('-'):
            final_signs = s
        else:
          final_signs = s

  if final_signs:
    return ''.join(final_signs)
  else:
    return ' not possible'


# keep this function call here 
print PlusMinus(19395223423493)