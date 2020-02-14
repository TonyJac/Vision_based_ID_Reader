import re

#SAMPLE DATA [FRONT OF ID CARD]
stringfront= """
VIT
VELLORE CAMPUS
Dev Shankar Paul
19BEE0375
HOSTELLER
"""

def extract_names(string):
    pattern=re.compile(r'[A-Z][a-z]+')
    names=pattern.findall(string)
    newname=' '.join(names)
    return newname

def extract_reg_number(string):
    pat3=re.compile(r'[0-2][0-9][B|M][A-Z][A-Z][0-2][0-9][0-9][0-9]')
    re3=pat3.findall(string)
    re3=''.join(re3)
    return re3

names=extract_names(stringfront)
regs=extract_reg_number(stringfront)

print(names)
print(regs)