# Hostel Accommodation & Student Services Management System

**HostelHub --- Database Management Systems (DBMS) Project 06**

## Student Details

  Field              Details
  ------------------ -----------------------
  **Student Name**   Navari Varshith Reddy
  **Roll Number**    25WU0102181
  **Mentor**         Dr. Cheekati Nagaraju
  **University**     Woxsen University
  **Project Date**   13 October 2026

------------------------------------------------------------------------

## Project Overview

HostelHub is a hostel accommodation and student-services management
system concept designed to organize student records, rooms and beds,
allocations, complaints, visitor entries, and reports through a web
interface and relational database design.

## Problem Statement

Hostel administration may face double-booked beds, rooms exceeding
capacity, missed fee dues, and complaints that are difficult to track.
HostelHub aims to organize these records and support consistent
validation through a structured database design.

## Objectives

-   Maintain student and hostel room information in an organized way.
-   Track room and bed availability.
-   Record student-to-room allocations.
-   Manage complaints and visitor entries.
-   Provide summary information through a dashboard and reports.
-   Apply database integrity rules to reduce inconsistent records.

## Main Website Modules

1.  **Dashboard** --- Summary of hostel activity and occupancy.
2.  **Students** --- Student directory and registration interface.
3.  **Rooms & Beds** --- Room capacity and bed availability.
4.  **Allocations** --- Student room-allocation register.
5.  **Complaints** --- Complaint and maintenance tracking.
6.  **Visitor Log** --- Visitor registration and status.
7.  **Reports** --- Summary of occupancy and student services.

## Database Design

The project presentation describes a design with 17 entities and 18
one-to-many relationships. It presents the schema as normalised to Third
Normal Form (3NF), with database constraints, partial unique indexes,
six triggers, and eight views.

The core relationship chain is:

`Student → Allocation ← Bed ← Room ← Hostel Block`

Related records include fee schedules, payments, complaints, maintenance
requests, visitors, and transfers.

## Database Integrity Rules

The presentation describes database checks for:

-   One active resident per bed.
-   One active allocation per student.
-   Gender-matched hostel blocks.
-   Valid allocation dates.
-   Payments not exceeding the billed fee.
-   Bed counts not exceeding room capacity.
-   Visitors being associated with residents.

The presentation reports that 11 out of 11 rule-breaking statements were
rejected in its database tests.

## Sample Results in the Presentation

-   **Students:** 3 records --- 2 Active and 1 Pending.
-   **Rooms:** 3 records with a total capacity of 7 beds.
-   **Beds:** 7 records --- 4 Occupied and 3 Available.

These are example results shown in the presentation, not live production
data.

## Testing Summary

The presentation reports 18 interface tests passed and 11 database
rule-violation tests rejected. It also reports no JavaScript errors
during the test run.

## Technologies

-   HTML and CSS --- web interface
-   JavaScript --- interface behavior and validation
-   Python Flask --- starter backend API
-   MySQL --- relational database design

## Repository Files

-   `index.html` --- website interface
-   `app.py` --- starter Flask API
-   `requirements.txt` --- Python dependencies
-   `.gitignore` --- files Git should ignore
-   `database/hostelhub.sql` --- SQL schema, if uploaded to the
    repository

## Future Scope

-   Connect the web interface to MySQL through the backend.
-   Add fee, transfer, and vacating screens.
-   Add login and role-based access.
-   Add fee-due notifications and report export.

## How to View the Website

Open `index.html` in a browser, or configure GitHub Pages in the
repository settings to publish the static frontend.

> **Implementation note:** The current website preview uses sample data
> in browser memory and is not connected to MySQL. The Flask backend
> requires configuration and deployment before it can be used online.

------------------------------------------------------------------------

**HostelHub \| DBMS Project 06 \| Woxsen University**
