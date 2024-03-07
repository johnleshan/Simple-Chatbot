import random
from time import sleep

def talk(text):
    print('\033[1;34m>>>\033[m {}\033[m'.format(text))

def ask_user():
    return str(input('What is your name? ')).strip().capitalize()

def greet(name):
    talk('Hello {}!'.format(name))

def ask_for_age():
    age = int(input('\033[1;34m>>>\033[m How old are you? '))
    return age

def ask_for_color():
    talk('What is your favorite color?')
    color = str(input('\033[1;34m>>>\033[m ')).strip().lower()
    return color

def ask_for_city():
    city = str(input('\033[1;34m>>>\033[m What is your favorite city? '))
    return city

def ask_for_food():
    talk('What is your favorite food?')
    food = str(input('\033[1;34m>>>\033[m ')).strip().lower()
    return food

def ask_for_sport():
    talk('What is your favorite sport?')
    sport = str(input('\033[1;34m>>>\033[m ')).strip().lower()
    return sport

def show_results(name, age, color, city, food, sport):
    talk("\n")
    talk('Here are your results: ')
    sleep(2)
    print('\033[1;34m>>>\033[m \033[1;36mYour name is {}\033[m'.format(name))
    sleep(2)
    print('\033[1;34m>>>\033[m \033[1;36mYou are {} years old\033[m'.format(age))
    sleep(2)
    print('\033[1;34m>>>\033[m \033[1;36mYour favorite color is {}\033[m'.format(color.capitalize()))
    sleep(2)
    print('\033[1;34m>>>\033[m \033[1;36mYour favorite city is {}\033[m'.format(city.capitalize()))
    sleep(2)
    print('\033[1;34m>>>\033[m \033[1;36mYour favorite food is {}\033[m'.format(food))
    sleep(2)
    print('\033[1;34m>>>\033[m \033[1;36mYour favorite sport is {}\033[m'.format(sport.capitalize()))
    sleep(2)

def main():
    name = ask_user()
    greet(name)
    age = ask_for_age()
    color = ask_for_color()
    city = ask_for_city()
    food = ask_for_food()
    sport = ask_for_sport()
    show_results(name, age, color, city, food, sport)

if __name__ == '__main__':
    main()