def checksum(words):
    total=0
    for w in words:
        total+=w
        total=(total&0xffff)+(total>>16)
    total=(total&0xffff)+(total>>16)
    return (~total)&0xffff
def verify(words,csum):
    return checksum(words+[csum])==0
def parity_2d(block):
    rows=[r+[sum(r)%2] for r in block]
    return rows+[[sum(c)%2 for c in zip(*rows)]]
words=[0x4500,0x0054,0x1c46,0x4000,0x4001]
c=checksum(words)
print(f'checksum : {c:04X}')
print('no error :',verify(words,c))
changed=words[:];changed[2]^=0x0100
print('1 word changed :',verify(changed,c))
print('2 words swapped:',verify([words[1],words[0]]+words[2:],c))
for row in parity_2d([[1,0,1,1],[0,1,0,0],[1,1,1,0],[0,0,1,1]]):print(*row)
