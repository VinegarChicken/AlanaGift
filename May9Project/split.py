import xml.etree.ElementTree as ET
import datetime
root = ET.parse('Alana.xml').getroot()
split = ET.Element("media")
currentDate = datetime.date(2023, 5, 9)
for item in root.iter('mms'):
    ms = item.get('date')
    dt = datetime.datetime.fromtimestamp(int(ms)/1000.0)
    if dt.date() != currentDate:
        ET.ElementTree(split).write("split_"+str(currentDate.month)+"."+str(currentDate.day)+".xml")
        split = ET.Element("media")
        currentDate = dt.date()
    split.append(item)
    if ms == '1685918166000':
        ET.ElementTree(split).write("split_"+str(currentDate.month)+"."+str(currentDate.day)+".xml")
