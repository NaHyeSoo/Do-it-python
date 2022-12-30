def computepay(hours,rate) :
    #print("In computepay",hours,rate)
    if hours > 40 :
        reg = hours * rate
        otp = (hours - 40) * (rate * 0.5)
        pay = reg + otp
    else:
        pay = hours * rate
    #print("returning",pay)
    return pay

sh = input("enter hours: ")
sr = input("enter rate: ")
fh = float(sh)
fr = float(sr)
# print(fh,fr)
xp = computepay(fh,fr)

print("pay:",xp)
