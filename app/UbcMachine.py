from UbcState import UbcState as UbcState
from UbcStore import UbcStore as UbcStore

class UbcMachine():
    def __init__(self):
        self.state = UbcState()
        self.store = UbcStore()

    def start_new_assay(self):
        return self.state.start_new_assay()

    def cancel_assay(self, assay_id):
        return self.state.cancel_assay(assay_id)
