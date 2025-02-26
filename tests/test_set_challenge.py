import set_challenge

def test_common_names():
    """Test that intersection of sets works correctly."""
    expected_common = {"Joe", "Chleo"}
    assert set_challenge.common_names == expected_common
