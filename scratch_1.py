# printfile.py
#     Prints a file to the screen.


from tkinter.filedialog import  askopenfilename

from tkinter.filedialog import asksaveasfilename
def main():


    infilename = askopenfilename()

    a = open(infilename,"r")

    print(a.readlines())

print()

main()
