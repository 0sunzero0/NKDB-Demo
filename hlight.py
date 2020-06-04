import re

def hlight_term(string, term):
    if len(term) < 2:
        idx = string.find(term[0])
        begin = max(18,idx-10)
        pattern = "r'("+term[0]+")'"
        result = string[begin:begin+500]
        return result
    else:
        begin = 400
        for i in range(len(term)):
            begin = min(begin,string.find(term[i]))
        begin = max(18,begin)
        result = string[begin:begin+500]
        return result
