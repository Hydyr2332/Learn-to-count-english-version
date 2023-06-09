# Import random
import random

# Function for checking the correctness of the entered digit
def number_control(num):
    # Check until the word stop or number is entered
    while True:
        if num == 'stop':
            break
        elif not num.isdigit():
            num = input('Ваш ответ: ')
        else:
            break
    return num


# Getting to know the game
print('Компютер составляет пример. Введите ответ.')
print('Для завершения работы введите STOP')
print('*'*50)


# Scoring
point = 0
# Counting games
task_processing = 0
# Counting correct answers
correct_answer = 0
# Counting wrong answers
incorrect_answer = 0
# Proven correct answers
percentage = 0



# Main cycle
user = ''
while user != 'stop':
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    argument = ['-','+','*','/']
    argument_choice = random.choice(argument)

    # Conditions if the first random number is smaller than the second, then swap
    if number1 < number2:
        number1, number2 = number2, number1

    # If the result of division is an infinitely long real number,then find a suitable answer until it is found
    if argument_choice == '/':
        for i in range(100):
            number_sum = eval(str(number1) + argument_choice + str(number2))
            if number_sum - int(number_sum) == 0.0:
                print(f"{number1} {argument_choice} {number2} = {int(number_sum)}")
                break
            else:
                number1 = random.randint(1, 100)
                number2 = random.randint(1, 100)

    # Variable for counting the sum of two random digits and a random arithmetic operator
    number_sum = eval(str(number1) + argument_choice + str(number2))

    # User results
    print(f'Ваши очки: {point}')
    print(f'Обработано задач: {task_processing}')
    print(f'Правильных ответов: {correct_answer}')
    print('-' * 40)

    # The user variable sets the number from the user and checks the entered data
    print(f"{number1} {argument_choice} {number2} = {number_sum}")
    user = input('Ваш ответ: ')
    user = number_control(user)

    # conditions if the user entered the word stop or runs out of points, then the game ends
    if user == 'stop':
        break
    elif point < 0:
        print('У вас закончились очки')
        break
    user = int(user)

    # Variable for counting games
    task_processing += 1

    # Conditions if the answer is correct
    if user == number_sum:
        point += 10
        correct_answer += 1
        print('')
        print('Правильно!')
        print('')

    # Conditions if the answer is wrong
    elif user != number_sum:
        point -= 5
        incorrect_answer += 1
        print('')
        print(f'Ответ неправильный... Правильно: {number_sum}')
        print('')


# Contents and results of the game
print('*'*50)
print('СТАТИСТИКА ИГРЫ')
print(f'Всего примеров: {task_processing}')
print(f'Правильных ответов: {correct_answer}')
print(f'Неправильных ответов: {incorrect_answer}')
print(f'Процент верных ответов: {int((correct_answer/task_processing)*100)}%')
print(f'Возвращайтесь!')
