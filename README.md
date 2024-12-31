# Ground Control Station Software for Autonomous UAVs
![GitHub Release](https://img.shields.io/github/v/release/ParagonAutonomous/GCS)
[![GitHub Issues](https://img.shields.io/github/issues/ParagonAutonomous/GCS)](https://github.com/ParagonAutonomous/GCS/issues)
![Last Commit](https://img.shields.io/github/last-commit/ParagonAutonomous/GCS)

> Ground Control Station (GCS) software for management of Paragon Autonomous' UAVs. This software provides tools for region mapping, mission planning, multi-drone coordination, real-time telemtry monitoring, and wildfire event handling.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
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
