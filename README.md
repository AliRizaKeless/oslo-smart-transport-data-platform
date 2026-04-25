Oslo Smart Transport Data Platform

Tech Stack

- Python
- SQL
- Git
- Data Engineering
- ETL
- CSV / JSON
- Azure (planned)
- Terraform (planned)
- Power BI (planned)


An end-to-end Azure-based data engineering project inspired by modern public transport analytics in Oslo.


Project Goals

\- Build scalable cloud data pipelines

\- Process transport and weather data

\- Design data warehouse models

\- Create dashboards and KPIs

\- Apply machine learning for demand prediction



Tech Stack

\- Python

\- SQL

\- Azure

\- Terraform

\- Power BI

\- GitHub Actions


Project Structure
```text

infra/terraform

src/ingestion

src/transform

src/ml

sql

docs

tests


Status

Project started and under active development.

Last updated: April 2026

How to Run

1. Install dependencies

```bash
pip install -r requirements.txt

2. Run ingestion script
python src/ingestion/ruter_api_ingest.py

3. Run transform script
python src/transform/transform_posts.py

4. Check processed output
data/processed/processed_post.csv

Project Roadmap

Phase 1
- API data ingestion
- Raw data storage
- Data transformation
- CSV export

Phase 2
- SQL database loading
- Dashboard reporting
- Data quality checks

Phase 3
- Azure deployment
- Terraform infrastructure
- CI/CD pipeline

Phase 4
- Machine learning predictions
- Real transport analytics

