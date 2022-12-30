sh = input("enter hours: ")
sr = input("enter rate: ")
try:
    fh = float(sh)
    fr = float(sr)
except:
    print("숫자로 입력해주세요!")
    quit()
print(fh,fr)
if fh > 40 :
    reg = fr *fh
    otp = (fh - 40) * (fr * 0.5)
    xp = reg + otp
else:
    xp = fh * fr
print("pay:",xp)
