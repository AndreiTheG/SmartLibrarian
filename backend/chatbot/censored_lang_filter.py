from better_profanity import profanity

profanity.load_censor_words()

def is_inappropiate(text: str) -> bool:
    return profanity.contains_profanity(text)