# idea: primarily design a function that can calculate the amount of people needed for a given event according to Maurer's scheme
# additionally add other features such as food/drinks calculations for SEG-VER 
# make accesible from Telegram as then no reliance on random webpages or terrible excel sheets remains. 

def maurerScheme(maxPeople,expectedPeople,eventCategory, expectedVIP, flagDanger):
	
	if flagDanger:
		bonusDanger = 10
	if expectedVIP => 15:
		bonusVIP = 30
	elif expectedVIP < 15 and expectedVIP >= 10:
		bonusVIP = 20
	elif expectedVIP < 10 and expectedVIP >= 5:
		bonusVIP = 10 
	elif expectedVIP < 5:
		bonusVIP = 0
	
	#could probably try some modulo shit to reduce if blocks	
	
	# need something like switch for all the input values to all the 
	maurerPoints = (pointsMaxPeople+pointsExpectedPeople)*modifierEventCategory + bonusVIP + bonusDanger
	
	#set numPeople, numCars according to the maurerPoints calculated
	# numPeople and numCars should be Dicts with the keys: Helfer, Notarzt, KTW, RTW, EL, SAN-Hist  	
	return numPeople, numCars, needExtra  	#TODO does return work like this with multiple return values?
