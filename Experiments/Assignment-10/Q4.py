class parent:
    def method1(self):
        print("This is parent method1")
    def method2(self):
        print("This is parent method2")
class child(parent):
    def method1(self):
        print("This is child method1")
    def method2(self):
        print("This is child method2")
obj=child()
obj.method1()
obj.method2()