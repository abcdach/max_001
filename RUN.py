##############################################
# v0.01			export PS1='> '
##############################################
import commands
import os 
import re
import time
##############################################



 
Dir_Path = os.path.dirname(os.path.realpath(__file__))
#print Dir_Path
##############################################

#from os import listdir
#from os.path import isfile, join

#PATH=Dir_Path+"/"
#f=[]
#try:
#	onlyfiles = [f for f in listdir(PATH) if isfile(join(PATH, f))]
#	if f:
#		print "OK"
#		print onlyfiles
#	else:
#		print "Dir is empty"
#except:
#	print "DIR ERROR"
#
#import glob
#Dev_List = glob.glob(PATH+"*")
#print Dev_List
##############################################
import glob
import ntpath

MAX_DevList = ["","",""]*256
MAX_DevNum  = int(0)
##############################################
for Dev_Path in glob.glob(Dir_Path+"/DEV/OP/*"):
	Dev_Name = ntpath.basename(Dev_Path)
	MAX_DevList[MAX_DevNum]=(Dev_Name[0],Dev_Name,Dev_Path+"/")
	MAX_DevNum=MAX_DevNum+1
##############################################
for Dev_Path in glob.glob(Dir_Path+"/DEV/RP/*"):
	Dev_Name = ntpath.basename(Dev_Path)
	MAX_DevList[MAX_DevNum]=(Dev_Name[0],Dev_Name,Dev_Path+"/")
	MAX_DevNum=MAX_DevNum+1
##############################################
for Dev_Path in glob.glob(Dir_Path+"/DEV/UN/*"):
	Dev_Name = ntpath.basename(Dev_Path)
	MAX_DevList[MAX_DevNum]=(Dev_Name[0],Dev_Name,Dev_Path+"/")
	MAX_DevNum=MAX_DevNum+1
##############################################
for i in xrange(MAX_DevNum):
	print MAX_DevList[i]
##############################################	
def Finde_Dev(dev):
	for i in xrange(MAX_DevNum):
		if(dev==MAX_DevList[i][1]):
			_Type = MAX_DevList[i][0]
			_Name = MAX_DevList[i][1]
			_Path = MAX_DevList[i][2]
			return (_Type,_Path)
	return ("","")
##############################################
(_Dev_Type,_Dev_Path) = Finde_Dev("pOP_ILI9341")
if(len(_Dev_Path)>0):
	print _Dev_Type
	print _Dev_Path

##############################################











#exit(0)






##############################################
DevList = [""]*256
Data    = [""]*2
##############################################
DevList[0]="1,MAXIOT,"
DevList[1]="0,bRP_WebGUI,"
DevList[2]="0,pOP_ILI9341,"
DevList[3]="0,pOP_8229BSF,"
DevList[4]="1,pOP_BMP180,"
DevList[5]="0,pRP_MFRC522_S0,"
DevList[6]="0,pRP_MFRC522_S1,"
DevList[7]="0,pRP_RELAY,"
DevList[8]="0,pUN_Host_IP,"
DevList[9]="0,pUN_MIZ_1,"
##############################################
Path = os.path.dirname(os.path.realpath(__file__))
#print Path
##############################################
for i in xrange(MAX_DevNum):
	_dev = MAX_DevList[i][1]
	print "Kill screen : "+_dev
	commands.getoutput("screen -S _dev -X quit")
	time.sleep(0.2)
	#exit(0)
##############################################
cou = 0
while 1:
	cou = cou + 1
	print "cou:"+str(cou)
	time.sleep(1)
	screen = commands.getoutput('screen -ls')
	for i in range(len(DevList)):
		if(len(DevList[i])>0):
			Data = re.split(',+',DevList[i])
			if(len(Data)>2):
				#print Data
				screen_comm = str(Data[0])
				screen_name = str(Data[1])
				screen_argu = str(Data[2])
				vel = screen.find(screen_name)
				if(vel > 0):
					screen_stat = "1"
				else:
					screen_stat = "0"
				#print "screen_comm:"+screen_comm
				#print "screen_name:"+screen_name	
				#print "screen_stat:"+screen_stat
				if(screen_comm!=screen_stat):
					if(screen_comm=="1"):
					
						(_Dev_Type,_Dev_Path) = Finde_Dev(screen_name)
						if(len(_Dev_Path)>0):
							if(_Dev_Type=="p"):#Python
								print "START : "+screen_name+" "+screen_argu
								comm = "screen -dmS "+screen_name+" bash -c 'cd "+_Dev_Path+" && python RUN.py "+screen_argu+"'"
								#print comm
								ddd = commands.getoutput(comm)
								#print ddd
								time.sleep(1)
							if(_Dev_Type=="c"):#C
								print "START : "+screen_name+" "+screen_argu
								comm = "screen -dmS "+screen_name+" bash -c 'cd "+_Dev_Path+" && ./RUN "+screen_argu+"'"
								#print comm
								ddd = commands.getoutput(comm)
								#print ddd
								time.sleep(1)
							if(_Dev_Type=="b"):#BASH
								print "START : "+screen_name+" "+screen_argu
								comm = "screen -dmS "+screen_name+" bash -c 'cd "+_Dev_Path+" && ./RUN.sh "+screen_argu+"'"
								#print comm
								ddd = commands.getoutput(comm)
								#print ddd
								time.sleep(3)
							
							
							
						if(screen_name=="MAXIOT"):#
							#print "START : "+screen_name+" "+screen_argu
							comm = "screen -dmS "+screen_name+" bash -c '/etc/MAXIOT/MAXIOT_SERVER "+screen_argu+"'"
							print comm
							ddd = commands.getoutput(comm)
							#print ddd
							time.sleep(7)							
							#/etc/MAXIOT/MAXIOT_SERVER
					if(screen_comm=="0"):
						print "STOP  : "+screen_name				
						commands.getoutput("screen -S "+screen_name+" -X quit")







