# code to show how to use nested boxlayouts. 
  
# import kivy module  
import kivy  
    
# this restricts the kivy version i.e  
# below this kivy version you cannot  
# use the app or software  
kivy.require("1.9.1")  
    
# base Class of your App inherits from the App class.  
# app:always refers to the instance of your application  
from kivy.app import App    
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label 
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle

from geopy.geocoders import Nominatim

# class in which we are creating the button by using boxlayout
# defining the App class 
class BoxLayoutApp(App):

##    class MyLabel(Label):
##    def on_size(self, *args):
##        self.canvas.before.clear()
##        with self.canvas.before:
##            Color(0, 1, 0, 0.25)
##            Rectangle(pos=self.pos, size=self.size)
        
    def build(self): 
  
        # The app layout will be contained in a box 'MainBox' 
        MainBox = BoxLayout(orientation ='vertical', spacing = 1)
        
        #Create a horizontal layout box to store the latitude user input
        latbox = BoxLayout(orientation ='horizontal', spacing = 2, size_hint = (1, 0.2))
        #Create a horizontal layout box to store the longitude user input
        lonbox = BoxLayout(orientation ='horizontal', spacing = 2, size_hint = (1, 0.2)) 

        #Create the label for latitude
        latlabel = Label(text = "Latitude", font_size = '40sp')
        #Create the user text box for latitude
        latentry = TextInput(text ="-31")
        #Add both to the latitude user input box
        latbox.add_widget(latlabel)
        latbox.add_widget(latentry)
        #Create the label for longitude
        lonlabel = Label(text = "Longitude", font_size = '40sp')
        #Create the user text box for longitude
        lonentry = TextInput(text ="116")
        #Add both to the longitude user input box
        lonbox.add_widget(lonlabel)
        lonbox.add_widget(lonentry) 
  
        #Add the latitude and longitude input boxes to the main box to display all components
        MainBox.add_widget(latbox) 
        MainBox.add_widget(lonbox)

        #Create a button to get the location result from the latitude and longitude and bind it to the function
        getresult = Button(text="Where are you?", font_size = '40sp', size_hint = (1, 0.1))
        getresult.bind(on_press=lambda a:self.getresult(latentry, lonentry, coordinates, address))

        #Create lables that display the user entered coordinates and the geocoded address
        coordinates = Label(text = "Coordinates", size_hint = (1, 0.1))
        address = Label(text = "Address", size_hint = (1, 0.4))

        #Add the button and result labels to the main layout
        MainBox.add_widget(getresult) 
        MainBox.add_widget(coordinates) 
        MainBox.add_widget(address) 
  
        return MainBox

        

    def getresult(self, latentry, lonentry, coordinates, address):

        #Declare variable that checks if the latitude and longitude values are numeric, set to True as default.
        values_are_all_numeric = True
        #Get the user inputs for latitude and longitude from the respective widgets and convert to floating point numbers.
        #If there is an error in converting any input to float then set the value to check if it is numeric to false.
        try:
             latitude = float(latentry.text)
        except ValueError:
             values_are_all_numeric = False

        try:
             longitude = float(lonentry.text)
        except ValueError:
             values_are_all_numeric = False

        #If values are numeric, continue to process of geocoding, otherwise indicate to user that the coordinates are not numeric and the address can't be found.
        if values_are_all_numeric == False:
             coordinates.text = "Latitude and/or longitude value not numeric!"
             address.text = "Can't get location due to user input error!"
        else:
             #Initialize the Nominatim API
             geolocator = Nominatim(user_agent="geoapiExercises")
             #Assign Latitude & Longitude values
             Latitude = str(latitude)
             Longitude = str(longitude)
             #Display the Latitude and Longitude as a cordinate pair in the coordinates label
             coordinates.text = "Location: " + str(Latitude) + ", " + str(Longitude)
             #Get location with geocode
             location = geolocator.geocode(Latitude+","+Longitude)
             result = str(location)
             r = result.split(',')
             mylocation = ''
             for i in r:
                 mylocation += i
                 mylocation += '\n'
             address.text = mylocation
       
    
        

  
# creating the object root for BoxLayoutApp() class   
root = BoxLayoutApp()  
    
# run function runs the whole program  
# i.e run() method which calls the  
# target function passed to the constructor.  
root.run() 
