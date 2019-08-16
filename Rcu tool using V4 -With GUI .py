#GUI Import and start
from tkinter import *
from tkinter.filedialog import askopenfilename
from bs4 import BeautifulSoup
from tkinter.filedialog import askdirectory
import tkinter.messagebox
import os



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
        postcode_count = 0
        pripostcode_count = 0
        NiNumber_count = 0
        ULN_count = 0
        Email_count = 0
        telnum_count = 0
        addLines4_count = 0
        addLines2_count = 0
        addLines3_count = 0
        addLines1_count = 0
        familyname_count = 0
        surname_count = 0
        dob_count = 0
        with open(name,'r') as infile:
            xml_text = infile.read()

        soup = BeautifulSoup(xml_text, 'xml')

        ####################
        ##Anonymising data##
        ####################

        #Date Of Birth# 
        for dob_tag in soup.find_all("DateOfBirth"):
            dob_count = len(soup.find_all("DateOfBirth"))
            dob_tag.string = ""


        #Full Name#
        for surname_tag in soup.find_all("FamilyName"):
            surname_count = len(soup.find_all("FamilyName"))
            surname_tag.string = ""
        for familyname_tag in soup.find_all("GivenNames"):
            familyname_count = len(soup.find_all("GivenNames"))
            familyname_tag.string = ""

        #Adress Lines#
        for addlines1_tag in soup.find_all("AddLine1"):
            addLines1_count = len(soup.find_all("AddLine1"))
            addlines1_tag.string = ""
        for addlines2_tag in soup.find_all("AddLine2"):
            addLines2_count = len(soup.find_all("AddLine2"))
            addlines2_tag.string = ""
        for addlines3_tag in soup.find_all("AddLine3"):
            addLines3_count = len(soup.find_all("AddLine3"))
            addlines3_tag.string = ""
        for addlines4_tag in soup.find_all("AddLine4"):
            addLines4_count = len(soup.find_all("AddLine4"))
            addlines4_tag.string = ""

        #Telephone number#
        for telnum_tag in soup.find_all("TelNo"):
            telnum_count = len(soup.find_all("TelNo"))
            telnum_tag.string = ""

        #Email Address#
        for Email_tag in soup.find_all("Email"):
            Email_count = len(soup.find_all("Email"))
            Email_tag.string = ""

        #Unique Learner Numeber#
        for ULN_tag in soup.find_all("ULN"):
            ULN_count = len(soup.find_all("ULN"))
            ULN_tag.string = ""
    
        #National Insurance Number#
        for NiNumber_tag in soup.find_all("NINumber"):
            NiNumber_count = len(soup.find_all("NINumber"))
            NiNumber_tag.string = ""

        # Find and Add three tags for
        # Deprivation Band
        # Local Authority District
        # Local Authoirty Ward
        for item in soup.select('Learner'):
            finaltag = item.select('LearningDelivery')[-1]
            new_tag = soup.new_tag("Local_Authority_Ward")
            new_tag.append("")
            finaltag.insert_after(new_tag)
            new_tag = soup.new_tag("Local_Authority_District")
            new_tag.append("")
            finaltag.insert_after(new_tag)
            new_tag = soup.new_tag("Deprivation_Band")
            new_tag.append("")
            finaltag.insert_after(new_tag)



        #Add postcode #todo start adding postcode matches to the above fields.



        #Postcodes (Deleting last 3 digits)#
        for pripostcode_tag in soup.find_all("PostcodePrior"):
            pripostcode_count = len(soup.find_all("PostcodePrior"))
            pripostcode_tag.string = pripostcode_tag.string[:-3]

        for postcode_tag in soup.find_all("Postcode"):
            postcode_count = len(soup.find_all("Postcode"))
            postcode_tag.string = postcode_tag.string[:-3]



        # Output And Save Modified FilePrior Postcodes

        nameFile = os.path.basename(name)
        print(str(name))

        with open(outputlocation + "\RCU_" + nameFile , "w") as outfile:
            outfile.write(soup.prettify())

        tkinter.messagebox.showinfo('Field Check',
        'Number of fields anonymised\n'
        'Postcodes : ' + str(postcode_count) + '\n'
        'Prior Postcodes : '+ str(pripostcode_count) +'\n'
        'national insurance numbers : ' + str(NiNumber_count) + '\n'
        'ULNs : ' + str(ULN_count) +'\n'
        'Emails : ' + str(Email_count) +'\n'
        'Telephone Numbers : ' + str(telnum_count) +'\n'
        'Address Line 1 : ' + str(addLines4_count) +'\n'
        'Address Line 2 : ' + str(addLines3_count) +'\n'
        'Address Line 3 : ' + str(addLines2_count) +'\n'
        'Address Line 4 : ' + str(addLines1_count) +'\n'
        'Family Names : ' + str(familyname_count) +'\n'
        'Surnames : ' + str(surname_count) +'\n'
        'dates of births : ' + str(dob_count) +'\n')
        tkinter.messagebox.showinfo("Finished Anonymisation!", "Finished Anonymisation! Thank you. \nFile explorer will automatically open in your selected output location. This file will need to be uploaded manually")
        os.startfile(outputlocation)

    except:
         tkinter.messagebox.showinfo("Failed Anonymisation!", "Anonymisation Failed! Please retry or contact RCU \n  Tel: 01772 734855  |  Email: Mides@rcu.co.uk")

#Programme View
root.geometry ("500x350")
OverviewLabel3 = Label(root, text="Tel: 01772 734855  |  Email: Mides@rcu.co.uk", bd=1, relief=SUNKEN,)
OverviewLabel = Label(root, text='\n You will be asked for your ILR first then asked to give a output location for the produced ILR \n')
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
