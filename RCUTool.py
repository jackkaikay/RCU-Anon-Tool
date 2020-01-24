import xml.etree.ElementTree as ET
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory
import tkinter.messagebox
import os
import pandas as pd
import csv
from PIL import Image, ImageTk
import sys
from zipfile import ZipFile
from os.path import basename
import threading


# This function sorts images for pyinstaller (https://stackoverflow.com/questions/7674790/bundling-data-files-with-pyinstaller-onefile/44352931#44352931)
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


depbandtxt = resource_path('Dependencies\DeprivationBand.txt')
icoimg = resource_path('Dependencies\RCU2.ico')
pngimg = resource_path("Dependencies\RCULOGO_Smallpng.png")


def OpenFile():
    statusBar.config(text='STATUS: Loading ILR File...', fg='red')
    filename = depbandtxt
    depDepend = pd.read_csv(filename)
    depDepend.set_index('Postcode', inplace=True)

    name = askopenfilename(filetypes=(("XML File", "*.XML"), ("All Files", "*.*")),
                           title="Choose the ILR file.")

    nameFile = os.path.basename(name)
    if name == '':
        statusBar.config(text='Status: Please Load ILR File', fg='Black')
        tkinter.messagebox.showinfo("Failed Anonymisation!",
                                    "Please Select a Valid ILR File")
    else:
        statusBar.config(text='STATUS: Selecting Output location', fg='red')
        outputlocation = askdirectory(title="Select Output Location.")
        statusBar.config(text='STATUS: Anonymising ILR File... Please Wait', fg='red')
    if outputlocation == '':
        statusBar.config(text='Status: Please Select Valid Output Location', fg='Black')
        tkinter.messagebox.showinfo("Failed Anonymisation!",
                                    "Please Select a Valid Output location")
    else:
        UKPRN_Name = nameFile[4:12]

        try:
            statusBar.config(text='STATUS: Anonymising ILR File...', fg='red')
            ET.register_namespace("", 'ESFA/ILR/2018-19')
            dom = ET.parse(name)
            root = dom.getroot()
            ####################
            ##Anonymising data##
            ####################

            # Date Of Birth#
            for ns in root.findall('{ESFA/ILR/2018-19}Learner'):
                name = ns.find('{ESFA/ILR/2018-19}DateOfBirth')
                try:
                    name.text = '2099-01-01'
                except:
                    print('No DateOfBirth Found')

            # Full Name#
            for ns in root.findall('{ESFA/ILR/2018-19}Learner'):
                name = ns.find('{ESFA/ILR/2018-19}FamilyName')
                try:
                    name.text = 'NULL'
                except:
                    print('No FamilyName Found')

            for ns in root.findall('{ESFA/ILR/2018-19}Learner'):
                name = ns.find('{ESFA/ILR/2018-19}GivenNames')
                try:
                    name.text = 'NULL'
                except:
                    print('No GivenNames Found')

            # Adress Lines#
            for ns in root.findall('{ESFA/ILR/2018-19}Learner'):
                name = ns.find('{ESFA/ILR/2018-19}AddLine1')
                try:
                    name.text = 'NULL'
                except:
                    print('No AddLine1 Found')
            for ns in root.findall('{ESFA/ILR/2018-19}Learner'):
                name = ns.find('{ESFA/ILR/2018-19}AddLine2')
                try:
                    name.text = 'NULL'
                except:
                    print('No AddLine2 Found')
            for ns in root.findall('{ESFA/ILR/2018-19}Learner'):
                name = ns.find('{ESFA/ILR/2018-19}AddLine3')
                try:
                    name.text = 'NULL'
                except:
                    print('No AddLine3 Found')
            for ns in root.findall('{ESFA/ILR/2018-19}Learner'):
                name = ns.find('{ESFA/ILR/2018-19}AddLine4')
                try:
                    name.text = 'NULL'
                except:
                    print('No AddLine4 Found')

            # Telephone number#
            for ns in root.findall('{ESFA/ILR/2018-19}Learner'):
                name = ns.find('{ESFA/ILR/2018-19}TelNo')
                try:
                    name.text = 'NULL'
                except:
                    print('No TelNo Found')

            # Email Address#
            for ns in root.findall('{ESFA/ILR/2018-19}Learner'):
                name = ns.find('{ESFA/ILR/2018-19}Email')
                try:
                    name.text = 'NULL'
                except:
                    print('No Email Found')
            # Unique Learner Numeber#
            for ns in root.findall('{ESFA/ILR/2018-19}Learner'):
                name = ns.find('{ESFA/ILR/2018-19}ULN')
                try:
                    name.text = '99999999'
                except:
                    print('No ULN Found')

            # National Insurance Number#
            for ns in root.findall('{ESFA/ILR/2018-19}Learner'):
                name = ns.find('{ESFA/ILR/2018-19}NINumber')
                try:
                    name.text = 'NULL'
                except:
                    print('No NINumber Found')

            # Find and Add three tags for
            # Deprivation Band
            # Local Authority District
            # Local Authoirty Ward / ADD IF BOX TICKED

            if 0 == 0:
                LRN_List = {}
                LRN_Num = 0
                for ns in root.findall('{ESFA/ILR/2018-19}Learner'):
                    ns = ns.find('{ESFA/ILR/2018-19}LearnRefNumber')
                    ns = ns.text
                    print(ns)
                    LRN_List[LRN_Num] = ns
                    LRN_List[LRN_Num] = ns
                    LRN_Num += 1

                PCD_List = {}
                PCD_Num = 0
                for ns in root.findall('{ESFA/ILR/2018-19}Learner'):
                    ns = ns.find('{ESFA/ILR/2018-19}Postcode')
                    ns = ns.text
                    print(ns)
                    PCD_List[PCD_Num] = ns
                    PCD_List[PCD_Num] = ns
                    PCD_Num += 1

                print(LRN_List)
                print(PCD_List)
                statusBar.config(text='STATUS: Creating Deprivation Band CSV Output...', fg='red')
                with open(outputlocation + '\RCU_' + nameFile[:-4] + '.csv', 'w', newline='') as csvfile:
                    filewriter = csv.writer(csvfile, delimiter=',',
                                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
                    filewriter.writerow(
                        ['UKPRN', 'Learner_Ref_Number', 'Deprivation_Band', 'Local_Authority_District',
                         'Local_Authority_Ward'])

                    Num = 0

                    for learners in PCD_List:
                        try:
                            filewriter.writerow(
                                [UKPRN_Name, LRN_List[Num], depDepend.loc[PCD_List[Num], 'Deprivation_Band'],
                                 depDepend.loc[PCD_List[Num], 'LAD_Code'],
                                 depDepend.loc[PCD_List[Num], 'Merged_Ward_Code']])
                            Num += 1

                        except:
                            print('No Postcode Found')
                            assign = 'Null'
                            assignLad = 'Null'
                            assignWd = 'Null'
                            filewriter.writerow([UKPRN_Name, LRN_List[Num], str(assign), str(assignLad), str(assignWd)])
                            Num += 1

                # Postcodes (Deleting last 3 digits)#
            for ns in root.findall('{ESFA/ILR/2018-19}Learner'):
                name = ns.find('{ESFA/ILR/2018-19}Postcode')
                try:
                    name.text = name.text[:-4]
                except:
                    print('No Postcode Found')
            for ns in root.findall('{ESFA/ILR/2018-19}Learner'):
                name = ns.find('{ESFA/ILR/2018-19}PostcodePrior')
                try:
                    name.text = name.text[:-4]
                except:
                    print('No PostcodePrior Found')

            # Output And Save Modified FilePrior Postcodes

            statusBar.config(text='STATUS: Outputting Files to Selected Location...', fg='red')
            dom.write(outputlocation + '\RCU_' + nameFile + '.anon', encoding='utf-8', xml_declaration=True)

            zipObj = ZipFile(outputlocation + '\RCU_' + nameFile + '.zip', 'w')
            zipObj.write(outputlocation + '\RCU_' + nameFile + '.anon', basename('RCU_' + nameFile + '.anon'))
            zipObj.write(outputlocation + '\RCU_' + nameFile[:-4] + '.csv', 'RCU_' + nameFile[:-4] + '.csv')
            zipObj.close()

            tkinter.messagebox.showinfo("Finished Anonymisation!",
                                        "Finished Anonymisation! Thank you. \nFile explorer will automatically open in your selected output location.")
            os.startfile(outputlocation)
            statusBar.config(text='Status: File Anonymised... Thank you for using the RCU Anonymiser tool', fg='Black')
        except:
            tkinter.messagebox.showinfo("Failed Anonymisation!",
                                        "Anonymisation Failed! Please retry or contact RCU \n  Tel: 01772 734855  |  Email: Mides@rcu.co.uk")
            statusBar.config(text='Status: Please Load ILR File', fg='Black')


def informationbox():
    popup = Tk()

    def leavemini():
        popup.destroy()

    popup.geometry("310x525")
    popup.resizable(width=False, height=False)
    popup.title("Additional Information")
    popupbutton1 = tkinter.Button(popup, padx=5, pady=5, text="Ok", fg="Black", bg="Yellow", command=leavemini)
    popup.iconbitmap(icoimg)
    popuplabel1 = Label(popup, anchor='w',
                        text=' Removes personally identifiable fields from the ILR files. \n \n \n Version 1.0 \n Copyright © RCU Ltd. \n \n Deletes following information where it exists \n \n  Postcodes\n Prior Postcodes \n  National Insurance Numbers \nULNs\nEmails\nTelephone Numbers\nAddress Line 1\nAddress Line 2\nAddress Line 3\nAddress Line 4\nFamily Names\nSurnames\n dates of birth\n \n \n How to use \n All anonymisation is done from the "Select ILR" button\n add \n much \n more \n text  \n \n For any further required assistance \n Tel: 01772 734855  |  Email: Mides@rcu.co.uk \n')
    popuplabel1.pack(fill='both')
    popupbutton1.pack()
    popup.mainloop()


def LoadingBox():
    popup = Tk()

    def leavemini():
        popup.destroy()

    popup.geometry("310x525")
    popup.resizable(width=False, height=False)
    popup.title("Additional Information")
    popupbutton1 = tkinter.Button(popup, padx=5, pady=5, text="Ok", fg="Black", bg="Yellow", command=leavemini)
    popup.iconbitmap(icoimg)
    popuplabel1 = Label(popup, anchor='w',
                        text=' Removes personally identifiable fields from the ILR files. \n \n \n Version 1.0 \n Copyright © RCU Ltd. \n \n Deletes following information where it exists \n \n  Postcodes\n Prior Postcodes \n  National Insurance Numbers \nULNs\nEmails\nTelephone Numbers\nAddress Line 1\nAddress Line 2\nAddress Line 3\nAddress Line 4\nFamily Names\nSurnames\n dates of birth\n \n \n How to use \n All anonymisation is done from the "Select ILR" button\n add \n much \n more \n text  \n \n For any further required assistance \n Tel: 01772 734855  |  Email: Mides@rcu.co.uk \n')
    popuplabel1.pack(fill='both')
    popupbutton1.pack()
    popup.mainloop()


if __name__ == '__main__':
    root = Tk()
    root.iconbitmap(icoimg)
    root.title("RCU Anonymiser Tool")
    root.geometry("500x365")
    OverviewLabel3 = Label(root, text='Anonymiser Tool', font='Helvetica 14 bold')
    OverviewLabel4 = Label(root, text="Tel: 01772 734855  |  Email: Mides@rcu.co.uk", bd=1, )
    OverviewLabel = Label(root,
                          text='\n This programme will produce a zip file ready for upload (Anonymised ILR + Optional CSV) \n Please insert the ILR file below (XML Format) to start the process')

    OverviewLabel2 = Label(root, text=" \nPlease insert the ILR file below (XML Format) to start the process.")
    img = Image.open(pngimg)
    rculogo = ImageTk.PhotoImage(img)
    Label(root, image=rculogo).pack()

    # Top Frame
    topFrame = Frame(root)
    topFrame.pack(side=TOP)

    # Bottom Frame
    bottomFrame = Frame(root)
    bottomFrame.pack(side=BOTTOM)

    # Widgits (Buttons)
    checkVar1 = IntVar()
    Process = threading.Thread(target=OpenFile)
    Button1 = Button(root, text="              Select ILR             ", fg="Black", bg="Yellow",
                     command=Process.start, padx=1, pady=1)
    Button2 = Button(root, text="       Extra Information       ", command=informationbox, padx=1, pady=1)
    statusBar = Label(root, text="Status: Please Load ILR File", bd=1, relief=SUNKEN, anchor=W, fg='black')
    statusBar.pack(side=BOTTOM, fill=X)
    spaceLabel = Label(root, text="")
    OverviewLabel3.pack()
    OverviewLabel4.pack()
    OverviewLabel.pack()
    spaceLabel.pack()
    Button1.pack()
    Button2.pack()

    # Start Event
    root.mainloop()
