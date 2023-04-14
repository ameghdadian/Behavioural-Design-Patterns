from editor import History, Editor

def main():
    editor = Editor()
    history = History()

    editor.content = "a"
    history.push(editor.create_state())

    editor.content = "b"
    history.push(editor.create_state())

    editor.content = "c"

    editor.restore(history.pop())
    editor.restore(history.pop())

    print(editor.content)

main()
