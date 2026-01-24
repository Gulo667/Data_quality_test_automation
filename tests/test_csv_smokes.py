import csv
import os
from pathlib import Path
import pytest
import pandas as pd

CSV_PATH=Path(__file__).parent.parent/ "employee_list.csv"

#validate that the csv file exists on the specific location
@pytest.mark.csv
def test_employee_csv_exists():
    assert os.path.exists(CSV_PATH), f"CSV file does not exist at {CSV_PATH}"

#validate the csv file can be loaded and is not empty
@pytest.mark.csv
def test_employee_csv_loads_successfully():
    with CSV_PATH.open(newline="", encoding="utf-8") as f:
        reader=csv.DictReader(f)
        assert reader.fieldnames is not None
        
#validate csv file is not empty:
@pytest.mark.csv
def test_employee_csv_not_empty():
    df = pd.read_csv(CSV_PATH)
    assert not df.empty or df.columns is not None
    
#validate the CSV file has expected columns:

@pytest.mark.csv
def test_employee_csv_has_required_colimns():
    required_columns={"ID","Name","Surname","Department","Salary"}
    with CSV_PATH.open(newline="", encoding="utf-8") as f:
        reader=csv.DictReader(f)
        fieldnames=reader.fieldnames
        
    assert required_columns.issubset(fieldnames)
