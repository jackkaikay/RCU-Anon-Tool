#GUI Import and start
from tkinter import *
from tkinter.filedialog import askopenfilename
from bs4 import BeautifulSoup

#Create window interface / Labels 
root = Tk()

root.title("RCU Anonymiser Tool")



def OpenFile():
    name = askopenfilename(initialdir="C:/Users/Batman/Documents/Programming/tkinter/",
                           filetypes =(("Text File", "*.txt"),("All Files","*.*")),
                           title = "Choose a file."
                           )
    print (name)
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

        #Unique Learner Numebr#
        for ULN_tag in soup.find_all("ULN"):
            ULN_tag.string = "NULL"
    
        #National Insurance Number#
        for NiNumber_tag in soup.find_all("NINumber"):
            NiNumber_tag.string = "NULL"

        #Postcodes (Deleting last 3 digits)#
        for pripostcode_tag in soup.find_all("PostcodePrior"):   
            pripostcode_tag.string = pripostcode_tag.string[:-3]
   
        for postcode_tag in soup.find_all("Postcode"):   
            postcode_tag.string = postcode_tag.string[:-3]

    

        # Find and Add three tags for
        # Deprivation Band
        # Local Authority District
        # Local Authoirty Ward 
        for item in soup.select('Learner'):
            finaltag=item.select('LearningDelivery')[-1]
            new_tag = soup.new_tag("law-ru")
            new_tag.append("NULL")
            finaltag.insert_after(new_tag)
            new_tag = soup.new_tag("lad-ru")
            new_tag.append("NULL")
            finaltag.insert_after(new_tag)
            new_tag = soup.new_tag("db-ru")
            new_tag.append("NULL")
            finaltag.insert_after(new_tag)
    
    




        ###################################  
        ## Output And Save Modified File ##
        ###################################

    
        with open("SEND_ME_TO_RCU2.xml", "w") as outfile:
            outfile.write(soup.prettify())
    except:
         print("No file exists")


        
#root.geometry ("400x400")

OverviewLabel = Label(root, text="Please insert the ILR file below (XML Format)")
OverviewLabel2 = Label(root, text="I am going to explain how to use the tool")


########
#Frames#
########
#Top Frame 
topFrame = Frame(root)
topFrame.pack(side=TOP)
#Bottom Frame
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

#Widgits (Buttons) 

Button1 = Button(bottomFrame, text="    Select ILR File   ", fg="Black", bg="Yellow", command=OpenFile)
Button2 = Button(bottomFrame, text="Select Output Location", fg="Red")
Button3 = Button(bottomFrame, text="RUN!", fg="Red", bg="Black")

Button1.pack(side=LEFT)
Button2.pack(side=LEFT)
Button3.pack(side=RIGHT)

OverviewLabel.pack()
OverviewLabel2.pack()

#Start Event 
root.mainloop()
