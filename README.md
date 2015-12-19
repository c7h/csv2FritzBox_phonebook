csv2FritzBox_phonebook
======================

convert a csv-File (e. g. from Google Contacts) to a Fritz!Box Phonebook (xml)


# Example Usage

1. Export your [Google Contacts](https://contacts.google.com) (Format *Outlook CSV*) to `contacts.csv`
2. run `python csv2FritzBox_phonebook.py -i contacts.csv -o fritzbox_phonebook.xml`
3. open the ["*restore phonebook*" dialouge](http://fritz.box/fon_num/fonbook_restore.lua)
3. upload `fritzbox_phonebook.xml`

# Notes

tested with Fritz!Box 7312
