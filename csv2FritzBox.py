'''
Created on 19.04.2014

convert your Contacts to FritzBox-Phonebook xml


@author: Christoph Gerneth
'''

from csv import DictReader
import xml.etree.ElementTree as et


filename_in  = "/home/christoph/Downloads/contacts.csv"
filename_out = "/home/christoph/contacts_test.xml"

outlook_list = ["First Name",
                "Middle Name",
                "Last Name",
                "Title",
                "Suffix",
                "Initials",
                "Web Page",
                "Gender",
                "Birthday",
                "Anniversary",
                "Location",
                "Language",
                "Internet Free Busy",
                "Notes",
                "E-mail Address",
                "E-mail 2 Address",
                "E-mail 3 Address",
                "Primary Phone",
                "Home Phone",
                "Home Phone 2",
                "Mobile Phone",
                "Pager",
                "Home Fax",
                "Home Address",
                "Home Street",
                "Home Street 2",
                "Home Street 3",
                "Home Address PO Box",
                "Home City",
                "Home State",
                "Home Postal Code",
                "Home Country",
                "Spouse",
                "Children",
                "Manager's Name",
                "Assistant's Name",
                "Referred By",
                "Company Main Phone",
                "Business Phone",
                "Business Phone 2",
                "Business Fax",
                "Assistant's Phone",
                "Company",
                "Job Title",
                "Department",
                "Office Location",
                "Organizational ID Number",
                "Profession",
                "Account",
                "Business Address",
                "Business Street",
                "Business Street 2",
                "Business Street 3",
                "Business Address PO Box",
                "Business City",
                "Business State",
                "Business Postal Code",
                "Business Country",
                "Other Phone",
                "Other Fax",
                "Other Address",
                "Other Street",
                "Other Street 2",
                "Other Street 3",
                "Other Address PO Box",
                "Other City",
                "Other State",
                "Other Postal Code",
                "Other Country",
                "Callback",
                "Car Phone",
                "ISDN",
                "Radio Phone",
                "TTY/TDD Phone",
                "Telex",
                "User 1",
                "User 2",
                "User 3",
                "User 4",
                "Keywords",
                "Mileage",
                "Hobby",
                "Billing Information",
                "Directory Server",
                "Sensitivity",
                "Priority",
                "Private",
                "Categories"
                ]

trans_number = {"Home Phone": "home",
                "Mobile Phone": "mobile",
                "Business Phone": "work",
                "Home Fax": "fax_work",
                }


with open(filename_in, "rb") as f:
    #reader = DictReader(f, outlook_list)
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
        
        
    