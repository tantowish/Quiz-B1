a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

rata1 = (a[0]+a[1]+a[2]+a[3]+a[4])/5
rata2 = (b[0]+b[1]+b[2]+b[3]+b[4])/5
rata3 = (c[0]+c[1]+c[2]+c[3]+c[4])/5

rataan = (rata1+rata2+rata3)/3

if(rataan>75):
    print("Memahami Materi")
else:
    print("Belum Memahami Materi")