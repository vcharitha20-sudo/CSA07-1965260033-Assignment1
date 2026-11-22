import struct
import zlib

def mac_bytes(text):
    return bytes(int(part,16) for part in text.split(':'))
def mac_text(raw):
    return ':'.join(f'{b:02x}' for b in raw)
def build(dst,src,ethertype,payload):
    header=struct.pack('!6s6sH',mac_bytes(dst),mac_bytes(src),ethertype)
    payload=payload.ljust(46,b'\x00')
    fcs=struct.pack('<I',zlib.crc32(header+payload))
    return header+payload+fcs
def parse(frame):
    dst,src,typ=struct.unpack('!6s6sH',frame[:14])
    ok=struct.pack('<I',zlib.crc32(frame[:-4]))==frame[-4:]
    return mac_text(dst),mac_text(src),hex(typ),len(frame),ok
for data in (b'BIN-42 qty=17 ok', b'A'*1400):
    frame=build('00:1d:9c:c7:b0:41','3c:52:82:4e:11:07',0x0800,data)
    print('parsed:',parse(frame),'overhead:',len(frame)-len(data),'percentage:',round(100*(len(frame)-len(data))/len(frame),2))
    bad=bytearray(frame);bad[20]^=1
    print('1 bit flipped: FCS ok =',parse(bytes(bad))[-1])
