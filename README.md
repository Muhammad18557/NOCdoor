# NOCdoor - The Glassdoor for NOC Internships

## Overview

NOCdoor is a platform designed for NUS Overseas Colleges (NOC) students to share and access feedback about their internship experiences. The platform aims to simplify the internship selection process by providing a centralized repository of insights, ratings, and reviews tailored to the unique needs of NOC students.

## Project Structure

- **Frontend**: Built with Next.js and Tailwind CSS.
- **Backend**: Built with FastAPI, SQLAlchemy, and Alembic.

## Requirements

- **Node.js**: For running the frontend application.
- **Python 3.8+**: For running the backend application.
- **PostgreSQL**: For the database.

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Muhammad18557/NOCdoor.git
cd NOCdoor
```

### 2. Frontend

1. Navigate to the `frontend/` directory:

   ```bash
   cd frontend
   ```

2. Install the dependencies:

   ```bash
   npm install
   ```

3. Start the development server:

   ```bash
    npm run dev
   ```

4. Open [http://localhost:3000](http://localhost:3000) in your browser.

### 3. Backend

1. Navigate to the `backend/` directory:
   ```bash
   cd backend
   ```
2. Create a virtual environment:
   ```bash
    python -m venv venv
   ```
3. Activate the virtual environment:
   ```bash
    source venv/bin/activate
   ```
4. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Configure your PostgreSQL database and update the SQLALCHEMY_DATABASE_URL in the `.env` file.
   Apply database migrations using Alembic:

   ```bash
   alembic upgrade head
   ```

6. Start the backend server:
   ```bash
   uvicorn app.main:app --reload
   ```
7. Open [http://localhost:8000](http://localhost:8000) in your browser.
