#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 16:44:34 2022

@author: laurastump
"""

from tkinter import* # easiest way to develop GUI so importing everything from tkinter
from translate import Translator #package helps translate major languages

Screen = Tk() #creation of root window
Screen.title("Language Translation") #displaying title

#stores language of text that is being translated
InputLanguageChoice = StringVar()

#stpres language that the text is to be translated in
TranslateLanguageChoice = StringVar()

#These are the languages that will be available to choose from // more can be added or deleted
LanguageChoices = {'English', 'Hindi', 'French', 'German', 'Spanish', 'Italian', 'Korean', 'Japanese', 'Chinese', 'Russian', 'Arabic'}

#setting language to English
InputLanguageChoice.set('English')

#setting translation to Italian, but can change to whatever language above
TranslateLanguageChoice.set('Italian')

#creating a function for text translation
def Translate():
    translator = Translator(from_lang = InputLanguageChoice.get(), to_lang = TranslateLanguageChoice.get())
    Translation = translator.translate(TextVar.get())
    OutputVar.set(Translation)
    
#choice for input language
InputLanguageChoiceMenu = OptionMenu(Screen,InputLanguageChoice,*LanguageChoices)
Label(Screen,text="Pick a Language").grid(row=0,column=1)
InputLanguageChoiceMenu.grid(row=1,column=1)

#choice of translated language
NewLanguageChoiceMenu = OptionMenu(Screen,TranslateLanguageChoice,*LanguageChoices) # provides options to user
Label(Screen,text="Translated Language").grid(row=0,column=2) #helps implement display boxes
NewLanguageChoiceMenu.grid(row=1,column=2) #arrangement of widgets

Label(Screen,text="Enter Text").grid(row=2,column =0)
TextVar = StringVar()
TextBox = Entry(Screen,textvariable=TextVar).grid(row=2,column = 1)
 
Label(Screen,text="Output Text").grid(row=2,column =2)
OutputVar = StringVar()
TextBox = Entry(Screen,textvariable=OutputVar).grid(row=2,column = 3)
 
#Button for calling function // creates a button #relief provides 3D effects around widget
B = Button(Screen,text="Translate",command=Translate, relief = GROOVE).grid(row=3,column=1,columnspan = 2)
 
mainloop() #helps run tkinter within the loop