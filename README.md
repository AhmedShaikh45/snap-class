# SnapClass

> A Streamlit-based classroom management prototype designed to connect teachers and students through subjects, enrollment, class sharing, attendance workflows, and AI-assisted voice attendance.

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python\&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit\&logoColor=white)](https://streamlit.io/)
[![Supabase](https://img.shields.io/badge/Supabase-Backend-3ECF8E?logo=supabase\&logoColor=white)](https://supabase.com/)
[![scikit--learn](https://img.shields.io/badge/scikit--learn-ML-F7931E?logo=scikit-learn\&logoColor=white)](https://scikit-learn.org/)
[![Face Recognition](https://img.shields.io/badge/Face%20Recognition-Computer%20Vision-000000)](https://github.com/ageitgey/face_recognition)
[![Segno](https://img.shields.io/badge/Segno-QR%20Codes-8A2BE2)](https://github.com/heuer/segno)

---

## Table of Contents

* [Overview](#overview)
* [Project Goal](#project-goal)
* [Current State](#current-state)
* [Core Concept](#core-concept)
* [Features](#features)
* [User Roles](#user-roles)
* [Teacher Workflow](#teacher-workflow)
* [Student Workflow](#student-workflow)
* [Attendance Architecture](#attendance-architecture)
* [Voice Attendance](#voice-attendance)
* [Face Recognition Direction](#face-recognition-direction)
* [Subject Management](#subject-management)
* [Enrollment and Class Sharing](#enrollment-and-class-sharing)
* [QR Code Generation](#qr-code-generation)
* [Application Architecture](#application-architecture)
* [Project Structure](#project-structure)
* [Technology Stack](#technology-stack)
* [Requirements](#requirements)
* [Installation](#installation)
* [Environment Configuration](#environment-configuration)
* [Running the Application](#running-the-application)
* [How the Streamlit App Works](#how-the-streamlit-app-works)
* [UI and Design System](#ui-and-design-system)
* [Data Model Direction](#data-model-direction)
* [Security Considerations](#security-considerations)
* [Known Limitations](#known-limitations)
* [Development Status](#development-status)
* [Recommended Development Roadmap](#recommended-development-roadmap)
* [Future Improvements](#future-improvements)
* [Contributing](#contributing)
* [License](#license)
* [Author](#author)

---

# Overview

**SnapClass** is a classroom-management project built with Python and Streamlit.

The project is designed around a simple problem:

> Teachers need a faster way to organize classes, enroll students, share class information, and record attendance without relying on repetitive manual workflows.

SnapClass explores a centralized classroom workflow with two roles:

* **Teacher**
* **Student**

The application entry point allows a user to choose a portal and stores the selected role in Streamlit session state.

The repository also contains components for:

* Subject creation
* Subject cards
* Student enrollment
* Quick enrollment
* Class sharing
* QR-code generation
* Attendance results
* Voice-based attendance
* Photo-related UI
* Custom Streamlit styling

The project is structured as a modular Streamlit application rather than a single large script.

---

# Project Goal

SnapClass is intended to become an AI-assisted classroom platform where teachers can manage subjects and attendance while students can join classes using simple enrollment mechanisms.

The long-term concept can be represented as:

```text
Teacher
   │
   ├── Create Subject
   ├── Manage Class
   ├── Share Class Code / QR
   └── Record Attendance
          │
          ├── Voice Recognition
          └── Face Recognition

Student
   │
   ├── Join Class
   ├── View Enrolled Subjects
   └── Participate in Attendance
```

The current repository contains part of this architecture, with several modules implemented as UI or prototype components and additional backend/recognition modules referenced by the code but not currently present in the tracked source tree.

---

# Current State

The repository is best described as an **active prototype / work in progress**.

The current tracked code includes:

* Streamlit application entry point
* Home portal selection
* Reusable UI components
* Subject card component
* Subject-creation dialog
* Class-sharing dialog
* Voice-attendance dialog
* Quick-enrollment component
* Styling system
* Dependency configuration

The entry point currently references:

```text
src.screens.teacher_screen
src.screens.student_screen
```

and some components reference backend or recognition modules such as:

```text
src.database
src.pipelines
```

Those referenced modules are not currently present in the tracked repository tree on the inspected `main` branch.

Therefore, features such as the complete teacher dashboard, complete student dashboard, database operations, and actual recognition pipelines should be considered **planned/in-progress from the current repository state**, rather than documented as fully runnable functionality.

---

# Core Concept

SnapClass is organized around four major concepts:

## 1. Users

A classroom platform needs different experiences for teachers and students.

The current application stores the selected role in:

```python
st.session_state["login_type"]
```

with values such as:

```text
teacher
student
None
```

---

## 2. Subjects

A subject represents a class/course.

The subject UI supports concepts such as:

* Subject name
* Subject code
* Section
* Teacher ownership
* Student enrollment
* Class sharing

Example:

```text
Subject Name: Introduction to Computer Science
Subject Code: CS101
Section: A
```

---

## 3. Enrollment

Students can be connected to subjects.

The codebase contains components for:

* Direct enrollment
* Quick enrollment
* Enrollment status checking
* Class-code based joining

---

## 4. Attendance

Attendance is intended to be one of the major features.

The repository already contains a voice-attendance UI that:

1. Captures classroom audio.
2. Retrieves enrolled students.
3. Retrieves enrolled students' voice embeddings.
4. Sends the recorded audio and candidate embeddings to an audio-processing pipeline.
5. Produces scores for students.
6. Converts the scores into Present / Absent results.
7. Prepares attendance records for logging.

A separate face-recognition dependency stack is also included in `requirements.txt`, indicating a broader biometric-attendance direction.

---

# Features

## Implemented / Present in Repository

### Role Selection

The home screen provides two entry paths:

* Student Portal
* Teacher Portal

The selected role is stored in Streamlit session state.

---

### Custom Landing Page

The home screen includes:

* SNAP CLASS branding
* Student / teacher portal cards
* Custom colors
* Custom typography
* Hidden Streamlit chrome
* Two-column layout

---

### Subject Creation UI

The repository includes a dialog for creating a subject with:

* Subject Code
* Subject Name
* Section

The component validates that all three values are filled before attempting to create the subject.

---

### Subject Cards

Subjects can be represented using a reusable card containing:

* Subject name
* Subject code
* Section
* Optional statistics

The card uses custom HTML/CSS injected through Streamlit.

---

### Class Sharing

A subject-sharing dialog builds a join URL from a subject code.

The current implementation generates a URL in the following form:

```text
snapclass-main.streamlit.app/?join-code=<subject-code>
```

The class information can be shared through:

* Direct link
* Subject code
* QR code

---

### QR Code Generation

The project uses **Segno** to create a QR code for classroom joining.

Flow:

```text
Subject Code
      ↓
Join URL
      ↓
Segno
      ↓
PNG QR Code
      ↓
Display / Share
```

---

### Voice Attendance UI

The repository contains a dedicated Streamlit dialog called:

```text
Voice Attendance
```

The teacher can record classroom audio using Streamlit's audio input widget.

The system then prepares the recorded audio for recognition.

---

### Attendance Result Preparation

The voice-attendance component constructs a Pandas DataFrame with fields including:

* Name
* ID
* Source
* Status

Example status values:

```text
Present
Absent
```

The component also prepares attendance log records containing:

* student ID
* subject ID
* timestamp
* presence flag

---

# User Roles

SnapClass is designed around two roles.

## Teacher

The teacher portal is intended for classroom administration.

The intended responsibilities include:

* Creating subjects
* Managing classes
* Sharing classes
* Managing enrollment
* Recording attendance
* Viewing attendance results

The current repository contains multiple teacher-oriented components, but the complete teacher dashboard is still under development.

---

## Student

The student portal is intended for:

* Joining subjects
* Managing enrollment
* Accessing enrolled classes
* Participating in attendance workflows

The student screen is referenced by the main application but is only a minimal placeholder in the current tracked repository.

---

# Teacher Workflow

The intended workflow is:

```text
Teacher
   ↓
Teacher Portal
   ↓
Create Subject
   ↓
Subject Created
   ↓
Share Class Code / QR
   ↓
Students Join
   ↓
Attendance
   ↓
Attendance Results
```

### Creating a Subject

The subject-creation dialog asks for:

```text
Subject Code
Subject Name
Section
```

Example:

```text
CS101
Introduction to Computer Science
A
```

---

# Student Workflow

The intended student flow is:

```text
Student Portal
      ↓
Find / Join Subject
      ↓
Enter or Scan Class Code
      ↓
Enrollment
      ↓
View Subject
      ↓
Attendance
```

The quick-enrollment component is designed around subject-code-based joining.

---

# Attendance Architecture

Attendance is intended to support automated recognition.

The project shows two recognition directions:

1. **Voice-based recognition**
2. **Face-based recognition**

These are separate modalities that could potentially be used together.

---

# Voice Attendance

The current voice attendance component is one of the most detailed functional pieces in the repository.

## User Flow

The teacher opens:

```text
Voice Attendance
```

and sees instructions to record students saying that they are present.

The teacher then records classroom audio.

---

## Step 1 — Capture Audio

The application uses:

```python
st.audio_input("Record classroom audio")
```

The captured audio is read into bytes.

---

## Step 2 — Retrieve Enrolled Students

The component queries the backend for students enrolled in the selected subject.

Conceptually:

```text
Selected Subject
      ↓
subject_students
      ↓
students
```

---

## Step 3 — Retrieve Voice Profiles

For enrolled students with stored voice profiles, the component prepares:

```python
{
    student_id: voice_embedding
}
```

These become candidate profiles for the recognition pipeline.

---

## Step 4 — Process Audio

The component calls:

```python
process_bulk_audio(
    audio_bytes,
    candidates_dict
)
```

The expected result is a student-to-score mapping.

Conceptually:

```text
Student A → recognition score
Student B → recognition score
Student C → recognition score
```

---

## Step 5 — Convert Scores to Attendance

The current UI converts a positive score into presence:

```text
score > 0
    ↓
Present
```

otherwise:

```text
Absent
```

The result contains:

* Student name
* Student ID
* Recognition source/score
* Attendance status

---

## Step 6 — Prepare Attendance Logs

The component prepares records containing:

```text
student_id
subject_id
timestamp
is_present
```

These records are passed to the attendance-result workflow.

---

# Face Recognition Direction

The current `requirements.txt` includes dependencies associated with face-recognition workflows:

```text
scikit-learn
dlib-bin
face_recognition_models
```

This indicates that biometric attendance is part of the project's intended architecture.

However, the actual face-recognition processing pipeline is not present in the current tracked repository tree.

Therefore, face recognition should currently be understood as an **intended / in-progress subsystem**, not as a fully runnable feature.

A future face-attendance pipeline could follow:

```text
Camera / Image
      ↓
Face Detection
      ↓
Face Encoding
      ↓
Compare with Registered Students
      ↓
Similarity / Distance
      ↓
Attendance Decision
      ↓
Attendance Database
```

---

# Subject Management

Subjects are represented using:

```text
Name
Code
Section
```

The reusable subject card displays these fields and can optionally display statistics.

The card API accepts:

```python
stats=[
    (icon, label, value),
]
```

This makes it possible to add dashboard information such as:

```text
Students
Attendance
Classes
Assignments
```

without rewriting the component.

---

# Enrollment and Class Sharing

SnapClass includes a class-sharing workflow based around a subject code.

The sharing component constructs a join URL:

```text
snapclass-main.streamlit.app/?join-code=<subject-code>
```

A teacher can then:

* Copy the link
* Copy the subject code
* Share the link by email or messaging
* Display a QR code

This provides a simple mechanism for students to join a class.

---

# QR Code Generation

The QR workflow uses **Segno**.

The process is:

```text
Subject Code
      ↓
Join URL
      ↓
segno.make()
      ↓
PNG
      ↓
Streamlit Image
```

The generated QR code is displayed with a classroom-joining caption.

---

# Application Architecture

The project follows a lightweight modular architecture.

```text
SnapClass
│
├── app.py
│
├── screens/
│     ├── home_screen.py
│     ├── teacher_screen.py
│     └── student_screen.py
│
├── components/
│     ├── subject_card.py
│     ├── header.py
│     ├── footer.py
│     ├── enrollment dialogs
│     ├── attendance dialogs
│     └── sharing dialogs
│
└── ui/
      └── base_layout.py
```

The architecture also leaves room for backend modules such as:

```text
database/
pipelines/
recognition/
services/
```

which are referenced by some components.

---

# Project Structure

The currently tracked repository is:

```text
snap-class/
│
├── .gitignore
├── app.py
├── requirements.txt
│
└── src/
    │
    ├── components/
    │   ├── dialog_add_photo.py
    │   ├── dialog_attendance_results.py
    │   ├── dialog_auto_enroll.py
    │   ├── dialog_create_subject.py
    │   ├── dialog_enroll.py
    │   ├── dialog_share_subject.py
    │   ├── dialog_voice_attendance.py
    │   ├── footer.py
    │   ├── header.py
    │   └── subject_card.py
    │
    ├── screens/
    │   ├── home_screen.py
    │   ├── student_screen.py
    │   └── teacher_screen.py
    │
    └── ui/
        └── base_layout.py
```

---

# Technology Stack

## Application

* Python
* Streamlit

## Data Processing

* NumPy
* Pandas

## Machine Learning

* scikit-learn

## Computer Vision

* dlib
* face recognition model package

## Backend

* Supabase

## Security

* bcrypt

## QR Codes

* Segno

## Image Processing

* Pillow

---

# Requirements

The current `requirements.txt` declares:

```text
numpy
pandas
scikit-learn
dlib-bin
git+https://github.com/ageitgey/face_recognition_models
setuptools<70.0.0
supabase
bcrypt
segno
pillow
streamlit
```

---

# Installation

## 1. Clone the Repository

```bash
git clone https://github.com/AhmedShaikh45/snap-class.git
cd snap-class
```

---

## 2. Create a Virtual Environment

### Windows

```powershell
python -m venv venv
.\venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

The dependency list contains `dlib-bin` and a GitHub-hosted face-recognition model package, so installation may take longer than a typical Streamlit application.

---

# Environment Configuration

The repository ignores:

```text
.env
```

which is appropriate for storing local secrets.

Some source files reference a Supabase configuration module that is not currently included in the tracked source tree. Therefore, the exact configuration interface cannot be verified from the current repository snapshot.

A typical setup would use values such as:

```env
SUPABASE_URL=your_project_url
SUPABASE_KEY=your_key
```

Use the exact variable names required by your final `src/database/config.py` implementation when that backend module is added.

Never commit database credentials or private keys to GitHub.

---

# Running the Application

From the project root:

```bash
streamlit run app.py
```

The application will start through Streamlit and provide a local browser URL.

---

# How the Streamlit App Works

The main entry point is:

```text
app.py
```

It imports:

```python
home_screen
teacher_screen
student_screen
```

The application initializes:

```python
st.session_state["login_type"] = None
```

when the session begins.

Navigation then follows this state model:

```text
login_type = None
        ↓
Home Screen

login_type = "teacher"
        ↓
Teacher Screen

login_type = "student"
        ↓
Student Screen
```

This provides a simple role-selection state machine.

---

# UI and Design System

SnapClass uses a custom UI layer rather than relying entirely on Streamlit's default styling.

The primary styling file is:

```text
src/ui/base_layout.py
```

---

## Home Background

The home screen uses:

```text
#5865F2
```

as the primary background.

Portal containers use:

```text
#E0E3FF
```

---

## Accent Color

Subject cards use:

```text
#EB459E
```

for borders and accents.

---

## Typography

The design imports:

* Climate Crisis
* Outfit

The current styling uses:

* **Climate Crisis** for large headings
* **Outfit** for body text and supporting copy

---

## Streamlit Chrome

The project hides Streamlit's default:

* Header
* Footer
* Main menu

to create a more application-like interface.

---

# Data Model Direction

The current components reference several logical entities.

A high-level model is:

```text
Teacher
   │
   └── Subjects
          │
          ├── Students
          │      │
          │      └── Voice Profile
          │
          └── Attendance
```

The voice-attendance component specifically references:

```text
subject_students
students
```

and a student record containing fields such as:

```text
student_id
name
voice_embedding
```

This implies a many-to-many student-to-subject relationship.

A production implementation could use:

```text
teachers
students
subjects
subject_students
attendance
```

as the core relational structure.

---

# Security Considerations

SnapClass is intended to work with student identity and potentially biometric information.

This makes security particularly important for any production deployment.

## Secrets

Never commit:

* Supabase keys
* Database passwords
* Service-role keys
* API keys
* Encryption keys

---

## Passwords

The repository includes:

```text
bcrypt
```

which is appropriate for password hashing.

Passwords should never be stored as plaintext.

---

## Biometric Data

The project references:

```text
voice_embedding
```

and face-recognition tooling.

These should be treated as sensitive information.

Production deployments should consider:

* Encryption at rest
* Encrypted transport
* Access control
* Data minimization
* Explicit consent
* Retention limits
* Secure deletion

---

## Role-Based Access

Teacher and student data should not be accessible interchangeably.

Supabase Row Level Security or equivalent backend authorization should be used before production deployment.

---

# Known Limitations

## 1. Prototype State

The project is not yet a complete production-ready classroom management system.

Several components are present, but some supporting backend and recognition modules are missing from the current tracked tree.

---

## 2. Teacher Screen

The main application references:

```text
src/screens/teacher_screen.py
```

but the tracked implementation is currently only a minimal placeholder.

---

## 3. Student Screen

Likewise:

```text
src/screens/student_screen.py
```

is currently a minimal placeholder.

---

## 4. Missing Backend Modules

Some UI components import:

```text
src.database
src.pipelines
```

but those packages are not currently present in the inspected repository tree.

---

## 5. Local Windows Asset Paths

The current home screen and header reference Windows-specific files under:

```text
C:\Users\Ahmed\Downloads\
```

These paths are machine-specific and will not work on another computer.

For portability, move image assets into the repository and use relative paths.

---

## 6. Voice Recognition Pipeline

The voice-attendance component references:

```text
src.pipelines.voice_pipeline
```

but this module is not currently in the tracked repository.

Therefore the current repository contains the **voice-attendance interface and orchestration logic**, but not the full recognition implementation.

---

## 7. Face Recognition Pipeline

The repository includes face-recognition dependencies, but an operational face-recognition pipeline is not present in the current source tree.

---

## 8. Production Authentication

The current role-switching logic is based on Streamlit session state.

That is not sufficient by itself for secure multi-user authentication.

---

# Development Status

| Area                             | Status                                  |
| -------------------------------- | --------------------------------------- |
| Streamlit application shell      | Present                                 |
| Student / Teacher role selection | Present                                 |
| Custom UI styling                | Present                                 |
| Subject creation UI              | Present                                 |
| Subject card UI                  | Present                                 |
| Class sharing UI                 | Present                                 |
| QR generation                    | Present                                 |
| Voice attendance UI              | Present                                 |
| Attendance result preparation    | Present                                 |
| Supabase backend implementation  | Referenced / incomplete in current tree |
| Teacher dashboard                | In progress                             |
| Student dashboard                | In progress                             |
| Voice recognition engine         | Referenced / missing in current tree    |
| Face recognition engine          | Intended / missing in current tree      |
| Production authentication        | Incomplete                              |

---

# Recommended Development Roadmap

## Phase 1 — Backend

Implement:

* Supabase configuration
* Database schema
* Teacher table
* Student table
* Subject table
* Enrollment relationship
* Attendance table
* Voice profile storage

---

## Phase 2 — Authentication

Add:

* Teacher registration
* Student registration
* Login
* Password hashing
* Session management
* Role-based authorization

---

## Phase 3 — Teacher Dashboard

Build:

* Subject creation
* Subject management
* Student list
* Enrollment management
* Attendance dashboard
* Attendance export
* Class sharing

---

## Phase 4 — Student Dashboard

Build:

* Subject list
* Join-by-code
* QR-code joining
* Enrollment status
* Attendance history

---

## Phase 5 — Voice Recognition

Implement:

* Voice enrollment
* Voice embeddings
* Audio preprocessing
* Speaker recognition
* Confidence thresholds
* Multi-speaker handling
* Attendance decision logic

---

## Phase 6 — Face Recognition

Implement:

* Face enrollment
* Face embeddings
* Classroom camera capture
* Multiple-face detection
* Face matching
* Confidence thresholds
* Attendance logging

---

## Phase 7 — Analytics

Add:

* Attendance percentages
* Weekly trends
* Monthly trends
* Subject statistics
* Absence alerts
* Student attendance reports
* CSV/PDF exports

---

# Future Improvements

## AI Features

Potential AI functionality:

* AI-generated attendance summaries
* Attendance anomaly detection
* Natural-language attendance queries
* Student performance insights
* AI classroom assistant
* Automated absence summaries

---

## Computer Vision

Potential improvements:

* Real-time classroom face recognition
* Multi-person face tracking
* Liveness detection
* Better lighting robustness
* Camera calibration
* Multiple camera support

---

## Voice AI

Potential improvements:

* Speaker diarization
* Better voice embeddings
* Noise suppression
* Multiple-language support
* Confidence calibration
* Automatic segmentation of multiple students speaking

---

## Classroom Management

Possible future modules:

* Assignments
* Announcements
* Notes
* Timetable
* Exams
* Student performance tracking
* Teacher dashboards
* Parent notifications

---

# Contributing

Contributions are welcome.

Create a branch:

```bash
git checkout -b feature/your-feature
```

Make your changes:

```bash
git add .
git commit -m "Add your feature"
```

Push the branch:

```bash
git push origin feature/your-feature
```

Then open a pull request.

For new UI components, prefer:

```text
src/components/
```

For screen-level logic:

```text
src/screens/
```

For shared styling:

```text
src/ui/
```

As the application grows, keep backend and recognition logic separated from presentation code.

---

# License

No explicit license file is currently present in the repository.

Until a license is added, do not assume that the project has been released under a specific open-source license.

---

# Author

## Ahmed Shaikh

GitHub:

https://github.com/AhmedShaikh45

Repository:

https://github.com/AhmedShaikh45/snap-class

---

# Project Summary

SnapClass demonstrates how a classroom-management platform can combine:

```text
Streamlit
     +
Supabase
     +
Machine Learning
     +
Computer Vision
     +
Voice Recognition
     +
QR Codes
     +
Attendance Automation
     =
AI-Assisted Classroom Management
```

The project demonstrates practical work across:

* Python
* Streamlit
* Modular UI architecture
* Session-state navigation
* Supabase-oriented application design
* Machine learning dependencies
* Computer vision
* Voice recognition architecture
* QR-code generation
* Attendance automation
* Security considerations for identity data

The current repository is an evolving prototype: the application shell and core UI workflows are in place, while the backend, complete dashboards, and biometric recognition layers are positioned for further implementation.
