guests_1 = [ "Bethaney Bain", "Kacey Johns", "Manpreet Saunders" ]
guests_2 = [ "Elwood Curtis", "Diya Griffin", "Kacey Johns" ]
guests_3 = [ "Tobey Weiss", "Tobey Weiss", "Tobey Weiss1" ]

# Concatenate all lists into one
guests = guests_1 + guests_2 + guests_3
print (guests)

# Create an empty list for the final result
guests_fin=[]

# Iterate through the combined list and add each element to the final list
# only if it doesn't already exist in the final list
for elem in guests:
    if elem not in guests_fin:
        guests_fin.append(elem)

# Print the final list 
# Sort the final list alphabetically
print(guests_fin.sort())