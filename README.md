# HostelHub --- Hostel Accommodation & Student Services Management System

**DBMS Project 06 \| Database Management Systems**

## Student Details

-   **Student Name:** Navari Varshith Reddy
-   **Roll Number:** 25WU0102181
-   **Mentor:** Dr. Cheekati Nagaraju
-   **University:** Woxsen University
-   **Project Date:** 13 October 2026

------------------------------------------------------------------------

## Project Presentation

This section presents the key information from the HostelHub DBMS
project presentation directly in this README.

### 1. Project Overview

HostelHub is a hostel accommodation and student-services management
system designed to organize student records, room and bed availability,
allocations, complaints, visitor entries, and reports through a web
interface and relational database design.

### 2. Problem Statement

Hostel administration may face problems such as double-booked beds,
rooms exceeding capacity, missed fee dues, and complaints that are
difficult to track. HostelHub aims to organize these records and support
consistent validation through a structured database design.

### 3. Project Objectives

-   Maintain student and hostel room information in an organized way.
-   Track room and bed availability.
-   Record student-to-room allocations.
-   Manage complaints and visitor entries.
-   Provide summary information through a dashboard and reports.
-   Apply database integrity rules to reduce inconsistent records.

### 4. Proposed Solution and System Architecture

The project is presented as a hostel management interface supported by a
relational database design. The architecture can be understood in four
parts:

1.  **Users:** Warden, accounts officer, and administrator.
2.  **Web interface:** HTML and CSS interface with JavaScript behavior.
3.  **Application logic:** Validation and allocation rules.
4.  **Database:** MySQL relational schema for hostel records.

### 5. Main Website Modules

-   **Dashboard:** Overview of hostel activity, occupancy, available
    beds, and complaints.
-   **Students:** Student directory and registration interface.
-   **Rooms & Beds:** Room capacity, sharing type, occupied beds, and
    availability.
-   **Allocations:** Student-to-room assignment register.
-   **Complaints:** Service requests, priorities, and status tracking.
-   **Visitor Log:** Visitor registration and check-in/check-out status.
-   **Reports:** Occupancy, fee estimates, resident counts, and
    complaint summaries.

### 6. Database Design and ER Model

The project presentation describes a database design containing **17
entities** and **18 one-to-many relationships**. It presents the schema
as normalised to **Third Normal Form (3NF)**, with database constraints,
partial unique indexes, six triggers, and eight views.

The core relationship chain is:

`Student → Allocation ← Bed ← Room ← Hostel Block`

Related records include fee schedules, payments, complaints, maintenance
requests, visitors, and transfers. The ER diagram uses crow's-foot
notation to show one-to-many relationships.

### 7. Normalisation to 3NF

The presentation describes the following design choices to reduce
duplication:

-   Room capacity is associated with the room type rather than repeated
    in every room record.
-   Fee amounts are stored in `fee_schedule` and referenced through
    `fee_id`.
-   The date a student leaves is stored in `allocation.vacated_on`.
-   Block gender is stored with `hostel_block`.
-   Occupancy and balance are calculated through views instead of being
    stored as duplicated values.

### 8. Database Integrity Rules

The presentation describes database-level checks for the following
hostel rules:

  Business rule                            Enforcement described in the presentation
  ---------------------------------------- -------------------------------------------
  One active resident per bed              Unique index and capacity trigger
  One active allocation per student        Partial unique index
  Gender-matched blocks                    Trigger
  Valid allocation dates                   CHECK constraint
  Payment does not exceed the fee          Trigger
  Beds do not exceed room capacity         Trigger
  Visitors are associated with residents   Trigger

The presentation reports that **11 out of 11 rule-breaking statements
were rejected** by the database tests.

### 9. Sample Database Results

The presentation includes these example MySQL query results:

-   **Students:** 3 records --- 2 Active and 1 Pending.
-   **Rooms:** 3 records with a total capacity of 7 beds.
-   **Beds:** 7 records --- 4 Occupied and 3 Available.

These are sample results shown in the presentation, not live production
data.

### 10. Testing and Results

The presentation reports the following test outcomes:

  Test area                               Reported result
  --------------------------------------- --------------------------------
  Interface testing                       18 tests passed
  Database rule-violation testing         11 invalid statements rejected
  JavaScript errors during the test run   None reported

Examples shown include preventing allocation to a room without a free
bed, disabling confirmation when no eligible student is available,
rejecting a male student in a female block, and rejecting a payment that
exceeds the billed fee.

### 11. Conclusion

HostelHub demonstrates how a structured relational database and a web
interface can support hostel administration. The project focuses on
normalisation, integrity constraints, triggers, views, room allocation,
student records, and complaint tracking.

### 12. Future Scope

-   Connect the website interface to MySQL through the backend.
-   Add fee, transfer, and vacating screens.
-   Introduce login and role-based access.
-   Add fee-due notifications and report export.

------------------------------------------------------------------------

## Technologies Used

-   **HTML and CSS** --- Web interface
-   **JavaScript** --- Interface behavior and validation
-   **Python Flask** --- Starter backend API
-   **MySQL** --- Relational database design

## Repository Files

-   `index.html` --- Website interface
-   `app.py` --- Starter Flask API
-   `requirements.txt` --- Python dependencies
-   `.gitignore` --- Files Git should ignore
-   `database/hostelhub.sql` --- SQL schema, if uploaded to the
    repository

## How to View the Website

Open `index.html` in a web browser, or configure GitHub Pages in the
repository settings to publish the static frontend.

> **Implementation note:** The current website preview uses sample data
> in browser memory and is not connected to MySQL. The Flask backend
> requires configuration and deployment before it can be used online.
> The database results and test figures above are the results reported
> in the project presentation.

------------------------------------------------------------------------

**HostelHub \| DBMS Project 06 \| Woxsen University**
