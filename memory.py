import psutil

def size():
    return round(psutil.virtual_memory().total/(1024*1024*1024),2)