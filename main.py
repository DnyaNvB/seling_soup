import numpy as np

array = list(map(int, input().split()))

is_true = np.zeros(len(array)) # false

pocket = 0

for i in range(len(array)):
  if pocket != 0:
    if (pocket - array[i]) >= 0 and array[i] > 5:
      pocket = pocket - array[i] + 5
      is_true[i] = True
    elif array[i] == 5:
      is_true[i] = True
      pocket = pocket + 5
    elif pocket - array[i] < 5:
      print("No")
      break
  elif array[i] == 5:
        is_true[i] = True
        pocket = pocket + 5
if is_true.all() == True:
  print("yes")
