from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
import pandas as pd
from ydata_profiling import ProfileReport
import io

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/get_profile_html", response_class=HTMLResponse)
async def get_profile_html():
    try:
        df = pd.read_csv('InjectionMolding_Raw_Data.csv')
        profile = ProfileReport(df, explorative=True)
        profile.to_file("output3.html")
        # HTML을 문자열로 생성
        html_string = profile.to_html()
        
        return HTMLResponse(content=html_string, status_code=200)
    except Exception as e:
        return HTMLResponse(content=f"<h1>Error</h1><p>{str(e)}</p>", status_code=500)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)