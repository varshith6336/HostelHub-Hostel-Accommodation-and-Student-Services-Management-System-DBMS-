# HostelHub — Hostel Accommodation & Student Services Management System

**DBMS Project 06**

## Project files
- [`index.html`](index.html) — standalone HostelHub website demo.
- [`database/hostelhub.sql`](database/hostelhub.sql) — MySQL database schema.
- [`backend/app.py`](backend/app.py) — starter Flask API.
- [`backend/requirements.txt`](backend/requirements.txt) — Python dependencies.
- [`report/Hostel_DBMS_PBL_Report_HostelHub.docx`](report/Hostel_DBMS_PBL_Report_HostelHub.docx) — project report, if included in this repository.
- [`HostelHub_DBMS_Presentation.pptx`](HostelHub_DBMS_Presentation.pptx) — project presentation slides.

## Project presentation
[**Open or download the HostelHub DBMS presentation (.pptx)**](HostelHub_DBMS_Presentation.pptx)

To view it, download the PowerPoint file from this repository and open it with Microsoft PowerPoint or another compatible presentation app. GitHub may not display the slides directly in its code viewer.

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
In repository **Settings → Pages**, choose **Deploy from a branch**, select `main`, and choose `/(root)`. GitHub Pages hosts the static frontend only; it does not host Flask or MySQL. Never upload `.env` files or database passwords.
