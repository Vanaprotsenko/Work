class Book:
   def __init__(self,name,author):
      self.name = name
      self.author = author
   def spisok(self):
      visitors=[
         {
            f"{self.author}:'Jame Jr'",
            f"{self.name}:'The way to successfully'"
         }
      ]
      return visitors
book1=Book('The way to successfully','Jame Jr')
book1.spisok()
print(book1)


