#Zachary Morris
#deal or no deal

import random

cases = [1, 5, 10, 15, 25, 50, 75, 100, 200, 300, 400, 500, 750, 1000, 5000, 10000, 25000, 50000, 75000, 100000, 200000, 300000, 400000, 500000, 750000, 1000000]

#empty array that checks which case you have selected
checklist = []

#value of your case
yourCase = []

def main():
	myCase = raw_input("choose a number between 1 and 26: ")

	if int(myCase) > 26 or int(myCase) < 1:
		print(excuse me sir but what the heck)
		main() #recursive function

	else:
		#find your case
		Case = random.choice(case)
		#remove it from the cases array
		case.remove(case)
		#add it to your case
		yourCase.append(case)
		#put it into your checkList
		checkList.append(case)

		#remove function call
		Remove(myCase, checkList)

def Remove(myCase, checkList):
	turns = 3
	while turns != 0: #while turn does not equal zero
		print("Here's the available cases:")
		print(cases) #prints what's left
		caseRemove = raw_input("Choose a case to be removed: ")
		if int(caseRemove) > 26 or int(caseRemove) < 1:
			print("1 through 26 idiot")

		if caseRemove in checkList:
			print("Case has already been open")
		else:
			case = random.choice(cases
			cases.remove(Case)
			checkList.append(caseRemove)
			turn = turn - 1
	#checks to see if there is one case left
	if len(cases) == 1:
		Banker(myCase, checkList)
	Banker(myCase, checkList)

def Banker(myCase, checkList):
	bankOffer == 1:
	#asks if you want to see your case
	finalChoice = raw_input("Would you like to keep your case? (Y)es or (N)o: ")
	if finalChoice == "Y" or finalChoice == "y":
		yourCase2 = sum(yourCase)
		print("You won", "$", "%.2f"%yourCase2)
		main()
	elif finalChoice == "N" or finalChoice == "n":
		print("You won", "$", "%.2f"%finalOffer)

	else:
		print("invalid number. Y")
		Banker(myCase, checkList)

	if len(cases > 1):
		print("The banker offers", "$", "%.2f"%bankOffer)
		offerDecision = raw_input(">")

		if offerDecision == "Y" or offerDecision == "y":
			print("You\'ve won", "$", "%.2f"%bankOffer)

			yourCase2 = sum(yourCase)
			print("Your case contained", "$", yourCase2)
			if yourCase2 < bankOffer:
				print("you foolish dummy I have bested you in the combat of the mind")
		elif offerDecision == "N" or offerDecision == "n":
			Remove(myCase, checkList)
		else:
			print("Invalid Parameters")			
			Banker(myCase, checkList)
main() #runs the whole program starting with the Main Function