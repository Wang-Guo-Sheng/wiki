class MdConverter():

    def __init__(self, fname):
        self.fname = fname
        self.ftype = "omd"
        self.text = self.reader(self, fname)

    def reader(self, fname):
        with open(fname, 'r') as f:
            text = f.read()

        if ftype == "xmd":
            self.xmdreader(fname)
        elif ftype == "omd":
            self.omdreader(fname)


# Wikilinks
r'\[[^\]]*\]\(\#[^\)]+\)'

# URL

# RefCite
r'<<ref[^>]*>>'

# RefList
r'<<showrefs[^>]*>>'
