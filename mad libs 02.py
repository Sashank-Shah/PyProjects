from random import randint
import copy

story = '''
if you giva a {} a {}, he/she is going to ask for a {}.
When you give him/her the {}, he/she will want to {}.
when he/she will is finished, he/she will want to go to {}.
The he/she will {} and {} to the {}. Since that doesn't work out, he/she will want to go to  {}.
'''

word_dict = {
	'animal': ['cow', 'dog', 'cat', 'horse'],
	'food': ['apple', 'tomato', 'pineapple'],
	'noun': ['he', 'she', 'chair', 'pen'],
	'verb': ['come', 'go', 'eat', 'find']
}

def getting_word(type, local_dict):
	words = local_dict[type]
	count = len(words)-1
	indexing = randint(0, count)
	return words.pop(indexing)

def story_fun():
	local_dict = copy.deepcopy(word_dict)
	return story.format(
		getting_word('animal', local_dict),
		getting_word('food', local_dict),
		getting_word('noun', local_dict),
		getting_word('noun', local_dict),
		getting_word('verb', local_dict),
		getting_word('verb', local_dict),
		getting_word('verb', local_dict),
		getting_word('noun', local_dict),
		getting_word('verb', local_dict),
		getting_word('noun', local_dict),
		
	)

print("Story1: ")
print(story_fun())

print("Story2: ")
print(story_fun())

print("Story3: ")
print(story_fun())

print("Story4: ")
print(story_fun())