#Builg Your own PythonPet-->Python-emon..

#print "<(0_o)>"


#---------------------Python Modules and Imports------->>. <(0_o)>
import random # <--allows ability to choose random values from a dictionary
import os     # <--allows ability 

#---------------------Variables and Values------------->>. <(0_o)>


#dictionary
droidD = {
	'appearance': "<(0_o)>",
	'name': "Droid",
	'age': 2121,
	'weight': 10,
	'hungry': True,
	'phrases': ["I want your clothes, your boots and your motorcycle", "come with me if you want to live", "hasta la vista, baby", "T-1000", "Will Smith sucks", "Don't confuse me with R2-D2"]
}


pyPet = droidD


#----------------------------Opening-------------->>. <(0_o)>

def startup_AndroidPet():

	print("                              ")
	print("******************************")
	print("Welcome to Anroid's Lab o_o;")
	print("            |_|                ")
	print("          <(o_o)>              ")             		 
	print("******************************")
	print("         0(_____)0             ")
	print("          [0] [0]              ")  



def androidStatus():
	print "========================================"

	print " * Hello, my name is "+ (droidD['name'])
	print "----------------------------------------"
	print " * I weigh "+str (droidD['weight']) +" pounds"
	print "----------------------------------------"
	if droidD['hungry']:
		print " !! I am hungry"
	else:
		print " *burrrp** I'm full"

	print "========================================"


		

startup_AndroidPet()
androidStatus()

#----------------------------functionality-------------->>. <(0_o)>

terminate = False

while not terminate:
	print "##########################"
	# print(raw_input)
	user_input = raw_input("> ")

	if user_input == "quit":
		terminate = True

	elif user_input == "stats":
		androidStatus()

	elif user_input == "chat":
		print random.choice (droidD['phrases'])
		print("            |_|                ")
		print("          <(o_o)>              ")             		 
		print("         0(_____)0             ")
		print("          [0] [0]              ")  


	elif user_input =="feed":
		print("            |_|                ")
		print("          <(o_o)>              ")             		 
		print("         0(_____)0             ")
		print("          [0] [0]              ")  

		(droidD['weight']) = (droidD['weight']) + 5
		(droidD['hungry']) = False
		print "I NOW weigh " + str (droidD['weight'])
	else:
		print "Sorry, There's an error"

print "Good-bye"
