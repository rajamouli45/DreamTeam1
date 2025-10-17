
Software Requirements Specification (SRS)

Project: Fable Website

`1. Introduction`
Purpose:
 To develop a simple website where users can read, write, and share short fables or stories.
Scope:
 The system allows users to register, log in, post stories, read others' stories, and comment on them.
 Admin can manage stories and users.
Technologies:
Frontend: HTML, CSS, JavaScript, Next.js
Backend: Python Flask
Database: MySQL

`2. Overall Description`
Users:
Reader: Reads and comments on stories.
Writer: Adds, edits, and deletes their stories.
Admin: Manages users and content.

Features:
User registration and login
Story upload and management
Reading and commenting system
Admin controls

Environment:
 Runs on any modern browser (Chrome, Edge, Firefox).


`3. Functional Requirements`
User Login/Signup:
 Register with name, email, and password; login securely.
Story Management:
 Add, edit, delete, and view stories by category.
Commenting System:
 Logged-in users can comment on stories.
Admin Features:
 Admin can remove inappropriate stories or users.


`4. Non-Functional Requirements`
TypeRequirementPerformancePages load within 3 secondsSecurityEncrypt passwordsUsabilitySimple, clean UIReliabilitySmooth performance without crashesScalabilityCan add more features later


`5. Database Structure`
Users: user_id, name, email, password, role
Stories: story_id, title, category, content, author_id, date
Comments: comment_id, story_id, user_id, text, date


`6. Future Enhancements`
Add likes/ratings
Upload story cover images
Add dark mode
Mobile app version

`7. Conclusion`
The Fable Website will be a simple and interactive storytelling platform built using Next.js, Flask, and MySQL, suitable for beginners to develop and expand.
