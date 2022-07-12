import sys
import os

if __name__ == "__main__":
    langs = sys.argv[1] #.split(',')
    #langs = 'python,golang,java'.split(',')
    for lang in langs:
        if lang.casefold() == 'python':
            Out = os.popen('pip list').read()
            print(Out)
        elif lang.casefold() == 'java':
            os.popen('gradle init')
            Out = os.popen('gradle dependencies').read()
            print(Out)
        elif lang.casefold() == 'nodejs' or lang.casefold() == 'javascript':
            Out = os.popen('npm list').read()
            print(Out)
        elif lang.casefold() == 'go':
            Out = os.popen("go list -f '{{ join .Deps \"\n\" }}'")
            print(Out)
        else:
            print('Unknown lang')
