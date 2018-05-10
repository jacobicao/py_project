import datetime as dt
# 工具类
def is_float(s):
    try:
        float(s)
    except ValueError:
        return False
    return True

def is_days(s):
    if not s.isdigit() or int(s)>30 or int(s)<1:
        return False
    return True

def is_date(s):
    try:
        dt.datetime.strptime(s,'%Y-%m-%d')
    except ValueError:
        return False
    return True