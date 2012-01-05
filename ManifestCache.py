
class ManifestCache:
    '''This class implements a manifest file cache.
    '''
    DEFAULT_CACHE = "cache"

    def __init__(self, cachedir=None):
        if cachedir == None:
            self.cachedir = ManifestCache.DEFAULT_CACHE
        else:
            self.cachedir = cachedir

        if os.path.isdir(self.cachedir):
            self._load()

    def store(self, manifest, label=None):
        pass

    def get_path(self, label):
        pass
    
    def get_manifest(self, label):
        pass

    def exists(self, label):
        pass

    def _get_from_memcache(self, label):
        pass

    def _load(self):
        pass
    
    
class Manifest:
    def __init__(self, name="", data=""):
        self.name = name
        self.data = data

    def __str__(self):
        return self.name

    def __repr__(self):
        return "Manifest(name=%r, data=%s)" % (self.name, self.data)

class MemCache:
    def __init__(self, size=1):
        self.size = size
        self.items = []
        self.item_data = {}

    def store(self, key=None, value=None):
        if key in self.items:
            return
        if len(self.items) <= self.size:
            self.items.append(key)
            self.item_data[key] = value
        else:
            self.remove(self.items[0])
            self.items.append(key)
            self.item_data[key] = value

    def get(self, key=None):
        if key in self.items:
            self.refresh(key)
            return self.item_data[key]

    def remove(self, key=None):
        if key in self.items:
            self.items.remove(key)
            del self.item_data[key]

    def refresh(self, key=None):
        if key in self.items:
            if self.items.index(key) == (self.size -1):
                self.items.remove(key)
                self.items.append(key)

    
