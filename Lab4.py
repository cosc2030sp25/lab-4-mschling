# Russell Todd
# Lab 4 for UWYO COSC 2030
# Stacks and Queues
#
# You'll be checking parentheses and reversing strings just like you did in C++
# However, in Python the class you'll be using is a List

paren1 = "(()((((()()()((()(((()()()()(((()(()()()(())()())()()))))()()()))()))()())())())))";
paren2 = "()((((((()(((((()((()()()()()(()))))))))()))()(())(())(((((()()(())))(()()())(()))";
paren3 = "(()((()(()()(()(((((()()(()()()((((()()(()()))()))))()()())))))()()())()()))())())";
paren4 = "(()()(((()()(()(()()(()()()()()()(()(((((((((())())))))()))))()()))()())()()))()))";
paren5 = "((())";
paren6 = ")))(((";

rev1 = "sekopog";
rev2 = "racecar";
rev3 = "regnolsignirtssiht";
rev4 = "wonybnwodsihtevahyllufepohdluohssyuguoy";

parens = [paren1, paren2, paren3, paren4, paren5, paren6]
rever = [rev1, rev2, rev3, rev4]

# Finish this function
# You must complete it using a List in a similar manner as a Queue
def parenCheck(toCheck):
    pseudoQueue = []
    for i in toCheck :
        if i == '(':
            pseudoQueue.append('(')
        elif i == ')':
            if len(pseudoQueue) != 0:
                pseudoQueue.pop()
            else:
                return False
        else:
            return False
    if len(pseudoQueue) == 0:
        return True
    else:
        return False



# Finish this function
# You must complete it using a List in a similar manner as a Stack
def stringReverse(toReverse):
    pseudoStack = []
    for i in range(len(toReverse)-1, 0, -1):
        pseudoStack.append(toReverse[i])
    pseudoStack.append(toReverse[0])
    word = ""
    for i in pseudoStack:
        word = word + str(i)
    return word

# Time to check some parentheses
for i in range(6):
    print("\nChecking string"+str(i+1))
    if parenCheck(parens[i]):
        print("Your code says that string"+str(i+1)+" is good. ")
        if i == 0 or i == 2 or i == 3:
            print("Correct!")
        else:
            print("Incorrect!")
    else:
        print("Your code says that string"+str(i+1)+" is bad. ")
        if i == 1 or i == 4 or i == 5:
            print("Correct!")
        else:
            print("Incorrect!")

# Time to reverse some strings
for j in range(4):
    print("\nReversing string"+str(j+1))
    print(stringReverse(rever[j]))
