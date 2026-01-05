import csv
from pathlib import Path
import pytest

CSV_PATH=Path(__file__).parent.parent/ "employee_list.csv"

#validate the csv file can be loaded and is not empty
@pytest.mark.csv
def test_employee_csv_loads_successfully():
    with CSV_PATH.open(newline="", encoding="utf-8") as f:
        reader=csv.DictReader(f)
        rows=list(reader)
        
    assert rows, "CSV file is empty or not loaded"
    
#validate the CSV file has expected columns

@pytest.mark.csv
def test_employee_csv_has_required_colimns():
    required_columns={"ID","Name","Surname","Department","Salary"}
    with CSV_PATH.open(newline="", encoding="utf-8") as f:
        reader=csv.DictReader(f)
        fieldnames=reader.fieldnames
        
    assert required_columns.issubset(fieldnames)
