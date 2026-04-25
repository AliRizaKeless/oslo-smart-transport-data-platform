\# Oslo Smart Transport Data Platform



An end-to-end Azure-based data engineering project inspired by modern public transport analytics in Oslo.



\## Project Goals



\- Build scalable cloud data pipelines

\- Process transport and weather data

\- Design data warehouse models

\- Create dashboards and KPIs

\- Apply machine learning for demand prediction



\## Tech Stack



\- Python

\- SQL

\- Azure

\- Terraform

\- Power BI

\- GitHub Actions



\## Project Structure



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

## How to Run

1. Install dependencies

```bash
pip install -r requirements.txt

2. Run ingestion script
python src/ingestion/ruter_api_ingest.py

3. Run transform script
python src/transform/transform_posts.py

4. Check processed output
data/processed/processed_post.csv


