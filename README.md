# Malaria Prevalence Predictor Deployment Package

This package contains the files required to run and deploy the malaria prevalence prediction application.

## Packaged Files
* `app.py`: The interactive Streamlit dashboard application.
* `malaria_climate_model.pkl`: Saved Random Forest Regressor trained on historical environment data.
* `requirements.txt`: Python package dependencies.
* `Dockerfile`: Container image configuration for building a dockerized deployment.
* `docker-compose.yml`: Multi-container run specification for simple local orchestration.

## Running Locally
1. Ensure you have Python installed.
2. Install dependencies: `pip install -r requirements.txt`
3. Launch Streamlit: `streamlit run app.py`

## Running with Docker Compose
1. Execute `docker compose up --build` to containerize and spin up the service at `http://localhost:8501`.
