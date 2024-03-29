from sys import argv
from os.path import exists

script, from_file, to_file = argv
print(f"Copying from {from_file} to {to_file}")
with open(from_file) as in_file:
    indata = in_file.read()
    print(f"The input file is {len(indata)} bytes long")
    print(f"Does the output file exist? {exists(to_file)}")
    print("Ready, hit RETURN to continue, CTRL-C to abort.")
    input()
    with open(to_file, "w") as out_file:
        out_file.write(indata)
        print("Alright, all done.")
