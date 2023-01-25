class AIChatBot:
	def __init__(self):
		pass
	def showSubjectName(self):
		print("AI for robotic")

	def showStudentYear(self):
		ID = input("Enter student ID:")
		if ID[0:2]  == "65" 	:
			print("year 1")
		elif ID[0:2]  == "64" :
			print("year 2")
		elif ID[0:2]  == "63" :
			print("year 3")
		elif ID[0:2]  == "62" :
			print("year 4")			
		elif ID[0:2]  == "61" :
			print("year 5")		
		elif ID[0:2]  == "60" :
			print("year 6")	
		elif ID[0:2]  == "59" :
			print("year 7")	
		elif ID[0:2]  == "58" :
			print("year 8")							
	def calculator(self):
		operator = input("Enter operatore +-:")
		number1	= int(input("Enter number1:") )
		number2	= int(input("Enter number2:") )
		if operator == "+":
			print("{} + {} = {}".format(number1,number2, number1+number2) )
		elif operator == "-":
			print("{} - {} = {}".format(number1,number2, number1-number2) )
	def main(self):
		self.showSubjectName()
		self.showStudentYear()
		self.calculator()
		
if __name__ == "__main__":
	while True:
		ins = AIChatBot()
		ins.main()

