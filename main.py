"""
Startup Metrics Dashboard - FastAPI Backend
Day 1: Initial setup with health check and basic structure
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime, date
from decimal import Decimal
import os

app = FastAPI(
    title="Startup Metrics Dashboard API",
    description="Track key SaaS metrics: MRR, churn, CAC, LTV, burn rate",
    version="0.1.0"
)

# CORS middleware for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Data models
class HealthResponse(BaseModel):
    status: str
    timestamp: datetime
    version: str
    message: str

class MetricValue(BaseModel):
    value: float
    currency: Optional[str] = "USD"
    period: str
    last_updated: datetime

class MRRData(BaseModel):
    mrr: float
    growth_rate: Optional[float] = None
    customers: int
    arpu: float  # Average Revenue Per User
    period: str

# In-memory storage (will be replaced with database)
metrics_store = {
    "mrr": [],
    "customers": []
}

# Routes
@app.get("/", response_class=HTMLResponse)
async def serve_dashboard():
    """Serve the main dashboard HTML"""
    html_path = os.path.join(os.path.dirname(__file__), "index.html")
    if os.path.exists(html_path):
        with open(html_path, "r") as f:
            return f.read()
    return "<h1>Dashboard HTML not found</h1>"

@app.get("/health", response_model=HealthResponse)
async def health_check():
    """Health check endpoint"""
    return HealthResponse(
        status="healthy",
        timestamp=datetime.now(),
        version="0.1.0",
        message="Startup Metrics Dashboard API is running"
    )

@app.get("/api/v1/metrics/summary")
async def get_metrics_summary():
    """Get summary of all key metrics"""
    return {
        "mrr": {
            "current": 0.0,
            "previous": 0.0,
            "growth_rate": 0.0,
            "currency": "USD"
        },
        "customers": {
            "total": 0,
            "new_this_month": 0,
            "churned_this_month": 0
        },
        "churn_rate": 0.0,
        "cac": 0.0,
        "ltv": 0.0,
        "ltv_cac_ratio": 0.0,
        "burn_rate": 0.0,
        "runway_months": 0,
        "last_updated": datetime.now()
    }

@app.get("/api/v1/metrics/mrr")
async def get_mrr():
    """Get Monthly Recurring Revenue data"""
    if not metrics_store["mrr"]:
        return {
            "current_mrr": 0.0,
            "previous_mrr": 0.0,
            "growth_rate": 0.0,
            "currency": "USD",
            "period": date.today().strftime("%Y-%m"),
            "message": "No MRR data available yet. Add your first revenue data."
        }
    
    latest = metrics_store["mrr"][-1]
    return latest

@app.post("/api/v1/metrics/mrr")
async def add_mrr_data(data: MRRData):
    """Add new MRR data point"""
    metrics_store["mrr"].append({
        "mrr": data.mrr,
        "growth_rate": data.growth_rate,
        "customers": data.customers,
        "arpu": data.arpu,
        "period": data.period,
        "timestamp": datetime.now()
    })
    return {
        "success": True,
        "message": "MRR data added successfully",
        "data": data
    }

@app.get("/api/v1/metrics/mrr/history")
async def get_mrr_history(limit: int = 12):
    """Get historical MRR data"""
    return {
        "data": metrics_store["mrr"][-limit:],
        "total_records": len(metrics_store["mrr"])
    }

@app.get("/api/v1/about")
async def about():
    """Information about the dashboard"""
    return {
        "name": "Startup Metrics Dashboard",
        "description": "Track key SaaS metrics to make data-driven decisions",
        "metrics_supported": [
            "MRR (Monthly Recurring Revenue)",
            "Churn Rate",
            "CAC (Customer Acquisition Cost)",
            "LTV (Lifetime Value)",
            "Burn Rate",
            "Runway"
        ],
        "upcoming_features": [
            "Stripe integration",
            "Automated metric calculations",
            "Benchmark comparisons",
            "Alert notifications",
            "Cohort analysis"
        ],
        "day": 1,
        "github": "https://github.com/gauravrodrigues/startup-metrics-dashboard"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
