#I use print a fair amount just so the spacing is a bit better, just a head's up.

#difficulty paragraphs

easy = '''The __1__ language is one of the most common __2__ languages.  More specifically, __1__ is an __3__ oriented __4__ programming language designed as a general purpose tool. '''

medium = '''A __1__ can be a series of any words, letters, numbers, or symbols.  An __2__ is the position within a __1__. The statement 'def example_text()' is used to create a __3__.  Python is one of the most frequently used languages for __4__ learning.'''

hard = '''Within python <=,>=,!=,==,=, and * are all examples of __1__. An __2__ is the value that the __1__ work on.  A repeating action is called a __3__ loop.  One way to end a __3__ loop is to use a __4__.  '''

#answers

easy_answers = ['python','programming','object','dynamic']

medium_answers = ['string','index','function','machine']

hard_answers = ['operators','operand','while','break']



qa_index = 0 #question/answer index

qa_index_max = 4

containers = ['__1__','__2__','__3__','__4__'] #blank reference



def get_level(): #difficulty selection
    global difficulty
    global answers
    difficulty_selection = raw_input('Please choose a difficulty level: easy / medium / hard:  ').lower()
    if difficulty_selection == 'easy': #easy
        difficulty=easy
        answers=easy_answers
        print ''
        print 'Easy Selected!'
        return try_selection()
    if difficulty_selection == 'medium': #medium
        difficulty=medium
        answers=medium_answers
        print ''
        print 'Medium Selected!'
        return try_selection()
    if difficulty_selection == 'hard': #hard
        difficulty=hard
        answers=hard_answers
        print ''
        print 'Hard Selected!' 
        return try_selection()
    else: #misspelling or otherwise incorrect input
        print ''
        print "That quiz doesn't seem to exist, please try choosing another!"
        print ''
        return get_level()

def try_selection(): #number of tries
    global tries
    print ''
    tries = raw_input('How many guesses would you like to have per question?:  ')
    if tries.isdigit() == True: #tests for number, if input is letter than it asks again and states to input a number
        import os
        clear = lambda: os.system('cls')
        clear()
        return play_game()
    else:
        print ''
        print 'Please select a number!'
        return try_selection()
    


def play_game():
    global qa_index
    global guesses
    global difficulty
    guesses = 0
    guesses_left = int(tries) - int(guesses)
    print 'You now have 3 guesses per question!'
    print ''
    print difficulty
    while qa_index < qa_index_max:
        print ''
        print 'What should go in ' + containers[qa_index] + '?' #question
        print ''
        user_answer_1 = raw_input().lower()
        if user_answer_1 == answers[qa_index]: #correct answer
            print ''
            difficulty = difficulty.replace(containers[qa_index],answers[qa_index]) #replace blank with answers
            import os
            clear = lambda: os.system('cls')
            clear()
            print difficulty
            print ''
            print 'Correct!'
            qa_index = qa_index + 1
            guesses = 0
        else: #wrong answer
            import os
            clear = lambda: os.system('cls')
            clear()
            print difficulty
            print ''
            print 'Wrong, please try again.'
            guesses = guesses + 1
            print ''
            print 'You have ' + str(int(tries) - int(guesses)) + ' guesses left!' #remaining guesses based on number chosen previously
        if int(tries) - int(guesses) <= 0: #guesses remaining counter
            print ''
            print '--------------------------------------------------'
            print '====================GAME  OVER===================='
            print '--------------------------------------------------'
            print ''
            print 'Would you like to start over?'
            game_over = raw_input('yes (Main Menu)  /  no (Close Game):  ')
            if game_over == 'yes': #clear previous, restart
                import os
                clear = lambda: os.system('cls')
                clear()
                qa_index = 0 #reset global qa_index value to previous state
                get_level()
            if game_over == 'no': #exit interpreter
                exit()
            else:
                return wrong_option_loser()
    if qa_index == qa_index_max: #this is the screen that will display upon getting all 4 answers correct
        import os
        clear = lambda: os.system('cls')
        clear()
        print difficulty
        print ''
        print '+------------------------------------+'
        print '|              WINNER!!!             |'
        print '+------------------------------------+'
        print 'Would you like to go to the main menu?'
        print 'yes (Main Menu)  /  no (Close Game)'
        print ''
        winner = raw_input()
        if winner == 'yes': #clear previous, restart
            import os
            clear = lambda: os.system('cls')
            clear()
            qa_index = 0 #reset global qa_index value to previous state
            get_level()
        if winner == 'no': #exit interpreter
            exit()
        else:
            return wrong_option_winner()


def wrong_option_loser(): #if user fails to type yes/no properly
    global qa_index
    import os
    clear = lambda: os.system('cls')
    clear()
    print '--------------------------------------------------'
    print '====================GAME  OVER===================='
    print '--------------------------------------------------'
    print 'That does not seem to be an option.'
    print "*Please type 'yes' or 'no' without any formatting*"
    print 'Would you like to go to the main menu?'
    print ''
    print 'yes (Main Menu)  /  no (Close Game)'
    print ''
    loser = raw_input()
    if loser == 'yes': #clear previous, restart
        import os
        clear = lambda: os.system('cls')
        clear()
        qa_index = 0 #reset global qa_index value to previous state
        get_level()
    if loser == 'no': #exit interpreter
        exit()
    else: #loop to beginning
        return wrong_option_loser()


def wrong_option_winner(): #if user fails to type yes/no properly
    global qa_index
    import os
    clear = lambda: os.system('cls')
    clear()
    print '+------------------------------------+'
    print '|              WINNER!!!             |'
    print '+------------------------------------+'
    print 'That does not seem to be an option.'
    print "*Please type 'yes' or 'no' without any formatting*"
    print 'Would you like to go to the main menu?'
    print ''
    print 'yes (Main Menu)  /  no (Close Game)'
    print ''
    winner = raw_input()
    if winner == 'yes': #clear previous, restart
        import os
        clear = lambda: os.system('cls')
        clear()
        qa_index = 0 #reset global qa_index value to previous state
        get_level()
    if winner == 'no': #exit interpreter
        exit()
    else: #loop to beginning
        return wrong_option_winner()
    
        

get_level()

#str.isdigit() reference - https://www.tutorialspoint.com/python/string_isdigit.htm
#global variables reference - https://stackoverflow.com/questions/14051916/python-how-to-make-a-local-variable-inside-a-function-global
#clear interpreter reference - https://stackoverflow.com/questions/517970/how-to-clear-the-interpreter-console
#exit python interpreter reference - https://stackoverflow.com/questions/9730409/exiting-from-python-command-line
