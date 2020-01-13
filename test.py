#!python3

result = {}
"""
with open('C:/##YZHI/test.txt.txt','r') as f:
    for line in f:
        line = line.split()
        if line and line[1][0].isdigit():
            interface, address, *other = line
            result[interface] = address

print(result)
"""

with open('C:/##YZHI/test.txt.txt','r') as f:
	for line in f:
		line = line.split()
		if line[1][0].isdigit():
			interface,address,*ala = line
			result[interface] = address
			
