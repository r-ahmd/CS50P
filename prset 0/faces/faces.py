def convert(a):
    if a == ":)":
        return "🙂"
    else:
        return "🙁"


def main():
    print("Enter text: ", end="")
    a = input().split()
    for word in a:
        if word == ":)" or word == ":(":
            ind = a.index(word)
            a[ind] = convert(word)
    print ("Converted: ", end="")
    for word in a:
        print(word, end=" ")
    print("")




if __name__ == "__main__":
    main()
