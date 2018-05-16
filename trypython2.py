# -Problen 43, 44, 45, 46----------------------------------------------------

# text = input("Enter some text ")
# print(text.upper())
# print(text.lower())
# print(text.title())

# print(text[::-1]) 
# works by doing [begin:end:step] - by leaving begin and end off and specifying a step of -1, it reverses a string.

# -Problem 47----------------------------------------------------

# number = int(input("Enter a number "))
# if number < 10:
#     print("Small")
# else:
#     print("Big")
    
# -Problem 48----------------------------------------------------
    
# num1 = int(input("Enter first number "))
# num2 = int(input("Enter second number "))

# if num1 == num2:
#     print("Same")
# else:
#     print("Not Same")

# -Problem 49----------------------------------------------------

# num = int(input("Enter a number "))

# if num == 1:
#     name = input("Enter your name ")
#     print("Your name is "+name)
# if num == 2:
#     age = input("Enter your age ")
#     age_int = int(age)
#     print("Your age is "+age)
    
# -Problem 50, 51, 52----------------------------------------------------

# nums = []
# for i in range(10):
#     number = int(input("Enter a number: "))
#     nums.append(number)
    
# print(nums)


# print(sum(nums))

# for x in nums:
#     print(x)

# -Intro to while loops ----------------------------------------------------

# i = 0

# while i < 100:
#     print(i)
#     i += 2

# -Intro to data structures----------------------------------------------------

# people = {
#     "Joe": 23, 
#     "Ann": 24, 
#     "Barbara": 67, 
#     "Pete": 55, 
#     "Tim": 34, 
#     "Sam": 13, 
#     "Josh": 5
# }

# name = input("Enter name: ")
# print (people[name])

# -Intro to data structures----------------------------------------------------

# people = {
#     "Joe": {"age": 23, "eyes": "blue", "height": 134, "nationality": "Irish"}, 
#     "Ann": {"age": 13, "eyes": "green", "height": 172, "nationality": "Irish"}, 
#     "Bob": {"age": 23, "eyes": "red", "height": 234, "nationality": "Turkmenistan"}, 
#     "Sam": {"age": 45, "eyes": "grey", "height": 134, "nationality": "French"}, 
#     "Tina": {"age": 46, "eyes": "blue", "height": 154, "nationality": "American"}, 
# }

# name = input("Enter name: ")
# person = people[name]

# what = input("What do you want to know? ")
# print (person[what])


# -Problem 53----------------------------------------------------

# def add(a, b):
#     return a + b

# print(add(3,5))

# -Problem 54----------------------------------------------------

# def addTwoNums():
#     a = int(input("First Number "))
#     b = int(input("Second Number "))
#     return a + b
    
# print(addTwoNums())

# -Problem 55----------------------------------------------------

# def function(n):
#     return n%2 == 0

# print(function(100))    
# print(function(99))    
# print(function(93))    
# print(function(27))    
# print(function(22))    
# print(function(2))    

# -Problem 56----------------------------------------------------

# def message():
#     return "This is a message"
    
# print(message())
# print(message)

# -Problem 57----------------------------------------------------

# list = [1,2,3,4,5,6]
# print(sum(list))

# -Problem 58----------------------------------------------------
# Use the range function to create a range from 0 to 99, use the list function to convert the range into a list. Print the list
# x = list(range(0, 100))
# print(x)

# -Problem 59----------------------------------------------------
# Use the range and list functions to create a list of all of the even numbers from 10 to 50 (including 50). Print out the length of that list

# x = list(range(10, 51, 2))
# print(x)

# -Problem 60----------------------------------------------------
# print the 3rd item of the fifth list.

# list = [[0], [0,1], [0,1,2], [1,2,3], [1,2,3,4], [1,2,3,4,5], [1,2,3,4,5,6]]
# print(list[4][2])

# outerList = []
# for i in range(1,8):
#     innerList = list(range(i))
#     outerList.append(innerList)
    
# print(outerList)


# -Problem 61----------------------------------------------------
# Create an empty list called evens. Write a for loop that loops through all the numbers from 0 to 10. Append the even numbers to the evens list. Print out the evens list

# evens = []
# nums = range(0,11)

# for i in nums:
#     if i%2 == 0:
#         evens.append(i)

# print(evens)
    

# -Problem 62----------------------------------------------------
# Create any list with at least 10 items. Use python's list slicing syntax to print
#   The first item
#   The last item
#   All but the first item
#   All but the last item

# list=["item1", "item2", "item3", "item4", "item5", "item6", "item7", "item8", "item9", "item10"]

# print(list[0])
# print(list[-1])
# print(list[1:])
# print(list[:-1])


# -Problem 63----------------------------------------------------
# Create a dictionary that represents a student. Each student has a name, an age, a nationality, and a list of subjects

# student = {
#     "name":"John", 
#     "age":20, 
#     "nationality":"Irish", 
#     "subjects":["Maths", "Physics", "Music"] 
# }
# for subject in student["subjects"]:
#     print(subject)


# -Problem 64----------------------------------------------------
# Create a list containing at least 4 of the students described in challenge 63. Convert the list into a dictionary, use the the students names as the key for the dictionary.

# students = [
#     {"name":"John", "age":20, "nationality":"Irish",    "subjects":["Maths", "Physics", "Music"] },
#     {"name":"Ben",  "age":21, "nationality":"British",  "subjects":["English", "German", "Music"] },
#     {"name":"Mary", "age":22, "nationality":"American", "subjects":["Geography", "History", "Music"] },
#     {"name":"Jen",  "age":23, "nationality":"French",   "subjects":["Art", "Painting", "Theatre"] },
#     ]
    
# studentsToDictionary = {
#     "John": {"name":"John", "age":20, "nationality":"Irish",    "subjects":["Maths", "Physics", "Music"] },
#     "Ben": {"name":"Ben",  "age":21, "nationality":"British",  "subjects":["English", "German", "Music"] },
#     "Mary": {"name":"Mary", "age":22, "nationality":"American", "subjects":["Geography", "History", "Music"] },
#     "Jen": {"name":"Jen",  "age":23, "nationality":"French",   "subjects":["Art", "Painting", "Theatre"] },
#     }



# -Problem 65----------------------------------------------------
# Create a dictionary where the keys are words in the english language, and the values are the lengths of the words.
# words = ["Apple", "Car", "Fruit", "Phone"]

# d = {}
# for word in words:
#     d[word] = len(word)
# print(d)

# Faster way
# d = {word: len(word) for word in words}
# print(d)

# -Problem 66----------------------------------------------------
# Data Structures Challenge
# A Musician has a name, nationality, and gender. A Musician can play in any number of bands. A Musician can play multiple instruments. For each instrument they have a competency level between 1 and 100.
# Create a data structure that stores the details of each musician along with the bands and instruments.
# It should be possible to get the details of any musician by name, so use a dictionary to store the musician details.


Musicans = {
    "Jimmy":{
        "name":         "Jimmy Base",
        "nationality":  "Spanish",
        "gender":       "male",
        "bands":        ["The Black Cats", "Harmonica Boys", "The blues bros"],
        "instruments":  {
            "guitar": 80, 
            "piano":  60,
            "drums":  83,
            "base":   80,
            "sax":    40
        }
    }
}






