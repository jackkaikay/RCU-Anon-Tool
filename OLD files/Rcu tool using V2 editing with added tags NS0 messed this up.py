#Importing BS4# 
from bs4 import BeautifulSoup

#Importing ElementTree# 





#Opening Origional XML File, Setting soup to BS# 
with open("ILR_mock_data.xml", "r") as infile:
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

###################################  
## Output And Save Modified File ##
###################################

with open("SEND_ME_TO_RCU.xml", "w") as outfile:
    outfile.write(soup.prettify())


#Introducing Element tree for adding tags#
root = ET.parse("SEND_ME_TO_RCU.xml").getroot()
c = ET.Element("c")
c.text = "JACKTEST"

root.insert(3, c)
ET.dump(root)

tree = ET.ElementTree(root)
#Replace output with Origional one above "SEND_ME_TO_RCU.xml" When done testing# 
tree.write("TESTJACKJACK.xml")
