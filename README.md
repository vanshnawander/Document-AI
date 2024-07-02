# Project Setup

## Backend (FastAPI)

### Prerequisites

- Python 3.x
- Virtualenv

### Setup

1. Navigate to the `backend` folder:

    ```sh
    cd backend
    ```

2. Create a virtual environment:

    ```sh
    python -m venv venv
    ```

3. Activate the virtual environment:

    - On Windows:

        ```sh
        .\venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```sh
        source venv/bin/activate
        ```

4. Install the required dependencies:

    ```sh
    pip install -r requirements.txt
    ```

5. Make sure you have a `.env` file in the `backend` folder with the following content:

    ```env
    OPENAI_API_KEY=your_openai_api_key_here
    ```
6. Run the test.ipynb jupyter notebook for database creation before using the App

7. Run the FastAPI app:

    ```sh
    python -m uvicorn main:app --reload
    ```

## Frontend (React)

### Prerequisites

- Node.js
- npm

### Setup

1. Navigate to the `frontend` folder:

    ```sh
    cd frontend
    ```

2. Install the dependencies:

    ```sh
    npm install
    ```

3. Start the React app:

    ```sh
    npm start
    ```

### Running the Script

To execute the script in the `backend` folder, use the following command:

```sh
python script.py

```

