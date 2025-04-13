# Pneunet - Cloud Computing Project

A FastAPI-based web application for medical image analysis, specifically focused on pneumonia detection using deep learning models.

## Project Structure

```
.
├── app/                    # Main application directory
│   ├── main.py            # FastAPI application entry point
│   ├── logger.py          # Logging configuration
│   └── templates/         # HTML templates
├── tests/                 # Test directory
│   └── test_main.py       # Application tests
├── data/                  # Data directory for storing images and models
├── logs/                  # Application logs
├── .github/              # GitHub configuration
│   └── workflows/        # CI/CD workflows
├── dockerfile            # Docker configuration
├── requirements.txt      # Python dependencies
├── pytest.ini           # PyTest configuration
├── .env                 # Environment variables
└── README.md            # Project documentation
```

## Features

- FastAPI-based REST API
- Web interface for image upload and analysis
- Deep learning model integration for pneumonia detection
- Docker support for containerized deployment
- Automated testing with PyTest
- CI/CD pipeline with GitHub Actions
- Comprehensive logging system

## Prerequisites

- Python 3.10 or higher
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

## Testing

The project uses PyTest for testing. To run the tests:

```bash
pytest tests/ -v
```

Test logs are automatically generated in the `logs/` directory.

## CI/CD Pipeline

The project includes a GitHub Actions workflow that:

- Runs on push to main branch and pull requests
- Sets up Python 3.10
- Installs dependencies
- Runs tests
- Uploads test logs as artifacts

## API Endpoints

- `GET /`: Web interface
- `GET /api/v1/`: API root endpoint

## Development

The project uses:

- FastAPI for the backend
- Jinja2 for templating
- PyTest for testing
- GitHub Actions for CI/CD
- Custom logging configuration

## Contributing

Write me <b>edgarabasov1@gmail.com</b>
