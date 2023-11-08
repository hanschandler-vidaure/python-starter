import datetime
import random
from datetime import datetime
import hashlib

def first():
  myList = []
  for _ in range(0, 10):
    myList.append(random.randint(0, 100))
  total = sum(myList)
  print(myList)
  
  # optional
  index = 1
  for int in myList:
    print(f'{index} = {int}')
    index+=1

  print(f'The sum is: {total}')

def second():
  width = float(input('Enter width: '))
  height = float(input('Enter height: '))
  length = float(input('Enter length: '))
  volume = (width * height * length)
  volume = round(volume, 2)
  print(f'Volume is: {volume}.')

def third():
    bool = False
    array = input('Enter list of numbers: ')
    myList = array.split(',')
    first = myList[0].strip()
    last = myList[-1].strip()
    if first == last:
        bool = True
    print(bool)

def fourth():
    text = '''
    Python was conceived in the late 1980s by Guido van Rossum at Centrum Wiskunde & Informatica (CWI) 
    in the Netherlands as a successor to ABC programming language, which was inspired by SETL capable 
    of exception handling and interfacing with the Amoeba operating system. Its implementation began in 
    December 1989. Van Rossum shouldered sole responsibility for the project, as the lead developer, 
    until 12 July 2018, when he announced his permanent vacation from his responsibilities as Python's 
    Benevolent Dictator For Life, a title the Python community bestowed upon him to reflect his 
    long-term commitment as the project's chief decision-maker. In January 2019, active Python core 
    developers elected a 5-member Steering Council to lead the project. As of 2021, the current members of this council 
    are Barry Warsaw, Brett Cannon, Carol Willing, Thomas Wouters, and Pablo Galindo Salgado."
    '''
    wordCount = 0
    wordList = text.split(' ')
    # for word in wordList:
    #     if (word == 'Python'):
    #         wordCount += 1
    for word in wordList:
        string = word.casefold()
        if "python" in string:
            wordCount += 1
    print(wordCount)

def fifth():
    myList = [1,2,3]
    mySet = {3,4,5}
    mySet.update(myList)
    print(mySet)

def sixth():
    myList = [11, 100, 101, 999, 1001]
    myList.reverse()
    print(myList)

def seventh():
    number = random.randint(1,100)
    print(number, end="")
    if number < 10:
        print(": You lose.")
    elif number < 50:
        print(": Try again")
    else:
        print(": You win!")

def eighth():
    myList = [6,2,7,3,77,7,1]
    lowest = myList[0]
    for num in myList:
        if num < lowest:
            lowest = num
    print(lowest)

def ninth():
    strInput = input('Enter a string: ')
    if strInput.isupper():
        print("True")
    else:
        print("False")
    # print(strInput.isupper())

def tenth():
    # vowels = {a,e,i,o,u}
    vowels = 0
    consonants = 0
    strInput = input('Enter a string: ')
    for letters in strInput:
        if letters=="a" or letters=="e" or letters=="i" or letters=="o" or letters=="u":
            vowels+=1
        else:
            consonants+=1
    print("Vowels: ")
    print(vowels)
    print("Consonants: ")
    print(consonants)

def eleventh():
    dates = str(date.today().strftime("%m/%d/%Y"))
    f = open("output.txt", "w")
    f.write(f"Today's date is: {dates}.")
    f.close()
    
def twelfth():
    try:
        strInput = float(input('Enter a string: '))
        if type(strInput) == float:
            raise FloatException('Input is entered as float!')
        strInput*=-1
        print(strInput)
    except FloatException as fe:
        print(fe)

class FloatException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def thirteenth():
    done = False
    while done != True:
        firstInt = (input('Enter first integer: '))
        if firstInt.lower() == "exit":
            break
        else:
            firstInt = int(firstInt)
        secondInt = (input('Enter second integer: '))
        if secondInt.lower() == "exit":
            break
        else:
            secondInt = int(secondInt)
        total = firstInt + secondInt
        print(f"Answer: {total}")

def fourteenth():
    done = False
    while done != True:
        firstInt = (input('Enter first integer: '))
        if firstInt.lower() == "exit":
            break
        else:
            firstInt = int(firstInt)
        secondInt = (input('Enter second integer: '))
        if secondInt.lower() == "exit":
            break
        else:
            secondInt = int(secondInt)
        
        while done != True:
            operator = (input('Enter operation (add, sub, mul, div): ')).lower()
            if operator == "exit":
                break
            elif operator == "add":
                done=True
                print(f"Answer: {firstInt + secondInt}")
            elif operator == "sub":
                done=True
                print(f"Answer: {firstInt - secondInt}")
            elif operator == "mul":
                done=True
                print(f"Answer: {firstInt * secondInt}")
            elif operator == "div":
                done=True
                print(f"Answer: {firstInt / secondInt}")
                # print(operate(operator,firstInt,secondInt))
            else:
                print("Invalid operator, try again")
        
        
def operate(operation,x,y):
    match operation:
        case "add":
            return x + y
        case "sub":
            return x - y
        case "mul":
            return x * y
        case "div":
            return x / y

def fifteenth():
    done = False
    while done != True:       
        f = open("output2.txt", "a")
        firstInt = (input('Enter first integer: '))
        if firstInt.lower() == "exit":
            break
        else:
            firstInt = int(firstInt)
        secondInt = (input('Enter second integer: '))
        if secondInt.lower() == "exit":
            break
        else:
            secondInt = int(secondInt)
        
        done1 = False
        while done1 != True:
            operator = (input('Enter operation (add, sub, mul, div): ')).lower()
            dates = f'{str(datetime.now())}' 
            if operator == "exit":
                break
            elif operator == "add":
                done1=True
                f.write(f"{dates} {firstInt} add {secondInt} = {firstInt+secondInt}.\n")
                print(f"{dates} {firstInt} add {secondInt} = {firstInt+secondInt}.")
            elif operator == "sub":
                done1=True
                f.write(f"{dates} {firstInt} sub {secondInt} = {firstInt-secondInt}.\n")
                print(f"{dates} {firstInt} sub {secondInt} = {firstInt-secondInt}.")
            elif operator == "mul":
                done1=True
                f.write(f"{dates} {firstInt} mul {secondInt} = {firstInt*secondInt}.\n")
                print(f"{dates} {firstInt} mul {secondInt} = {firstInt*secondInt}.")
            elif operator == "div":
                done1=True
                f.write(f"{dates} {firstInt} div {secondInt} = {firstInt/secondInt}.\n")
                print(f"{dates} {firstInt} div {secondInt} = {firstInt/secondInt}.")
            else:
                print("Invalid operator, try again")
    f.close()

def sixteenth():
    dictionary = {}
    while 1:
        username = str(input("Enter your username: "))
        if username.lower() == "exit":
            break
        string = str(input("Enter your secret password: "))
        password = hashlib.sha256(string.encode()).hexdigest()
        # password = hashlib.sha256()
        # password.update(b'{string}')
        # password.hexdigest()
        dictionary.update({username:password})
    for x,y in dictionary.items():
        print(f'{x} :\n{y}')
        
def seventeenth():
    dictionary = {}
    while 1:
        operation = str(input("Enter mode (add|login): "))
        if operation.lower() == "exit":
            break
        if any(operation.lower() == x for x in ["add","login"]):
            username = str(input("Enter your username: "))
            string = str(input("Enter your secret password: "))
            password = hashlib.sha256(string.encode()).hexdigest()

            match operation:
                case "add":
                    dictionary.update({username:password})
                case "login":
                    if password == dictionary[username]:
                        print('Password is correct')
                    else:
                        print('Incorrect Password')
        else:
            print("Incorrect operation.")

    for x,y in dictionary.items():
        print(f'{x} :\n{y}')

# def eighteenth():

    
if __name__ == "__main__":  
#   first()
#   second()
#   third()
#   fourth()
#   fifth()
#   sixth() 
#   seventh()
#   eighth()
#   ninth()
#   tenth()
#   eleventh()
#   twelfth()
#   thirteenth()
#   fourteenth()
#   fifteenth()
#   sixteenth()
    seventeenth()