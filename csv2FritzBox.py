'''
Created on 19.04.2014

convert your Contacts to FritzBox-Phonebook xml


@author: Christoph Gerneth
'''

from csv import DictReader
import xml.etree.ElementTree as et


filename_in  = "/home/christoph/Downloads/contacts.csv"
filename_out = "/home/christoph/contacts_test.xml"


trans_number = {"Home Phone": "home",
                "Mobile Phone": "mobile",
                "Business Phone": "work",
                "Home Fax": "fax_work",
                }


with open(filename_in, "rb") as f:
    reader = DictReader(f)
    phonebooks = et.Element("phonebooks")
    phonebook = et.SubElement(phonebooks, tag="phonebook")
    for cr in reader:
        contact = et.SubElement(phonebook, "contact")
        
        category = et.SubElement(contact, "category")
        category.text = "0"
        
        person = et.SubElement(contact, "person")
        realName = et.SubElement(person, "realName")
        realName.text = "%s %s" % (cr["First Name"], cr["Last Name"])
        
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
    et.dump(phonebooks)
        
        
    