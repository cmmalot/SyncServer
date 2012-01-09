import os


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

        self.memcache = MemCache(50)

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

    def _get_dir_and_file_name(self, label):
        try:
            parts = label.split('.')
        except ValueError, e:
            #TODO: Handle error
         filename = parts.pop()       
         dirname = os.path.join(parts)
         return (dirname, filename)


class Manifest:
    def __init__(self, label="", data=""):
        self.label = label
        self.data = data

    def __str__(self):
        return self.label

    def __repr__(self):
        return "Manifest(label=%r, data=%s)" % (self.label, self.data)


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
                return
            self.items.remove(key)
            self.items.append(key)

    
