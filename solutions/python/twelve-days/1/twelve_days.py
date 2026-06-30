def recite(start_verse, end_verse):
    days = [
        "first",
        "second",
        "third",
        "fourth",
        "fifth",
        "sixth",
        "seventh",
        "eighth",
        "ninth",
        "tenth",
        "eleventh",
        "twelfth",
    ]

    gifts = [
        "a Partridge in a Pear Tree",
        "two Turtle Doves",
        "three French Hens",
        "four Calling Birds",
        "five Gold Rings",
        "six Geese-a-Laying",
        "seven Swans-a-Swimming",
        "eight Maids-a-Milking",
        "nine Ladies Dancing",
        "ten Lords-a-Leaping",
        "eleven Pipers Piping",
        "twelve Drummers Drumming",
    ]

    verses = []

    for verse_number in range(start_verse, end_verse + 1):
        day = days[verse_number - 1]

        # Cogemos los regalos de esa estrofa hacia atrás.
        current_gifts = gifts[:verse_number][::-1]

        # Desde la segunda estrofa, el último regalo lleva "and".
        if verse_number > 1:
            current_gifts[-1] = "and " + current_gifts[-1]

        gifts_text = ", ".join(current_gifts)

        verse = (
            f"On the {day} day of Christmas my true love gave to me: "
            f"{gifts_text}."
        )

        verses.append(verse)

    return verses