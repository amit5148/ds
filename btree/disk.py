HDD = {}

class Page():
    _page_id = 0

    def __init__():
        _page_id += 1
        self.page_id = _page_id
        self.content = ''

def DiskRead(page_id):
    return HDD.get(page_id)

def DiskWrite(p):
    HDD[p.page_id] = p

def AllocatePage():
    p = Page()
    HDD[page_id] = p
    return p