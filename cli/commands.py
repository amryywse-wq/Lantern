from core import dataframe as df

read_flags = {
    '-h' : df.DataManager.load,
}

select_flags = {
    '-e' : df.DataManager.select,
}

calc_flags = {
    '-m' : df.DataManager.calc,
}
del_col_flags = {
    '-e' : df.DataManager.delete_col,
}

show_flags = {
    '-s' : df.DataManager.show,
}