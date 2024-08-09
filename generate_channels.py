import xml.etree.ElementTree as ET
import os

def filter_channels(input_file, output_file):
    tree = ET.parse(input_file)
    root = tree.getroot()
    
    filtered_root = ET.Element(root.tag)
    
    for channel in root.findall('channel'):
        xmltv_id = channel.get('xmltv_id')
        
        if xmltv_id:
            filtered_root.append(channel)
    
    filtered_tree = ET.ElementTree(filtered_root)
    filtered_tree.write(output_file, encoding='utf-8', xml_declaration=True)

input_file = 'sites/tvpassport.com/tvpassport.com.channels.xml'
output_file = 'updated_channels.xml'

filter_channels(input_file, output_file)
