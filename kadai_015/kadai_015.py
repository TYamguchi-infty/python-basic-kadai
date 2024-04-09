class Human():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def printinfo(self):
        print(f"名前は{self.name}です")
        print(f"年齢は{self.age}歳です")

#インスタンス化
name = "Taro"
age = 26
human = Human(name, age)

human.printinfo()