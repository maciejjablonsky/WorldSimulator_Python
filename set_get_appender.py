import sys

file = open(sys.argv[1], "a")
var_name = sys.argv[2]
if file.writable():
    file.write("\n\t@property")
    file.write("\n\tdef {0:s}(self):".format(var_name))
    file.write("\n\t\treturn self._{0:s}\n".format(var_name))
    file.write("\n\t@{0:s}.setter".format(var_name))
    file.write("\n\tdef {0:s}(self, {0:s}):".format(var_name))
    file.write("\n\t\tself._{0:s} = {0:s}\n".format(var_name))
    file.close()
