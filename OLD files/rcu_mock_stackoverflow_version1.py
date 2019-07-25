import xml.etree.ElementTree as ET

with open('ILR_mock_data.xml', encoding='latin-1') as f:
  tree = ET.parse(f)
  root = tree.getroot()

  for elem in root.getiterator():
    try:
      elem.text = elem.text.replace('FEATURE NAME', 'THIS WORKED')
      elem.text = elem.text.replace('FEATURE NUMBER', '123456')
    except AttributeError:
      pass

tree.write('output.xml', encoding='latin-1')
