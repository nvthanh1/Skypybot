import Skype4Py
import config as gbconfig
import json
from common import get_project_path

# Get Skype class instance
skype = Skype4Py.Skype()

# Establish the connection from the Skype object to the Skype ddclient.
skype.Attach()

# Get all contact from object. This function might not be used in this case

def get_all_contacts():

    print 'Your contacts list:'
    for user in skype.Friends:
        yield user.FullName

# Get key value in the contact list.This function might not be used in this case

def get_key_in_list_contact():

    for i in range(len(LIST_CONTACT)):
        for k, v in LIST_CONTACT[i].iteritems():
            yield k


def get_file():
    returndata = {}
    try:
        root_path = get_project_path()
        # print root_path
        file_path = "%s/%s" % (root_path, gbconfig.FILE_CONTACT)
        filename = open(file_path, 'r')
        returndata = json.loads(filename.read())
        filename.close()
    except Exception as e:
        print 'What the fuck? I could not load your file:', gbconfig.FILE_CONTACT
    return returndata



def main_function():
    get_file()

for contact,message in get_file().iteritems():
    skype.SendMessage(contact,message)
    print "Message has been sent"

if __name__ == "__main__":
    main_function()

