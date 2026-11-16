import matplotlib.pyplot as plt
import numpy as np


class pyplot :

    def __init__(self):

        self.bar_conf = {
            'figsize' : (10,6), 
            'title' : "Unassigned",
            'xtitle' : "Unassigned",
            'ytitle' : "Unassigned",
        }


    def bar(self, df, arg, flg:str=''):
        print(arg)
        if len(arg) < 2 :
            print("Not enough arguments to proceed...")
            return False
       
        x, y = arg[0], arg[1]

        plt.figure(figsize=self.bar_conf['figsize'])
        plt.bar(df[x], df[y], label = x)
        plt.title(self.bar_conf['title'])
        plt.xlabel(self.bar_conf['xtitle'])
        plt.ylabel(self.bar_conf['ytitle'])
        plt.legend()
        plt.tight_layout()

        plt.savefig(f"saved{self.bar_conf['title']}")
        plt.show()

