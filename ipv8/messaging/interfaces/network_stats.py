class NetworkStat:
    """
    Represents an individual network statistic. This is used to compose the overall community statistics.
    Includes the following properties for the given statistic:
        - identifier: char
        - num_up: integer
        - num_down: integer
        - bytes_up: integer
        - bytes_down: integer
        - first_measured_up: float
        - first_measured_down: float
        - last_measured_up: float
        - last_measured_down: float
    """
    def __init__(self, identifier):
        self.identifier = identifier
        self.num_up = 0
        self.num_down = 0
        self.bytes_up = 0
        self.bytes_down = 0
        self.first_measured_up = 0
        self.first_measured_down = 0
        self.last_measured_up = 0
        self.last_measured_down = 0

    def add_sent_stat(self, timestamp, num_bytes):
        self.num_up += 1
        self.bytes_up += num_bytes
        self.last_measured_up = timestamp

        if not self.first_measured_up:
            self.first_measured_up = timestamp

    def add_received_stat(self, timestamp, num_bytes):
        self.num_down += 1
        self.bytes_down += num_bytes
        self.last_measured_down = timestamp

        if not self.first_measured_down:
            self.first_measured_down = timestamp

    def to_dict(self):
        return {
            "identifier": self.identifier,
            "num_up": self.num_up,
            "num_down": self.num_down,
            "bytes_up": self.bytes_up,
            "bytes_down": self.bytes_down,
            "first_measured_up": self.first_measured_up,
            "first_measured_down": self.first_measured_down,
            "last_measured_up": self.last_measured_up,
            "last_measured_down": self.last_measured_down
        }

    def __str__(self):
        return (f"NetworkStat{{num_up:{self.num_up}, num_down:{self.num_down}, "
                f"bytes_up:{self.bytes_up}, bytes_down:{self.bytes_down}, ...}}")
