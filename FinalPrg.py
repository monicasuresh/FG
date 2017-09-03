import numpy as np
import pylab as pl

import random
import math


# to differinate central coordinates with other coordinates
def check(n,c):
	#print n
	k=1
	for i in range(len(c)):
		if(c[i]==n):
			k=0
			break
		else:
			k=1
	return k

#close of function check

#ploting 
def ploting(b,a):
	x=[]
	y=[]
	
	for m,n in b:
		pl.plot(m,n,'gD')
	
	for i in range(len(a)):
	
		for j in range(len(a[i])):
			for k in range(len(a[i][j])):
					if(k%2==0):
						x.append(a[i][j][k])
					else:
						y.append(a[i][j][k])
	
		
		pl.plot(x,y,'bo')
		pl.plot(x,y,'r')
		del x[:]
		del y[:]
	

#close of function ploting

#terminating condition checking by comparing the Central coordinates with new Central coordinates 

def terminate(count,ngroup,cg,fr,cgg,tN):
	print tN
	if(count != len(ngroup)):
		prev=[]
		for j in range(len(ngroup)):
			if(ngroup[j]<(0,0)):
				prev.append(j)
				prev.append(cg[j])
		
	
		del cg[:]
		for i in range(len(ngroup)):
			cg.append(ngroup[i])
		
	
		ss=0
		for k in range(len(cg)):
			if(cg[k]<(0,0)):
				if(k==prev[ss]):
					del cg[k]
					cg.insert(k,prev[ss+1])
					ss=ss+2
		
		if(tN == (len(fr)*len(fr))):
			print "stop"
			exit(1)
		else:
			process(cg,fr,tN)
		
	elif(count == len(ngroup)):
		print "found"
		print cg
		print cgg
		ploting(cg,cgg)
		
	

#close of function termination

#To compare Central coordinates with new Central coordinates by generating count and passing to terminating condition
def compareCentralPoints(ngroup,c):
	tc=[]
	for s in range(len(c)):
		tc.append(c[s])	
	print tc
	count=0
	for i in range(len(ngroup)):
		if(tc[i] == ngroup[i]):
			count = count + 1
	
	return count
	

#close of function compareCentralPoints


#finding the new central point in each sub list
def newpoint(group):
	ngroup=[]
	for i in range(len(group)):
		sum1=0
		sum2=0
		num=len(group[i])
		if(num!=0):
			for j in range(len(group[i])):
				for k in range(len(group[i][j])):
					if(k%2==0):
						sum1=sum1+group[i][j][k]
					else:
						sum2=sum2+group[i][j][k]
		
			ngroup.append(((sum1/num),(sum2/num)))	
		else:
			ngroup.append(())
			continue

	return ngroup

#close of function newpoint

#finding smallest and placing in a group
def compare(a,distance,col,row):
	group = [[] * col for i in range(row)]
	pos=0
	count=len(distance[0])
	for i in range(count):
		s=[]
		for j in range(len(distance)):
			s.append(distance[j][i])
		s.sort()
		for k in range(len(s)):
			if(s[0] == distance[k][i]):
				pos=k
				break
	
		group[pos].insert(i,a[pos][i])
	#newpoint()
	for h in range(len(group)):
		l=len(group[h])
		if(l<=0):
			group[h].insert(l,(-1,-1))
			
	return group

#close of function compare

#process function for calculating and storing the distance and corresponding data 
def process(cg,fr,t):
	
	t=t+1
	#num of column to separate and store the data in a group
	col=len(fr)/2

	#num of row required to create a group
	row=len(cg)

	a = [[] * col for i in range(row)]
	distance = [[] * col for i in range(row)]

	j=0
	for i in range(len(fr)):
		k=check(fr[i],cg)
		if(k==1):
			for x,y in fr[i:i+1]:
				p=0
				for m,n in cg:
					dis=math.sqrt((m-x)**2 + (n-y)**2)
					#store the friends data for each central group
					a[p].insert(j,(x,y))
					#store the friends data distance for each central group
					distance[p].insert(j,dis)
					p=p+1
			j=j+1
		
		else:
			continue	
	
	cgg=compare(a,distance,col,row)
	newCentral=newpoint(cgg)
	count=compareCentralPoints(newCentral,cg)
	terminate(count,newCentral,cg,fr,cgg,t)
	
	
#close of function process

#main function
def main():
	friends=[]
	centralGroup=[]
	t=0

	print "enter the limits of Random numbers"
	n=input()

	print "enter the minimum for random numbers"
	xn=input()

	print "enter the maximum for random numbers"
	yn=input()
	
	if(xn>=0 and yn>=0):
		if(yn > xn):
			print "enter the number of groups"
			g=input()
	
			pl.xlim(0, (yn*2))
			pl.ylim(0, (yn*2))
	
			#random numbers are generated for given x and y limits
			for i in range(n):
				friends.append((random.randint(xn,yn),random.randint(xn,yn)))
		
			#print "Friend houses:"
			#print friends
		
			#generate group for the give random numbers
			"""for j in range(g):
				index=random.randint(0,n-1)
				centralGroup.append(friends[index])
			"""
			gg=random.sample(range(0,n-1),g)
			for i in gg:
				centralGroup.append(friends[i])
			
			print "CentralGroups:"
			print centralGroup
			
			process(centralGroup,friends,t)
	
		else:
			print "max limits must be greater than min limits of random numbers"

	else:
		print "minimum and maximum random number limits must be greater than and equal to zero"

#close of function main



#calling main function to run the program
main()
pl.show()




