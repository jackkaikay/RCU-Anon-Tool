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
import webbrowser

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


def openWebsite():
    webbrowser.open_new(r'http://rcu.co.uk/')

def closeProg():
    root.destroy()

def OpenFile():
    Button1.config(state='disabled', relief=SUNKEN, text='      ILR Anonymising..      ', bg='light yellow')
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
        restart_program()
    else:
        statusBar.config(text='STATUS: Selecting Output location', fg='red')
        outputlocation = askdirectory(title="Select Output Location.")
        statusBar.config(text='STATUS: Anonymising ILR File... Please Wait', fg='red')
    if outputlocation == '':
        statusBar.config(text='Status: Please Select Valid Output Location', fg='Black')
        tkinter.messagebox.showinfo("Failed Anonymisation!",
                                    "Please Select a Valid Output location")
        restart_program()
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
            Button1.pack_forget()
            Button2.pack_forget()
            OverviewLabel.pack_forget()
            spaceSaver.pack_forget()
            after1.pack()
            spaceLabel.pack_forget()
            afterButton1.pack()
            spaceSaver.pack()
            afterButton2.pack()
        except:
            tkinter.messagebox.showinfo("Failed Anonymisation!",
                                        "Anonymisation Failed! Please retry or contact RCU \n  Tel: 01772 734855  |  Email: Mides@rcu.co.uk")
            Button1.status(text="            Load ILR File           ", fg="Black", bg="Yellow",
                   command=Process.start, padx=1, pady=1)
            statusBar.config(text='Status: Please Load ILR File', fg='Black')


def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)


if __name__ == '__main__':
    root = Tk()
    root.iconbitmap(icoimg)
    root.title("RCU ILR Anonymiser")
    root.geometry("500x365")
    OverviewLabel3 = Label(root, text='RCU ILR Anonymiser', font='Helvetica 14 bold')
    spaceSaver = Label(root, text="", bd=1, )
    OverviewLabel = Label(root,
                          text='\n This programme will produce a zip file ready for upload (Anonymised ILR + Optional CSV) \n Please insert the ILR file below (XML Format) to start the process')

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
    Button1 = Button(root, text="            Load ILR File           ", fg="Black", bg="Yellow",
                     command=Process.start, padx=1, pady=1)
    Button2 = Button(root, text="       Extra Information       ", command=openWebsite, padx=1, pady=1, bg='light yellow')
    statusBar = Label(root, text="Status: Please Load ILR File", bd=1, relief=SUNKEN, anchor=W, fg='black')
    statusBar.pack(side=BOTTOM, fill=X)
    spaceLabel = Label(root, text="")
    OverviewLabel3.pack()
    OverviewLabel.pack()
    spaceLabel.pack()
    Button1.pack()
    spaceSaver.pack()
    Button2.pack()
    after1 = Label(root,
                          text='\n Thank your for anonymising using the RCU ILR Anoymiser \n press below to be taken directly to the upload area \n')
    afterButton1 = Button(root, text="            Upload ILR           ", fg="Black", bg="Yellow",

                     command=openWebsite, padx=1, pady=1)
    afterButton2 = Button(root, text="     Back to ILR Anonymisation     ", command=restart_program, padx=1, pady=1,
                     bg='light yellow')

    # Start Event
    root.mainloop()
