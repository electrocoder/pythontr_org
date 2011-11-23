import re
import commands as cmd
import string
import time
import numpy
import visual.graph as vg
import visual as v
import random
class wifiscan:		
	def graphtool(self,count):
		self.ssidlabel=[]
		self.ssidcolor=[]
		self.f=vg.gdisplay(title='AterOS PyWifi-Analyzer==========Signal Quality',xmin=(-1.0*count/4),xmax=count,ymin=0.0,ymax=1.0,xtitle='count',ytitle='quality ratio')
		self.g=vg.gdisplay(title='AterOS PyWifi-Analyzer==========Signal Level',xmin=(-1.0*count/4),xmax=count,ymin=-100.0,ymax=0.0,xtitle='count',ytitle='level dbm')
	def scan(self):
		self.data_temp=[]
		self.wifilist_temp=cmd.getoutput('iwlist wlan0 scan')
		self.wifilist_temp2=re.split("\n",self.wifilist_temp)
		if self.wifilist_temp2[0]=='wlan0     Scan completed :':
			for i in range(len(self.wifilist_temp2)):
				m=re.findall('(?:Cell)',self.wifilist_temp2[i])
				if m!=[]:
					essid=(string.strip(self.wifilist_temp2[i+5])[7:-1])
					self.data_temp.append(essid)
					quality=float(str(string.split(string.strip(self.wifilist_temp2[i+3]))[0][8:])[:2])/float(str(string.split(string.strip(self.wifilist_temp2[i+3]))[0][8:])[3:])
					self.data_temp.append(quality)
					signallevel=float(string.split(string.strip(self.wifilist_temp2[i+3]))[2][6:])
					self.data_temp.append(signallevel)
			return self.data_temp
		else :
			return None
	def datagen(self):
		self.data=self.scan()
		if self.data!=None:
			for i in range((len(self.data)/3)):
				if self.data[3*i] not in self.ssidlabel:
					self.ssidlabel.append(self.data[3*i])
					clr=(random.random(),random.random(),random.random())
					self.ssidcolor.append(clr)
			print self.data
			return self.ssidlabel,self.ssidcolor
		else:
			return None
	def graphdata(self,count,ncounts):
		status=self.datagen()
		if status!=None:
			for i in range(len(self.ssidlabel)):
				if self.ssidlabel[i] in self.data:
					quality=vg.gdots(gdisplay=self.f,color=self.ssidcolor[i],size=2)
					level=vg.gdots(gdisplay=self.g,color=self.ssidcolor[i],size=2)
					vg.label(display=self.f.display,text=str(self.ssidlabel[i]),pos=(-(1.0*ncounts/5.0),(-0.07*i+1.0)),color=self.ssidcolor[i],height=7,font='sans')
					vg.label(display=self.g.display,text=str(self.ssidlabel[i]),pos=(-(1.0*ncounts/5.0),(7*i-100)),color=self.ssidcolor[i],height=7,font='sans')
					quality.plot(pos=(count,self.data[self.data.index(self.ssidlabel[i])+1]))
					level.plot(pos=(count,self.data[self.data.index(self.ssidlabel[i])+2]))
		else:
			print "sorry i can not found any wireless network!!! Try again :)"
cc=wifiscan()
ncounts=400
cc.graphtool(ncounts)
for i in range(ncounts):
	cc.graphdata(i,ncounts)
