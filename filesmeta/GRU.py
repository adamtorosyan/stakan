class Gru:
    def __init__(self):
        self._extensions = {}

    def add_minion(self, minion):
        ex = minion.ex
        for e in ex:
            self._extensions[e] = minion

    def get_meta_inf(self, path):
        res = {}
        ex = path.split(".")[-1]
        res = self._extensions["*"].collect_common_metadata(path)
        if ex in self._extensions:
            res.update(self._extensions[ex].get_meta_inf(path))
        else:
            res.update({"error": "Unsupported file format"})
        return res

    def process_file(self, file_path):
        return self.get_meta_inf(file_path)

    def process_files(self, file_paths):
        all_metadata = []

        for file_path in file_paths:
            metadata = self.process_file(file_path)
            all_metadata.append(metadata)

        return all_metadata
