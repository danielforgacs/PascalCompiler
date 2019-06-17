def open_file(src):
    return src

def lex(filecontents):
    filecontents = list(filecontents)
    tok = ""
    string = ""
    state = 0
    for char in filecontents:
        tok += char
        if tok == " ":
            tok = ""
        elif tok == "PRINT":
            print('found: PRINT')
            tok = ""
        elif tok == "\"":
            if state == 0:
                state = 1
            elif state == 1:
                print('found: STRING: %s' % string)
                string = ""
                state = 0
        elif state == 1:
            string += char
            tok = ""

def run(src):
    data = open_file(src)
    lex(data)


if __name__ == '__main__':
    pass

    src = '''PRINT "Hello world"'''
    run(src)
