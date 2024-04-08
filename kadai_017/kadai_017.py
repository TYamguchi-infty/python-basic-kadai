class Human():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def check_adalt(self):
        if self.age >= 20:
            print(f"{self.name}さんは大人です")
        else:
            print(f"{self.name}さんは大人ではありません")

names = ["Taro", "Jiro", "Hanako"]
ages = [26, 15, 30]

for i in range(len(names)):
    human = Human(names[i], ages[i])
    human.check_adalt()