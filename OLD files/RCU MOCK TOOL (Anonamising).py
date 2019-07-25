import os 
from xml.etree import ElementTree as et 

base_path  = os.path.dirname(os.path.realpath(__file__))

xml_file = os.path.join(base_path, "ILR_mock_data.xml") 

tree = et.parse(xml_file) 

# root = tree.getroot()

# for child in root:
#     print(child.tag, child.attrib)

#for child in root:
#    for element in child:
#        print(element.tag, ":", element.text)


for element in tree.findall('.//Learner/DateOfBirth'):
    element.text = 'NULL'

tree.write(open('ILR_Aoned_output.xml', 'wb'))



print("YOU SHOULD SEE THIS") 
