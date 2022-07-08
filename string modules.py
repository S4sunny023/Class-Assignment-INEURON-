import logging
logging.basicConfig(filename="string.log", level=logging.DEBUG,format="%(levelname)s %(asctime)s %(message)s")

class String_s:
    logging.info("we are in string class")

    def __init__(self, i_str):
        logging.info("string constructer is called")
        self.i_str = i_str
    def extract_data(self):
        try:
            logging.info("we are going to extract data with a gap of 3 places")
            return self.i_str[0:300:3]
        except Exception as e:
            logging.error(e)

    def reverse_str(self):
        try:
            logging.info("we are going to reverse the string")
            return  self.i_str[::-1]
        except Exception as e:
            logging.error(e)

    def split_str(self):
        try:
            logging.info("conversion of entire string in upper case")
            return self.i_str.upper().split(" ")
        except Exception as e:
            logging.error(e)

    def lower_str(self):
        try:
            logging.info("convert whole string in uppercase")
            return self.i_str.lower()
        except Exception as e :
            logging.error(e)

    def capitalize_str(self):
        try:
            logging.info("capitalizing the string")
            return self.i_str.capitalize()
        except Exception as e :
            logging.error(e)

    def check_alphanum(self, str):
        try:
           logging.info("trying to check is alphanum")
           return str.isalum()
        except Exception as e:
            logging.error(e)

    def expant_tab(self, str):
        try:
            logging.info("trying to expand data")
            return str.expandtabs()
        except Exception as e:
            logging.error(e)

    def strip_str(self, str):
        try:
            logging.info("we are going to strip the string")
            return  str.strip()
        except Exception as e :
            logging.error(e)

    def lstrip_str(self, str):
        try:
            logging.info("we are going to left strip the data")
            return str.lstrip()
        except Exception as e :
            logging.error(e)

    def rstrip_str(self, str):
        try:
            logging.info("we are going to right strip the string")
            return str.rstrip()
        except Exception as e :
             logging.error(e)

    def replac_str(self, line, str1, str2):
        try:
            logging.info("replacing string to another string")
            return line.replace(str1, str2)
        except Exception as e:
            logging.error(e)

    def center_str(self, str):
        try:
            logging.info("putting string in center")
            return  str.center()
        except Exception as e:
            logging.error(e)


