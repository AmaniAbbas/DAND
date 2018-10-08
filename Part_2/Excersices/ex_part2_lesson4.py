'''
Quiz: Days and Hours
Try your hand at writing a function that uses a tuple to return multiple values.
Write an hours2days function that takes one argument, an integer, that is a
time period in hours. The function should return a tuple of how long that period
is in days and hours, with hours being the remainder that can't be expressed in
days.
For example, 39 hours is 1 day and 15 hours, so the function should return (1,15).
'''
def hours2days(hours):
    days = hours//24
    hrs = hours%24
    p = (days, hrs)
    return p


print(hours2days(24))
print(hours2days(25))
print(hours2days(10000))

'''
Quiz: Default Arguments
print_list is a function that takes a list as its input and prints it line by
line as a numbered or bulleted list. It takes three arguments:

l: The list to print
numbered: set to True to print a numbered list.
bullet_character: The symbol placed before each list element. This is ignored
if numbered is True.
'''
def print_list(l, numbered = False, bullet_character = '-'):
    for index, element in enumerate(l):
        if numbered:
            print("{}: {}".format(index+1, element))
        else:
            print("{} {}".format(bullet_character, element))


print_list(["cats", "in", "space"], True)
print_list(["cats", "in", "space"])

'''
Quiz: Flying Circus cast list
You're going to create a list of the actors who appeared in the television
programme Monty Python's Flying Circus.
Write a function called create_cast_list that takes a filename as input and
returns a list of actors' names. It will be run on the file
flying_circus_cast.txt (this information was collected from imdb.com).
Each line of that file consists of an actor's name, a comma, and then some
(messy) information about roles they played in the programme. You'll need to
extract only the name and add it to a list.
You might use the .split() method to process each line.
'''
def create_cast_list(filename):
    cast_list = []
    #use with to open the file filename
    with open('flying_circus_cast.txt') as f:
        #use the for loop syntax to process each line
        for line in f:
            tlist= line.split(',')
            actor= tlist[0]
            cast_list.append(actor)
    #and add the actor name to cast_list
    return cast_list

print(create_cast_list('flying_circus_cast.txt'))

'''
Quiz: Password Generator
Write a function called generate_password that selects three random words from
the list of words word_list and concatenates them into a single string.
Your function should not accept any arguments and should reference the global
variable word_list to build the password.
'''
word_file = "words.txt"
word_list = []

#fill up the word_list
with open(word_file,'r') as words:
	for line in words:
		# remove white space and make everything lowercase
		word = line.strip().lower()
		# don't include words that are too long or too short
		if 3 < len(word) < 8:
			word_list.append(word)

def generate_password():
    from random import choice
    password = choice(word_list)+choice(word_list)+choice(word_list)
    return password

# test function
print(generate_password())
"""
Alternatively, you could use the random.sample function and .join method for strings:

def generate_password():
    return str().join(random.sample(word_list,3))
"""
