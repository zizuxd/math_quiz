from random import randint

def userinfo():
    # Prompts user for name and university ID.
    while True:
        name = input("Enter your name: ")
        if name:
            break
        else:
            print("Name cannot be empty. Please try again.")

    while True:
        id = input("Please enter your university ID: ")
        
        if id.isdigit() and id != "":
            break
        else:
            print("ID cannot be empty or contain letters. Please try again.")

    return name, id

def printHeader():
    # Prints the header information for the quiz.
    header_info = "Python Math Quiz"
    
    print()
    print("="*100)
    print()
    print('%58s' %(header_info), '\n')
    print("="*100, '\n')
    print("This quiz consists of ten questions each worth l point.")
    print('You are allowed two attempts. The highest score is selected.')
    print()
    print()
    print('Note:')
    print('  -Round the result of float type to 1 decimal place (e.g. 2.75 should become 2.8)')
    print('  -Python rounds to the nearest even number when a number is exactly halfway between two others\n  For example: 2.25 round to 2.2 whereas 2.75 rounds to 2.8')

def getRandomOperator():
    # Randomly selects an operator from +, -, *, /, %, //.
    operators = "+-*/%//"
    operator_index = randint(0, 6)
    
    if operator_index == 6:
        final_operator = '//'
    else:
        final_operator = operators[operator_index]
    
    return final_operator

def generateExpression():
    # Generates a random mathematical expression.
    n1 = randint(0, 10)
    n2 = randint(0, 10)
    n3 = randint(0, 10)
    op1 = getRandomOperator()
    op2 = getRandomOperator()
    
    expression = str(n1)+op1+str(n2)+op2+str(n3)
    return n1, n2, n3, op1, op2, expression

def getPrecedence(operate):
    # Determines the precedence of an operator.
    if operate in "*/%" or operate in "//":
        presedence = 2
    else:
        presedence = 1
 
    return presedence

def evaluateOperation(num1, num2, operator1):
    # Evaluates an operation given the operands and operator.
    if operator1 == '/':
        if num2 != 0:
            operation = num1/num2
        else:
            operation = "Division by zero"
    elif operator1 == '%':
        if num2 != 0:
            operation = num1%num2
        else:
            operation = "Modulus of zero"
    elif operator1 == '*':
        operation = num1*num2
    elif operator1 == '//':
        if num2 != 0:
            operation = num1//num2
        else:
            operation = 'Division by zero'
    elif operator1 == '+':
        operation = num1+num2
    elif operator1 == '-':
        operation = num1-num2
        
    if type(operation) == float:
        operation = round(operation, 1)
    
    return operation

def has_decimal_zero(number):
    # Checks if a number has a decimal zero.
    return number == int(number)

def evaluateExpression(number1, number2, number3, operator1, operator2):
    # Evaluates a mathematical expression.
    presedence1 = getPrecedence(operator1)
    presedence2 = getPrecedence(operator2)
    
    if presedence1 > presedence2:
        result_1 = evaluateOperation(number1, number2, operator1)
        if result_1 == 'Division by zero' or result_1 == 'Modulus of zero' or result_1 == 'Division by zero':
            return result_1
        final_result = evaluateOperation(result_1, number3, operator2)
    elif presedence1 < presedence2:
        result_2 = evaluateOperation(number2, number3, operator2)
        if result_2 == 'Division by zero' or result_2 == 'Modulus of zero' or result_2 == 'Division by zero':
            return result_2
        final_result = evaluateOperation(number1, result_2, operator1)
    elif presedence1 == presedence2:
        result = evaluateOperation(number1, number2, operator1)
        if result == 'Division by zero' or result == 'Modulus of zero' or result == 'Division by zero':
            return result
        final_result = evaluateOperation(result, number3, operator2)
        
    return final_result

def createExpression():
    # Creates a valid mathematical expression and evaluates it.
    while True:
        n1, n2, n3, op1, op2, final_expression = generateExpression()
        result = evaluateExpression(n1, n2, n3, op1, op2)
        
        if result == 'Division by zero' or result == 'Modulus of zero' or result == 'Division by zero':
            n1, n2, n3, op1, op2, final_expression = generateExpression()
            result = evaluateExpression(n1, n2, n3, op1, op2)
        else:
            if has_decimal_zero(result) == True:
                result = int(result)
            break
    
    return result, final_expression

def printReport(user, id, score, attempts):
    # Prints the assessment report.
    if score == 10:
        feedback = "Excellenet!!"
    elif 8 <= score <= 9:
        feedback = "Very Good"
    elif 5 <= score <= 7:
        feedback = 'Good'
    elif score < 5:
        feedback = 'Talk to your instructor'
    
    print()
    print('='*100)
    print('%-30s%-13s%-14s%-13s%-30s' %('Name', 'Id', 'Attempts', 'Score', 'Feedback'))
    print('='*100)
    print('%-30s%-13s%-14s%-13s%-30s' %(user, id, attempts, score, feedback))
    print('='*100)

def main():
    attempt = 0
    score = 0
    user_name, user_id = userinfo()
    print("\nHello", user_name +". The quiz is starting.....")
    printHeader()
    
    for i in range(10):
        answer, finalExpression = createExpression()
        print()
        print("Q" + str(i+1) + ':', finalExpression, '=', end = " ")
        # Assume the user will always input integer or float values
        result = float(input(""))
        
        if result == answer:
            print("Correct")
            score += 1
        else:
            print("Incorrect, answer is: ", answer)
    
    final_score = score
    attempt += 1
    
    print()
    print('Attempt#:', attempt)
    print('Score:', score)
    
        
    if score < 10 and attempt < 2:
        score_2 = 0
        print()
        repeat = input("Would you like to try again? Y/N  ")
        
        if repeat.lower() == 'y':
            printHeader()
            for i in range(10):
                answer, finalExpression = createExpression()
                print()
                print("Q" + str(i+1) + ':', finalExpression, '=', end = " ")
                result = float(input(""))
        
                if result == answer:
                    print("Correct")
                    score_2 += 1
                else:
                    print("Incorrect, answer is: ", answer)
            
            if score >= score_2:
                final_score = score
            else:
                final_score = score_2
                
            attempt += 1
            print()
            print('Attempt#:', attempt)
            print('Score:', score_2)
        
        print('Thank you - you have completed this assessment!')
        print('Your score report is prsented below...')
        
        printReport(user_name, user_id, final_score, attempt)
        
    else:
        print('Thank you - you have completed this assessment!')
        print('Your score report is prsented below...')
        printReport(user_name, user_id, final_score, attempt)

main()
