class Human():
    def __init__(self):
        self.name = "Taro"
        self.age = 25
        
    def printinfo(self):
        print(f"名前は{self.name}です")
        print(f"年齢は{self.age}歳です")
        
human = Human()

human.printinfo()