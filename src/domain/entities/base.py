from dataclasses import asdict, dataclass


@dataclass(slots=True, frozen=True)
class BaseEntity:
    def to_dict(self):
        return asdict(self)

