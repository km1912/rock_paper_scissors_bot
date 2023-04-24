# import statements
import random
from lexicon.lexicon_ru import LEXICON_RU

# func, returning random bot choice in game
def get_bot_choice() -> str:
    return random.choice(['rock', 'paper', 'scissors'])

# func, that returns key from dict that The value 
# passed as an argument is stored - the user's choice
def _normalize_user_answer(user_answer: str) -> str:
    for key in LEXICON_RU:
        if LEXICON_RU[key] == user_answer:
            return key
    raise Exception

# determining winner func
def get_winner(user_choice: str, bot_choice: str) -> str:
    user_choice = _normalize_user_answer(user_choice)
    rules: dict[str, str] = {'rock': 'scissors',
                             'scissors': 'paper',
                             'paper': 'rock'}
    if user_choice == bot_choice:
        return 'nobody_won'
    elif rules[user_choice] == bot_choice:
        return 'user_won'
    else:
        return 'bot_won'
