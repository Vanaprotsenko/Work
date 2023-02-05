class Player:
    def __init__(self,name,position):
        self.name = name
        self.position = position
    def show(self):
        print(f" {self.name} - {self.position}")
    def __str__(self):
        all=f"Имя {self.name} - {self.position}"
        return all
class football_team(Player):
    def __str__(self):
        all=f"Имя {self.name} - {self.position}"
        return all

forward=Player("Ronaldo","forward")
midfield=Player("Modric","midfield")
defence=Player("Ramos","defence")
goalkeeper=Player("Leno","goalkeeper")
forward.show()
midfield.show()
defence.show()
goalkeeper.show()
