from Libs.GUI import GUI
from Libs.Verify import Verify

class App:
    def __init__(self):
        try:
            self.Graph= GUI()
            self.Verify= Verify(self.Graph)
        except Exception:
            exit()

X= App()
