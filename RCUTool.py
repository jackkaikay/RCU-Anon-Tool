import xml.etree.ElementTree as ET
from tkinter import *
from tkinter.filedialog import askopenfilename
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
pngimg = resource_path("Dependencies\Banner.png")
pngimg2 = resource_path("Dependencies\Banner2.png")

def callback(url):
    webbrowser.open_new(url)

def closeProg():
    root.destroy()

def OpenFile():
    Button1.config(state='disabled', relief=SUNKEN, text='      Selecting ILR File...      ', bg='light yellow')
    statusBar.config(text='STATUS: Selecting ILR File...', fg='red')
    filename = depbandtxt
    depDepend = pd.read_csv(filename)
    depDepend.set_index('Postcode', inplace=True)

    name = askopenfilename(filetypes=(("XML File", "*.XML"), ("All Files", "*.*")),
                           title="Choose the ILR file.")
    if name == '':
        tkinter.messagebox.showinfo("Failed Anonymisation!",
                                    "Please Select a Valid ILR File")
        restart_program()
    else:
        filelocation = os.path.dirname(name)
        print(filelocation)
        nameFile = os.path.basename(name)
        if name == '':
            statusBar.config(text='Status: Please Load ILR File', fg='Black')
            tkinter.messagebox.showinfo("Failed Anonymisation!",
                                        "Please Select a Valid ILR File")
            restart_program()

        else:
            result = tkinter.messagebox.askquestion('Would you like to continue?', 'Anonymising: ' + nameFile + '\n \nOutput Location:  ' + filelocation + '\n \nWould you like to continue?')
            if result == 'yes':




                UKPRN_Name = nameFile[4:12]

                try:
                    statusBar.config(text='STATUS: Anonymising ILR File... Please Wait', fg='red')
                    ET.register_namespace("", 'ESFA/ILR/2019-20')
                    dom = ET.parse(name)
                    root = dom.getroot()

                    ####################
                    ##Anonymising data##
                    ####################
                    if root.find('{ESFA/ILR/2019-20}Learner') == None:
                        tkinter.messagebox.showinfo("Failed Anonymisation!",
                                                    "Incorrect ILR year detected.\nThis tool is compatible with the 2019/20 ILR only. \nFor any other year please contact RCU Ltd directly")
                        restart_program()
                    else:


                        # Full Name#
                        Button1.config(state='disabled', relief=SUNKEN, text='      Anonymising  1/13      ', bg='light yellow')
                        for ns in root.findall('{ESFA/ILR/2019-20}Learner'):
                            name = ns.find('{ESFA/ILR/2019-20}FamilyName')
                            try:
                                name.text = 'NULL'
                            except:
                                print('No FamilyName Found')
                        Button1.config(state='disabled', relief=SUNKEN, text='      Anonymising  2/13      ', bg='light yellow')
                        for ns in root.findall('{ESFA/ILR/2019-20}Learner'):
                            name = ns.find('{ESFA/ILR/2019-20}GivenNames')
                            try:
                                name.text = 'NULL'
                            except:
                                print('No GivenNames Found')

                        # Adress Lines#
                        Button1.config(state='disabled', relief=SUNKEN, text='      Anonymising  3/13      ', bg='light yellow')
                        for ns in root.findall('{ESFA/ILR/2019-20}Learner'):
                            name = ns.find('{ESFA/ILR/2019-20}AddLine1')
                            try:
                                name.text = 'NULL'
                            except:
                                print('No AddLine1 Found')

                        Button1.config(state='disabled', relief=SUNKEN, text='      Anonymising  4/13      ', bg='light yellow')

                        for ns in root.findall('{ESFA/ILR/2019-20}Learner'):
                            name = ns.find('{ESFA/ILR/2019-20}AddLine2')
                            try:
                                name.text = 'NULL'
                            except:
                                print('No AddLine2 Found')

                        Button1.config(state='disabled', relief=SUNKEN, text='      Anonymising  5/13      ', bg='light yellow')
                        for ns in root.findall('{ESFA/ILR/2019-20}Learner'):
                            name = ns.find('{ESFA/ILR/2019-20}AddLine3')
                            try:
                                name.text = 'NULL'
                            except:
                                print('No AddLine3 Found')
                        Button1.config(state='disabled', relief=SUNKEN, text='      Anonymising  6/13      ', bg='light yellow')
                        for ns in root.findall('{ESFA/ILR/2019-20}Learner'):
                            name = ns.find('{ESFA/ILR/2019-20}AddLine4')
                            try:
                                name.text = 'NULL'
                            except:
                                print('No AddLine4 Found')

                        # Telephone number#
                        Button1.config(state='disabled', relief=SUNKEN, text='      Anonymising  7/13      ', bg='light yellow')
                        for ns in root.findall('{ESFA/ILR/2019-20}Learner'):
                            name = ns.find('{ESFA/ILR/2019-20}TelNo')
                            try:
                                name.text = 'NULL'
                            except:
                                print('No TelNo Found')

                        # Email Address#
                        Button1.config(state='disabled', relief=SUNKEN, text='      Anonymising  8/13      ', bg='light yellow')
                        for ns in root.findall('{ESFA/ILR/2019-20}Learner'):
                            name = ns.find('{ESFA/ILR/2019-20}Email')
                            try:
                                name.text = 'NULL'
                            except:
                                print('No Email Found')
                        # Unique Learner Numeber#
                        Button1.config(state='disabled', relief=SUNKEN, text='      Anonymising  9/13      ', bg='light yellow')
                        for ns in root.findall('{ESFA/ILR/2019-20}Learner'):
                            name = ns.find('{ESFA/ILR/2019-20}ULN')
                            try:
                                name.text = '99999999'
                            except:
                                print('No ULN Found')

                        # National Insurance Number#
                        Button1.config(state='disabled', relief=SUNKEN, text='      Anonymising  10/13      ', bg='light yellow')
                        for ns in root.findall('{ESFA/ILR/2019-20}Learner'):
                            name = ns.find('{ESFA/ILR/2019-20}NINumber')
                            try:
                                name.text = 'NULL'
                            except:
                                print('No NINumber Found')

                        Button1.config(state='disabled', relief=SUNKEN, text='      Anonymising  11/13      ', bg='light yellow')
                        for ns in root.findall('{ESFA/ILR/2019-20}Learner'):
                            name = ns.find('{ESFA/ILR/2019-20}UCASPERID')
                            try:
                                name.text = 'NULL'
                            except:
                                print('No UCASPERID Found ')

                        Button1.config(state='disabled', relief=SUNKEN, text='      Anonymising  12/13      ', bg='light yellow')
                        for ns in root.findall('{ESFA/ILR/2019-20}Learner'):
                            name = ns.find('{ESFA/ILR/2019-20}UCASAPPID')
                            try:
                                name.text = 'NULL'
                            except:
                                print('No UCASAPPID ID Fond')

                        Button1.config(state='disabled', relief=SUNKEN, text='      Anonymising  13/13      ', bg='light yellow')
                        for ns in root.findall('{ESFA/ILR/2019-20}Learner'):
                            name = ns.find('{ESFA/ILR/2019-20}SSN')
                            try:
                                name.text = 'NULL'
                            except:
                                print('No SSN Found')


                        # Find and Add three tags for
                        # Deprivation Band
                        # Local Authority District
                        # Local Authoirty Ward / ADD IF BOX TICKED

                        if 0 == 0:
                            LRN_List = {}
                            LRN_Num = 0
                            for ns in root.findall('{ESFA/ILR/2019-20}Learner'):
                                ns = ns.find('{ESFA/ILR/2019-20}LearnRefNumber')
                                ns = ns.text
                                print(ns)
                                LRN_List[LRN_Num] = ns
                                LRN_List[LRN_Num] = ns
                                LRN_Num += 1

                            PCD_List = {}
                            PCD_Num = 0
                            for ns in root.findall('{ESFA/ILR/2019-20}Learner'):
                                ns = ns.find('{ESFA/ILR/2019-20}Postcode')
                                ns = ns.text
                                print(ns)
                                PCD_List[PCD_Num] = ns
                                PCD_List[PCD_Num] = ns
                                PCD_Num += 1
                            Button1.config(state='disabled', relief=SUNKEN, text='   Deprivation Band Creation   ', bg='light yellow')
                            print(LRN_List)
                            print(PCD_List)
                            statusBar.config(text='STATUS: Creating Deprivation Band CSV Output...', fg='red')
                            with open(filelocation + '\RCU_' + nameFile[:-4] + '.csv', 'w', newline='') as csvfile:
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
                        Button1.config(state='disabled', relief=SUNKEN, text='      Anonymising  1/2     ', bg='light yellow')
                        for ns in root.findall('{ESFA/ILR/2019-20}Learner'):
                            name = ns.find('{ESFA/ILR/2019-20}Postcode')
                            try:
                                name2 = name.text
                                sep = ' '
                                nameSplit = name2.split(sep, 1)[0]
                                name.text = nameSplit
                            except:
                                print('No Postcode Found')

                        Button1.config(state='disabled', relief=SUNKEN, text='     Anonymising  2/2...    ', bg='light yellow')
                        for ns in root.findall('{ESFA/ILR/2019-20}Learner'):
                            name = ns.find('{ESFA/ILR/2019-20}PostcodePrior')
                            try:
                                name2 = name.text
                                sep = ' '
                                nameSplit = name2.split(sep, 1)[0]
                                name.text = nameSplit
                            except:
                                print('No Postcode Found')

                        Button1.config(state='disabled', relief=SUNKEN, text='     Outputting Files...     ', bg='light yellow')
                        statusBar.config(text='STATUS: Outputting Files to Selected Location... Please Wait', fg='red')
                        for ns in root.findall('{ESFA/ILR/2019-20}Learner'):
                            for xs in ns.findall('{ESFA/ILR/2019-20}LearningDelivery'):
                                name = xs.find('{ESFA/ILR/2019-20}LSDPostcode')
                                try:
                                    name2 = name.text
                                    sep = ' '
                                    nameSplit = name2.split(sep, 1)[0]
                                    print(nameSplit)
                                    name.text = nameSplit
                                except:
                                    print('No Postcode Found')

                        # Output And Save Modified FilePrior Postcodes

                        print(str(nameFile))
                        dom.write(filelocation + '\RCU_' + nameFile + '.anon', encoding='utf-8', xml_declaration=True)
                        zipObj = ZipFile(filelocation + '\RCU_' + nameFile[:-4] + '.zip', 'w')
                        zipObj.write(filelocation + '\RCU_' + nameFile + '.anon', basename('RCU_' + nameFile + '.anon'))
                        zipObj.write(filelocation + '\RCU_' + nameFile[:-4] + '.csv', 'RCU_' + nameFile[:-4] + '.csv')
                        zipObj.close()
                        tkinter.messagebox.showinfo("Finished Anonymisation!",
                                                    "Finished Anonymisation! Thank you. \nFile explorer will automatically open in your selected output location.")
                        path = os.path.realpath(filelocation)
                        os.startfile(path)

                        #os.startfile()
                        statusBar.config(text='Status: File Anonymised... Thank you for using the RCU Anonymiser tool', fg='Black')
                        restart_program()
                except:
                        tkinter.messagebox.showinfo("Failed Anonymisation!",
                                                    "Anonymisation Failed! Please retry or contact RCU \n "
                                                    "Tel: 01772 734855  |  Email: Mides@rcu.co.uk")
                        restart_program()
            else:
                restart_program()

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

if __name__ == '__main__':
    root = Tk()
    root.configure(background='black')
    root.iconbitmap(icoimg)
    root.title("RCU ILR Anonymiser - V1.00 2019/20")
    root.geometry("600x400")
    root.resizable(0, 0)

    img = Image.open(pngimg)
    rculogo = ImageTk.PhotoImage(img)
    mainimg = Label(root, image=rculogo, borderwidth=0, highlightthickness=0)

    # Top Frame
    topFrame = Frame(root)
    topFrame.pack(side=TOP)

    # Bottom Framepyinst
    bottomFrame = Frame(root)
    bottomFrame.pack(side=BOTTOM)

    # Widgits (Buttons)
    Process = threading.Thread(target=OpenFile)
    Button1 = Button(root, text="           Select ILR File          ", fg="Black", bg="yellow",
                     command=Process.start, padx=1, pady=1)
    statusBar = Label(root, text="Status: Please Load ILR File", bd=1, relief=SUNKEN, anchor=W, fg='black')
    spaceLabel = Label(root, text="",bg='black', fg='white')
    spaceSaver = Label(root, text="", bd=1, bg='black', fg='white')
    spaceSaver2 = Label(root, text="", bd=1, bg='black', fg='white')
    websiteLabel = Label(root, text="About ILR \n Anonymiser", fg="Yellow", bg='black', cursor="hand2")
    versionNumber = Label(root, text="V1.00",  fg="Yellow", bg='black', font=('', 8))
    websiteLabel.bind("<Button-1>", lambda e: callback("https://www.rcu.co.uk/anonymiser/"))
    afterButton1 = Button(root, text="            Close           ", fg="Black", bg="yellow",
                     command=closeProg, padx=1, pady=1)
    afterButton2 = Button(root, text="          Restart           ", command=restart_program, padx=1, pady=1,
                     bg='yellow')

    #Packing Frames
    mainimg.pack()
    spaceSaver.pack()
    versionNumber.place(x=0, y=360)
    Button1.pack()
    spaceSaver2.pack()
    websiteLabel.place(x=525,y=342.5)
    statusBar.pack(side=BOTTOM, fill=X)


    # Start Event
    root.mainloop()
