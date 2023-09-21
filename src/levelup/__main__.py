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
    #mapObject = map
    #mapObject.generateMap(mapObject,0,0)
    #mapObject.printMap(mapObject)
    main()
