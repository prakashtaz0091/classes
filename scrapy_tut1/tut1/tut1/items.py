from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Book:
    name: Optional[str] = field(default=None)
    price: Optional[str] = field(default=None)
    rating: Optional[str] = field(default=None)
    image_url: Optional[str] = field(default=None)
