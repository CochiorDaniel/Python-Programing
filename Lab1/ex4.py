def text_convert(input_string):
    result = []
    word_start = 0

    for i in range(1, len(input_string)):
        if input_string[i].isupper():
            result.append(input_string[word_start:i].lower())
            word_start = i
    result.append(input_string[word_start:].lower())

    return '_'.join(result)


str1 = input("UpperCamelCase: ")

lowercase_text = text_convert(str1)
print("Converted string:", lowercase_text)

