#real_data < source: API, Database, Keyboard, File

meeting_presense = [
    "Alex",
    "Alexandru",
    "Stefan",
    "Habib",
    "Livia",
    "Victor",
    "X",
    "Serghei",
    "Stepan"
]

print("Students present at the meeting:  ", len(meeting_presense))

for s in meeting_presense:
    print(s)


#####################################
#  search iterative
name = input ("Who? ")
for s in meeting_presense:
    if s == name:
        print(name, "found!!!")
        
