from typing import Dict, Optional


class InputFile:
    def __init__(
        self,
        file_path: str,
        kwargs: Optional[Dict] = None,
        index_col: Optional[str] = None,
        year: Optional[int] = None,
        pop_col_init: Optional[str] = None,
        land_col: Optional[str] = None,
        filter_land_flag: Optional[bool] = False,
        filter_land_col: Optional[str] = None,
        filter_land_value: Optional[str] = None,
    ) -> None:
        self.file_path: str = file_path
        self.kwargs: Optional[Dict] = kwargs
        self.index_col: Optional[str] = index_col
        self.year: Optional[int] = year
        self.pop_col_init: Optional[str] = pop_col_init
        self.land_col: Optional[str] = land_col
        self.filter_land_flag: Optional[bool] = filter_land_flag
        self.filter_land_col: Optional[str] = filter_land_col
        self.filter_land_value: Optional[str] = filter_land_value
        self.set_rename_pop_col()

    def set_rename_pop_col(self) -> None:
        if self.pop_col_init:
            self.pop_col_rename: Optional[str] = (
                f'{self.pop_col_init.replace(" ", "_")}_{self.year}'
            )
