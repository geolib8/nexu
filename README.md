# Flask Application: Car Brands and Models API

## Overview

This Flask application provides a RESTful API to manage car brands and models. It allows for creating, listing, updating, and querying car brands and their associated models, offering a structured approach for vehicle inventory systems.

## Features

- CRUD operations for car brands.
- CRUD operations for models within specific car brands.
- Ability to query models based on their price range.
- Enforcement of unique names for brands and for models within a brand.
- Capability to update the average price of a model with validations for input data.

## Getting Started

### Prerequisites

Before you begin, ensure you have met the following requirements:
- Python 3.8 or newer installed on your machine.
- pip for managing Python packages.

### Installation

Follow these steps to get your development environment set up:

1. **Clone the repository to your local machine:**

2. **Create and activate a virtual environment (recommended):**
- On Windows:
  ```
  python -m venv venv
  venv\Scripts\activate
  ```
- On Unix or MacOS:
  ```
  python3 -m venv venv
  source venv/bin/activate
  ```

3. **Install the required dependencies:**


### Running the Application

To start the Flask application, run:

This command will start the server on `http://127.0.0.1:5000/`, making the API endpoints accessible for interaction.

## API Endpoints

The application defines the following RESTful endpoints:
- `GET /brands` - Retrieves a list of all car brands.
- `POST /brands` - Creates a new car brand.
- `GET /brands/:id/models` - Retrieves all models for a specific brand.
- `POST /brands/:id/models` - Adds a new model to a specific brand.
- `PUT /models/:id` - Updates the average price of a specific model.
- `GET /models` - Queries models based on a specified price range.

## Testing

Ensure all tests pass to confirm the API's functionality and integrity.

## Linting

### Flake8

The project uses `flake8` for linting to adhere to Python's PEP 8 style guide:



