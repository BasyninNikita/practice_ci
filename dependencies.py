import sys
import os

if __name__ == "__main__":
    langs = sys.argv[1].split(',')
    #langs = 'python,go,java'.split(',')
    for lang in langs:
        if lang == 'python':
            Out = os.popen('pip list').read()
            print(Out)
        else:
            print('Unknown lang')
    print(langs)
