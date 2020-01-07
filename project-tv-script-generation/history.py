import json
import os

HISTORY_FILE = "history.json"

SESSION_PARAMS = [
    "sequence_length",
    "batch_size",
    "num_epochs",
    "learning_rate",
    "embedding_dim",
    "hidden_dim",
    "n_layers",
    "dataset_size",
]

class LoggingSession():

    def __init__(self, namespace):
        self.params = dict()
        for param in SESSION_PARAMS:
            self.params[param] = namespace[param]
        self.history = list()

    def new_epoch_started(self):
        self.epoch_history = list()
        self.history.append(self.epoch_history)

    def log(self, value):
        self.epoch_history.append(value)

    def json(self):
        return {
            "params": self.params,
            "history": self.history
        }

logging_session = None

def start_logging_session(namespace):
    print("Sarting logging session ...")
    global logging_session
    logging_session = LoggingSession(namespace)

def new_epoch_started():
    logging_session.new_epoch_started()

def log(value):
    logging_session.log(value)

def dump_logging_session():
    print("Dumping logging session ...")
    sessions = list()
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as history_file:
            sessions = json.load(history_file)
    with open(HISTORY_FILE, "w") as history_file:
        sessions.append(logging_session.json())
        json.dump(sessions, history_file, indent=4, sort_keys=True)
