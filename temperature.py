class FahrenheitfromCelsius:
    def __init__(self, Celsius):
        self.Celsius = Celsius
       
    def displayFahrenheit(self):
         print(self.Celsius * 9/5 + 32)
           
class CelsiusfromFahrenheit:
    def __init__(self,Fahrenheit):
        self.Fahrenheit= Fahrenheit
    
    def displayCelsius(self):
        print((self.Fahrenheit - 32)*(5/9))