#! /usr/bin/python


def findw(var,pro):
	l1 = [var]
	l2 = []
	i = 0
	if i % 2 == 0:
		l2 = l1
		for i in l2:
			if pro.has_key(i):
				s = pro[i]
				for j in s:
					if len(j) == 1 and j>='A' and j<='Z':
						l2.append(j)
	else:
		l1 = l2
		for i in l1:
			if pro.has_key(i):
				s = pro[i]
				for j in s:
					if len(j) == 1 and j>='A' and j<='Z':
						l1.append(j)
	if l1 == l2:
		return l1

def print_production(pro):
	for i in pro.keys():
		r = pro[i]
		print i,'->',
		for j in r:
			if j == r[-1]:
				print j
			else:
				print j,'|',

productions = dict()
terminals = []
variables = []
pro = "something"
while(pro!="$"):
	pro = raw_input()
	l = list(pro)
	for i in l:
		if i>='a' and i<='z':
			if i not in terminals:
				terminals.append(i)
		elif i>='A' and i<='Z':
			if i not in variables:
				variables.append(i)
	try:
		l = pro.split('->')[0]
	except:
		print 'Invalid Production'
		exit()
	try:
		r = pro.split('->')[1].split('|')
		if productions.has_key(l):
			v = list(productions[l])
		else:
			v = []
		for i in r:
			if i not in v:
				v.append(i)
		productions[l] = v
	except:
		pass
print 'Given Grammar:'
print terminals,variables
print_production(productions)
prod2 = dict()
print 'New Production:'
for i in variables:
	w = findw(i,productions)
	for j in w:
		if prod2.has_key(i):
			v = prod2[i]
		else:
			v = []
		if productions.has_key(j):
			p = productions[j]
			for k in p:
				if len(k) > 1:
					if k not in v:
						v.append(k)
				elif k>='a' and k<='z':
					if k not in v:
						v.append(k)
		prod2[i] = v
print_production(prod2)
