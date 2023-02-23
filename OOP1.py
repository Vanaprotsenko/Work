from random import randint
class Book:
    def __init__(self,name,book):
      self.name = name
      self.book= book
    def __str__(self):
        total=f"{self.name} узяв книгу {self.book} "
        return total
    def take_book(self,visitors):
        print(f"{self.user} узяв книгу{self.name} автора{self.author}")
        username=input("Username:")
        book=input("Book:")
        username['key'].append(visitors)
        book ['key'].append(visitors)
        visitors=[
            f"{self.name}:'Jame'",
            f"{self.book}:'The Way to succeed'",
        ]
        print(f"{self.name} взял книгу {self.book}")


take1=Book()
take1.take_book()


