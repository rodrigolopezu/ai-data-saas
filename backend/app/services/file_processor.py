import pandas as pd
import io

def validate_sheet(df: pd.DataFrame) -> bool:
    rows, columns = df.shape
    print(f"rows: {rows}, columns: {columns}")
    if rows <= 1:
        print("FAIL: rows")
        return False
    if columns <= 1:
        print("FAIL: columns")
        return False
    df_clean = df.dropna(axis=1, how='all')
    _, clean_columns = df_clean.shape
    if clean_columns <= 1:
        return False
    if any(str(col).startswith("Unnamed") for col in df_clean.columns):
        return False
    return True

def validate_sheets(file: io.BytesIO) -> list[str]:
    excel_file = pd.ExcelFile(file)
    sheets = excel_file.sheet_names
    print(f"sheets found: {sheets}")
    valid_sheets = []
    for sheet in sheets:
        df = pd.read_excel(file, sheet_name=sheet, nrows=2)
        if validate_sheet(df):
            valid_sheets.append(sheet)
    return valid_sheets
            
