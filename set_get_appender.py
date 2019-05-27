import sys

file = open(sys.argv[1], "a")
var_name = sys.argv[2]
if file.writable():
    file.write("\n    @property")
    file.write("\n    def {0:s}(self):".format(var_name))
    file.write("\n        return self._{0:s}\n".format(var_name))
    file.write("\n    @{0:s}.setter".format(var_name))
    file.write("\n    def {0:s}(self, {0:s}):".format(var_name))
    file.write("\n        self._{0:s} = {0:s}\n".format(var_name))
    file.close()
