import pandas as pd
from rich.table import Table
from rich.console import Console
from visualization import plots


class DataManager:

    def __init__(self):
        self.original_df = None
        self.current_df = None
        self.saved_df = {}
        self.saved_calc = {}
        self.pl = plots.pyplot()


    def load(self, filepath, extr:None):
        name = 'default'
        head = 0

        if extr is not None :
            try : 
                head = int(extr)
            except :
                name = extr

        try :
            if filepath[0].endswith(".csv"): 
                self.original_df = pd.read_csv(filepath[0], header=head)
                if len(filepath) > 1 :
                    column = [i for i in filepath[1:]]
                    self.current_df = self.original_df[column].copy()
                else:
                    self.current_df = self.original_df.copy()

                print("File Read Success....")


            elif filepath[0].endswith((".xlsx", ".xls")):
                self.original_df = pd.read_excel(filepath[0], header=head)
                if len(filepath) > 1 :
                    column = [i for i in filepath[1:]]
                    self.current_df = self.original_df[column].copy()
                else:
                    self.current_df = self.original_df.copy()
                print("File Read Success....")

            else :
                print(f"there is no such file as {filepath[0]}")
            
        except :
            if len(filepath) == 0 :
                print("Filename cannot be blank")
            else :
                print(f"there is no such file as{filepath[0]}")
    

    def select(self, col, flg:str=''):
        if len(flg) > 0 :
            if flg == '-e' :
                temp_df = self.original_df
                self.current_df = temp_df.drop(columns=col).copy()
        else :
            self.current_df = (
                self.original_df[col].copy()
            )

    def rem(self, args, flg:str=''):
        if len(flg) == 0 or len(args) != 3: 
            print("Please Specify the data type using : -i for int, -s for str and only 3 arguments are acceptable")
            return False
        else :
            if len(flg[0]) == 2:
                if flg[0] == '-i' :
                    comp = int(args[2])
                elif flg[0] == '-s' :
                    comp = args[2]
                else :
                    print("Unknown flag...m")
                    return False
            else :
                print(f"Unknown flag {flg[0]} ....")
                return False

        if len(args) == 3 :
            if args[1] == '!=' :
                try :
                    self.current_df = self.current_df[self.current_df[args[0]] != comp]
                except :
                    print("Something went wrong.., make sure the value and the Column name is correct")
                    return False
                
            elif args[1] == '>' :
                try :
                    self.current_df = self.current_df[self.current_df[args[0]] > comp]
                except :
                    print("Something went wrong.., make sure the value and the Column name is correct")
                    return False               

            elif args[1] == '>=' :
                try :
                    self.current_df = self.current_df[self.current_df[args[0]] >= comp]
                except :
                    print("Something went wrong.., make sure the value and the Column name is correct")
                    return False

            elif args[1] == '<' :
                try :
                    self.current_df = self.current_df[self.current_df[args[0]] < comp]
                except :
                    print("Something went wrong.., make sure the value and the Column name is correct")
                    return False

            elif args[1] == '<=' :
                try :
                    self.current_df = self.current_df[self.current_df[args[0]] <= comp]
                except :
                    print("Something went wrong.., make sure the value and the Column name is correct")
                    return False
            elif args[1] == '=' or args[1] == "==" :
                try :
                    self.current_df = self.current_df[self.current_df[args[0]] == comp]
                except :
                    print("Something went wrong.., make sure the value and the Column name is correct")
                    return False
            else :
                print(f"Unknown comparator symbol {args[1]}...")
                return False
        else :
            print(f"Expected 3 arguments but {len(args)} were given")
            return False


    def delete_col(self, col, flg:str=''):
        if len(flg) > 0 :
            if flg == '-e' :
                self.current_df = self.current_df[col].copy()
            else :
                print(f"Could not find {flg} in command")

        else:
            self.current_df =  self.current_df.drop(columns= col)

    def reset(self):
        self.current_df = self.original_df.copy()


    def show(self, name : str ="Default", flg:str=''):
        #Show saved
        if len(flg) > 0 :
            if len(self.saved_df) == 0 :
                print("There is 0 saved dataframe")
                return True
            
            if flg == '-s' :
                print("Saved df : ")
                for df in self.saved_df.keys() :
                    print(df)

                print(f"Currrently there are {len(self.saved_df)} saved dataframe")
                return True
            else :
                print(f"Invalid flag {flg}... do help to look at commands")
                return True    

        #Show df
        console = Console()
        table = Table(title=name, show_lines=True)
        try :
            for col in self.current_df.columns :
                table.add_column(str(col), style='cyan', no_wrap=True)

            for row in self.current_df.itertuples(index=False) :
                table.add_row(*[str(item) for item in row])


            console.print(table)
        except :
            print("Something went wrong, No Data Frame Selected")

    def calc(self, args, flg:str=''):
        if len(flg) == 0 :
            print("Please specify what do you want to calculate by adding : -(command)")
        else :
            if flg == '-m' :
                try :
                    avg = self.current_df[args[0]].mean()
                    print(f'Average value of {args[0]} is {avg:.2f}')
                except :
                    print("Make sure the name of the column is correct or the val is in integer or float")

    def save(self, args, flg:str=''):
        name = str(args[0])
        if not self.current_df.empty :
            self.saved_df[name] = self.current_df.copy()
            print(f"Current dataframe saved as '{args[0]}'")
            print(self.saved_df)
        else :
            print("No dataframe selected")
    
    def switch(self, args, flg:str=''):
        if str(args[0]) in self.saved_df :
            self.current_df = self.saved_df[str(args[0])]
        else :
            print(f"Could not find {args[0]} try show -s to see saved df")

    def des(self, args, flg:str=''):
        try :
            print(self.current_df.describe().round(2))
        except :
            print("No Data Frame selected")    

    def info(self, args, flg:str=''):
        try :
            self.current_df.info()
        except :
            print("No Data Frame selected...")

    def bar(self, args, flg:str=''):
        self.pl.bar(self.current_df, args)

    def input_test(self, args):
        print(args)

            

 
        

