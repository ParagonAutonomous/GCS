# Ground Control Station Software for Autonomous UAVs
[![GitHub Issues](https://img.shields.io/github/issues/ParagonAutonomous/GCS)](https://github.com/ParagonAutonomous/GCS/issues)
![Last Commit](https://img.shields.io/github/last-commit/ParagonAutonomous/GCS)
![Flask](https://img.shields.io/badge/Flask-v3.1.0-blue)
![Svelte](https://img.shields.io/badge/Svelte-v5.0.4-orange)

> Ground Control Station (GCS) software for management of Paragon Autonomous' UAVs. This software provides tools for region mapping, mission planning, multi-drone coordination, real-time telemtry monitoring, and wildfire event handling.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Tools and Libraries](#tools-and-libraries)
- [Contributing](#contributing)

## Features

## Installation

### Prerequisites
Before project setup, ensure the following tools are installed on your system:
- [Git](https://git-scm.com/)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- [Node.js and npm](https://nodejs.org/en/about/previous-releases) (Version 20+)
- [Python](https://www.python.org/) (Version 3.12+)

### Development Build

**Option 1: Using Docker (Recommended)**

1. Clone the Repository

``` bash
git clone https://github.com/ParagonAutonomous/GCS.git
cd GCS
```

2. Build and Start Development Environment

``` bash
docker-compose up --build
```
This will start:

- backend on `http://localhost:5050`
- frontend on `http://localhost:3030`

3. Edit and Test

- Edit code in your local IDE
- Changes will reflect in running Docker containers

4. Stop Containers
``` bash
docker-compose down
(or Ctrl+C)
```

**Option 2: Local Development**

1. Clone the Repository

``` bash
git clone https://github.com/ParagonAutonomous/GCS.git
cd GCS
```

2. Install Dependencies

``` bash
cd frontend
npm install
cd ../backend
python -m venv venv
source venv/bin/activate             # Use `venv\Scripts\activate` on Windows
pip install -r requirements.txt
cd ..
```

3. Run in Development Mode
``` bash
npm run dev                          # this will start both applications
```
This will start:

- backend on `http://localhost:5050`
- frontend on `http://localhost:3030`

or run individually:
``` bash
flask run --host=0.0.0.0 --port=5050 # flask app
npm run vite                         # svelte app
```



### Deployment Build


## Usage

## Tools and Libraries

### Backend
- [Flask](https://flask.palletsprojects.com/en/stable/): web application framework.
- [pymavlink](https://github.com/ArduPilot/pymavlink): MAVLink message processing library.
- [SQLAlchemy](https://www.sqlalchemy.org/): SQL toolkit and ORM.

### Frontend
- [Svelte](https://svelte.dev/): UI framework.
- [Flowbite Svelte](https://flowbite-svelte.com/): UI component library for Svelte.
- [Leaflet](https://leafletjs.com/): library for interactive maps.

## Contributing
