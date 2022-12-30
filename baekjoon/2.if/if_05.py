H,M = map(int,input().split())
if  M < 45 :
    if H == 0 :
        print(23,M+15)
    else :
       print(f'{H-1} {M+15}')             
elif  M >= 45 :
       print(f'{H} {M-45}') 






