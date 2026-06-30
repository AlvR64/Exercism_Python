def response(hey_bob):

    if hey_bob.strip() == "":
        return "Fine. Be that way!"

    is_upper = True if hey_bob.isupper() else False
    is_question = True if hey_bob.strip()[-1] == "?" else False
    
    match(is_upper, is_question):
        case(True, True):
            return "Calm down, I know what I'm doing!"
        case(True, False):
            return "Whoa, chill out!"
        case(False, True):
            return "Sure."

    return "Whatever."
