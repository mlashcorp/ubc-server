import threading
import uuid

def gen_assay_id():
    return uuid.uuid4()

class ThreadSafeMap():
    """ Thread safe map capable of setting and getting keys. """
    def __init__(self):
        self._lock = threading.Lock()
        self._map = {}

    def __getitem__(self, key):
        with self._lock:
            return self._map[key]            

    def __setitem__(self, key, value):
        with self._lock:
            self._map[key] = value

class UbcState():
    """ Stores the state of the ubc-server in thread-safe manner and validates operations against the running assay_id. """
    def __init__(self):
        self.state = ThreadSafeMap()

        self.state["running_assay"] = False
        self.state["assay_id"] = None
        self.state["assays_counter"] = 0
        self.state["progress"] = 0.0 # From 0.0 to 1.0 

    def __getitem__(self, key):
        return self.state[key]

    def __setitem__(self, key, value):
        self.state[key] = value

    def start_new_assay(self):
        """ Changes the state accordingly, generates and returns the started assay id or None if it cannot start. """
        if self["running_assay"]:
            return None
        else:
            self["running_assay"] = True
            self["assay_id"] = gen_assay_id()
            self["assays_counter"] += 1
            self["progress"] = 0.0

            return self["assay_id"]

    def cancel_assay(self, assay_id):
        """ Stops the assay given that the current running assay_id was given as argument. """
        if self["running_assay"] and str(self["assay_id"]) == str(assay_id):
            # assay_id validated. Stop it!
            self["running_assay"] = False
            self["assay_id"] = None
            self["progress"] = 0.0

            return True
        else:
            return False
            


            
