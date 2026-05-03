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
pip install -r requirements.txt

2. Run ingestion script
python src/ingestion/ruter_api_ingest.py

3. Run transform script
python src/transform/transform_posts.py

4. Check processed output
data/processed/processed_post.csv

5. Download data from Azure Blob Storage
python src/ingestion/download_from_blob.py

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

Architecture Flow
API Source  
↓  
Raw JSON Storage  
↓  
Python Transform  
↓  
Processed JSON / CSV  
↓  
SQL Database  
↓  
Dashboard / Analytics  
↓  
Azure Cloud Deployment

Next Steps
- Connect to real Oslo transport APIs
- Load data into SQL database
- Build Power BI dashboard
- Deploy pipeline to Azure
- Manage infrastructure with Terraform
- Add automated tests
- Add CI/CD with GitHub Actions

Demo
Successfully uploaded local JSON data to Azure Blob Storage using Python.

- Source: data/raw/sample_response.json
- Destination: Azure Blob Storage (raw container)

Verified Azure Storage Output
The pipeline has been tested successfully with Azure Blob Storage.

- Raw file uploaded to `raw/sample_response.json`
- Processed file uploaded to `processed/processed_post.csv`
