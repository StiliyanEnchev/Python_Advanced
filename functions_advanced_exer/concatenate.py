def concatenate(*strings, **grade_data):
    text = ''.join(strings)

    for key, value in grade_data.items():
        text = text.replace(key, value)

    return text