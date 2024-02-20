#algorithms with somple and multi lists.
# aggregation - ? HW1
#  - sum


# COVID-19
# number of case by cities
cases = [50 , 10, 100, -1, 0, 55, -1, 150, 0]  # 5 cities
#ALG1: calc total/sum of values
#s = cases[0] + cases[1] + cases[2] + cases[3] + cases[4]


#s = 0
#for c in cases:
#    if c >= 0:
#        s += c
#print("Total cases: ", s)

product_cat_prices = [ 0.50, 10.00, 1.50, 5.50, 2.50]

# ALG1: 
#discount = 0.9 
#for i in range (len(product_cat_prices)):
#    if product_cat_prices[i] > 5.00:
#        product_cat_prices[i] = product_cat_prices[i] * discount

# ALG2: print+iter+index

#for i in range (len(product_cat_prices)):
#    print(i,") ", product_cat_prices[i])


# 5 start rating for users / int
rating = [ 5, 3, 1, 4, 5, 2, 5]   #7 users
# index    0  1  2  3  4  5  6
print("USERNAME | rating")
#ALG 1: iter + print

for i in range (len(rating)):
    print("user", i + 1, "  | ", rating[i], end = " ") #,'*'*rating[i])

    for r in range (rating[i]):
        print("*", end ="")

    print()

