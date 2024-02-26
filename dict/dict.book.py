book = {
# key  :    value
"year" : 2020,
"title": 'Python Programming Basics',
"author": 'John Doe'
}

print("The book: ", book["title"])
print("Published on : ", book["year"])
print("Authored by : ", book["author"])

if book["year"] >= 2020:
    print("This book is fresh")
else:
    print(" This is not a fresh book")