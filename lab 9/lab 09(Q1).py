def count_lower_upper(string):
  counts={"upper":0,"lower":0}
  for i in string:
      if i.isupper():
          counts["upper"] +=1
      elif i.islower():
          counts["lower"] +=1
      return counts

string = input()
print(count_lower_upper(string))