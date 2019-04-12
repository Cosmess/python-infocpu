import psutil

def freq():
    return psutil.cpu_freq().max/1000
def cores():
    return psutil.cpu_count()
def phycores():
    return psutil.cpu_count(logical=False)
