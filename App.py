from Libs.GUI import GUI
from Libs.Verify import Verify

class App:
    def __init__(self):
        self.Graph= GUI()
        self.Verify= Verify(self.Graph)

X= App()
