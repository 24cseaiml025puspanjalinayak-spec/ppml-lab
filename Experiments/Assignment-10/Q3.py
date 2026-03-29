class Father:
    def skill1(self):
        print("Fther's skill: Advocate")
class Mother:
    def skill2(self):
        print("Mother's skill: cooking")
class Child(Father, Mother):
    def own_skill(self):
        print("Child's skill: coding")
obj = Child()
obj.skill1()
obj.skill2()
obj.own_skill()