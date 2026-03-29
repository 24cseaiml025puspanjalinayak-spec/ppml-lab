class parent:
    def display(self):
        print("This is a method from the parent class")
class child(parent):
    def show(self):
        print("This is a method from the child class")
obj = child()
obj.display()