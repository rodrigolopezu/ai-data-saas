import pandas as pd
import io

def validate_sheet(df: pd.DataFrame) -> bool:
    rows, columns = df.shape
    if rows <= 1:
        return False
    if columns <= 1:
        return False
    return True

def extract_sample(file: io.BytesIO, sheet: str) -> pd.DataFrame:
    df_full = pd.read_excel(file, sheet_name=sheet)
    total_rows = len(df_full)
    if total_rows<20:
        return df_full
    return pd.concat([df_full[:15], df_full[-5:]])

def validate_sheets(file: io.BytesIO) -> list[str]:
    excel_file = pd.ExcelFile(file)
    sheets = excel_file.sheet_names
    valid_sheets = []
    for sheet in sheets:
        df = pd.read_excel(file, sheet_name=sheet, nrows=2)
        if validate_sheet(df):
            valid_sheets.append(sheet)
    return valid_sheets

def extract_sheet(file: io.BytesIO, sheet: str) -> pd.DataFrame:
    return pd.read_excel(file, sheet_name=sheet)    

def data_wrangling(file: io.BytesIO, sheet: str, ai_response: dict) -> pd.DataFrame:
    headers = ai_response["headers"]
    skip_rows = ai_response["skip_rows"]
    skip_footer = ai_response["skip_footer"]
    df = pd.read_excel(file, sheet_name=sheet, names=headers, skiprows=skip_rows, skipfooter=skip_footer, header=0)
    return df

def build_schema (df: pd.DataFrame) -> dict:
    