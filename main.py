from printColor import *
import run_meliora
from Meliora import Meliora

# mode flag if 0 then text mode, if 1 then voice mode
mode = -1





def main():
    voice_mode = getInput(
        "Would you like to run in voice mode? (y/n)", yellow).upper()

    if voice_mode == "Y":
        red("Running in voice mode")
        mode = 1
        pass
    else:
        red("Starting text mode...")
        mode = 0
        pass
    MEL = Meliora(mode)
    run_meliora.setup(MEL)
    run_meliora.main()


if __name__ == '__main__':
    main()
