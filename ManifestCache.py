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



