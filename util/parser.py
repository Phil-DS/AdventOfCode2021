import re

def readAsMatrix(input,rowRegex=r'(.)'):
    '''
    
    '''
    rtn = []
    matcher = re.compile(rowRegex)
    for row in input.readlines():
        matches = [matcher.finditer(row)]

