"""Skype Controller module"""
import Skype4Py
import config as gbconfig
import json
from common import get_project_path

# Get Skype class instance
SKYPE_OBJ = Skype4Py.Skype()

# Establish the connection from the Skype object to the Skype ddclient.
SKYPE_OBJ.Attach()


# Get all contact from object. This function might not be used in this case


def get_file():
    """Function to get file contains list of skype's contact"""
    returndata = {}
    try:
        root_path = get_project_path()
        # print root_path
        file_path = "%s/%s" % (root_path, gbconfig.FILE_CONTACT)
        filename = open(file_path, 'r')
        returndata = json.loads(filename.read())
        filename.close()
    except Exception as ex:
        print 'What the fuck? I could not load your file: %s - %s' % (gbconfig.FILE_CONTACT, ex)

    return returndata


def main_function():
    """Runable function"""
    get_file()

for contact, message in get_file().iteritems():
    SKYPE_OBJ.SendMessage(contact, message)
    print "Message has been sent"

if __name__ == "__main__":
    main_function()
