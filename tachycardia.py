def is_tachycardic(arg_string):
    if 'tachycardic' in arg_string.lower():
        return True
    elif 'tchycardic' in arg_string.lower() or 'tahycardic' in arg_string.lower()\
            or 'tacycardic' in arg_string.lower()\
            or 'tachyardic' in arg_string.lower() \
            or 'tachycrdic' in arg_string.lower() \
            or 'tachycadic' in arg_string.lower() \
            or 'tachycard1c' in arg_string.lower() \
            or 'tachycardc' in arg_string.lower():
        return True  
    else:
        return False


def code_execute():
    prompt = input('Insert string: ')
    result = is_tachycardic(prompt)
    print(result)


if __name__ == "__main__":
    code_execute()
