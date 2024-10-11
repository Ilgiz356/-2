import random
def game():
    number_to_guess = random.randint(1,100)
    guess = None
    tries = 0

    while guess != number_to_guess:
        guess = int(input("Угадайте число от 1 до 100: "))
        tries += 1
        if guess < number_to_guess:
            print("Слишком мало! Попробуй снова.")
        elif guess > number_to_guess:
            print("Слишком много! Попробуй снова.")

    print(f"Поздравляю! Ты угадал число {number_to_guess} за {tries} попыток.")

    if __name__ == "__main__":
        game()