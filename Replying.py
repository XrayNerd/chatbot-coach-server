import random

muscle_exercises = {}
depth = 0

def replyToGreeting():
    return "Hello! I'm your personal trainer, Ciri."


def exercisesToDict():
    """Reads in a file, returns dictionary
        with muscles as key and exercises as
        values"""
    f=open("StrengthExercises.txt" , "r")
    file_string = f.read()
    file_list = file_string.splitlines()
    for line in file_list:
        temp_list = line.split(",")
        exercise, muscle = temp_list[0], temp_list[1]
        muscle = muscle[1:] # Remove space at beginning
        if muscle in muscle_exercises:
            # If it exists add to already existing list
            muscle_exercises[muscle].append(exercise)
        else:
            # Create new list and assign first exercise
            muscle_exercises[muscle] = [exercise]

def handleReply(greet=False, exerciseList=False,calorieCount=False, date=False, depth=0):
    returnString = ""
    if greet=True:
        returnString += replyToGreeting() + "<br />"

    if exerciseList != False:
        if depth == 0:
            returnString += generatePrimaryReply(muscleList)
        #Answer too vague, needs more infomation
        else:
            returnString += generateSecondaryReply(muscleList)

    if calorieCount != False:
        """TO DO"""
        continue

    if date != False:
        """TO DO"""
        continue

    return returnString

def generatePrimaryReply(muscleList):
    """Takes in a list of muscles that the user has inputed
    and returns a statement for an individual exercise or
    queries the user for an individual exercise"""
    for muscle in muscleList:
        reply = muscle
        replyLower = reply.lower()
        if replyLower in muscle_exercises.keys():
            returnString = "You could try these exercises!:<br />"

            #Add the exercises and a break to the end of the message string
            for exercise in muscle_exercises[replyLower]:
                returnString += exercise + "<br />"
            return returnString

def generateSecondaryReply(muscleList):
    """TO DO"""
    return 0

def motivationQuote():
    quote = ["No pain, no gain!" , "You the man/woman!"
    , "Hit it champ!" , "Just do it!(copyright NIKE)"]
    return random.choice(quote)

#greeting()
#exercisesToDict()
#motivationQuote()
