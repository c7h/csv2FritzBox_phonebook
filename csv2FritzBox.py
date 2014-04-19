'''
Created on 19.04.2014



@author: Christoph Gerneth
'''

from csv import DictReader
import xml.etree.ElementTree as et
import time


## optionsparser
from optparse import OptionParser
op = OptionParser(usage="convert your Contacts to FritzBox-Phonebook xml")
op.add_option("-i", dest="filename_in", help="input file (Outlook CSV format)")
op.add_option("-o", dest="filename_out", help="output file (xml)")
(options, args) = op.parse_args()

if options.filename_in and options.filename_out:
    filename_in = options.filename_in
    filename_out = options.filename_out
else:
    op.error("i need input AND output (-h is for help)")



trans_number = {"Home Phone": "home",
                "Mobile Phone": "mobile",
                "Business Phone": "work",
                "Home Fax": "fax_work",
                }



with open(filename_in, "rb") as f:
    reader = DictReader(f)
    phonebooks = et.Element("phonebooks")
    phonebook = et.SubElement(phonebooks, tag="phonebook")
    contact_count = 1
    for cr in reader:
        contact = et.SubElement(phonebook, "contact")
        
        category = et.SubElement(contact, "category")
        category.text = "0"
        
        person = et.SubElement(contact, "person")
        realName = et.SubElement(person, "realName")
        realName.text = "%s %s" % (cr["Last Name"], cr["First Name"])
        
        telephony = et.SubElement(contact, "telephony")
        number_counter = 0
        for key, value in trans_number.iteritems():
            if key in cr:
                if cr[key] != "":
                    phonenumber = et.SubElement(telephony, 
                                  "number", 
                                  {"id": str(number_counter),
                                   "prio": "0",
                                   "type": value,
                                   }
                                  )
                    phonenumber.text = cr[key]
                    number_counter += 1
        telephony.set("nid", str(number_counter+1))
        
        service = et.SubElement(contact, "services", {"nid": "1"})
        mail = et.SubElement(service, "email", {"classifier": "private", "id": "0"})
        mail.text = cr["E-mail Address"]
        
        et.SubElement(contact, "setup")
        
        mod_time = et.SubElement(contact, "mod_time")
        mod_time.text = str(int(time.time()))
        
        uid = et.SubElement(contact, "uniqueid")
        uid.text = str(contact_count)
        contact_count += 1
    elemTree = et.ElementTree(element=phonebooks)
    
    print "[parsed %i contacts]" % contact_count
    print "[writing to '%s']" % filename_out
    elemTree.write(filename_out)