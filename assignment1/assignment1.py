#Task 1
def hello():
    return "Hello!"
#Task 2
def greet(name):
    return f'Hello, {name}!'
#Task 3
def calc(a,b, operation = 'multiply'):
    try:
        if operation == 'add':
            return a + b
        elif operation == 'divide':
            return a / b
        elif operation == 'multiply':
            return a * b
        elif operation == 'subtract':
            return a - b
        elif operation == 'modulo':
            return a % b
        elif operation == 'int_divide':
            return a // b
        elif operation == 'power':
            return a**b
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"
#Task 4
def data_type_conversion(value,type_value):
    try:
        match type_value:
            case 'int':
                return int(value)
            case 'str':
                return str(value)
            case 'float':
                return float(value)
    except ValueError:
        return f"You can't convert {value} into a {type_value}."
#Task 5
def grade(*args):
    try:
        grade = sum(args) // len(args)
        if grade < 60:
            return 'F'
        if 60 <= grade <= 69:
            return 'D'
        if 70 <= grade <= 79:
            return 'C'
        if 80 <= grade <= 89:
            return 'B'
        if grade >= 90:
            return 'A'
    except TypeError:
        return "Invalid data was provided."
#Task 6
def repeat(string,count):
        new_string = ""
        for i in range (count+1):
            new_string = i * string
        return new_string
#Task 7
def student_scores(positional, **kwargs):
    if positional == 'best':
        score = max(kwargs.values())
        for key,value in kwargs.items():
            if value == score:
                return key
    elif positional == 'mean':
        return sum(kwargs.values())/len(kwargs)
#Task 8
def titleize(string):
   exception = ["a", "on", "an", "the", "of", "and", "is", "in"]
   new_string = string.lower()
   result = []
   new_list = new_string.split()
   for i,word in enumerate(new_list):
       if word in exception and i != 0 and i != (len(new_list)-1):
           result.append(word)
       else:
           result.append(word.capitalize())
   new_string = " ".join(result)
   return new_string
#Task 9
def hangman(secret,guess):
    result = ''
    for letter in str(secret):
        if letter in guess:
            result += letter
        else:
            result += "_"
    return result
#Task 10
def pig_latin(string):
    consonant = (
    'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z')
    vowel = ('a', 'e', 'i', 'o', 'u')
    new_string = []

    for word in string.split():
        count = 0
        if word.startswith(vowel):
            word = word + 'ay'
            new_string.append(word)
        elif word.startswith(consonant):
            for i, letter in enumerate(word):
                if letter in consonant:
                    if letter == 'q' and word[i + 1] == 'u':
                        count += 1
                    count += 1
                else:
                    break
            new_string.append(word[count:] + word[:count] + 'ay')
    return " ".join(new_string)


