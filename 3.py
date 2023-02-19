class Market:
  def __init__(self, name):
    self.name = name
  def func1(self,name):
     print(f"Магазин {self.name} Предоставляє будь які можливості для пошиву тканів")

class Sport():
  def func2(self, name):
   print(f"Магазин {self.name} може надати послуги протестувати спортовар ")

class Supermarket():
  def func3(self,name):
    print(f"Магазин {self.name} тут ви можете купляти товари 24/7")

class Pharmacy(Market,Sport,Supermarket):
  def func4(self, name):
    print(f"У аптеці під назвою {self.name} ви можете купляти ліки набагато дешевше ")  



c=Pharmacy("Аптека")
c.func1("Ательє")
c.func2("SportLife")
c.func3("ATB")
c.func4("Аптека")

