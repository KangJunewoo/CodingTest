'''
타일링 유형 또한 dp.

'''

n = int(input())
d = [0] * 1001

d[1] = 1
d[2] = 3
for i in range(3, n+1):
    d[i] = (d[i-1] + 2*d[i-2]) % 796796 # 전거에 2*1를 놓던지, 전전거에 2*2 혹은 1*2 두개를 놓던지.

print(d[n])
