def solve(exp):
  st = []
  for char in exp:
    #Push every character except closed bracket
    if (char != ")"):
      st.append(char)
      
    else:
      #Check if top element is open bracket
      if (st[-1] == "("):
        return "true"
        
      #Pop elements till open bracket is on top
      else:
        while (st[-1] != "("):
          st.pop()
        #Pop the open bracket
        st.pop()
      
  return "false"

exp = input()
print(solve(exp))
