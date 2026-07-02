def transform(legacy_data):

    new_data = {}
    
    for points in legacy_data:
        for letter in legacy_data[points]:
            new_data[letter.lower()] = points

    return new_data