story = '''
if you giva a {} a {}, he/she is going to ask for a {}.
When you give him/her the {}, he/she will want to {}.
when he/she will is finished, he/she will want to go to {}.
The he/she will {} and {} to the {}. Since that doesn't work out, he/she will want to go to  {}.
'''
def main():
	animal = input("Enter animal name: ")
	food = input("Enter food: ")
	location = input("Enter location name: ")
	noun = []
	noun.append(input("Enter nouns 01: "))
	noun.append(input("Enter nouns02: "))
	verb = []
	verb.append(input("Enter verb01 : "))
	verb.append(input("Enter verb02 : "))
	verb.append(input("Enter verb03 : "))
	verb.append(input("Enter verb04 : "))

	mad = story.format(animal, food, noun[0], noun[0], verb[0], verb[1], verb[2], verb[3], noun[1], location)
	print(mad)






main()