x,y = input().split()
x=int(x)
y=int(y)

def Primo(a):
    Divisiones = 0
    if a==1:
        return True
    else:
        for i in range(1,a+1):
            if a % i == 0:
                Divisiones = Divisiones +1
                if Divisiones >2:
                    return False
        if Divisiones < 2:
            return False
        elif Divisiones ==2:
            return True
if(x>0 and y<=10000000):
    for i in range(x,y+1):
        if i>=1 and i<=9:
            resultado=Primo(i)
            if resultado!=False:
                print(i)
        elif(i>=10 and i<=99):
            d=i//10
            resultadod=Primo(d)
            resultado=Primo(i)
            if(resultadod!=False and resultado!=False):
                print(i)
        elif(i>=100 and i<=999):
            c=i//100
            d=i//10
            resultadoc=Primo(c)
            resultadod=Primo(d)
            resultado=Primo(i)
            if(resultadoc!=False and resultadod!=False and resultado!=False):
                print(i)
        elif(i>=1000 and i<=9999):
            m=i//1000
            c=i//100
            d=i//10
            resultadom=Primo(m)
            resultadoc=Primo(c)
            resultadod=Primo(d)
            resultado=Primo(i)
            if(resultadom!=False and resultadoc!=False and resultadod!=False and resultado!=False):
                print(i)
        elif(i>=10000 and i<=99999):
            dm=i//1000
            m=i//1000
            c=i//100
            d=i//10
            resultadodm=Primo(dm)
            resultadom=Primo(m)
            resultadoc=Primo(c)
            resultadod=Primo(d)
            resultado=Primo(i)
            if(resultadodm!=False and resultadom!=False and resultadoc!=False and resultadod!=False and resultado!=False):
                print(i)
        elif(i>=100000 and i<=999999):
            cm=i//10000
            dm=i//1000
            m=i//1000
            c=i//100
            d=i//10
            resultadocm=Primo(cm)
            resultadodm=Primo(dm)
            resultadom=Primo(m)
            resultadoc=Primo(c)
            resultadod=Primo(d)
            resultado=Primo(i)
            if(resultadocm!=False and resultadodm!=False and resultadom!=False and resultadoc!=False and resultadod!=False and resultado!=False):
                print(i)
        elif(i>=1000000 and i<=10000000):
            M=i//100000
            cm=i//10000
            dm=i//1000
            m=i//1000
            c=i//100
            d=i//10
            resultadoM=Primo(M)
            resultadocm=Primo(cm)
            resultadodm=Primo(dm)
            resultadom=Primo(m)
            resultadoc=Primo(c)
            resultadod=Primo(d)
            resultado=Primo(i)
            if(resultadoM!=False and resultadocm!=False and resultadodm!=False and resultadom!=False and resultadoc!=False and resultadod!=False and resultado!=False):
                print(i)
else:
    print("Valores Invalidos")
            
        