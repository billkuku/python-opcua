if __name__ == "__main__":
    inputfile = open("StatusCode.csv")
    outputfile = open("../opcua/status_code.py", "w")
    outputfile.write("#AUTOGENERATED!!!\n")
    outputfile.write("\n")
    #outputfile.write("from enum import Enum\n")
    outputfile.write("\n")


    outputfile.write("def get_name_and_doc(val):\n")
    outputfile.write("    if val == 0:\n")
    outputfile.write("        return 'Good', 'Good'\n")
    for line in inputfile:
        name, val, doc = line.split(",", maxsplit=2)
        doc = doc.strip()
        doc = doc.replace("'", '"')
        outputfile.write("    elif val == {}:\n".format(val))
        outputfile.write("        return '{}', '{}'\n".format(name, doc))
    outputfile.write("    else:\n".format(val))
    outputfile.write("        raise Exception('Unknown StatusCode value: {}'.format(val))")


    '''
    outputfile.write("class StatusCode(Enum):\n")
    outputfile.write("    Good = 0\n")
    for line in inputfile:
        name, val, doc = line.split(",", maxsplit=2)
        doc = doc.strip()
        outputfile.write("    {} = {}\n".format(name, val))

    outputfile.write("""
    def __new__(self, value=0):
        Enum.__new__(self, value)

    def to_binary(self):
        return struct.pack("!I", self.value)

    @staticmethod 
    def from_binary(data):
        val = struct.unpack("!I", data.read(4))[0]
        sc = StatusCode(val)
        return sc

    def check(self):
        if self.value.name != "Good":
            raise Exception(self.name)
    """)


    #outputfile.write("\n")
    #outputfile.write("\n")
    #outputfile.write("def CheckStatusCode(statuscode):\n")
    #outputfile.write("    if statuscode.data == {}\n")

'''
