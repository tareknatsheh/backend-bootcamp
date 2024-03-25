import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from sensor import generate_record

def test_generate_record_has_the_keys():
    res = generate_record()
    assert "Timestamp" in res
    assert "newborn_count" in res
    assert "death_count" in res

def test_generate_record_values_types():
    res = generate_record()
    assert type(res["Timestamp"]) == str
    assert type(res["newborn_count"]) == int
    assert type(res["death_count"]) == int
