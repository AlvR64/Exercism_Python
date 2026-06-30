def translate_one(text):
    vowels = "aeiou"

    # Regla 1
    if text.startswith(("a", "e", "i", "o", "u", "xr", "yt")):
        return text + "ay"

    for index, letter in enumerate(text):

        # Regla 3
        if text[index:index + 2] == "qu":
            cut = index + 2
            return text[cut:] + text[:cut] + "ay"

        # Regla 4
        if letter == "y" and index > 0:
            return text[index:] + text[:index] + "ay"

        # Regla 2
        if letter in vowels:
            return text[index:] + text[:index] + "ay"


def translate(text):
    return " ".join(translate_one(part) for part in text.split())