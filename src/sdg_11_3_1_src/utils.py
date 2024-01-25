

from typing import Dict, Optional


class InputFile:
    def __init__(
        self,
        file_path: str,
        kwargs: Optional[Dict] = None,
        index_col: Optional[str] = None
    ) -> None:
        self.file_path = file_path
        self.kwargs = kwargs
        self.index_col = index_col
