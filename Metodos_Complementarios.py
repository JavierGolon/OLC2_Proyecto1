
def replace_str_index(text,index=0,replacement=''):
    sizestr = len(text)
    if index>sizestr-1:
        times = index-sizestr
        for i in range(0,times,1):
            text+=' '
        text+=replacement
        return text
    return '%s%s%s'%(text[:index],replacement,text[index+1:])

class resetable_range:
    def __init__(self, val):
        self.max = val
        self.val = 0
    def __iter__(self):
        return self
    def __next__(self):
        val = self.val
        if self.val == self.max:
            raise StopIteration
        self.val += 1
        return val
    def reset(self, val):
        self.val = val