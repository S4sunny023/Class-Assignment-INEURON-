import logging
logging.basicConfig(filename="dict.log", level=logging.DEBUG, format=("%(levelname)s %(asctime)s %(message)s"))

class Dict_d:

    def __init__(self,dic1):
        logging.info("dict constructer is called")
        self.dic1 = dic1


    def extract_dict(self,dic1):

        try:
            logging.info("extracting dict elements")
            for i in dic1:
                if type(i)== dict:
                    logging.info(i)
        except Exception as e:
            logging.error(e)

    def no_of_keys(self,dict1):
        try:
            logging.info("extracting no. of keys from dict")
            for i in dict1:
                if type(i)== dict:
                    for j in i.keys():
                        keycount = keycount+1
            return keycount
        except Exception as e:
            logging.error(e)

    def extract_sudh_dict(self):
        try:
            logging.info("extracting sudh keyword")
            return self.dic1[5]["key1"]
        except Exception as e:
            logging.error(e)

    def extractvalues(self,dict1):
        try:
            for i in dict1:
                if type(i)== dict:
                    return dict1.values()
        except Exception as  e:
            logging.error(e)


