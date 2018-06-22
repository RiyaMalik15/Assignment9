print("Question1")
class Circle:
    
     def __init__(self,r):
         self.radius=r
     def getArea(self):
         self.area=3.14*self.radius*self.radius
         print("area of the circle is",self.area)
     def getCircumference(self):
         self.circumference=2*3.14*self.radius
         print("circumference of the circle is",self.circumference)
radius=float(input("Enter the radius of the circle"))
obj = Circle(radius)
obj.getArea()
obj.getCircumference()
print('*'*10)
print('\n')

print("Question2")
class Student:
  def __init__(self,name,roll):
   self.naam=name
   self.roll_no=roll
  def display(self):
      print("The name of the student is:",self.naam)
      print("The roll no of the student is:",self.roll_no)
naam=input("Enter the name of the student")
roll_no=int(input("Enter the roll number the student"))
obj=Student(naam,roll_no)
obj.display()
print('*'*10)
print('\n')

print("Question3")
class Temperature:
    def __init__(self,temp):
     self.c=temp
    def convertFahernheit(self):
     far=(self.c * 9/5) + 32
     print("The given temperature in fahernheit is:",far)
    def convertCelcius(self):
     cel=(self.c - 32) * 5/9
     print("The given temperature in celcius is:",cel)
c=int(input("input the temperature to convert"))
      
obj=Temperature(c)
obj.convertFahernheit()
obj.convertCelcius()
print('*'*10)
print('\n')

print("Question4")
class MovieDetails:
  def __init__(self,movie_name,movie_release,movie_ratings,movie_artist):
        self.name=movie_name
        self.year=movie_release
        self.rate=movie_ratings
        self.art=movie_artist
  def display(self):
        print("The name of the movie is:",self.name)
        print("The releasing year of the movie is:",self.year)
        print("The ratings of the movie is:",self.rate)
        print("The artist of the movie is:",self.art)
  def update(self,m,y,r,a):
       self.name+=m
       self.year+=y
       self.rate+=r
       self.art+=a
        
name=input("Enter the name of the movie")
year=int(input("Enter the releasing year of the movie"))
rate=int(input("Enter the rating of the movie"))
art=input("Enter the artist of the movie")

obj=MovieDetails(name,year,rate,art)
obj.display()
  
name=input("Enter the name of the movie")
year=int(input("Enter the releasing year of the movie"))
rate=float(input("Enter the rating of the movie"))
art=input("Enter the artist of the movie")
  
obj.update(name,year,rate,art)
obj.display()
print('*'*10)
print('\n')
print("Question5")
class Expenditure:
    def __init__(self,expenditure,saving):
     self.exp=expenditure
     self.sav=saving
    def expend(self):
        print("The expenditure of the month is:",self.exp)
        print("The savings of the month is:",self.sav)
    def salary(self):
        sal=exp+sav
        print("The salary of the month is:",sal)
exp=int(input("input the expenditure of the month"))
sav=int(input("input the savings of the month"))
    
obj=Expenditure(exp,sav)
obj.expend()
obj.salary()
