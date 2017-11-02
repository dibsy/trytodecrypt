#ABCDEFGHIJKLMNOPQRSTUVWXYZ
#abcdefghijklmnopqrstuvwxyz
#0123456789
#-_.,;:?! 

import sys

UPPER = 'gligodhaohdjhgehiphlkhofibaidliggijbilmiohjbcjdnjgijjdjlojojkbekdpkgkkjfkmakol'
LOWER = 'cfkcifclacnldagddbdfmdihdlcdnneaieddefoeijeleenpfakfdffgafilflgfobgamgdhggcgin'
DIGIT = 'anhbacbcnbfibidbkobnjcaeccpakm'
SPECI = 'lbgleblgmljhlmclonmbimedmgo'

a = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
b = list('abcdefghijklmnopqrstuvwxyz')
c = list('0123456789')
d = list('-_.,;:?! ')

z = a + b + c + d
y=[]
encoded = 'eaidagdagenpmgodlceijmgoefodlceijcnllonmgodlcfilfgamgodnnflgfgafilmgofildihdagmgoefodlccnlcnledddagmgoedddagfobdagedd'

def insert(lst):
	global y
	i=0
	while i+1<len(lst):
		three_char = lst[i]+lst[i+1]+lst[i+2]
		#print three_char
		y.append(three_char)
		i=i+3


def decrypt():
	global encoded
	global y
	i = 0
	
	while i+2<len(encoded):
		three_char = encoded[i]+encoded[i+1]+encoded[i+2]
		ctr = 0
		for char in y:
			if char == three_char:
				sys.stdout.write(z[ctr])
			ctr = ctr+1
		i=i+3


def debug():
	global z
	global y
	for i in range(0,len(z)):
		print "["+str(i)+"]"+"["+z[i]+"]"+"["+y[i]+"]"



insert(UPPER)
insert(LOWER)
insert(DIGIT)
insert(SPECI)
decrypt()
#debug()






