import io
import pandas as pd
from fastapi import APIRouter, HTTPException, UploadFile, File
from ..schemas.models import SheetAnalysisResponse, AnalysisResponse, GraphicInstruction

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
            excel_file = pd.ExcelFile(file_data)
            return SheetAnalysisResponse(valid_sheets=excel_file.sheet_names)

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"File reading process failed: {str(e)}")