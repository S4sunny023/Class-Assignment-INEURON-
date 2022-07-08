import logging
logging.basicConfig(filename="tuple.log", level=logging.DEBUG, format=("%(levelname)s %(asctime)s %(message)s"))

class Tuple_t:
    def __init__(self,tup):
        logging.info("constructer for tuple is callled")
        self.tup = tup

    def extract_tup(self):
        logging.info("extracting tuple from collection")
        try:
            for i in self.tup:
                if type(i)== tuple:
                    logging.info(i)
        except Exception as e:
            logging.error(e)
