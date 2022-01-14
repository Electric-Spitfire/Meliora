from xmlrpc.client import Boolean
from printColor import *
import run_meliora
from Meliora import Meliora
import json

# mode flag if 0 then text mode, if 1 then voice mode
mode = -1





def main():
    voice_mode = getInput(
        "Would you like to run the program in voice mode? (y/n)", yellow).upper()

    if voice_mode == "Y":
        red("Running in voice mode")
        mode = 1
        # red("Starting voice mode...")
        # do something
        pass
    else:
        red("Starting text mode...")
        mode = 0
        # do something else
        pass
    MEL = Meliora(mode)
    run_meliora.setup(MEL)
    run_meliora.main()


if __name__ == '__main__':
    main()
