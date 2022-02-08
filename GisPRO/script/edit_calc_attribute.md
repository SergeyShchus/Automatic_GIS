-- Введіть перший символ рядка з великої літери в полі CITY_NAME .

   !CITY_NAME!.capitalize()

-- Видаліть будь-які пробіли з кінця рядка в полі CITY_NAME .

   !CITY_NAME!.rstrip()

-- Замініть будь-які випадки "california" на "california", знайдені в полі STATE_NAME .

   !STATE_NAME!.replace("california", "California")

-- Об’єднайте поля A і B, розділені двокрапкою.

   "{}:{}".format(!FieldA!, !FieldB!)

-- Округліть значення поля до двох знаків після коми.

   Expression:
   round(!area!, 2)
   
   Parser:
   Python


-- Використовуйте математичний модуль, щоб допомогти перетворити метри у фути. Перетворення зводиться до степеня 2 і множиться на площу.

   Parser:
   Python

   Expression:
   MetersToFeet((float(!shape.area!)))
   
   Code Block:
   def MetersToFeet(area):
       return math.pow(3.2808, 2) * area
	
	
-- Округліть значення поля до двох знаків після коми.

   Expression:
   round(!area!, 2)
   
   Parser:
   Python
   
-- Розранук площі з округленням

   round(AreaGeodetic($feature, 'hectares'), 2)

-- перетворити метри у фути. Перетворення зводиться до степеня 2 і множиться на площу.

   Parser:
   Python
   
   Expression:
   MetersToFeet((float(!shape.area!)))
   
   Code Block:
  def MetersToFeet(area):
      return math.pow(3.2808, 2) * area
	
	
-- Класифікуйте на основі значень полів.

   Parser:
   Python
   
   Expression:
   Reclass(!WELL_YIELD!)
   
   Code Block:
   def Reclass(WellYield):
       if (WellYield >= 0 and WellYield <= 10):
           return 1
       elif (WellYield > 10 and WellYield <= 20):
           return 2
       elif (WellYield > 20 and WellYield <= 30):
           return 3
       elif (WellYield > 30):
           return 4	

-- Класифікація по значенню площі поля:

   Expression:
   Reclass(!Area_fact!)
   
   Code Block:
   def Reclass(Area_fact):
       if (Area_fact >= 0 and Area_fact <= 10):
           return 1
       elif (Area_fact > 10 and Area_fact <= 20):
           return 2
       elif (Area_fact > 20 and Area_fact <= 30):
           return 3
       elif (Area_fact > 30):
           return 4


-- Умовно виконує групу операторів залежно від значення виразу.

   Parser:
   VB Script
   
   Expression:
   density
   
   Code Block:
   Dim density
   If [POP90_SQMI] < 100 Then
   density = "low"
   
   elseif [POP90_SQMI] < 300 Then
   density = "medium"
   
   else
   density = "high"
   end if
   
-- Обчисліть площу об’єкта.

Parser:
Python

Expression:
!shape.area!

-- Обчисліть максимальну х-координату об’єкта.

Parser:
Python

Expression:
!shape.extent.XMax!

-- Обчисліть кількість вершин об’єкта.

Parser:
Python

Expression:
MySub(!shape!)

Code Block:
def MySub(feat):    
    partnum = 0

    # Count the number of points in the current multipart feature
    partcount = feat.partCount
    pntcount = 0

    # Enter while loop for each part in the feature (if a singlepart 
    # feature this will occur only once)
    #
    while partnum < partcount:
        part = feat.getPart(partnum)
        pnt = part.next()

        # Enter while loop for each vertex
        #
        while pnt:
            pntcount += 1   
            pnt = part.next()
   
            # If pnt is null, either the part is finished or there 
            # is an interior ring
            #
            if not pnt: 
                pnt = part.next()
        partnum += 1
    return pntcount
	
	
Area and length properties of the geometry field can be modified with unit types expressed with an @ sign.

Areal unit of measure keywords:
ACRES | ARES | HECTARES | SQUARECENTIMETERS | SQUAREDECIMETERS | SQUAREINCHES | SQUAREFEET | SQUAREKILOMETERS | SQUAREMETERS | SQUAREMILES | SQUAREMILLIMETERS | SQUAREYARDS | SQUAREMAPUNITS | UNKNOWN
Linear unit of measure keywords:
CENTIMETERS | DECIMALDEGREES | DECIMETERS | FEET | INCHES | KILOMETERS | METERS | MILES | MILLIMETERS | NAUTICALMILES | POINTS | UNKNOWN | YARDS

-- Обчисліть довжину об’єкта в ярдах.

Parser:
Python

Expression:
!shape.length@yards!

-- Обчисліть геодезичну довжину об’єкта в ярдах.

Parser:
Python

Expression:
!shape.geodesicLength@yards!

-- Обчисліть поточну дату.

Parser:
Python

Expression:
time.strftime("%d/%m/%Y")

-- Обчисліть поточну дату та час.

Parser:
Python

Expression:
datetime.datetime.now()

-- Обчисліть дату 31 грудня 2000 року.

Parser:
Python

Expression:
datetime.datetime(2000, 12, 31)

-- Обчисліть кількість днів між поточною датою та значенням у полі.

Parser:
Python

Expression:
(datetime.datetime.now() - arcpy.time.ParseDateTimeString(!field1!)).days

-- Обчисліть дату, додавши 100 днів до значення дати в полі.

Parser:
Python

Expression:
arcpy.time.ParseDateTimeString(!field1!) + datetime.timedelta(days=100)

-- Обчисліть день тижня (наприклад, неділю) для значення дати в полі.

Parser:
Python

Expression:
arcpy.time.ParseDateTimeString(!field1!).strftime('%A')

-- Зразки коду — рядки
Поверніть три крайніх правих символи.

Parser:
Python

Expression:
!SUB_REGION![-3:]
Замініть будь-які регістри великої P на нижню p.

Parser:
Python

Expression:
!STATE_NAME!.replace("P","p")
Об’єднайте два поля за допомогою роздільника пробілів.

Parser:
Python

Expression:
!SUB_REGION! + " " + !STATE_ABBR!
Перетворити на правильний регістр
Наведені нижче приклади показують різні способи перетворення слів так, щоб кожне слово включало перший символ з великої, а решту літер — у нижньому регістрі.

Parser:
Python

Expression:
' '.join([i.capitalize() for i in !STATE_NAME!.split(' ')])
Parser:
Python

Expression:
!STATE_NAME!.title()
Регулярні вирази
Модуль re Python забезпечує операції зіставлення регулярних виразів, які можна використовувати для виконання складних правил зіставлення шаблонів і заміни рядків.

Замініть St або St, що починаються нові слова в кінці рядка на слово Street.

Parser:
Python

Expression:
update_street(!ADDRESS!)

Code Block:
import re
def update_street(street_name):
    return re.sub(r"""\b(St|St.)\Z""",  
                  'Street',
                  street_name)
Накопичувальні та послідовні розрахунки
Обчисліть послідовний ідентифікатор або номер на основі інтервалу.

Parser:
Python

Expression:
autoIncrement()

Code Block:
rec=0
def autoIncrement():
    global rec
    pStart = 1 #adjust start value, if req'd 
    pInterval = 1 #adjust interval value, if req'd
    if (rec == 0): 
        rec = pStart 
    else: 
        rec = rec + pInterval 
    return rec
Обчисліть сукупне значення числового поля.

Parser:
Python

Expression:
accumulate(!FieldA!)

Code Block:
total = 0
def accumulate(increment):
    global total
    if total:
        total += increment
    else:
        total = increment
    return total
Обчисліть відсоткове збільшення числового поля.

Parser:
Python

Expression:
percentIncrease(float(!FieldA!))

Code Block:
lastValue = 0
def percentIncrease(newValue):
    global lastValue
    if lastValue:
        percentage = ((newValue - lastValue) / lastValue)  * 100
    else: 
        percentage = 0
    lastValue = newValue
    return percentage
Випадкові значення
Використовуйте пакет сайту numpy для обчислення випадкових значень float від 0,0 до 1,0.

Parser:
Python

Expression:
getRandomValue()

Code Block:
import numpy

def getRandomValue():
    return numpy.random.random()
Обчислення нульових значень
Використовуючи вираз Python, нульові значення можна обчислити за допомогою Python None .

Примітка:
Наведене нижче обчислення буде працювати, лише якщо поле має значення NULL.

Використовуйте Python None для обчислення нульових значень.

Parser:
Python

Expression:
None
