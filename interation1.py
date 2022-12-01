import math 
import copy

posroute= []
posroute2= []
disttravel= int
dist=0
targetdist=8
roaddict = {}

class node:
	def __init__(self,name, xcord,ycord,adj):
		self.name = name
		self.xcord = xcord
		self.ycord = ycord
		self.adj = adj
	def buildroads(self):
		global roaddict
		# roaddict[self.name] = self.name + "-" +
		for ti in self.adj:
			roadname = self.name + "-" + ti.name
			roaddict[roadname] = 1

def disttravel(currentnode,previous,travellist):
	# print(posroute2)
	travellist.append(currentnode)
	# print(currentnode.name)
	tdist = 0
	for k in range(len(travellist)-1):
		dist1 = distance(travellist[k+1].xcord,travellist[k+1].ycord,travellist[k].xcord,travellist[k].ycord)
		tdist = tdist +dist1

	newdist = distance(currentnode.xcord,currentnode.ycord,previous.xcord,previous.ycord)
	if(currentnode.name == travellist[0].name and tdist == targetdist):
		# print("bing")
		# print("##########################")
		# for yo in travellist:
		# 	print(yo.name)
		# print("##########################")
		# print(travellist[0].name)
		posroute2.append(travellist.copy())
		# travellist.pop()
		# print(posroute)
	elif(tdist < targetdist):
		for i in currentnode.adj:
			if(i.name != previous.name):
				disttravel(i, currentnode, travellist)
				if(len(travellist) >0):
					travellist.pop()




def distance(x1,y1,x2,y2):
	par = (x2-x1)
	par2 =(y2-y1)
	part = par **2
	part2 = par2**2
	fpart = part +part2
	dist2 = math.sqrt(fpart)
	# dist2 = ((x2-x1)**2) +((y2-y1)**2)
	# dist2=dist**.5
	return dist2


A = node("A",0,0,[])
B = node("B",0,2,[])
C = node("C",2,2,[])
D = node("D",2,0,[])
E = node("E",8,0,[])

A.adj.append(B)
A.adj.append(E)
A.adj.append(D)
B.adj.append(A)
B.adj.append(C)
C.adj.append(B)
C.adj.append(D)
D.adj.append(C)
D.adj.append(A)

A.buildroads()
B.buildroads()
C.buildroads()
D.buildroads()


disttravel(A,A,posroute)
# print(len(posroute))
print("+++++++++++++++++++++")
count =0
# print(posroute2)
# print(posroute)
for p in posroute2:
	for p2 in p:
		print(p2.name+"->",end=" ")
	print(" ")


# d=distance(5,5,3,3)
# print(d)

print("###########################")
print(roaddict)