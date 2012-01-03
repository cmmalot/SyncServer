
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
