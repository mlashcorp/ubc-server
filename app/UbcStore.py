

class UbcStore():
    def __init__(self):
        self.db = {}

    def store_assay(self, assay_id, result):
        self.db[assay_id] = result
