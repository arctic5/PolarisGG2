import uuid


def parseUuid(string, buffer):
    uuidString = string.lower()
    if (len(uuidString) != 32):
        print "Invalid UUID"
        return 0
    else:
        posValueString = "0123456789abcdef"

        for i in range(0, 16):
            currentNibble = uuidString[i*2+1]
            if (posValueString.find(currentNibble) == 0):
                print "Invalid Uuid:" + string
                return -1
            numericByte = (posValueString.find(currentNibble) + 1) * 16

            currentNibble = uuidString[i*2+2]
            if (posValueString.find(currentNibble) == 0):
                print "Invalid Uuid:" + string
                return -1
            numericByte += (posValueString.find(currentNibble) - 1)
            write_ubyte(buffer, numericByte)