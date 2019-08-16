# GUI Import and start
from tkinter import *
from tkinter.filedialog import askopenfilename
from bs4 import BeautifulSoup
from tkinter.filedialog import askdirectory
import tkinter.messagebox
import os
import csv



# Create window interface / Labels
root = Tk()
root.iconbitmap(r'C:\Users\jkay\AppData\Local\Programs\Python\Python37-32\DLLs\RCU2.ico')
root.title("RCU Anonymiser Tool")
from PIL import Image, ImageTk


# Triggering the anonamising


def OpenFile():  # todo add vaildation
    name = askopenfilename(filetypes=(("XML File", "*.XML"), ("All Files", "*.*")),
                           title="Choose the ILR file.")

    outputlocation = askdirectory(title="Select Output Location.")

    try:
        with open(name, 'r') as infile:
            xml_text = infile.read()

        soup = BeautifulSoup(xml_text, 'xml')

        # Add postcode #todo start adding postcode matches to the above fields.
        #######################################################################

        for item in soup.select('Learner'):
            finaltag = item.select('LearningDelivery')[-1]
            new_tag = soup.new_tag("Deprivation_Band")

            db_lookup = open('Deprivation_Band_Lookup.csv')
            csv_db_lookup = csv.reader(db_lookup)

        if csv_db_lookup[0] == soup.find_all("Postcode"):
            new_tag.append(int(csv_db_lookup[1]))
            finaltag.insert_after(new_tag)


        ########################################################################


        # Postcodes (Deleting last 3 digits)#
        for pripostcode_tag in soup.find_all("PostcodePrior"):
            pripostcode_tag.string = pripostcode_tag.string[:-3]

        for postcode_tag in soup.find_all("Postcode"):
            postcode_tag.string = postcode_tag.string[:-3]

        # Output And Save Modified File

        nameFile = os.path.basename(name)
        print(str(name))

        with open(outputlocation + "\RCU_" + nameFile, "w") as outfile:
            outfile.write(soup.prettify())

        tkinter.messagebox.showinfo("Finished Anonymisation!",
                                    "Thank you. The file will be located\nin your selected output location\n" + outputlocation + "/RCU_" + nameFile)  # Make this appear in a widget.
    except:
        tkinter.messagebox.showinfo("Failed Anonymisation!",
                                    "Anonymisation Failed! Please retry or contact RCU \n  Tel: 01772 734855  |  Email: Mides@rcu.co.uk")


# Programme View
root.geometry("500x350")
OverviewLabel3 = Label(root, text="Tel: 01772 734855  |  Email: Mides@rcu.co.uk", bd=1, relief=SUNKEN, )
OverviewLabel = Label(root,
                      text='\n You will be asked for your ILR first then asked to give a output location for the produced ILR \n')
OverviewLabel2 = Label(root, text=" \nPlease insert the ILR file below (XML Format) to start the process.")
img = Image.open("RCULOGO.png")
rculogo = ImageTk.PhotoImage(img)
Label(root, image=rculogo).pack()

# Top Frame
topFrame = Frame(root)
topFrame.pack(side=TOP)

# Bottom Frame
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

# Widgits (Buttons)
Button1 = Button(bottomFrame, text="    Being Anonymisation   ", fg="Black", bg="Yellow", command=OpenFile)
Button1.pack(side=LEFT)

OverviewLabel3.pack()
OverviewLabel.pack()
OverviewLabel2.pack()

# Start Event
root.mainloop()
