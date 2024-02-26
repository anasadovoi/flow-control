#MOTIVATION


#PRODUCT DATA
#1. separate variables
product_name  = "Simple Product"
product_price = 100
product_avail = True


if product_price <500:
    print("The product", product_name, "is cheap")

#2. group it as a list
product = ["Simple Product", 100, True]

if product[1]<500:
    print("The product", product[0], "is cheap")


#3. group it as a dict
product = {"name":"Simple Product",
            "price":100,
            "avail": True}
if product["price"]<500:
    print("The product", product["name"], "is cheap")

