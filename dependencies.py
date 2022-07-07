import sys
import os

if __name__ == "__main__":
    langs = sys.argv[1].split(',')
    #langs = 'python,golang,java'.split(',')
    for lang in langs:
        if lang == 'python':
            Out = os.popen('pip list').read()
            print(Out)
        elif lang == 'java':
            pass
        elif lang == 'nodejs' or lang == 'javascript':
            Out = os.popen('npm list').read()
            print(Out)
        elif lang == 'go':
            Out = os.popen("go list -f '{{ join .Deps \"\n\" }}'")
            print(Out)
        else:
            print('Unknown lang')
