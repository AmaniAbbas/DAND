'''
Quiz: List Indexing
Complete this function, how_many_days, that takes as its input a number
representing the month, and returns how many days are in that month.
The days_in_month function that we've defined for you is a list of how many
days are in each month. For example, days_in_month(8) should return 31 because
the eighth month, August, has 31 days.

Remember to account for zero-based indexing!
'''
def how_many_days(month):
    """
    Returns the number of days in a month.
    WARNING: This function doesn't account for leap years!
    """
    month = month - 1
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = days_in_month[month]
    return(days)

'''
Quiz: Slicing Lists
Select the three most recent dates from this list using list slicing notation.
Hint: negative indexes work in slices!
'''
eclipse_dates = ['June 21, 2001', 'December 4, 2002', 'November 23, 2003',
                 'March 29, 2006', 'August 1, 2008', 'July 22, 2009',
                 'July 11, 2010', 'November 13, 2012', 'March 20, 2015',
                 'March 9, 2016']

# TODO: Modify this line so it prints the last three elements of the list
print(eclipse_dates[-3:])

'''
Quiz: Top Three
Write a function, top_three, that takes a list as its argument, and returns a
list of the three largest elements.
For example, top_three([2,3,5,6,8,4,2,1]) == [8, 6, 5]
'''
def top_three(input_list):
    """Returns a list of the three largest elements input_list in order from largest to smallest.

    If input_list has fewer than three elements, return input_list element sorted largest to smallest/
    """
    # TODO: implement this function
    input_list = sorted(input_list, reverse=True)
    return (input_list[:3])

'''
Quiz: Median
The function in this quiz, median, returns the median value of an input list.
Unfortunately it only works with lists that have an odd number of elements.
Modify the function so that when median is given a list with an even number of
elements, it returns the mean of the two central elements.
The provided test cases demonstrate the expected behavior.
'''
def median(numbers):
    numbers.sort() #The sort method sorts a list directly, rather than returning a new sorted list
    if len(numbers)%2 == 0:
        index1 = int(len(numbers)/2 -1)
        index2 = int(len(numbers)/2)
        result = (numbers[index1]+numbers[index2])/2
    else:
        middle_index = int(len(numbers)/2)
        result = numbers[middle_index]

    return (result)

test1 = median([1,2,3])
print("expected result: 2, actual result: {}".format(test1))

test2 = median([1,2,3,4])
print("expected result: 2.5, actual result: {}".format(test2))

test3 = median([53, 12, 65, 7, 420, 317, 88])
print("expected result: 65, actual result: {}".format(test3))


'''
Quiz: Sum of a List
Define a function, list_sum, that takes a list as its argument and returns the
sum of the elements in the list. Use a for loop to iterate over the list
'''
def list_sum(input_list):
    sum = 0
    # todo: Write a for loop that adds the elements
    # of input_list to the sum variable
    for num in input_list:
        sum = sum + num
    return sum



#These test cases check that list_sum works correctly
test1 = list_sum([1, 2, 3])
print("expected result: 6, actual result: {}".format(test1))

test2 = list_sum([-1, 0, 1])
print("expected result: 0, actual result: {}".format(test2))

'''
Quiz: XML Tag Counter
Write a function, tag_count, that takes as its argument a list of strings.
It should return a count of how many of those strings are XML tags. XML is a
data language similar to HTML. You can tell if a string is an XML tag if it
begins with a left angle bracket "<" and ends with a right angle bracket ">".

You can assume that the list of strings that will be given as input will not
contain empty strings.
'''
"""Write a function, `tag_count`, that takes as its argument a list
of strings. It should return a count of how many of those strings
are XML tags. You can tell if a string is an XML tag if it begins
with a left angle bracket "<" and ends with a right angle bracket ">".
"""
#TODO: Define the tag_count function
def tag_count(list1):
    count = 0
    for tag in list1:
        if tag[0] == '<' and tag[-1] == '>':
            count += 1
    # Your code goes here!
    return count

# Test for the tag_count function:
list1 = ['<greeting>', 'Hello World!', '</greeting>']
count = tag_count(list1)
print("Expected result: 2, Actual result: {}".format(count))



'''
Quiz: Create an HTML List
Write the html_list function. The function takes one argument, a list of
strings, and returns a single string which is an HTML list.
the string's first line should be the opening tag <ul>. Following that is one
line per element in the source list, surrounded by <li> and </li> tags.
The final line of the string should be the closing tag </ul>.
'''
#define the  html_list function
def html_list(list_of_strings):
    html_string = "<ul>\n"
    for string in list_of_strings:
        html_string += '<li>{}</li>\n'.format(string)
    html_string += "</ul>"
    # Your code goes here!
    return html_string

print(html_list(['First element', 'Second element', 'Third element']))


'''
Quiz: Starbox
The starbox function in the quiz below prints a box made out of asterisks.
The function takes two arguments, width and height, that specify how many
characters wide the box is and how many lines tall it is. The function isn't
quite complete: it prints boxes of the correct width, but the height argument
is ignored.
Complete the function so that both of the provided test cases print boxes that
are the correct size. Hint: The range function could be helpful!
'''
def starbox(width, height):
    """print a box made up of asterisks.

    width: width of box in characters, must be at least 2
    height: height of box in lines, must be at least 2
    """
    print("*" * width) #print top edge of box
    for i in range (height-2):
        print("*"+ " " * (width-2) + "*")
    print("*" * width) #print bottom edge of box

# Test Cases
print("Test 1:")
starbox(5, 5)

print("Test 2:")
starbox(2, 3)


'''
Quiz: Nearest Square
Implement the nearest_square function. The function takes an integer argument
limit, and returns the largest square number that is less than limit.
A square number is the product of an integer multiplied by itself,
for example 36 is a square number because it equals 6*6.
There's more than one way to write this code, but I suggest you use a while loop!
'''
#TODO: Implement the nearest_square function
def nearest_square(limit):
    n = 0
    while (n+1)**2 < limit:
        n += 1
    return (n*n)

test1 = nearest_square(40)
print("expected result: 36, actual result: {}".format(test1))



'''
Quiz: Break the String
Time to write your own loop with a break statement. Your task is to create a
string, news_ticker that is exactly 140 characters long. You should create the
news ticker by adding headlines from the headlines list, inserting a space in
between each headline. If necessary, truncate the last headline in the middle
so that news_ticker is exactly 140 characters long.
'''
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""
for headline in headlines:
    news_ticker = news_ticker + headline +" "
    if len(news_ticker) >= 140:
        news_ticker = news_ticker[:140]
        break
print(news_ticker)
print(len(news_ticker))


'''
Quiz: Refactor the Code
'''
# Checks the five answers provided to a multiple choice quiz and returns the results.

def check_answers(my_answers,answers):
    count = 0
    count_wrong = 0
    for i in range(len(my_answers)):
        if my_answers[i] == answers[i]:
            count +=1
        else:
            count_wrong +=1

    score_string = "You scored " + str(count) + " out of " + str(count+count_wrong)
    if count/(count+count_wrong) > 0.7:
        return "Congratulations, you passed the test! " + score_string +"."
    elif count_wrong/(count+count_wrong) >= 0.3:
        return "Unfortunately, you did not pass. " + score_string +"."

print(check_answers([1,2,3,4,5],[1,2,3,4,5]))
print(check_answers([1,2,3,4,5],["badger","badger","badger","badger","badger"]))


'''
Quiz: Deduplication
Write a function, remove_duplicates that takes a list as its argument and
returns a new list containing the unique elements of the original list.
The elements in the new list without duplicates can be in any order.
'''
def remove_duplicates(countries_list):
    new_list= []
    for country in countries_list:
        if country not in new_list:
            new_list.append(country)
    return(new_list)

country_list = ["Jordan", "Jordan", "USA"]
print(remove_duplicates(country_list))


'''
Quiz: Build a Set
In a similar way to building an empty list with my_list = [], you can create an
empty set with my_set = set(). Using this technique, and the add method, build
a set of all of the square numbers greater than 0 and less than 2,000.
'''
squares = set()

# todo: populate "squares" with the set of all of the integers less
# than 2000 that are square numbers

def nearest_square(limit):
    answer = 0
    while (answer+1)**2 < limit:
        answer += 1
    return answer**2


limit = 2000

while limit != 0:
    new = nearest_square(limit)
    squares.add(new)
    limit = nearest_square(limit) - 1
print(squares)


'''
Quiz: Users by Country
Suppose this dataset actually contains information about users who downloaded
and installed a certain application: for each user that did this their country
appears in the list. Now let's use a dict to perform a more sophisticated
analysis: how many users there are from each country?

Create a dict, country_counts, whose keys are country names, and whose values
are the number of times the country occurs in the countries list.
'''
country_counts = {}
for country in country_list:
    #todo: insert countries into the country_count dict.
    # If the country isn't in the dict already, add it and set the value to 1
    # If the country is in the dict, increment its value by one to keep count
    if country in country_counts:
        country_counts[country] += 1
    else:
        country_counts[country] = 1

print(country_counts)



'''
Quiz: Adding Values to Nested Dictionaries
Try your hand at working with nested dictionaries. Add another entry,
'is_noble_gas' to each dictionary in the elements dictionary.
'''
elements = {'hydrogen': {'number': 1, 'weight': 1.00794, 'symbol': 'H'},
            'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'He'}}

# todo: Add an 'is_noble_gas' entry to the hydrogen and helium dictionaries
# hint: helium is a noble gas, hydrogen isn't

elements['hydrogen']['is_noble_gas']= False
elements['helium']['is_noble_gas'] = True

print(elements['hydrogen']['is_noble_gas'])
print(elements['helium']['is_noble_gas'])

'''
Quiz: Flying Circus Records
A regular flying circus happens twice or three times a month.
For each month, information about the amount of money taken at each event is
saved in a list, so that the amounts appear in the order in which they happened.
The months' data is all collected in a dictionary called monthly_takings.
For this quiz, write a function total_takings that calculates the sum of
takings from every circus in the year.
'''
def total_takings(monthly_takings):
    month_list = []
    count = 0
    for month in monthly_takings:
        if month not in month_list:
            month_list.append(month)
            for i in range(len(monthly_takings[month])):
                count = count + monthly_takings[month][i]
    return count

monthly_takings = {'January': [54, 63], 'February': [64, 60], 'March': [63, 49],
                   'April': [57, 42], 'May': [55, 37], 'June': [34, 32],
                   'July': [69, 41, 32], 'August': [40, 61, 40], 'September': [51, 62],
                   'October': [34, 58, 45], 'November': [67, 44], 'December': [41, 58]}

print(total_takings(monthly_takings))

"""
the course solution was:
def total_takings(yearly_record):
    #total is used to sum up the monthly takings
    total = 0
    for month in yearly_record.keys():
        #I use the Python function sum to sum up over
        #all the elements in a list
        total = total + sum(yearly_record[month])
    return total
"""
