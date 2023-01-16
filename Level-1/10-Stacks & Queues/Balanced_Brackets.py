def solve(exp):
  st = []
  bracketPairs = {"{": "}", "[": "]", "(": ")"}
  closedBrackets = [*bracketPairs.values()]
  
  for char in exp:
    #Push every character except closed bracket
    if (char in bracketPairs):
      st.append(char)
      
    else:
      #Pass if the character is not a closing bracket
      if (char not in closedBrackets):
        pass
        
      else:
        #If stack is empty, then there is an extra closing bracket
        if (len(st) == 0):
          return "false"
        #If top bracket doesn't match
        elif (bracketPairs[st[-1]] != char):
          return "false"
        #If bracket pair matches
        else:
          st.pop()
          
  #If stack is not empty, then there is an extra opening bracket
  if (len(st) != 0):
    return "false"
  else:
    return "true"

exp = input()
print(solve(exp))
