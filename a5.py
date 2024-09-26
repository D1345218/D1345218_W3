a = int (input('輸入三位數字')) 
b = a%10
d = a//100
c= a//10 - d*10
print('結果:',b,c,d,sep="")