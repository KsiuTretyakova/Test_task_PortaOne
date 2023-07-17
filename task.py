# You can try it on repl.it
# https://replit.com/@OksanaGritsienk/TesttaskPortaOne

def word_processing():

    print("Enter text for analysis:")

    while True:
        text = "\n".join(iter(input, ""))
        if any(symbol.isalpha() for symbol in text) and len(text) > 0:
            break
        else:
            print("The text must contain letters and not be empty. Try again")

    text = text.split()

    list_letter = []
    for word in text:
        for letter in word:
            if word.count(letter) == 1 and letter.isalpha():
                list_letter.append(letter)
            break

    for elem in list_letter:
        if list_letter.count(elem) == 1:
            print(elem)
            break


if __name__ == "__main__":
    word_processing()
