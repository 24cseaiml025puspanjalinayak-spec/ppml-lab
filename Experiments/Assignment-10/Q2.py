class GrandParent:
    def property(self):
        print("Grand parents have agriculture and property.")
class Parent(GrandParent):
    def business(self):
        print("Parents runs a family business.")
class Child(Parent):
    def education(self):
        print("Child is pursuing higher education.")
obj = Child()
obj.property()
obj.business()
obj.education()