from random import randint

def get_num(prompt: str ) -> int:
    guess = -1
    try:
        guess = int(input(prompt))
    except Exception as e:
        isinstance(e, (ValueError, TypeError))
    return guess

def guess_game(max_attempts = 7, max_n: int = 112) -> int:
    attempts = 0
    secret = randint(0, max_n)
    guess = get_num('guess the number')
    while guess != secret and attempts < max_attempts:
        attempts += 1
        if guess < secret:
            guess = get_num(f'attempt {attempts} of {max_attempts} try again {guess} is too small')
        else:
            guess = get_num(f'attempt {attempts} of {max_attempts} try again {guess} is too large')
    if guess == secret:
        print(f'Correct guess! secret == {guess} it took {attempts} attempts')
    else:
        print(f'{attempts} attempts You lost too many attempts! secret == {secret} it took {attempts} attempts')
    return attempts


if __name__ == '__main__':
    guess_game()