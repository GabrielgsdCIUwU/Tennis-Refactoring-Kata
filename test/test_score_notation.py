import pytest
from src.score_notation import TennisScore

def test_get_score_name():
    assert "Love" == TennisScore.get_score_name(0)
    assert "Fifteen" == TennisScore.get_score_name(1)
    assert "Thirty" == TennisScore.get_score_name(2)
    assert "Forty" == TennisScore.get_score_name(3)

def test_get_score_name_invalid_values():
    with pytest.raises(ValueError, match="Invalid score value: -1"):
        TennisScore.get_score_name(-1)
    
    with pytest.raises(ValueError, match="Invalid score value: 4"):
        TennisScore.get_score_name(4)

