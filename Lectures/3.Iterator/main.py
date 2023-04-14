from iterator import GenericBrowseHistory

def main():
    history = GenericBrowseHistory()
    history.push("a")
    history.push("b")
    history.push("c")
    history.push("d")

    iterator = history.create_iterator()
    for i in iterator:
        print(i)


main()