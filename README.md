# HostelHub --- Hostel Accommodation & Student Services Management System

**Database Management Systems \| Project 06**

  Project detail      Information
  ------------------- -----------------------
  Student             Navari Varshith Reddy
  Roll Number         25WU0102181
  Mentor              Dr. Cheekati Nagaraju
  University          Woxsen University
  Presentation date   13 October 2026

------------------------------------------------------------------------

## 1. Project Overview

HostelHub is a hostel accommodation and student-services management
system concept designed to organize hostel records through a unified
interface and relational database design. It focuses on student records,
rooms and beds, allocations, complaints, visitor entries, and reports.

## 2. Problem Statement

Hostel administration can face several record-management problems:

-   **Double-booked beds:** one bed may accidentally be assigned to two
    students.
-   **Rooms over capacity:** room occupancy may exceed the intended
    capacity.
-   **Missed fee dues:** payments may be tracked in separate records.
-   **Unresolved complaints:** requests may lack a single place to track
    their progress.

**Objective:** Design a consistent database and interface that helps
prevent these errors through structured records and validation rules.

## 3. Proposed Solution and Architecture

The proposed architecture has four layers:

1.  **Users:** warden, accounts officer, and administrator.
2.  **Interface:** HostelHub web interface built with HTML and CSS, with
    seven screens.
3.  **Application logic:** JavaScript validation and allocation rules.
4.  **Data layer:** relational database schema designed for MySQL.

The presentation describes a database design with 17 entities converted
into 17 relations in Third Normal Form (3NF), with constraints, partial
unique indexes, six triggers, and eight views.

## 4. Main Interface Features

HostelHub presents seven main screens:

-   **Dashboard:** overview of hostel activity, occupancy, available
    beds, and complaints.
-   **Students:** student directory and registration interface.
-   **Rooms & Beds:** room capacity, sharing type, occupied beds, and
    availability.
-   **Allocations:** student-to-room assignment register.
-   **Complaints:** service requests, priorities, and status tracking.
-   **Visitor Log:** visitor registration and check-in/check-out status.
-   **Reports:** occupancy, fee estimates, resident counts, and
    complaint summaries.

## 5. Database Design

The database design shown in the presentation includes 17 entities and
18 one-to-many relationships. It uses crow's-foot notation in the ER
diagram: a bar represents "one," while a crow's foot represents "many."

The core relationship chain is:

`Student → Allocation ← Bed ← Room ← Hostel Block`

Fee records, visitors, complaints, and maintenance requests are also
represented in the data model.

### Normalisation to 3NF

The design aims to store each fact once and reduce duplication:

-   Room capacity is associated with the room type rather than repeated
    in every room record.
-   Fee amounts are stored in `fee_schedule` and referenced through
    `fee_id`.
-   The date a student leaves is stored in `allocation.vacated_on`.
-   Block gender is stored with `hostel_block`.
-   Occupancy and balance are calculated through views instead of being
    stored as duplicated values.

## 6. Database Integrity Rules

The presentation describes database-level checks for key hostel rules:

  Business rule                       Enforcement described in the presentation
  ----------------------------------- -------------------------------------------
  One active resident per bed         Unique index and capacity trigger
  One active allocation per student   Partial unique index
  Gender-matched blocks               Trigger
  Valid allocation dates              CHECK constraint
  Payment does not exceed the fee     Trigger
  Beds do not exceed room capacity    Trigger
  Visitors are only for residents     Trigger

The presentation reports that 11 out of 11 rule-breaking statements were
rejected by the database tests.

## 7. Sample Database Results

The presentation includes example MySQL query results:

-   **Students:** 3 records --- 2 Active and 1 Pending.
-   **Rooms:** 3 records with a total capacity of 7 beds.
-   **Beds:** 7 records --- 4 Occupied and 3 Available.

These are sample results shown in the presentation and should not be
interpreted as live production data.

## 8. Testing and Results

The presentation reports the following test outcomes:

  Area                                 Tests Reported result
  ---------------------------------- ------- -----------------
  HostelHub interface                     18 All passed
  Database rule violations                11 All rejected
  JavaScript errors during the run       --- None reported

Examples include preventing allocation to a room without a free bed,
disabling confirmation when no eligible student is available, rejecting
a male student in a female block, and rejecting a payment that exceeds
the billed fee.

## 9. Conclusion

HostelHub demonstrates how a structured relational database and a web
interface can support hostel administration. Its design emphasizes 3NF
normalisation, integrity constraints, triggers, views, room allocation,
and complaint tracking.

## 10. Future Scope

The presentation identifies the following improvements for future
development:

-   Connect the HostelHub interface to MySQL.
-   Add fee, transfer, and vacating screens.
-   Introduce login and role-based access.
-   Add fee-due notifications and report export.

## 11. Technologies and Project Files

The project materials refer to the following technologies:

-   HTML and CSS for the interface
-   JavaScript for interface behavior and validation
-   Python Flask as a starter backend API
-   MySQL for the relational database

Expected repository files include:

-   `index.html` --- website interface
-   `app.py` --- starter Flask API
-   `requirements.txt` --- Python dependencies
-   `.gitignore` --- files Git should ignore
-   `database/hostelhub.sql` --- database schema, if uploaded

## 12. How to View the Website

Open `index.html` in a web browser, or configure GitHub Pages in the
repository settings to publish the static frontend.

> **Implementation note:** The current website preview uses sample data
> in browser memory and is not yet connected to MySQL. The Flask backend
> also requires configuration and deployment before it can be used
> online. The database results and testing figures above are those
> reported in the project presentation.

------------------------------------------------------------------------

*HostelHub --- DBMS Project 06 \| Woxsen University*
