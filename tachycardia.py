def is_tachycardic(arg_string):
    if 'tachycardic' in arg_string.lower():
        return True
    elif 'tchycardic' or 'tahycardic' or 'tacycardic' or 'tachyardic' or 'tachycrdic' or 'tachycadic' or 'tachycard1c' or 'tachycardc' in arg_string.lower():
        return True # yeahhh this is not how it should be done but i think you would need import an external library to spell check
    else:
        return False


def code_execute():
    prompt = input('Insert string: ')
    result = is_tachycardic(prompt)
    print(result)


if __name__ == "__name__":
    code_execute()
