def is_tachycardic(arg_string):
    if 'tachycardic' in arg_string.lower():
       return True
    else:
       return False

def code_execute():
    prompt = input('Insert string: ')
    result = is_tachycardic(prompt)
    print(result)


if __name__ == "__name__":
    code_execute()

