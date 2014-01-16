# A recipe for a few disasters

# ask user for file to glitch
glitchfile = raw_input("Enter a file to glitch:")

def fileroot(x):
  root = ""
  for y in x:
    if y!=".":
      root+=y
    else:
      break
    return root
    
# ideas for other functionality?
  # 
  # overwrite random
  # auto-add the header/footer?
  # 
  
  

"""
readfile=open(glitchfile, "r")

with open(fileroot(glitchfile)+"_"+glitch_method, "w") as writefile: #update glitch method once a method is chosen
  
  #interval backwards overwrite (add amount=raw_input("Interval amount:")
  
  outfile = ""
  backwards = ""
  for x in range(len(readfile)-1,-1,-1):
    backwards += readfile[x]
  for x in range(len(readfile)):
    if x % amount = 0:
      outfile += backwards[x]
    else:
      outfile += readfile[x]
  writefile.write(outfile)

"""



#overwrite by interval
