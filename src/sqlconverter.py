import os


class Table():

    def __init__(self):
        self.column_values = []
        self.row_values = []
        self.import_file = ""

    def get_data_from_txt(self, filename, separator, quiet=False):

        self.import_file = filename

        if quiet == False:
            print("Getting data from: {0}".format(os.path.abspath(filename)))

        f = open(filename)
        content = f.read().splitlines()
        f.close()
    
        columns = content[0]
        rows = content[1:]

        self.column_values = self.__split_data__(columns, ';')

        for s in rows:
            self.row_values.append(self.__split_data__(s,separator))

        self.column_count = len(self.column_values)
        self.row_count = len(self.row_values)

        if quiet == False:
            print("Number of columns: {0}".format(self.column_count))

        for i, v in enumerate(self.row_values):
            if(len(v) != self.column_count):
                print("Warning: The number of fields in row nr {0} is diffrent from the number of columns".format(i+1))
        

        if quiet == False:
            print("Data imported successfully")

                  
    def summary(self):
        print()
        print("<---------------------------------------------------------------->\nTable summary:\n")
        print("Table imported from: {0}\n".format(os.path.abspath(self.import_file)))
        print("Number of columns: {0}\tNumber of records: {1}\n".format(self.column_count, self.row_count))
                
    def create_and_insert_sql(self, filename, types, tablename):

        if(len(types) != self.column_count):
            print("Number of columns differs from number of types")
            return -1

        sql = "CREATE TABLE {0} (".format(tablename)

        for i in range(len(self.column_values)):
            sql = sql + self.column_values[i] + " " + types[i] + ", "
        
        sql = sql[:len(sql) - 2] #delete ',' at the end
        sql = sql + ");\nINSERT INTO {0} (".format(tablename)
        
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

    def insert_sql(self, filename, types, tablename):
        sql = "INSERT INTO {0} (".format(tablename)
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


    def __split_data__(self, str, separator):
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