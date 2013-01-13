from random import randint

name = raw_input("Please enter your name: ")
print "Hello", name
print "This is a quiz on the multiplication tables"

while(True):
    number_of_questions_input = raw_input("How many questions would you like? ")
    try:
        number_of_questions = int(number_of_questions_input)
        break
    except ValueError:
        print "'{0}' is not a number!".format(number_of_questions_input)

correct_answers = 0
remaining_questions = number_of_questions

while remaining_questions > 0:

    first_number = randint(1,12)
    second_number = randint(1,12)
    
    while(True):
        answer_input = raw_input("What is {0} x {1}? ".format(first_number, second_number))
    
        try:
            answer = int(answer_input)
            break
        except ValueError:
            print "'{0}' is not a number!".format(answer_input)
    
    if answer == first_number * second_number:
        correct_answers += 1
    remaining_questions -= 1

print "You guessed {0}/{1} correct {2}".format(correct_answers, number_of_questions, name)
