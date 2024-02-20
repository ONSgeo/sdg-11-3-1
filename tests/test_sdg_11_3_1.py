import numpy as np
import pandas as pd
import pytest
from hypothesis import given
from hypothesis import strategies as st

from src.sdg_11_3_1_src.sdg_11_3_1 import SDG11_3_1
from user_params import UserParams

params: UserParams = UserParams()


def test_init():
    instance = SDG11_3_1("", params.root_dir)
    assert isinstance(instance, SDG11_3_1)


@given(
    st.floats(min_value=1, max_value=100000000, allow_nan=False),
    st.floats(min_value=1, max_value=100000000, allow_nan=False),
    st.integers(min_value=1, max_value=1000),
)
def test_population_growth_rate(past_pop, present_pop, years):
    instance = SDG11_3_1("", params.root_dir)

    result = instance.population_growth_rate(past_pop, present_pop, years)
    assert result == (np.log(present_pop) - np.log(past_pop)) / years
    assert isinstance(result, float)


@given(
    st.floats(min_value=1, max_value=1000000, allow_nan=False),
    st.floats(min_value=1, max_value=1000000, allow_nan=False),
    st.integers(min_value=1, max_value=1000),
)
def test_land_consumption_rate(past, present, years):
    instance = SDG11_3_1("", params.root_dir)

    result = instance.land_consumption_rate(past, present, years)
    assert result == ((present - past) / past) / years
    assert isinstance(result, float)


@given(
    st.floats(min_value=1, max_value=1000000, allow_nan=False),
    st.floats(min_value=1, max_value=1000000, allow_nan=False),
)
def test_land_consumption_rate_population_growth_rate_ratio(lcr, pgr):
    instance = SDG11_3_1("", params.root_dir)

    result = instance.land_consumption_rate_population_growth_rate_ratio(lcr, pgr)
    assert result == lcr / pgr
    assert isinstance(result, float)


@pytest.fixture
def create_filter_land_on_col_df():
    data = {"col1": [0, 1, 0, 2], "col2": [0, 1, 0, 1]}
    return pd.DataFrame().from_dict(data)


@pytest.mark.parametrize(
    "flag, col, val, expected_len",
    [
        (True, "col1", 0, 2),
        (True, "col2", 0, 2),
        (True, "col1", 1, 1),
        (True, "col2", 1, 2),
        (True, "col1", 3, 0),
        (False, "col1", 0, 4),
    ],
)
def test_filter_land_on_col(create_filter_land_on_col_df, flag, col, val, expected_len):
    instance = SDG11_3_1("", params.root_dir)

    result = instance.filter_land_on_col(create_filter_land_on_col_df, flag, col, val)
    assert len(result) == expected_len
    assert isinstance(result, pd.DataFrame)


@given(
    st.floats(min_value=0, max_value=1000000, allow_nan=False),
    st.integers(min_value=1, max_value=1000000),
)
def test_built_up_area_per_capita(bua, population):
    instance = SDG11_3_1("", params.root_dir)

    result = instance.built_up_area_per_capita(bua, population)
    assert result == bua / population
    assert isinstance(result, float)
