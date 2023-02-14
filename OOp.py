
class Phone:
    def __init__(self,name,owner):
        self.name = name
        self.owner = owner

    def __str__(self):
        total=f"User {self.owner} calling to {self.name} to {self.owner} on {self.name} "
        return total 
    def call(self,whom):
        print(f"{self.owner} calling with {self.name} to {self.owner} on {self.name}")
user1=Phone("Iphone 7","Kane")
user2=Phone("Iphone 11","Jack")
user1.call(user2)
user2.call(user1)        
