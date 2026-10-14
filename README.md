# HostelHub — Hostel Accommodation & Student Services Management System

**DBMS Project 06**

## Files
- `index.html`: current standalone website demo.
- `database/hostelhub.sql`: MySQL schema.
- `backend/app.py`: starter Flask API with MySQL health check and student list/create endpoints.
- `backend/requirements.txt`: Python dependencies.
- `report/`: project report, if included in this package.

## Website demo
Open `index.html` in a browser or publish it with GitHub Pages. The current frontend uses in-browser sample data. Its forms are **not yet connected to the Flask API**, so changes are temporary and are not stored in MySQL.

## Create the database
1. Open MySQL Workbench and connect to your MySQL Server.
2. Open `database/hostelhub.sql` and execute it.
3. Refresh Schemas and check for `hostelhub`.

## Run the starter API locally
Install Python 3.10+, open a terminal in `backend`, then run `pip install -r requirements.txt`. In PowerShell set your own credentials (do not commit passwords):

```powershell
$env:DB_HOST="127.0.0.1"
$env:DB_PORT="3306"
$env:DB_NAME="hostelhub"
$env:DB_USER="your_mysql_username"
$env:DB_PASSWORD="your_mysql_password"
python app.py
```

Visit `http://127.0.0.1:5000/api/health` and `http://127.0.0.1:5000/api/students`. API routes currently cover health, listing students, and creating students only. The frontend still needs to be wired to the API and all CRUD flows tested before claiming full integration.

## GitHub Pages
In repository Settings → Pages, choose Deploy from a branch, `main`, and `/(root)`. GitHub Pages hosts the static frontend only; it does not host Flask or MySQL. Never upload `.env` files or database passwords.
