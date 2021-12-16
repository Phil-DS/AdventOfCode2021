from day16_data import data
import numpy as np

bitData = ''.join(bin(d)[2:].zfill(4) for d in data)
# bit = 0
verCount = 0
def packetManager(start):
    global verCount
    bit = start
    version = int(''.join(bitData[bit:bit+3]),2)
    bit += 3

    typeId = int(''.join(bitData[bit:bit+3]),2)
    bit += 3

    val = None
    
    if typeId == 4:
        lit = ''
        while True:
            seg = bitData[bit:bit+5]
            lit += ''.join(seg[1:])
            bit += 5
            if seg[0] == '0':
                break
        val = int(lit,2)
        # return (bit,val, version)
    else:
        lengthId = bitData[bit]
        bit += 1
        values = []
        if lengthId == '0':
            lenSeg = int(bitData[bit:bit+15],2)
            bit += 15
            b = bit
            bit+=lenSeg
            while True:
                try:
                    b,v, ver = packetManager(b)
                except Exception as e:
                    print(e)
                    break
                values.append(v)
                if b >= bit:
                    break
                # verCount += ver
            
        else:
            countSeg = int(bitData[bit:bit+11],2)
            bit += 11
            for i in range(countSeg):
                try:
                    b,v, ver = packetManager(bit)
                except Exception as e:
                    print(e)
                    break
                bit = b
                # verCount += ver
                values.append(v)

        if typeId == 0:
            val = sum(values)
        elif typeId == 1:
            val = np.prod(values)
        elif typeId == 2:
            val = min(values)
        elif typeId == 3:
            val =  max(values)
        elif typeId == 5:
            val = int(values[0]>values[1])
        elif typeId == 6:
            val = int(values[0]<values[1])
        elif typeId == 7:
            val = int(values[0]==values[1])



    verCount += version
    return bit,val, version

rtn = packetManager(0)
print(verCount)
print(rtn)