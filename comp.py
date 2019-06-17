tokens = []


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
            if state == 0:
                tok = ""
        elif tok == "\n":
            tok = ""
        elif tok == "PRINT":
            # print('found: PRINT')
            tokens.append("PRINT")
            tok = ""
        elif tok == "\"":
            if state == 0:
                state = 1
            elif state == 1:
                string += '"'
                # print('found: STRING: %s' % string)
                tokens.append("STRING:"+string)
                string = ""
                state = 0
                tok = ""
        elif state == 1:
            string += tok
            tok = ""

    # print(tokens)
    return tokens


def parse(toks):
    i = 0 # +instruction counter

    while i < len(toks):
        if  toks[i] + " " + toks[i+1][0:6] == "PRINT STRING":
            print(toks[i+1][7:])
        i += 2


def run(src):
    data = open_file(src)
    toks = lex(data)
    parse(toks)


if __name__ == '__main__':
    pass

    src = '''
PRINT "Hello world"
PRINT "blabl kjdhsf"
PRINT "blak, 34rf 3rjhfg skjdh"
'''
    run(src)
