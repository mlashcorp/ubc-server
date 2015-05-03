from UbcState import UbcState as UbcState
from UbcStore import UbcStore as UbcStore
from threading import Thread
import random, time

ASSAY_TIME = 120

class UbcMachine():
    def timer_worker(self,assay_time):
        while True:
            print self.state["progress"]
            if self.state["progress"] > 1.1:
                result = { "result" : random.random() }

                self.store.store_assay(self.state["assay_id"], result) # results can be a map
                self.state["progress"] = 0.0
                self.state["running_assay"] = False
                
                self.state["assay_id"] = None

                print "Stored assays in machine:"
                print self.store.db

            elif self.state["running_assay"]:
                self.state["progress"] += 0.005
            
            else:
                return

            time.sleep(0.2)

    def __init__(self):
        self.state = UbcState()
        self.store = UbcStore()

    def start_new_assay(self):
        t = Thread(target=self.timer_worker, args=([ASSAY_TIME]))
        t.start()
        return self.state.start_new_assay()

    def cancel_assay(self, assay_id):
        return self.state.cancel_assay(assay_id)

