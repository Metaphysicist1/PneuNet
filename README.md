# Pneunet - Cloud Computing Project

A FastAPI-based web application for medical image analysis, specifically focused on pneumonia detection using deep learning models.

## Project Structure

```
.
├── app/                    # Main application directory
│   ├── main.py            # FastAPI application entry point
│   └── templates/         # HTML templates
├── data/                  # Data directory for storing images and models
├── dockerfile            # Docker configuration
├── requirements.txt      # Python dependencies
└── README.md            # Project documentation
```

## Features

- FastAPI-based REST API
- Web interface for image upload and analysis
- Deep learning model integration for pneumonia detection
- Docker support for containerized deployment

## Prerequisites

- Python 3.8 or higher
- Docker (optional, for containerized deployment)

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd <project-directory>
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Application

### Local Development

1. Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

2. Open your browser and navigate to `http://localhost:8000`

### Docker Deployment

1. Build the Docker image:

```bash
docker build -t pneunet .
```

2. Run the container:

```bash
docker run -p 8000:8000 pneunet
```

## API Endpoints

- `GET /`: Web interface
- `GET /api/v1/`: API root endpoint

## Development

The project uses FastAPI for the backend and Jinja2 for templating. The main application logic is in `app/main.py`.

## Contributing

Write me <b>edgarabasov1@gmail.com<b>
