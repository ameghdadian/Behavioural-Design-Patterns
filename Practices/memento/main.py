from document import (
    Document,
    History
)

def main():
    doc = Document()
    history = History()

    doc.content = "Haha"
    history.push(doc.create_state())

    doc.font_name = "Arial"
    history.push(doc.create_state())

    doc.font_size = 16
    history.push(doc.create_state())

    doc.font_size = 19
    history.push(doc.create_state())

    doc.content = "Blank emptiness"
    history.push(doc.create_state())

    print(doc)

    doc.restore(history.pop())
    doc.restore(history.pop())
    print(doc)
    doc.restore(history.pop())
    print(doc)

main()