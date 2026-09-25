#Multi level inheritance
class Father:
    def __init__(self,father):
        self.father = father
    def father_name(self):
        print('Father name:',self.father)

class Mother:
     def __init__(self,mother):
            self.mother= mother
     def mother_name(self):
            print('Mother name:',self.mother)

class Child(Father,Mother):
      def __init__(self,father,mother,child):
            Father.__init__(self,father)
            Mother.__init__(self,mother)
            self.child =child
      def child_name(self):
             print('Child name:',self.child)

c1 = Child('SATYANARAYANA','ANITHA','NIKKY')
c1.father_name()
c1.mother_name()
c1.child_name()

#HERIACH