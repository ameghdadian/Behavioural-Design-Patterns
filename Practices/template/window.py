from abc import ABC, abstractmethod

class Window(ABC):
    def close(self):
        self._pre_close()

        print("Removing the window from the screen");

        self._post_close()

    @abstractmethod
    def _pre_close(self):
        pass

    @abstractmethod
    def _post_close(self):
        pass


class GameWindow(Window):
    def _pre_close(self):
        print("Are you sure you want to exit the game?")

    def _post_close(self):
        print("Hope to see you soon!")


class AniVirusWindow(Window):
    def _pre_close(self):
        print("There are some work being done on the background. Are you sure?")

    def _post_close(self):
        print("Anivirus exiting")


def main():
    gwindow = GameWindow()
    gwindow.close()
    
    vwindow = AniVirusWindow()
    vwindow.close()


if __name__ == "__main__":
    main()