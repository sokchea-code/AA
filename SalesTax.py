#prompt the user for input
purchaseAmount=eval(input("Enter purchase amount: "))
#Compute sales tax

tax = purchaseAmount * 0.06

#Display the tax amount with two digit after decimal point 
print("sales tax is", int(tax * 100)/100.0)