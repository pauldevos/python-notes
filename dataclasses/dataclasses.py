from dataclasses import dataclass
# dict, tuple, namedtuple, dataclass, struct

@dataclass
class PlayByPlay:
    time: datetime
    nba_id: str

@dataclass
class Position:
    name: str
    lon: float = 0.0
    lat: float = 0.0

    
from dataclasses import make_dataclass

Position = make_dataclass('Position', ['name', 'lat', 'lon'])