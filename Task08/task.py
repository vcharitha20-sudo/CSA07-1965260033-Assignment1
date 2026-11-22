DATA=[[1,0,1,1],[0,1,0,0],[1,1,1,0],[0,0,1,1]]
def add_parity(block):
    rows=[r+[sum(r)%2] for r in block]
    return rows+[[sum(c)%2 for c in zip(*rows)]]
def correct(frame):
    bad_rows=[i for i,row in enumerate(frame) if sum(row)%2]
    bad_cols=[j for j in range(len(frame[0])) if sum(row[j] for row in frame)%2]
    if not bad_rows and not bad_cols:return 'no error'
    if len(bad_rows)==len(bad_cols)==1:
        r,c=bad_rows[0],bad_cols[0];frame[r][c]^=1
        return ('corrected',r,c)
    return 'uncorrectable'
sent=add_parity(DATA)
for flips in ([],[(1,2)],[(0,0),(2,3)],[(0,0),(0,1)],[(4,2)]):
    rx=[r[:] for r in sent]
    for r,c in flips:rx[r][c]^=1
    print('flipped',flips,'->',correct(rx),'data intact:',rx==sent)
