from dataclasses import dataclass
@dataclass
class Opera:
    opera_id: int
    opera_name: str

    def __eq__(self, other):
        return self.opera_id == other.opera_id
    def __hash__(self):
        return hash(self.opera_id)
    def __str__(self):
        return f"{self.opera_id} - {self.opera_name}"