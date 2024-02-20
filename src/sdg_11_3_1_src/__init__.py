"""SDG 9.1.1"""

from typing import List

from src.sdg_11_3_1_src.sdg_base.base_src.sdg_base_src.sdg_base import SDGBase

from .sdg_11_3_1 import SDG11_3_1, run_sdg11_3_1
from .utils import InputFile

__all__: List[str] = ["SDGBase", "SDG11_3_1", "run_sdg11_3_1", "InputFile"]
