import os
import xml.etree.ElementTree as etree


# users = '../Data/player/users.xml'

# # Get data from XML file
# xmlD = etree.parse(users)
# root = xmlD.getroot()
# password = root[0][1].text

x = ['1', '2', '3']
y = 0
while True:
    print(x[y])
    if len(x) - 1 == y:
        print('the range of x == y')
        break
    else:
        y += 1
