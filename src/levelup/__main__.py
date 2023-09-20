import sys
from levelup.ui import GameApp
from levelup.map import map

def main() -> None:
    app = GameApp()
    try:
        app.start()
    except KeyboardInterrupt:
        app.quit()
        sys.exit()


if __name__ == "__main__":
    map.printMap()
    main()
