from dataclasses import dataclass, asdict

@dataclass(slots=True, frozen=True)
class BaseEntity:
    def to_dict(self):
        return asdict(self)

