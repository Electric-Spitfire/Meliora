from printColor import *

if __name__ == '__main__':
    voice_mode = getInput("Would you like to run the program in voice mode? (y/n)",yellow).upper()
    
    if voice_mode == "Y":
        red("Running in voice mode")
        # red("Starting voice mode...")
        #do something
        pass
    else:
        red("Starting text mode...")
        #do something else
        pass

