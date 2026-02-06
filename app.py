from fastapi import FastAPI, UploadFile
import pandas as pd
from data_processor import process_financials
from ai_engine import generate_insights

app = FastAPI()

@app.post("/upload")
async def upload_file(file: UploadFile):
    df = pd.read_csv(file.file)
    metrics = process_financials(df)
    insights = generate_insights(metrics)
    return {"metrics": metrics, "insights": insights}