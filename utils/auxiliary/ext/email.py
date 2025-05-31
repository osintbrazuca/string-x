import re
from core.basemodule import BaseModule

class AuxRegexEmail(BaseModule):
    """
    AuxRegexEmail is a module that extracts email addresses from a given text using regular expressions.

    Attributes:
        meta (dict): Metadata information about the module, including name, description, author, and type.
        options (dict): Options required for the module, including the data value and the email regex pattern.

    Methods:
        __init__(): Initializes the AuxRegexEmail module with metadata and options.
        run(): Executes the email extraction process using the provided data value and regex pattern.
    """
    def __init__(self):
        super().__init__()


        # Define informações de meta informalções do módulo
        self.meta.update({
            "name": "Extractor",
            "description": "Extrai emails do texto fornecedido",
            "author": "MrCl0wn",
            "type":""
        })

        # Define opções requeridas para este módulo
        self.options = {
            "data": str(),
            "regex_email": "(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\\x01-\\x08\\x0b\\x0c\\x0e-\\x1f\\x21\\x23-\\x5b\\x5d-\\x7f]|\\\\[\\x01-\\x09\\x0b\\x0c\\x0e-\\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\\x01-\\x08\\x0b\\x0c\\x0e-\\x1f\\x21-\\x5a\\x53-\\x7f]|\\\\[\\x01-\\x09\\x0b\\x0c\\x0e-\\x7f])+)\\])"
        }

    def run(self):
        if (target_value := self.options.get("data")) and (regex_email := self.options.get("regex_email")): 
            regex_email = re.compile(regex_email,re.IGNORECASE)
            if regex_result_list := set(re.findall(regex_email, target_value)):
                for email in regex_result_list:
                    self.set_result(email)
