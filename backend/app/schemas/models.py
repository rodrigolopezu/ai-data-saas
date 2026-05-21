from pydantic import BaseModel

class SheetAnalysisResponse(BaseModel):
    valid_sheets: list[str]

class GraphicInstruction(BaseModel):
    graphic_type: str
    graphic_title: str
    graphic_description: str
    graphic_data: list[dict[str, str]]

class AnalysisResponse(BaseModel):
    graphics: list[GraphicInstruction]
    insights: list[str]