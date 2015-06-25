import xmltodict, json
from xml.dom import minidom
import sys
version = '0.1'

def ImageWrapperToJSON(input_file, output_file):

    #open XML document and get list of acqParam items
    xmldoc = minidom.parse(input_file)
    itemlist = xmldoc.getElementsByTagName('acqParam')
    
    acqparam_dict={}

    #for each acqparam element, get name and node value, store in acqparam_dict dictionary
    for s in itemlist:
        if (s.firstChild):
            #print(s.attributes['name'].value + ":" + s.firstChild.nodeValue)
            acqparam_dict[s.attributes['name'].value] = s.firstChild.nodeValue

    if bool(acqparam_dict):
        f = open(output_file, 'w')
        #dump JSON document of acqparam_dict dictionary
        f.write(json.dumps(acqparam_dict, sort_keys=False, indent=4))
        f.close()


