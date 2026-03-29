class parent:
    def __init__(self):
        print("Parent constructor")
class child(parent):
    def __init__(self):
        super().__init__()
        print("Child constructor")
c=child()