"""Program to sort dictionary elements"""

def sortFunction(e):
    return e['year']

cars={'A':{'car':'Ford' , 'year':2019},
      'B':{'car':'Toyota' , 'year':2018},
      'C':{'car':'BMW' , 'year':2010},
      'D':{'car':'Jeep' , 'year':2020},
      'E':{'car':'Audi' , 'year':2025}}

car1={'Ford': 'Freestyle', 'Year':2019, 'Color':'White' }
car2={'BMW': '320 D', 'Year':2025, 'Color':'White' }
car3={'Toyota': 'Fortuner', 'Year':2030, 'Color':'White' }
mycar={'First car':car1, 'Second car':car2, 'Third car':car3}
for x in mycar:
    print(x)
    for y in mycar[x]:
        print(y,':',mycar[x][y])
#cars.sort(reverse=True, key=sortFunction)