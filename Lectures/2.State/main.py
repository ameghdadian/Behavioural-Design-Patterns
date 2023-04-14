from state import Canvas, SelectionTool, BrushTool


def main():
    canvas = Canvas()
    canvas.current_tool = BrushTool()
    canvas.mouse_down()
    canvas.mouse_up()

main()