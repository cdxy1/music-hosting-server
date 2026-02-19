from dataclasses import asdict, dataclass


@dataclass(frozen=True, slots=True)
class BaseDTO:
    
    def to_dict(self):
        return asdict(self)
