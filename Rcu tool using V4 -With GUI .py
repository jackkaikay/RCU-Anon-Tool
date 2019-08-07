#GUI Import and start
from tkinter import *
from tkinter.filedialog import askopenfilename
from bs4 import BeautifulSoup
from tkinter.filedialog import askdirectory
import tkinter.messagebox

#Create window interface / Labels 
root = Tk()
root.iconbitmap(r'C:\Users\jkay\AppData\Local\Programs\Python\Python37-32\DLLs\RCU2.ico')
root.title("RCU Anonymiser Tool")
from PIL import Image, ImageTk

#Triggering the anonamising


def OpenFile(): #todo add vaildation
    name = askopenfilename(filetypes=(("XML File", "*.XML"), ("All Files", "*.*")),
                           title="Choose the ILR file.")

    outputlocation =askdirectory(title = "Select Output Location.")


    #Using try in case user types in unknown file or closes without choosing a file.
    try:
        with open(name,'r') as infile:
            xml_text = infile.read()

        soup = BeautifulSoup(xml_text, 'xml')

        ####################
        ##Anonymising data##
        ####################

        #Date Of Birth# 
        for dob_tag in soup.find_all("DateOfBirth"):
            dob_tag.string = "NULL"

        #Full Name#
        for surname_tag in soup.find_all("FamilyName"):
            surname_tag.string = "NULL"
        for familyname_tag in soup.find_all("GivenNames"):
            familyname_tag.string = "NULL"

        #Adress Lines#
        for addlines1_tag in soup.find_all("AddLine1"):
            addlines1_tag.string = "NULL"
        for addlines2_tag in soup.find_all("AddLine2"):
            addlines2_tag.string = "NULL"
        for addlines3_tag in soup.find_all("AddLine3"):
            addlines3_tag.string = "NULL"
        for addlines4_tag in soup.find_all("AddLine4"):
            addlines4_tag.string = "NULL"

        #Telephone number#
        for telnum_tag in soup.find_all("TelNo"):
            telnum_tag.string = "NULL"

        #Email Address#
        for Email_tag in soup.find_all("Email"):
            Email_tag.string = "NULL"

        #Unique Learner Numeber#
        for ULN_tag in soup.find_all("ULN"):
            ULN_tag.string = "NULL"
    
        #National Insurance Number#
        for NiNumber_tag in soup.find_all("NINumber"):
            NiNumber_tag.string = "NULL"

        # Find and Add three tags for
        # Deprivation Band
        # Local Authority District
        # Local Authoirty Ward
        for item in soup.select('Learner'):
            finaltag = item.select('LearningDelivery')[-1]
            new_tag = soup.new_tag("law-ru")
            new_tag.append("NULL")
            finaltag.insert_after(new_tag)
            new_tag = soup.new_tag("lad-ru")
            new_tag.append("NULL")
            finaltag.insert_after(new_tag)
            new_tag = soup.new_tag("db-ru")
            new_tag.append("NULL")
            finaltag.insert_after(new_tag)



        #Add postcode #todo start adding postcode matches to the above fields.



        #Postcodes (Deleting last 3 digits)#
        for pripostcode_tag in soup.find_all("PostcodePrior"):   
            pripostcode_tag.string = pripostcode_tag.string[:-3]
   
        for postcode_tag in soup.find_all("Postcode"):   
            postcode_tag.string = postcode_tag.string[:-3]



        # Output And Save Modified File

        with open(outputlocation + "\RCU_Anon.xml", "w") as outfile:
            outfile.write(soup.prettify())

        tkinter.messagebox.showinfo("Finished Anonymisation!", "Thank you. The file will be located\nin your selected output location") #Make this appear in a widget.
    except:
         tkinter.messagebox.showinfo("Failed Anonymisation!", "Anonymisation Failed! Please retry or contact RCU \n  Tel: 01772 734855  |  Email: Mides@rcu.co.uk")

#Programme View
root.geometry ("500x350")
OverviewLabel3 = Label(root, text="Tel: 01772 734855  |  Email: Mides@rcu.co.uk", bd=1, relief=SUNKEN,)
OverviewLabel = Label(root, text='\n You will be asked for your ILR first then asked to give a output location for the produced ILR \n This file will be called "RCU_Anon_ORIGFILENAME"')
OverviewLabel2 = Label(root, text=" \nPlease insert the ILR file below (XML Format) to start the process.")
img = Image.open("RCULOGO.png")
rculogo = ImageTk.PhotoImage(img)
Label(root, image=rculogo).pack()

#Top Frame
topFrame = Frame(root)
topFrame.pack(side=TOP)

#Bottom Frame
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

#Widgits (Buttons)
Button1 = Button(bottomFrame,  text="    Being Anonymisation   ", fg="Black", bg="Yellow", command=OpenFile)
Button1.pack(side=LEFT)

OverviewLabel3.pack()
OverviewLabel.pack()
OverviewLabel2.pack()


#Start Event 
root.mainloop()
