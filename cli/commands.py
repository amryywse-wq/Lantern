from core import dataframe as df

read_flags = {
    '-h' : df.DataManager.load,
}

select_flags = {
    '-e' : df.DataManager.select,
}

calc_flags = {
    '-a' : df.DataManager.calc,
}
del_col_flags = {
    '-e' : df.DataManager.delete_col,
}

show_flags = {
    '-s' : df.DataManager.show,
}

help = {
    'read' : "---read--- *read a .csv, .xls, .xslx file as dataframe\n-read (filepath)\n-read -h (header) (filepath) *let you choose header\n",
    'show' : "---show--- *show the current selected dataframe\n-show\n-show -s *let you see saved dataframe\n",
    'delCol' : "---delCol--- *delete selected column\n-delcol (column name)\n-delcol -e (column name) *delete column except (column name)\n",
    'reset' : "---reset--- *reset the current dataframe\n-reset\n",
    'rem' : "---rem--- *remove specific element\n-rem -i (column_name) (comparator[=,!=,>,<,etc]) (value) *if the value is integer\n-rem -s (column_name) (comparator[=,!=]) (value) *if the value is string\n",
    'select' : "---select--- *let you choose specific column as dataframe\n-select (column_name) *multiple column name allowed\n-select -e (column_name) *select all except (cloumn_name) *multiple allowed\n",
    'calc' : "---calc--- *let you calculate [max, min, median, mean] of said column\n-calc -a (column_name) *calculate mean for (column_name)\n",
    'save' : "---save--- *let you save the current dataframe\n-save (df name) *save current dataframe as (df name)\n",
    'switch' : "---switch--- *let you switch between dataframes\n-switch (df name)\n",
    'desc' : "---desc--- *show dataframe description using pandas's describe() function\n-desc\n",
    'info' : "---info--- *show dataframe information usinf pandas's info() function\n-info\n",
    'bar' : "---bar--- *create and save bar graph\n-bar (x values) (y values) *for each value you can use (column name)"
 }  