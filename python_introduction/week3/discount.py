# User input the original price
price1 = float(input("Please type in the original price:"))

# User input the discount offered
discount = float(input("Please type in the discount offered:"))

def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        return price * (1-discount_percent/100)
    else:
        return price
    
    
if __name__ == "__main__":
    print(calculate_discount(price1, discount))