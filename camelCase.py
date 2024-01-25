def camelCase(sentence):
    """convert sentence to camelCase for example, Display all books"""

    title_case = sentence.title() # upper case first letter of each work
    upper_camel_cased = title_case.replace('', '') # remove spaces
    #Lowercase first letter, join with rest of string
    #slices don't produce index out of bounds erros
    #so this works on empty strings, strings of length
    return upper_camel_cased[0:1].lower() + upper_camel_cased[1:]

def main():
    sentence = input('Enter your sentence: ')
    output = camelCase(sentence)
    print(output)

if __name__ == '__main__':
    main()