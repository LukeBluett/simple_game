import subprocess

R = "python3 " # Program to run file
F = "source/main.py " # main file location
D = "rm " # Delete files
XF = "builder.py~"
XD = " -r source/__pycache__" # unnecessary directory

def process(command):
    return subprocess.Popen(command.split(), stdout=subprocess.PIPE)

output, error = process(R + F).communicate()

output, error = process(D + XF).communicate()
output, error = process(D + XD).communicate()
