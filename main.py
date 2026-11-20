import cmd
from visualization import plots
from core import dataframe as df
from cli import parser as par
from cli import commands as flg

class LanternCLI(cmd.Cmd):

    intro = r"""    ─────────────────────────────────────
                 LANTERN
    ─────────────────────────────────────

    Data analysis environment
    Version 0.1.0  ·  Python

  Type 'help' to view available commands."""
    
    dataFrame = False
    saved_df = {}
    prompt = ">>"
    pl = plots.pyplot()

    df_name = "Default"

    #Read
    def do_read(self, arg):
        flags, arguments = par.Parser.parse_command(self, arg)

        if len(flags) > 0 :
            if len(flags) > 1 :
                print("arg 'start' only accept 1 flag at a time")
            else :
                if flags[0] == '-h' :
                    flg.read_flags[flags[0]]('read')
                else :            
                    extraArg = arguments.pop(0)
                    if flags[0] in flg.read_flags:
                        flg.read_flags[flags[0]](self, arguments, extraArg)
                
        else :
            df.DataManager.load(self,arguments, None)
            self.dataFrame = True
        
    #Show    
    def do_show(self, arg):
        flags, arguments = par.Parser.parse_command(self, arg)
        if len(flags) > 0 :
            if flags[0] in flg.show_flags :
                flg.show_flags[flags[0]](self, arguments, flags[0])
            else :
                print(f"Invalid flag {flags}")
        else :
            df.DataManager.show(self, arg)

    #Delete Column
    def do_delCol(self, arg):     
        flags, arguments = par.Parser.parse_command(self,arg)
        if len(flags) > 0 :
            if len(flags) > 1 :
                print("This command only accept 1 flag at a time")
            else :
                if flags[0] in flg.del_col_flags :
                    flg.del_col_flags[flags[0]](self, arguments, flags[0])
        else :
            df.DataManager.delete_col(self, arguments)

    #Reset DataFrame to first-time made df
    def do_reset(self, arg):
        df.DataManager.reset(self)
        print("Reset succesfull...")

    #Remove specific element 
    def do_rem(self, arg):
        flags, arguments = par.Parser.parse_command(self, arg)
        df.DataManager.rem(self, arguments, flags)


    #Select column
    def do_select(self, arg):
        flags, arguments = par.Parser.parse_command(self, arg)
        if len(flags) > 0 :
            if len(flags) > 1 :
                print("This command only accept 1 flag at a time")
            else :
                if flags[0] in flg.select_flags :
                    flg.select_flags[flags[0]](self, arguments, flags[0])            
                else :
                    print(f"could't find {flags[0]} on the command")
        else :
            df.DataManager.select(self, arguments)

    #Simple Calculation
    def do_calc(self, arg):
        flags, arguments = par.Parser.parse_command(self, arg)
        if len(flags) > 0 :
            if len(flags) > 1 :
                print("This command only accept 1 flag at a time")
            else :
                if flags[0] == '-h' :
                    flg.call_help('calc')
                else :
                    if flags[0] in flg.calc_flags :
                        flg.calc_flags[flags[0]](self, arguments, flags[0])
                    else :
                        print(f"could't find {flags[0]} on the command")

        else :
            print("This command need 1 flag to proceed ex : calc '-m column_name'")

    #Save the current df as 
    def do_save(self, arg):
        if self.dataFrame :
            flags, arguments = par.Parser.parse_command(self, arg)
            df.DataManager.save(self, arguments)
        print("Current dataframe saved successfully, do show -s to show current save")

    #Switch between df
    def do_switch(self,arg):
        flags, arguments = par.Parser.parse_command(self, arg)
        if len(flags) > 0 :
            if flags[0] == '-h' :
                flg.switch_flags[flags[0]]('switch')
        else :
            df.DataManager.switch(self, arguments)

    #Descibe df
    def do_desc(self, arg):
        flags, arguments = par.Parser.parse_command(self, arg)
        if len(flags) > 0 :
            if flags[0] == '-h' :
                flg.desc_flags[flags[0]]('desc')
            else :
                print(f"invalid flag {flags[0]}")
                
        else :
            df.DataManager.des(self,arguments)
        
    #Info df
    def do_info(self, arg):
        flags, arguments = par.Parser.parse_command(self,arg)
        df.DataManager.info(self, arg)

    #Bar graph
    def do_bar(self, arg):
        flags, arguments = par.Parser.parse_command(self, arg)
        df.DataManager.bar(self,arguments, flags)

    #Help
    def do_help(self, arg):
        for val in flg.help.values():
            print(val)


    #Exit
    def do_exit(self,arg):
        return True 



        
    
    
if __name__ == "__main__":
    LanternCLI().cmdloop()
