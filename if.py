print("Ви можете вибрати функцію 1 щоб записати загадку або функцію 2 щоб відгати загадку або функцію 0 щоб закінчити")
zagadka="В Полотняной стране По реке Простыне Плывет пароход То назад, то вперед,А за ним такая гладь — Ни морщинки не видать."
answer=" Утюг"
date=int(input("Введіть номер функціЇ"))
if date==1:
    new_zagadka=input("Введіть загадку ")
    new_answer=input("Введіть відповідь до неї")
elif date==2:
    print(zagadka)
    z=input("Введіть відповідь")
    while True:
     if z==answer:
        print("Вітаємо ви відгадали загадку")
     if date==0:
        break 
else:
 print("Відповідь не правильна ")
    
