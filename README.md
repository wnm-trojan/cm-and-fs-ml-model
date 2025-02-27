# Online Crop Management And Forecasting System ML Model

This is a vegetable sales prediction ML Model. This system is part of Online Crop Management And Forecasting System for Farmers and Agro Business Industry.

## Wikis
For more information about providing guidelines for your project, see https://medium.com/@warunamadushan92624.wm/building-a-sales-forecasting-api-system-with-fastapi-mysql-and-arima-a-step-by-step-guide-dac9e109df71

## Installation & Setup

### Prerequisites
- Python 3.12+
- MySQL Server
- Git
- Virtual Environment (optional but recommended)

### Clone the Repository
```bash
git clone https://github.com/wnm-trojan/cm-and-fs-ml-model.git
cd cm-and-fs-ml-model
```

### Create and Activate Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Configure Environment Variables
Create a `.env` file in the root directory and set up the database connection:
```
DATABASE_URL=mysql://root@localhost/fcms_db
```

### Apply Database Migrations
```bash
alembic upgrade head  # If using Alembic for migrations
```

### Run the FastAPI Server
```bash
uvicorn app.main:app --reload
```

### API Documentation
Once the server is running, you can access the interactive API docs:
- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

### Running Tests
```bash
pytest
```

## Contributing
1. Fork the repository
2. Create a feature branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Open a Pull Request

## License
This project is licensed under the MIT License.

