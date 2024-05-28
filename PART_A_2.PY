def rectangle():
   length=int (input("Enter Length: "))
   breadth=int (input("Enter Breath: "))
   area=length*breadth
   print(f"Area of Rectangle is {area} square units")
def square():
   side=int (input("Enter the side: "))
   area=side*side
   print(f"area of square is {area} square units")
def circle():
   radius=int (input("Enter the Radius: "))
   area=3.14*radius*radius
   print(f"area of circle is {area} square unite")
def triangle():
   base=int (input("Enter the Base: "))
   height=int (input("Enter the Height: "))
   area=0.5*height*base
   print(f"area of triangle is {area} square unite")
while True:
   print("Menu/n")
   print("1.rectangle")
   print("2.square")
   print("3.circle")
   print("4.triangle")
   print("5.Exit")
   choice=int(input("Enter your choice: "))
   if choice==1:
       rectangle()
   elif choice==2:
       square()
   elif choice==3:
       circle()
   elif choice==4:
       triangle()
   elif choice==5:
       print("Exited")
       break
   else:
       print("Invalid Choice")
       exit()