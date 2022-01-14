class Meliora:
    def __init__(self, mode) -> None:
        self.mode = mode
        pass

    def setMode(self, mode):
        pastVal = self.mode
        self.mode = mode
        return pastVal

    def getMode(self) -> int:
        return self.mode
