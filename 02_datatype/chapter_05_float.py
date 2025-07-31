from fractions import Fraction
from decimal import Decimal, getcontext

ideal_temp=36.5
current_temp = 45.5555555555

print(f"temparture difference is {current_temp-ideal_temp}")

ideal_temp1=36.5
current_temp1 = 45.55

print(f"temparture difference in other format {current_temp1-ideal_temp1}")

# Output
# by change some numbers of floating value can give differnt value which not inteted that is caled as floating point presion error
# ---- like this ------
# temparture difference is 9.0555555555
# temparture difference in other format 9.049999999999997

#  to resolve the this issue python use different modules for accurate results like 
# fraction - this can handle up to computer memory get run out  (unlimted) but it work with numerator, denominator optaiton to use it 
# decimals - this can handle by user how much we want to handle (user define)

# --- for Decimal ----

#getcontext() gives current values for result that we can get after calculation
print(getcontext())
#Context(prec=28, rounding=ROUND_HALF_EVEN, Emin=-999999, Emax=999999, capitals=1, clamp=0, flags=[], traps=[InvalidOperation, DivisionByZero, Overflow])

print(f"normal division {(1/7)}")
#normal division 0.14285714285714285

print(f"Decimial based operation with try to give more precise value{Decimal(1)/Decimal(7)}")
# Decimial based operation with try to give more precise value0.1428571428571428571428571429


# we can even set precise context as well where we can set how much decimal point number we want 
getcontext().prec= 7
print(getcontext())

#Context(prec=7, rounding=ROUND_HALF_EVEN, Emin=-999999, Emax=999999, capitals=1, clamp=0, flags=[Inexact, Rounded], traps=[InvalidOperation, DivisionByZero, Overflow])
print(f"Decimial based operation with try to give more precise value{Decimal(1)/Decimal(7)}")
#Decimial based operation with try to give more precise value 0.1428571

#Read More on https://docs.python.org/3/library/decimal.html

# --- for Fractions ----
# we can use fraction module like following to form opration like addintion and other but we have to write it done in numerator, denominator Fashion 
print(Fraction(1, 2)) #Output : 1/2

print(Fraction(4555555,100000)-Fraction(365,10)) #  Output 181111/20000
#to have floating value we have type cast it in float 
subtration=Fraction(4555555,100000)-Fraction(365,10)
print(f"fractions result {float(subtration)}")   # Output  fractions result 9.05555
 # Read More on https://docs.python.org/3/library/fractions.html



