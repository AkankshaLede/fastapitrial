
# FastAPI Calculator Application

This repository contains a simple calculator API built using FastAPI. It allows users to perform basic arithmetic operations such as addition, subtraction, multiplication, and division via HTTP POST requests.

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Features

- FastAPI-based REST API for basic arithmetic operations.
- Supports the following operations:
  - Addition
  - Subtraction
  - Multiplication
  - Division (with error handling for division by zero).
- Structured input using Pydantic models for data validation.

## Requirements

Before running the application, ensure you have the following installed:

- **Python 3.8+**
- FastAPI and Uvicorn for running the API.

### Required Python Packages

The required packages are listed in `requirements.txt`. They include:

- `fastapi==0.114.0`
- `uvicorn==0.30.6`
- `pydantic==2.9.1`

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/AkankshaLede/fastapitrial.git
   cd fastapitrial

2. Create and activate a virtual environment:

bash

python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install the required dependencies:

bash

    pip install -r requirements.txt

4. Running the Application

    Start the FastAPI server:

    bash

uvicorn main:app --reload

The API will be available at http://127.0.0.1:8000/.

To interact with the API, you can use the built-in Swagger UI at:

    Swagger UI: http://127.0.0.1:8000/docs

