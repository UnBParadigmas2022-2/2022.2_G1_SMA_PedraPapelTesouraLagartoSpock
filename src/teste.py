import pyfiglet

fig = pyfiglet.Figlet()

for font in fig.getFonts():
    print(font + "\n" + pyfiglet.figlet_format("hello", font = font)+ "\n\n")