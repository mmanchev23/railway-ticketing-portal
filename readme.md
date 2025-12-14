#  Railway Ticketing Portal 

**Course Project:** Software Testing & Quality Assurance
**Status:** Complete

## 📖 Project Description

The **Railway Ticketing Portal** is a software solution designed to manage railway bookings. The system handles distance-based pricing, dynamic rules (Rush Hour vs. Saver tickets), various passenger discounts (Senior, Family, Child), and reservation management.

This repository serves as a comprehensive **Software Testing Portfolio**, demonstrating the full lifecycle of testing—from requirements engineering and static inspection to white-box unit testing and black-box functional testing.

## 🎯 Project Goals

The primary goal of this project is to implement a core booking engine and subject it to rigorous testing methodologies to ensure quality and reliability. Key objectives include:

* Defining strict Functional and Non-Functional Requirements.
* Performing Static Testing (Inspections and Code Reviews).
* Implementing Structural (White-Box) Testing using Control Flow Graphs and Coverage Metrics
* Implementing Functional (Black-Box) Testing using BVA, ECP, and State Transitions.
* Ensuring full Requirement Traceability.

## ✅ Achievements & Roadmap

The following deliverables have been completed according to the course scoring criteria:

- [x] **Lab 1: Requirements Engineering**
    - [x] Functional (FR) & Non-Functional (NFR) Requirements list created.
    - [x] Behavior Driven Development (BDD) Scenarios defined in Gherkin syntax.
- [x] **Lab 2: Static Testing**
    - [x] Formal Requirement Inspection performed using a checklist.
    - [x] Self-Code Review executed with a defect report.
- [x] **Lab 3: White-Box Testing Design**
    - [x] Control Flow Graph (CFG) drawn for the pricing logic.
    - [x] Test cases designed for Statement (SC), Decision (DC), and Condition Coverage (CC).
- [x] **Lab 4: Unit Testing Implementation**
    - [x] `unittest` framework implemented for structural tests.
- [x] **Lab 5: Refactoring & Implementation**
    - [x] Code refactored for modularity.
    - [x] Implemented Profiles and Reservation features.
- [x] **Lab 6: Functional Testing**
    - [x] Requirement Traceability Matrix (RTM) created.
    - [x] Implemented Boundary Value Analysis (BVA) & Equivalence Class Partitioning (ECP).
    - [x] Implemented Decision Table & State Transition tests.
- [x] **Lab 7: Validation Plan**
    - [x] Final Validation, Verification, and Testing Plan document created.

## 📂 Project Structure

Below is an explanation of the files and directories in this repository.

### **Root Directory**

  * **`main.py`**: The entry point for manual verification of the system. Runs a quick "Smoke Test" of the pricing logic.
  * **`utils/`**: The source code package containing the system logic.
      * `system.py`: The core engine containing `calculate_price`, `search_trains`, and booking logic.
      * `passenger.py`: Defines passenger attributes and logic for age/card discounts.
      * `ticket.py`: Handles time parsing and ticket properties.
      * `reservation.py`: Manages reservation states (Confirmed/Cancelled).
      * `profile.py`: Manages user data.
  * **`labs/`**: Contains the specific deliverables for each course milestone.
    * `lab1/` (Requirements)
        * `fr.xlsx`: Detailed list of Functional Requirements.
        * `gherkin.docx`: Feature files describing scenarios in Given/When/Then format.
        * `Lab01 - Railway ticketing portal.pdf`: Original assignment instructions.
        * `nfr.xlsx`: Detailed list of Non-Functional Requirements.
    * `lab2/` (Static Testing)
        * `inspection.docx`: Report on the formal inspection of requirements.
        * `Lab02 - ReqChecklist.pdf` & `StaticTesting.pdf`: Templates and instructions used.
        * `review.docx`: Report on defects found during code review.
    * `lab3/` (Structure-Based Testing)
        * `cfg.png` / `cfg.drawio`: Visual Control Flow Graph of the `calculate_price` function.
        * `white-box.docx`: Documentation of test paths for SC, DC, and CC coverage.
    * `lab4/` (Unit Testing)
        * `tests.py`: Python script implementing the White-Box tests using `unittest`.
    * `lab5/` (Refactoring)
        * `refactoring.docx`: Notes on code improvements and new features added.
    * `lab6/` (Functional Testing)
        * `tests.py`: Python script implementing Black-Box tests (BVA, ECP, State Transition).
        * `rtm.docx`: Requirement Traceability Matrix mapping FRs to Test Cases.
        * `ftd.docx`: Functional Test Description document.
    * `lab7/` (Final Plan)
        * `plan.docx`: The comprehensive Verification, Validation, and Testing Plan.

## 🚀 How to Run the Tests

To execute the tests, navigate to the root directory and run the specific test modules.

**1. Run Unit Tests (White-Box):**

```bash
python -m unittest labs/lab4/tests.py
```

**2. Run Functional Tests (Black-Box):**

```bash
python -m unittest labs/lab6/tests.py
```

**3. Run Manual Verification:**

```bash
python main.py
```
