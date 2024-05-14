import random
logo = '''

 ___                                 _____  _                _   _                    _                  
(  _`\                              (_   _)( )              ( ) ( )                  ( )                 
| ( (_) _   _    __    ___   ___      | |  | |__     __     | `\| | _   _   ___ ___  | |_      __   _ __ 
| |___ ( ) ( ) /'__`\/',__)/',__)     | |  |  _ `\ /'__`\   | , ` |( ) ( )/' _ ` _ `\| '_`\  /'__`\( '__)
| (_, )| (_) |(  ___/\__, \\__, \     | |  | | | |(  ___/   | |`\ || (_) || ( ) ( ) || |_) )(  ___/| |   
(____/'`\___/'`\____)(____/(____/     (_)  (_) (_)`\____)   (_) (_)`\___/'(_) (_) (_)(_,__/'`\____)(_)   
                                                                                                         
                                                                                                         

'''
print(logo)
print("Welcome to the Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# Set Lives
lives = 0

# Player chooses difficulty
difficulty = input("Choose a difficulty. Type 'easy' or 'hard':").lower()
if difficulty == 'hard':
  lives = 5
else:
  lives = 10

# Choose number between 1-100
number = random.randint(1,100)

# Game loop
while lives > 0:
  print(f"You have {lives} attempts remaining to guess the number.")
  guess = int(input("Make a guess:"))
  lives -= 1
  
  if guess > number:
    if lives > 0:
      print("Too high.")
      print("Guess again.")
    
  elif guess < number:
    if lives > 0:
      print("Too low.")
      print("Guess again.")
    
  else:
    print(f"You got it! The answer is {number}")
    break

if lives == 0 and guess != number:
  print("You've run out of lives. You lost!")
  print(f"The number was {number}.")