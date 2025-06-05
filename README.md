# Django




## Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/kasyap04/ems-backend.git
    ```

2. Navigate to the project directory:

    ```bash
    cd ems-backend
    ```

3. (Optional) Create and activate a virtual environment:

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

4. Install the dependencies:

    ```bash
    pip install -r requirement.txt
    ```

## Setup
Once the dependencies are installed, you can start the Django application:

 ```bash
python manage.py migrate
```

 ```bash
python manage.py createsuperuser
```

## Running the App

```bash
python manage.py runserver 0.0.0.0:8000
```