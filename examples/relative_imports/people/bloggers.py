from dataclasses import dataclass
from random import randint

@dataclass
class Blogger:
    id: str
    name: str
    happy: bool
    member_id: int = randint()


