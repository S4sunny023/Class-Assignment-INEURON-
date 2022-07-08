import logging
logging.basicConfig(filename="list.log", level=logging.DEBUG, format=("%(levelname)s %(asctime)s %(message)s"))

class List_l:
    logging.info("we are working for list class")

    def __init__(self,l_list):
        logging.info("list constructer is called")
        self.l_list = l_list

    def extract_list(self,l_list):
         try:
             logging.info("extracting the list")
             for i in l_list:
                 if type(i) == list:
                     return logging.info(i)
         except Exception as e:
             logging.error(e)

    def reverse_list(self,l_list):
        try:
            logging.info("we wre reversing the list")
            return self.l_list[::-1]
        except Exception as e:
            logging.error(e)

    def extract_odd(self,l_list):
        try:
            logging.info("extracting odd numbers from list")
            for i in l_list:
                if type(i)== list:
                    for j in i:
                        if type(k)==int and (k%2 != 0):
                            return logging.info(k)
        except Exception as e:
            logging.error(e)

    def list234access(self, l_list):
        try:
            logging.info("accessing 234 from the list")
            return  self.l_list[5][0]
        except Exception as e:
            logging.error(e)

    def list456acess(self,l_list):
        try:
            logging.info("accessing 456 from the list")
            return self.l_list[5][1]
        except Exception as e:
            logging.error(e)

    def extract_listt(self, l_list):
        try:
            logging.info("extracting list1 elements")
            logging.info(self.l_list[5])
            logging.info("extracting list2 elementa")
            logging.info(self.l_list[6])
            logging.info("extracting list from dict")
            logging.info(self.l_list[8][234])
            




