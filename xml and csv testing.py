# GUI Import and start
from tkinter import *
from tkinter.filedialog import askopenfilename
from bs4 import BeautifulSoup
from tkinter.filedialog import askdirectory
import tkinter.messagebox
import csv
import os





# Create window interface / Labels
root = Tk()
root.iconbitmap(r'C:\Users\jkay\AppData\Local\Programs\Python\Python37-32\DLLs\RCU2.ico')
root.title("RCU Anonymiser Tool")


def OpenFile(): #todo add vaildation
    name = askopenfilename(filetypes=(("XML File", "*.XML"), ("All Files", "*.*")),
                           title="Choose the ILR file.")

    outputlocation =askdirectory(title = "Select Output Location.")
    try:
        with open(name, 'r') as infile:
            xml_text = infile.read()

        soup = BeautifulSoup(xml_text, 'xml')

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

        for postcode_tag in soup.find_all("Postcode"):
            postcode_tag.string = postcode_tag.string

        for postcode_tag in soup.find_all("Postcode"):
            postcode_tag.string = postcode_tag.string
            with open('Deprivation_Band_Lookup.csv') as csvfile:
                readCSV = csv.reader(csvfile, delimiter=',')
                for row in readCSV:
                    if row[0] == postcode_tag.string:
                        dep_band_final = row[1]
                        print(dep_band_final)   #  DE14 1SS is the one real postcode = 5







            nameFile = os.path.basename(name)
            print(str(name))

        with open(outputlocation + "\RCU_" + nameFile, "w") as outfile:
            outfile.write(soup.prettify())

            tkinter.messagebox.showinfo("Finished Anonymisation!",
                                        "Finished Anonymisation! Thank you.  \nFile explorer will automatically open in your selected output location. This file will need to be uploaded manually")
            os.startfile(outputlocation)

    except:
        tkinter.messagebox.showinfo("Failed Anonymisation!",
                                "Anonymisation Failed! Please retry or contact RCU \n  Tel: 01772 734855  |  Email: Mides@rcu.co.uk")


# Programme View
root.geometry("500x300")
OverviewLabel3 = Label(root, text='Anonymiser Tool', font='Helvetica 14 bold')
OverviewLabel4 = Label(root, text="Tel: 01772 734855  |  Email: Mides@rcu.co.uk", bd=1)
OverviewLabel = Label(root,
                      text='\n You will be asked for your ILR first then asked to give a output location for the produced ILR \n Please insert the ILR file below (XML Format) to start the process')
# OverviewLabel2 = Label(root, text=" \nPlease insert the ILR file below (XML Format) to start the process.")



# Top Frame
topFrame = Frame(root)
topFrame.pack(side=TOP)

# Bottom Frame
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

# Widgits (Buttons)
Button1 = Button(bottomFrame, text="              Select ILR             ", fg="Black", bg="Yellow", command=OpenFile,
                 padx=1, pady=1)
Button1.pack()
# Button1.place(x=175, y=315 )

OverviewLabel3.pack()
OverviewLabel4.pack()
OverviewLabel.pack()
# OverviewLabel2.pack()


# Start Event
root.mainloop()
