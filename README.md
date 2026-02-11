# Startup Metrics Dashboard

A comprehensive SaaS metrics dashboard for tracking MRR, churn, CAC, LTV, burn rate, and other key startup metrics. Built to help founders make data-driven decisions.

## 🚀 Day 1 - Initial Setup

**Current Features:**
- FastAPI backend with RESTful API
- Health check endpoint
- MRR (Monthly Recurring Revenue) tracking
- Basic metric summary endpoint
- API documentation (auto-generated)

## 📊 Metrics Supported

- **MRR** - Monthly Recurring Revenue
- **Churn Rate** - Customer and revenue churn
- **CAC** - Customer Acquisition Cost
- **LTV** - Customer Lifetime Value
- **Burn Rate** - Monthly cash burn
- **Runway** - Months of runway remaining

## 🛠️ Tech Stack

- **Backend:** FastAPI (Python)
- **Frontend:** HTML/CSS/JavaScript (coming Day 2)
- **Future:** Stripe integration, PostgreSQL, Chart.js

## 🏃 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/gauravrodrigues/startup-metrics-dashboard.git
cd startup-metrics-dashboard

# Install dependencies
pip install -r requirements.txt

# Run the server
python main.py
```

### Access the API

- **API Base URL:** http://localhost:8000
- **Interactive Docs:** http://localhost:8000/docs
- **Health Check:** http://localhost:8000/

## 📡 API Endpoints

### Core Endpoints

- `GET /` - Health check
- `GET /api/v1/about` - Dashboard information
- `GET /api/v1/metrics/summary` - Summary of all metrics

### MRR Endpoints

- `GET /api/v1/metrics/mrr` - Get current MRR
- `POST /api/v1/metrics/mrr` - Add MRR data point
- `GET /api/v1/metrics/mrr/history` - Get historical MRR data

## 🗺️ Development Roadmap

### Week 1: Core Metrics
- ✅ Day 1: FastAPI setup + MRR tracking
- Day 2: Frontend dashboard UI
- Day 3: Customer churn calculation
- Day 4: CAC tracking
- Day 5: LTV calculation
- Day 6: LTV/CAC ratio visualization
- Day 7: Burn rate & runway

### Week 2: Integrations
- Day 8: Stripe integration (revenue)
- Day 9: Customer data import
- Day 10: CSV data upload
- Day 11: Historical data visualization
- Day 12: Chart.js integration
- Day 13: Metric trends & growth rates
- Day 14: Weekly summary report

### Week 3: Advanced Features
- Day 15: Cohort analysis
- Day 16: Benchmark comparisons
- Day 17: Alert notifications
- Day 18: Custom metric builder
- Day 19: Multi-currency support
- Day 20: Export to PDF/CSV
- Day 21: API key authentication

### Week 4: Polish & Deploy
- Day 22: Mobile responsive design
- Day 23: Dark mode
- Day 24: Database persistence (PostgreSQL)
- Day 25: Docker containerization
- Day 26: CI/CD pipeline
- Day 27: Deployment to cloud
- Day 28: Performance optimization
- Day 29: Documentation & tutorials
- Day 30: Launch & demo video

## 🎯 Why This Project?

This dashboard demonstrates:
- Understanding of SaaS business metrics
- Full-stack development skills
- API design and REST principles
- Daily deployment discipline
- Product thinking for startups

## 📈 Daily Progress

Track daily commits and features at: https://github.com/gauravrodrigues/startup-metrics-dashboard/commits/main

## 🤝 Contributing

This is a daily learning project. Each day adds one meaningful feature.

## 📝 License

MIT License - feel free to use this for your own startup!

## 📧 Contact

Built by Gaurav Rodrigues
- GitHub: [@gauravrodrigues](https://github.com/gauravrodrigues)
- Project: [startup-metrics-dashboard](https://github.com/gauravrodrigues/startup-metrics-dashboard)

---

**Day 1 Status:** ✅ Backend API structure complete, MRR tracking live
**Next Up:** Frontend dashboard with first visualization
