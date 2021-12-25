from day24_data import instructions
import itertools
import functools

def sliceItUp():
    sliced = []
    curr = [instructions[0]]
    for i in range(1,len(instructions)):
        if instructions[i][0] == 'inp':
            sliced.append(curr)
            curr = []
        curr.append(instructions[i])

    sliced.append(curr)
    return sliced    

splitInstr = sliceItUp()

class Variable:
    def __init__(self, value=0):
        self.value = value

    def __repr__(self) -> str:
        return self.value
    
    def __str__(self) -> str:
        return self.value
    
    def inp(self,value):
        self.value = value
    
    def add(self,value):
        self.value += value

    def mul(self,value):
        self.value *= value

    def div(self,value):
        self.value = int(self.value/value)
    
    def mod(self,value):
        self.value = self.value % value

    def eql(self,value):
        self.value = int(self.value == value)

@functools.cache
def runProgram(inp, instr, x, y, z, w):
    memory = {
        # l:Variable() for l in 'wxyz'
        'w': Variable(value=w),
        'x': Variable(value=x),
        'y': Variable(value=y),
        'z': Variable(value=z),
    }

    for func,variable,value in splitInstr[instr]:
        if func == 'inp':
            memory[variable].inp(inp)
        else:
            funcToCall = getattr(memory[variable],func)
            if value in 'wxyz':
                funcToCall(memory[value].value)
            else:
                funcToCall(int(value))

    # assert len(inputStack) == 0,'Failed to use all inputs'
    # return memory['z'].value == 0
    return memory


for i,monad in enumerate(itertools.product(range(9,0,-1),repeat=14)):
    if i%1000 == 0:
        print(i)
    memory = {
        l:Variable() for l in 'wxyz'
    }
    for instr,inp in enumerate(monad):
        memory = runProgram(inp, instr, memory['x'].value,memory['y'].value,memory['z'].value,memory['w'].value)
    if memory['z'].value == 0:
        print(int(''.join(monad)))