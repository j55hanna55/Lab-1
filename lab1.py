#Ask user to enter the cents
cent = int(input('How many cents ? '))
qt="quarter"
dm="dime"
py="penny"
rem1=cent%25
quarter=int((cent-rem1)/25)
rem2=rem1%10
dime=int((rem1-rem2)/10)
rem3=rem2%5
penny=rem3
if(quarter>1):
   qt="quarters"
if(dime>1): 
   dm="dimes"
if(penny>1):
   py="pennies"
   
#display the output 
print(quarter,qt,",",dime,dm,penny,py)
