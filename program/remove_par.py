#change parentheses

def trans(fs):  #[[1],[2,3]]->[1,2,3]
    f_t=str(fs)
    f_t=f_t.replace("]","")  #remove right parenthesis
    f_t=f_t.replace("[","")
    f_t=f_t.replace(" ","")
    fs=[]
    for i in f_t.split(','):
        fs.append(int(i))
    fs=sorted(fs)
    return fs

def t_trans(tt):  #(1,)->[1]  #(1, 2)->[1,2]
    f_t=str(tt)
    f=[]
    if(len(tt))<2:
        f_t=f_t.replace("(","[")
        f_t=f_t.replace(")","]")
        f_t=f_t.replace(",","")
    else:    
        f_t=f_t.replace("(","[")
        f_t=f_t.replace(")","]")
    f_t=eval(f_t)
    return f_t