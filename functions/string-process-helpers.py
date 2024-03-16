# str (string) < methods

# 'Dorin'
# ' dorin '
# ' DOrin '
# ' dORin '

def removeSpace(name):
    name_ = name.strip()
    return(name_)

def fixCase(name):
    name_ = name.capitalize()
    return name_

##############################
#correct_name = fixCase(removeSpace('  dORin '))

#HW: rewrite the code so functions pass variable 
name_nospace= removeSpace('  dORin ')
correct_name = fixCase(name_nospace)
print(f"|{correct_name}|")
