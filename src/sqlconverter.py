#@version 0.2.5 

import os

class Table():

    def __init__(self):
        self.column_values = []
        self.row_values = []
        self.import_file = ""
        self.column_count = 0
        self.row_count = 0
        self.types = dict()

    def get_data_from_txt(self, filename, separator, quiet=False):

        self.import_file = filename

        if quiet == False:
            print("Getting data from: {0}".format(os.path.abspath(filename)))

        f = open(filename)
        content = f.read().splitlines()
        f.close()
    
        columns = content[0]
        rows = content[1:]

        self.column_values = self.__split_data__(columns, separator)

        for s in rows:
            self.row_values.append(self.__split_data__(s,separator))

        self.column_count = len(self.column_values)
        self.row_count = len(self.row_values)

        if quiet == False:
            print("Number of columns: {0}".format(self.column_count))

        for i, v in enumerate(self.row_values):
            if(len(v) != self.column_count):
                print("Warning: Number of fields in row nr {0} ({1}) is diffrent from number of columns ({2})".format(i+1, len(v), self.column_count))
        
        for col in self.column_values:
            print("Insert type for %s" % col)
            inserted_type = input()
            self.types.update({col : inserted_type})

        print(self.types)

        if quiet == False:
            print("Data imported successfully from {0}".format(filename))

                  
    def summary(self):
        print()
        print("<-----------------------Table summary----------------------->\n\n")
        print("Table imported from: {0}\n".format(os.path.abspath(self.import_file)))
        print("Number of columns: {0}\tNumber of records: {1}\n".format(self.column_count, self.row_count))
        print("Columns:\n%s" % self.types)

    def insert_sql(self, filename, tablename,create_new_table = False, quiet=False):
        if create_new_table == True:
            sql = sql = "CREATE TABLE {0} (".format(tablename)

            for i in range(len(self.column_values)):
                sql = sql + self.column_values[i] + " " + self.types[self.column_values[i]] + ", "

            sql = sql[:len(sql) - 2] #delete ',' at the end
            sql = sql + ");\n"

        else:
            sql = ""

        sql += "INSERT INTO {0} (".format(tablename)
        for col in self.column_values:
            sql = sql + col + ", "
        
        sql = sql[:len(sql) - 2]
        sql = sql + ") VALUES "

        for row in self.row_values:
            str = "("

            for val in row:
                str = str +"\"" +val + "\"" ", "
            
            str = str[0:len(str) - 2]
            str = str + "), "
            sql = sql + str

        sql = sql[:len(sql) - 2]
        
        f = open(filename, "w")
        f.write(sql)

        if quiet==False:
            print("Data exported to {0}".format(filename))

    def __split_data__(self, str, separator): #transforms string "field1;field2,....fieldn" into list [field1, field2,....fieldn]
        arr = []
        b = 0
        e = str.find(separator, b)
        arr.append(str[b:e])

        while e >= 0:
            b = e
            e = str.find(separator , e+1)
            if e == -1:
                arr.append(str[b+1:len(str)])
                break
            arr.append(str[b+1:e])

        return arr