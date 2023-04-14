from typing import List

from command import Command


class ResizeCommand(Command):
    def execute(self):
        print('Resize')


class BlackAndWhiteCommand(Command):
    def execute(self):
        print("Black and white")


# Here is the Composite command
# It is a command composed of other commands
class CompositeCommand(Command):
    def __init__(self):
        self.commands:List[Command] = []

    def add(self, command: Command):
        self.commands.append(command)

    def execute(self):
        for command in self.commands:
            command.execute()
            

def main():
    composite = CompositeCommand()
    composite.add(ResizeCommand())
    composite.add(BlackAndWhiteCommand())
    composite.execute()


if __name__ == '__main__':
    main()

