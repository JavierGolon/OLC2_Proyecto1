
def replace_str_index(text,index=0,replacement=''):
    sizestr = len(text)
    if index>sizestr-1:
        times = index-sizestr
        for i in range(0,times,1):
            text+=' '
        text+=replacement
        return text
    return '%s%s%s'%(text[:index],replacement,text[index+1:])

