import io
from fastapi import APIRouter, HTTPException, UploadFile, File, Form
from ..schemas.models import SheetAnalysisResponse, AnalysisResponse, GraphicInstruction
from ..services.file_processor import validate_sheets, extract_sheet, validate_sheet, extract_sample, data_wrangling
from ..services.ai_service import analyze_structure

SUPPORTED_TYPES = {
    "text/csv": "csv",
    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet": "xlsx",
    "application/vnd.ms-excel": "xls"
}

router = APIRouter(prefix="/analyze", tags=["analyze"])


@router.post("/sheet", response_model=SheetAnalysisResponse)
async def analyze_sheet(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        file_type = SUPPORTED_TYPES.get(file.content_type)

        if not file_type:
            raise HTTPException(status_code=400, detail="File type not supported")

        file_data = io.BytesIO(contents)

        if file_type == "csv":
            return SheetAnalysisResponse(valid_sheets=["Data"])
        elif file_type in ("xlsx", "xls"):
            return SheetAnalysisResponse(valid_sheets=validate_sheets(file_data))

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"File reading process failed: {str(e)}")


@router.post("/analysis", response_model=AnalysisResponse)
async def analyze_data(file: UploadFile = File(...), sheet_name: str = Form(...)):
    try:
        contents = await file.read()
        file_data = io.BytesIO(contents)
        df = extract_sheet(file_data, sheet_name)

        if not validate_sheet(df):
            raise HTTPException(status_code=400, detail="Sheet is not valid for analysis")

        sample = extract_sample(file_data, sheet_name)
        structure = analyze_structure(sample)
        clean_df = data_wrangling(file_data, sheet_name, structure)

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"File analysis process failed: {str(e)}")