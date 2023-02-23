from random import randint
class Hero :
    def __init__(self,name,weapon,hp,demage,skill=None):
        self.name = name
        self.weapon = weapon
        self.hp = hp
        self.demage= demage
        self.skill = skill
    def __str__(self):
        total=f"Имя: {self.name}\nОружие: {self.weapon}\nЗдоровье: {self.hp}\nУрон: {self.demage}\n"
        return total
    def attack(self, target):
        if self.skill:
            if randint(1,2)==2:
                self.use_skill(target)
            
        print(f"{self.name} атакует {target.name} использует {self.weapon} наносит урон: {self.demage}")
        target.hp-=self.demage
        print(f" У {target.name} осталось здоровья {target.hp}")
    def use_skill(self,target):
        print(f"{self.name} использует навык {self.skill.name} на {target.name} и на носит {self.skill.demage}")
        target.hp-=self.skill.demage
        print(f" У {target.name} осталось здровья {target.hp}")
class Skill:
    def __init__(self,name,demage):
        self.name=name
        self.demage=demage
skill1=Skill("super kick ",50)
skill2=Skill("огненый шар",75)
hero1=Hero("Ronald","AK-47",100,15,skill1)
print(hero1)
hero2=Hero("Goblin","Лук",125,20)
print(hero2)
hero1.attack(hero2)
hero2.attack(hero1)
hero1.attack(hero2)
hero3=Hero("маг","посах",150,25,skill2)
hero3.attack(hero2)


     

