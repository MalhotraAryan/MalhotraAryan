'''
This program represents a game called Hangman which is basically a movie guessing game.
It is linked to mysql and stores user records in a database.
Each user is given 8 attempts and each user's performance is judged by the score and the time taken.

This program uses various libraries like random, datetime, and mysql connector.
The user can sign in, sign up, delete account, or change the password of their account.
The user is given two hints to use in case he/she is stuck.

This program is purely based on libraries, conditionals and loops.
No user defined functions have been created.
'''
import random
import datetime
import mysql.connector as m1                                                        
mydb = m1.connect(host="localhost",user="root",passwd = "admin", database = "hangman")
mycursor = mydb.cursor()
startAgain = False
print('''Welcome to Hangman! This Hangman is a game to guess movies letter by letter. Here is some general information:-
      1) You have to guess movie letters from a-z.
      2) Enter the letters in lower case.
      3) The game will be timed.
      4) You will have 8 attempts to guess the movie.
      5) The number of attempts left will give your score out of 8.
      6) You will get two hints.''')
ch = input('''Do you want to sign up or login or delete an existing account or change the password of an existing account?\n\
Enter S for sign up, L for login, D for deleting an existing account, or C for changing the password of an existing account here: ''')
while ch == "S" or ch=="s" or ch == "L" or ch == "l" or ch == "d" or ch == "D" or ch == "C" or ch == "c":
    if ch == "S" or ch == "s":
        userName = input("Enter a username:- ")
        mycursor.execute("SELECT USERNAME FROM LOGIN")
        result1 = mycursor.fetchall()
        for i in result1:
            if i[0] == userName:
                print("UserName already exists.")
                break
        else:
            password = input("Enter a password that is 8-30 characters long here: ")
            if 8 <= len(password) <= 30:
                mycursor.execute("SELECT PASSWORD FROM LOGIN")
                result2 = mycursor.fetchall()
                for j in result2:
                    if j[0] == password:
                        print("This password is currently being used by an existing user.")
                        break
                else:
                    sql = "Insert into login values (%s,%s)"
                    val = (userName,password)
                    mycursor.execute(sql,val)
                    print(mycursor.rowcount,"record inserted into database")
                    mydb.commit()
            else:
                print("Password does not meet length criteria.")
    elif ch =="L" or ch == "l":
        username = input("Enter your existing username here: ")
        mycursor.execute("SELECT USERNAME FROM LOGIN")
        result3 = mycursor.fetchall()
        for i in result3:
            if i[0] == username:
                password = input("Enter the password to your existing account here: ")
                sql = "SELECT PASSWORD FROM LOGIN WHERE USERNAME = %s"
                val = (username,)
                mycursor.execute(sql,val)
                result4 = mycursor.fetchall()
                for j in result4:
                    if j[0] == password:
                        startAgain = True
                        print("LOGIN SUCCESSFUL.....")
                        break
                else:
                    print("You entered the wrong password.")
                break
        else:
            print("This username does not exist. Please restart the game to sign up.")
    elif ch == "d" or ch == "D":
        username = input("Enter your existing username here: ")
        mycursor.execute("SELECT USERNAME FROM LOGIN")
        result5 = mycursor.fetchall()
        for i in result5:
            if i[0] == username:
                password = input("Enter the password to your existing account here: ")
                sql = "SELECT PASSWORD FROM LOGIN WHERE USERNAME = %s"
                val = (username,)
                mycursor.execute(sql,val)
                result6 = mycursor.fetchall()
                for j in result6:
                    if j[0] == password:
                        sql_1 = "DELETE FROM LOGIN WHERE USERNAME = %s"
                        val_1 = (username,)
                        mycursor.execute(sql_1,val_1)
                        mydb.commit()
                        print("Account Deleted Successfully.")
                        break
                else:
                    print("You entered the wrong password.")
                break
        else:
            print("This username does not exist. Please enter D to try again.")
    elif ch == "c" or ch == "C":
        username = input("Enter your existing username here: ")
        mycursor.execute("SELECT USERNAME FROM LOGIN")
        result7 = mycursor.fetchall()
        for i in result7:
            if i[0] == username:
                password = input("Enter the current password to your existing account here: ")
                sql = "SELECT PASSWORD FROM LOGIN WHERE USERNAME = %s"
                val = (username,)
                mycursor.execute(sql,val)
                result8 = mycursor.fetchall()
                for j in result8:
                    if j[0] == password:
                        new_password = input("Enter the new password that you want for your account here: ")
                        if 8 <= len(new_password) <= 30:
                            sql_1 = "UPDATE LOGIN SET PASSWORD = %s WHERE USERNAME = %s"
                            val_1 = (new_password,username)
                            mycursor.execute(sql_1,val_1)
                            mydb.commit()
                            print("Password Changed Successfully.")
                            break
                        else:
                            print("New password does not meet length criteria")
                            break
                else:
                    print("You entered the wrong password.")
                break
        else:
            print("This username does not exist. Please enter C to try again.")
    ch = input("\n\nConsider the following response options:\n\
Enter S to repeat the sign up process if there was some failure.\n\
Enter L to try logging in again.\n\
Enter D to try deleting an existing account again\n\
Enter C to try changing the password again.\n\
If login was successful, enter N.\n\
If you have not logged in and want to quit, then enter N.\n\
NOTE THAT IT IS COMPULSORY TO LOGIN WHETHER DIRECTLY OR AFTER SIGNING UP TO START THE GAME.\n\
Enter your response here(S or L or D or C or N): ")

figure = ['''

                 _____

                |     |

                      |

                      |

                      |

                     _|_''', '''

                 _____

                |     |

                O     |

                      |

                      |

                     _|_''', '''

                 _____

                |     |

                O     |

                |     |

                      |

                     _|_''','''

                 _____

                |     |

                O     |

                |     |

                |     |

                     _|_''', '''

                 _____

                |     |

                O     |

               /|     |

                |     |

                     _|_''', '''

                 _____

                |     |

                O     |

               /|\    |

                |     |

                     _|_''', ''' 

                 _____

                |     |

                O     |

               /|\    |

                |     |

               /     _|_''', '''

                 _____

                |     |

                O     |

               /|\    |

                |     |

               / \   _|_''']



movieList = ["independence day","jumanji","war", "zindagi na milegi dobara"]

bh = input("Do you want to start the game? Enter S to start or any other character to quit here: ")
if bh == "S" or bh == "s":
    startAgain = True
else:
    startAgain = False


while startAgain:
    start_time = datetime.datetime.now().replace(microsecond = 0)
    print(figure[0])
    movieList = ["independence day","jumanji","war","zindagi na milegi dobara"]
    wordSelected = random.choice(movieList).lower()
    guessInput = None
    lettersGuessed = []
    blanksForWord = []
    l1 = []
    for l in wordSelected:
        if l == " ":
            blanksForWord.append(" ")
        else:
            blanksForWord.append('-')
    noOfHints = 2
    attemptsLeft = 8
    while attemptsLeft > 0:
        if (attemptsLeft != 0 and '-' in blanksForWord):
            print('\n You have',attemptsLeft,'attempts left.')
            print("".join(blanksForWord))
        try:
            guessInput = str(input('\n Guess any 1 letter between A-Z: ')).lower()
        except:
            print('That is not a valid input. Please try again.')
            continue
        else:
            if not guessInput.isalpha():
                print('That is not a letter. Plaese try again.')
                continue
            elif len(guessInput) > 1:
                print('That is more than 1 letter. Please try again.')
                continue
            elif guessInput in lettersGuessed:
                print('You have already guessed that letter. Please try again.')
                continue
            else:
                pass
            lettersGuessed.append(guessInput)
            pendingLettersList = list(wordSelected)
            if guessInput not in wordSelected:
                attemptsLeft -= 1
                print("Oops! Wrong guess!")
                print(figure[len(figure)-1-attemptsLeft])
            else:
                beginSearch = True
                indexToBeginSearch = 0
                while beginSearch:
                       try:
                            indexMatch = wordSelected.index(guessInput,indexToBeginSearch)
                            blanksForWord[indexMatch] = guessInput
                            indexToBeginSearch = indexMatch + 1
                       except:
                           beginSearch = False
            print("".join(blanksForWord))
            hint = "y"
            while hint in ("y" or "Y" or "yes" or "Yes" or "YES") and "-" in blanksForWord:
                if noOfHints > 0:
                    hint = str(input("\n Do you want a hint?: "))
                    if hint == "y" or hint == "Y" or hint == "yes" or hint == "Yes" or hint == "YES":
                        for i in lettersGuessed:
                            if i in pendingLettersList:
                                x = pendingLettersList.count(i)
                                for j in range(x):
                                    pendingLettersList.remove(i)
                        hintLetter = random.choice(pendingLettersList).lower()
                        beginSearch = True
                        indexToBeginSearch = 0
                        while beginSearch:
                                    try:
                                        indexMatch = wordSelected.index(hintLetter,indexToBeginSearch)
                                        blanksForWord[indexMatch] = hintLetter
                                        indexToBeginSearch = indexMatch + 1
                                        lettersGuessed.append(hintLetter)
                                    except:
                                        beginSearch = False
                        print("".join(blanksForWord))
                        noOfHints -= 1
                    elif hint in ("n" or "N" or "no" or "No" or "NO"):
                        break
                    else:
                        print("You entered an inappropriate choice.")
                elif noOfHints == 0:
                        print("You have no hints left.")
                        break
            if attemptsLeft == 0:
                print('Sorry the game is over. The word was ' + wordSelected)
                end_time = datetime.datetime.now().replace(microsecond = 0)
                timeTaken = end_time - start_time
                sql_2 = "INSERT INTO ALLSCORES VALUES (%s,%s,%s,%s)"
                val_2 = (username,0,timeTaken,"LOST")
                mycursor.execute(sql_2,val_2)
                mydb.commit()
                print("\n\nYour Current Score details\n\n")

                gap = " "*3
                headerRow = f"{'Username':10s}{gap}{'Score':5s}{gap}{'TimeTaken':10s}{gap}{'Result':6s}"
                print("="*40)
                print(headerRow)
                print("-"*40)
                data = [username,0,str(timeTaken),"LOST"]
                record = f"{data[0]:10s}{gap}{data[1]:^5d}{gap}{data[2]:10s}{gap}{data[3]:6s}"
                print(record)
                print("="*40)

                print("\n\nHere are the maximum scores of each user\n\n")

                print("="*40)
                print(headerRow)
                print("-"*40)
                mycursor.execute("SELECT username,max(score),timeTaken,result FROM ALLSCORES GROUP BY USERNAME")
                maxScore = mycursor.fetchall()
                for i in maxScore:
                    record1 = f"{i[0]:10s}{gap}{i[1]:^5d}{gap}{str(i[2]):10s}{gap}{i[3]:6s}"
                    print(record1)
                print("="*40)

                print("\n\nHere are all scores for the previous games you played\n\n")

                print("="*40)
                print(headerRow)
                print("-"*40)
                sql_3 = "SELECT * FROM ALLSCORES WHERE USERNAME = %s"
                val_3 = (username,)
                mycursor.execute(sql_3,val_3)
                maxScore1 = mycursor.fetchall()
                for i in maxScore1:
                    record2 = f"{i[0]:10s}{gap}{i[1]:^5d}{gap}{str(i[2]):10s}{gap}{i[3]:6s}"
                    print(record2)
                print("="*40)

                reply = input( '\n Would you like to play again?(yes or no): ').lower()

                if reply not in ('yes' or 'y' or 'Yes' or 'YES'):
                    startAgain = False
                    print('Thanks for playing Hangman.')
                break
            if '-' not in blanksForWord:
                print('''

           ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆

           ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆    

                    

                        \O/      

              ~WINNER~   |   ~WINNER~        

                         |    

                        / \ 

                                           

           ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆

           ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆''')

                print('\n Congratulations you have won.', wordSelected, 'was the word.')

                end_time = datetime.datetime.now().replace(microsecond = 0)
                timeTaken = end_time - start_time
                sql_2 = "INSERT INTO ALLSCORES VALUES (%s,%s,%s,%s)"
                val_2 = (username,attemptsLeft,timeTaken,"WON")
                mycursor.execute(sql_2,val_2)
                mydb.commit()

                print("\n\nYour Current Score details\n\n")

                
                gap = " "*3
                headerRow = f"{'Username':10s}{gap}{'Score':5s}{gap}{'TimeTaken':10s}{gap}{'Result':6s}"
                print("="*40)
                print(headerRow)
                print("-"*40)
                data = [username,attemptsLeft,str(timeTaken),"WON"]
                record = f"{data[0]:10s}{gap}{data[1]:^5d}{gap}{data[2]:10s}{gap}{data[3]:6s}"
                print(record)
                print("="*40)

                print("\n\nHere are the maximum scores of each user\n\n")

                print("="*40)
                print(headerRow)
                print("-"*40)
                mycursor.execute("SELECT username,max(score),timeTaken,result FROM ALLSCORES GROUP BY USERNAME")
                maxScore = mycursor.fetchall()
                for i in maxScore:
                    record1 = f"{i[0]:10s}{gap}{i[1]:^5d}{gap}{str(i[2]):10s}{gap}{i[3]:6s}"
                    print(record1)
                print("="*40)


                print("\n\nHere are all scores for the previous games you played\n\n")


                print("="*40)
                print(headerRow)
                print("-"*40)
                sql_3 = "SELECT * FROM ALLSCORES WHERE USERNAME = %s"
                val_3 = (username,)
                mycursor.execute(sql_3,val_3)
                maxScore1 = mycursor.fetchall()
                for i in maxScore1:
                    record2 = f"{i[0]:10s}{gap}{i[1]:^5d}{gap}{str(i[2]):10s}{gap}{i[3]:6s}"
                    print(record2)
                print("="*40)
                

                reply = input( '\n Would you like to play again?(yes or no): ').lower()

                if reply not in ('yes' or 'y' or 'Yes' or 'YES'):

                    startAgain = False

                    print('Thanks for playing Hangman.')

                break
