class Book:
    def __init__(self,name,book):
      self.name = name
      self.book= book
    def __str__(self):
        total=f"{self.name} узяв книгу {self.book} "
        return total

book1=Book('Гарі поттер 1','Джоан Роулінг')
book2=Book('Гарі поттер 2','Джоан Роулінг')
visitors=[
    {'name':'Alex Ronald',
    'books':[book1,book2]},
    {
        'name':'Alfred',
        'books':[book1],
    }
]



