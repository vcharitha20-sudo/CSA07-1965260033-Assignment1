FLAG='01111110'
def stuff(bits):
    out='';ones=0
    for b in bits:
        out+=b
        ones=ones+1 if b=='1' else 0
        if ones==5:out+='0';ones=0
    return FLAG+out+FLAG
def unstuff(frame):
    body=frame[8:-8];out='';ones=0;i=0
    while i<len(body):
        out+=body[i];ones=ones+1 if body[i]=='1' else 0
        if ones==5:i+=1;ones=0
        i+=1
    return out
for data in ('0110111110110','01111110','1111111111','1010101','00110011'):
    f=stuff(data)
    print('data',data,'sent',f[8:-8],'extra bits',len(f)-len(data)-16,'restored',unstuff(f)==data)
