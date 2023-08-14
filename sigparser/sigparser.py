"""
Signatures parser
"""
import types
import parser_modules

import json



class SignatureParser:
    """
    Parses text input to get information about a person
    """

    def __init__(self):

        """
        We collect all the modules we have in parser_modules
        which will extract the data from input
        The module name should start with "look_for_"
        """
        self.parser_modules = [parser_modules.__dict__.get(mod) for mod in dir(parser_modules)
                               if isinstance(parser_modules.__dict__.get(mod), types.ModuleType)
                                    and mod.startswith("look_for_")]

    def get_information(self, input):
        """
        returns the dictionary of parsed information
        """
        result = dict()

        # call the function "run" of each parsing module
        for module in self.parser_modules:
            result = module.run(input, result)

        return result
    

_SigParser = SignatureParser()
def parse_signature(input_text):
    """
    extracts the signature information using SignatureParser
    """
    return json.dumps(_SigParser.get_information(input_text))


sig_filename = input("Give path name:")
signature=None
try:
    signature = open(sig_filename, "r").read()
    print(parse_signature(signature))
except IOError:
        print("Cannot open {} for reading".format(sig_filename))



