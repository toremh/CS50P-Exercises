# Call main
# main asks for input, calls convert on input
# convert changes any :) to emoji in text string

def main():
    t = input("Type text. \n")
    print(convert(t))
    return

def convert(text):
    text = text.replace(":)","🙂")
    text = text.replace(":(","🙁")
    return text

main()
