# Course platform

This is online learning project.

## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

Make sure you have installed:

- Python (version 3.8 and up)
- Pip
- Virtualenv

### Installation

Clone the repository and activate the virtual environment:

git clone https://github.com/RomanKondratiuk/Course_platform.git
cd Cource_platform_docker
virtualenv env
source env/bin/activate

Install the dependencies:

pip install -r requirements.txt

Configuration

Copy the .env.sample file to a new .env file and configure the environment variables:

cp .env.sample .env

Running

Start the local server:

python manage.py runserver
