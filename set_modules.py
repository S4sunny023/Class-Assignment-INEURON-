import logging
logging.basicConfig(filename="set.log", level=logging.DEBUG, format=("%(levelname)s %(asctime)s %(message)s"))

class Set_s:
    def __init__(self,set1):
        logging.info("set constructer is formed")
        self.set1 = set1

    def list2set(self):
        try:
            logging.info("filter out dublicate elements in a list")
            return set(self.set1)
        except Exception as e:
            logging.error(e)

class Genric:
    def __init__(self, lst1):
        logging.info("basic constructer is formed")
        self.lst1 = lst1

    def extract_numeric(self):
        try:
            logging.info("extracting numeric values")
            for i in self.lst1:
                if type(i)== dict:
                    for j in i.keys():
                        if type(j)== int:
                            logging.info(j)
                        if type(i[j])==int:
                            logging.info(i[j])
                if type(i)==list or type(i)==set or type(i)==tuple:
                    for k in i:
                        if type(k)==int:
                            logging.info(k)
                if type(i)==int:
                    logging.info(i)
        except Exception as e :
            logging.error(e)

    def sumofnumeric(self):
        try:
            logging.info("sum of numeric values in the collectiom")
            sum = 0
            for i in self.lst1:
                if type(i)== dict:
                    for j in i.keys():
                        if type(j)==int:
                            sum = sum + j
                        if type(i[j])== int:
                            sum = sum+i[j]
                if type(i)==list or type(i)== tuple or type(i)== set:
                    for k in i:
                        if type(k)==int:
                            sum= sum + k
            return sum
        except Exception as e :
            logging.error(e)

    def extract_ineuron(self):
        try:
            logging.info("extracting string ineuron from collection")
            for i in self.lst1:
                if type(i) == dict:
                    for j in i.keys():
                        if type(j) == str:
                            if j == "ineuron"
                                logging.info(j)
                        if type(i[j]) == str:
                            if i[j]=="ineuron"
                                logging.info(i[j])
                if type(i) == list or type(i) == set or type(i) == tuple:
                    for k in i:
                        if type(k) == str:
                            if k == "ineuron"
                                logging.info(k)
                if type(i) == str:
                    if i == "ineuron"
                        logging.info(i)
        except Exception as e:
            logging.error(e)

    def no_of_occurance(self):
        try:
            logging.info("counting no. of occurance in the collection")
            l = []
            for i in self.lst1:
                if type(i)== dict:
                    for j in i.keys():
                        if type(j)==str or type(j)==int:
                            l.append(j)
                        if type(i[j])== str or type(i[j])== int:
                            l.append(i[j])
                if type(i)== list or type(i)==tuple or type(i)== list:
                    for k in i:
                        if type(k)==int or type(k)==str:
                            l.append(k)
                elif type(i)==str or type(i)==int:
                    l.append(i)
            for i in set(l):
                logging.info(l.count(i))
        except Exception as e:
            logging.error(e)

    def extract_alphanum(self):
        try:
            logging.info("extracting alpha num")
            l = []
            for i in self.lst1:
                if type(i)== dict:
                    for j in i.keys();
                    if type(j)==str:
                        if j.isalnum():
                            l.append(j)
                    if type(i[j])== str:
                        if i[j].isalnum:
                            l.append(i[j])
                if type(i)==list or type(i)==tuple or type(i)==set:
                    for k in i:
                        if type(k)==str:
                            if k.isalnum():
                                l.append(k)
                if type(i)==str:
                    if i.isalnum:
                        l.append(i)
            logging.info(l)
        except Exception as e:
            logging.error(e)



    def mul_of_num(self):
        try:
            logging.info("multiplying all the integer elements")
            mul = 1
            for i in self.lst1:
                if type(i)==dict:
                 for j in i.keys():
                     if type(j)== int:
                         mul = mul*j
                     if type(i[j])==int:
                         mul = mul*i[j
                 if type(i)== list or type(i)== set or type(i)== tuple:
                     for k in i :
                         if type(k)==int:
                             mul = mul*k
                 elif type(i)= int:
                     mul = mul* i
             logging.info(mul)
        except Exception as e:
            logging.error(e)









