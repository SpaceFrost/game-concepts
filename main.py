from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.checkbox import CheckBox
from kivy.uix.button import Button
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView  

class Quiz(App):
    
    def build (self):
    
        self.layout = BoxLayout(orientation = "vertical", padding = 20, spacing = 30)

        firstQ = Label(text = "How old is the earth?")
        firstAnsLay = BoxLayout( orientation = "horizontal")
        firstAnsA =  Label(text = "A. 100 Years Old")
        firstAnsACheck = CheckBox(active = False)
        firstAnsB =  Label(text = "B. 5 Trillion Years Old")
        firstAnsBCheck = CheckBox(active = False)
        firstAnsC =  Label(text = "C. 8 Billion Years Old")
        firstAnsCCheck = CheckBox(active = False)
        firstAnsD =  Label(text = "D. 100 Years Old")
        firstAnsDCheck = CheckBox(active = False)
        
        secondQ = Label(text = "What's the largest mountain in the world?")
        secondAnsLay = BoxLayout( orientation = "horizontal")
        secondAnsA =  Label(text = "A. Mt. Kilamanjaro")
        secondAnsACheck = CheckBox(active = False)
        secondAnsB =  Label(text = "B. Mt. Everest")
        secondAnsBCheck = CheckBox(active = False)
        secondAnsC =  Label(text = "C. Mt. Fuji")
        secondAnsCCheck = CheckBox(active = False)
        secondAnsD =  Label(text = "D. Mt. Kangchenjunga")
        secondAnsDCheck = CheckBox(active = False)
        
        thirdQ = Label(text = "What's the largest living animal in the world?")
        thirdAnsLay = BoxLayout( orientation = "horizontal")
        thirdAnsA =  Label(text = "A. Blue Whale")
        thirdAnsACheck = CheckBox(active = False)
        thirdAnsB =  Label(text = "B. Great White Shark")
        thirdAnsBCheck = CheckBox(active = False)
        thirdAnsC =  Label(text = "C. Elephant")
        thirdAnsCCheck = CheckBox(active = False)
        thirdAnsD =  Label(text = "D. Bald Eagle")
        thirdAnsDCheck = CheckBox(active = False)
        
        fourthQ = Label(text = "Who is the biggest singer in the world as of September 2025?")
        fourthAnsLay = BoxLayout( orientation = "horizontal")
        fourthAnsA =  Label(text = "A. Britney Spears")
        fourthAnsACheck = CheckBox(active = False)
        fourthAnsB =  Label(text = "B. Taylor Swift")
        fourthAnsBCheck = CheckBox(active = False)
        fourthAnsC =  Label(text = "C. The Weeknd")
        fourthAnsCCheck = CheckBox(active = False)
        fourthAnsD =  Label(text = "D. Billie Eillish")
        fourthAnsDCheck = CheckBox(active = False)
        
        fifthQ = Label(text = "What is the largest star in the universe?")
        fifthAnsLay = BoxLayout( orientation = "horizontal")
        fifthAnsA =  Label(text = "A. DO 26226")
        fifthAnsACheck = CheckBox(active = False)
        fifthAnsB =  Label(text = "B. V582 Cassiopeiae")
        fifthAnsBCheck = CheckBox(active = False)
        fifthAnsC =  Label(text = "C. VV Cephei")
        fifthAnsCCheck = CheckBox(active = False)
        fifthAnsD =  Label(text = "D. Stephenson 2-18")
        fifthAnsDCheck = CheckBox(active = False)
        
        sixthQ = Label(text = "What basketball team won March Madness 2018")
        sixthAnsLay = BoxLayout( orientation = "horizontal")
        sixthAnsA =  Label(text = "A. Florida Gators")
        sixthAnsACheck = CheckBox(active = False)
        sixthAnsB =  Label(text = "B. Villanova Wildcats")
        sixthAnsBCheck = CheckBox(active = False)
        sixthAnsC =  Label(text = "C. Kansas Jayhawks")
        sixthAnsCCheck = CheckBox(active = False)
        sixthAnsD =  Label(text = "D. Loyola Ramblers")
        sixthAnsDCheck = CheckBox(active = False)
        
        sixthQ = Label(text = "Who is the scientist that discovered the theory of relativity?")
        sixthAnsLay = BoxLayout( orientation = "horizontal")
        sixthAnsA =  Label(text = "A. Neil Degrasse Tyson")
        sixthAnsACheck = CheckBox(active = False)
        sixthAnsB =  Label(text = "B. Stephen Hawking")
        sixthAnsBCheck = CheckBox(active = False)
        sixthAnsC =  Label(text = "C. Charles Darwin")
        sixthAnsCCheck = CheckBox(active = False)
        sixthAnsD =  Label(text = "D. Albert Einstein")
        sixthAnsDCheck = CheckBox(active = False)
        
        self.layout.add_widget(firstQ)
        self.layout.add_widget(firstAnsLay)
        self.layout.add_widget(firstAnsA)
        self.layout.add_widget(firstAnsACheck)
        self.layout.add_widget(firstAnsB)
        self.layout.add_widget(firstAnsBCheck)
        self.layout.add_widget(firstAnsC)
        self.layout.add_widget(firstAnsCCheck)
        self.layout.add_widget(firstAnsD)
        self.layout.add_widget(firstAnsDCheck)
        
        self.layout.add_widget(secondQ)
        self.layout.add_widget(secondAnsLay)
        self.layout.add_widget(secondAnsA)
        self.layout.add_widget(secondAnsACheck)
        self.layout.add_widget(secondAnsB)
        self.layout.add_widget(secondAnsBCheck)
        self.layout.add_widget(secondAnsC)
        self.layout.add_widget(secondAnsCCheck)
        self.layout.add_widget(secondAnsD)
        self.layout.add_widget(secondAnsDCheck)
        
        self.layout.add_widget(thirdQ)
        self.layout.add_widget(thirdAnsLay)
        self.layout.add_widget(thirdAnsA)
        self.layout.add_widget(thirdAnsACheck)
        self.layout.add_widget(thirdAnsB)
        self.layout.add_widget(thirdAnsBCheck)
        self.layout.add_widget(thirdAnsC)
        self.layout.add_widget(thirdAnsCCheck)
        self.layout.add_widget(thirdAnsD)
        self.layout.add_widget(thirdAnsDCheck)
        
        self.layout.add_widget(fourthQ)
        self.layout.add_widget(fourthAnsLay)
        self.layout.add_widget(fourthAnsA)
        self.layout.add_widget(fourthAnsACheck)
        self.layout.add_widget(fourthAnsB)
        self.layout.add_widget(fourthAnsBCheck)
        self.layout.add_widget(fourthAnsC)
        self.layout.add_widget(fourthAnsCCheck)
        self.layout.add_widget(fourthAnsD)
        self.layout.add_widget(fourthAnsDCheck)
        
        self.layout.add_widget(fifthQ)
        self.layout.add_widget(fifthAnsLay)
        self.layout.add_widget(fifthAnsA)
        self.layout.add_widget(fifthAnsACheck)
        self.layout.add_widget(fifthAnsB)
        self.layout.add_widget(fifthAnsBCheck)
        self.layout.add_widget(fifthAnsC)
        self.layout.add_widget(fifthAnsCCheck)
        self.layout.add_widget(fifthAnsD)
        self.layout.add_widget(fifthAnsDCheck)
        
        self.layout.add_widget(sixthQ)
        self.layout.add_widget(sixthAnsLay)
        self.layout.add_widget(sixthAnsA)
        self.layout.add_widget(sixthAnsACheck)
        self.layout.add_widget(sixthAnsB)
        self.layout.add_widget(sixthAnsBCheck)
        self.layout.add_widget(sixthAnsC)
        self.layout.add_widget(sixthAnsCCheck)
        self.layout.add_widget(sixthAnsD)
        self.layout.add_widget(sixthAnsDCheck)
        
        return self.layout
        
    
if __name__ == "__main__":
    Quiz().run()