# Digital Education Competency Quiz
A fun and practical quiz that focuses on practical, everyday digital platforms and behaviours for education staff.

## Introduction

The Digital Education Competency (DEC) Quiz App is a minimum viable product developed for the Department for Education (DfE) to support assessment of digital capability across schools in England. The DfE has introduced six core digital standards that will become mandatory from 2030, and the app provides a simple way to gather insight that can inform targeted training and future guidance for the sector.

The desktop application is built using Python and Tkinter. It begins by collecting the user’s name and school before presenting six multiple‑choice questions, each mapped to one of the DfE’s digital standards. The MVP is aimed at school leaders and is designed to explore how they might respond to realistic digital‑related scenarios. The questions are written so that users can apply logic to reach the correct answer, helping build confidence while still offering meaningful data.

Validation rules and GUI prompts ensure that users provide valid information, including acceptable characters for names and schools, and that each question has a selected response. These checks help maintain clean, reliable data suitable for later analysis. Questions are loaded from a CSV file, and user submissions are stored in another CSV, chosen for its accessibility, portability and compatibility with widely used software.

Because the purpose of the app is to gather insight rather than assess performance, no score or correct answers are shown at the end. This avoids implying a pass or fail and keeps the focus on supportive development.

Future iterations could introduce data analysis, visualisation, customisable questions, differentiated access levels and enhanced accessibility features. The MVP keeps scope intentionally limited to core functionality, enabling rapid deployment, early user feedback, stakeholder confidence and a clear direction for future development.

## Design

### User Experience Mapping

I’ve developed a user persona map and a persona matrix to capture the range of personalities and behaviours that exist across the education community. Instead of relying on a single stereotypical profile for each role, this approach is intentionally more inclusive and better reflects real‑world diversity. People in the same position can have very different levels of digital confidence and experience, so a behaviour‑based model provides a more accurate foundation for design decisions. For example, not all governors are retired with low technology confidence; some may work in ICT or digital roles in their day‑to‑day careers. By focusing on behaviours, motivations and capability rather than assumptions about age or background, the personas offer a more representative and equitable view of the users the system needs to support.

User Personas:

**Figure 1:** Below is my User Persona Map. I have created six personas that can be broadly applied to individuals working across the education sector. The names have been selected carefully to avoid implying bias related to gender, age or ethnicity. Each persona includes an overarching tagline and a more detailed description. Developing this User Persona Map is valuable because it helps shape the design of my application and can support the DfE in planning future training and guidance for schools.

<img src="doc_assets/User_Personas.png" alt="Figure 1: A User Persona Map showing 6 fictional personas designed to replicate typical school capabilities" width="400">

**Figure 1:** User Persona Map

Personas Matrix:

**Figure 2:** The next item is the User Persona Matrix. This takes the personality profiles from the map and plots how my application, alongside a wider training and guidance package, could support the development of each persona. The horizontal axis represents confidence, while the vertical axis represents actual capability. Each persona is shown using an emoji placed at the point that best reflects their current position, with an arrow indicating the direction in which they could develop in the short to medium term. The overall aim is to move more personas toward higher levels of confidence and capability. This approach also recognises the gap that can exist between perceived and actual ability. For example, the “Cautious User” is highly capable but unlikely to reach the highest levels of confidence due to their naturally cautious disposition. Similarly, the “Confident Collaborator” appears to lose confidence as capability increases; this reflects the idea that greater expertise often brings greater awareness of risk, tempering overconfidence.

<img src="doc_assets/Persona_Matrix.png" alt="Figure 2: A Persona Matrix, plotting typical confidence vs capability, along with trends for improvement" width="1500">

**Figure 2:** User Persona Matrix

### GUI Prototyping

**Figure 3:** A wireframe was produced during the initial planning phase to outline how users would move through the quiz. It maps the sequence of interactions, beginning with entering name and school, progressing through each question, and concluding with the submission confirmation. Included in the design are indicative error-handling prompts.

Its purpose was to organise the arrangement of screens, identify where validation should occur, and establish the overall navigation logic before any coding took place. The wireframe focuses purely on flow and interaction rather than visual styling, acting as a structural guide rather than a final design

<img src="doc_assets/EdTech_Quiz_Prototype.png" alt="Figure 3: A prototype wireframe demonstrating user journey for completion of the EdTech Quiz" width="1386">

**Figure 3:** Wireframe

### Accessibility Assessment

(Need to do and incorporate things I've put into func and non-func requirements

### Functional and Non-Functional Requirements 

Functional Requirements

| ID   | Requirement |
|------|-------------|
| FR1  | The application must allow a participant to enter their name. |
| FR2  | The application must allow a participant to enter their school name. |
| FR3  | The application must validate that both fields are completed before starting the quiz. |
| FR4  | The application must load quiz questions from a CSV file. |
| FR5  | The application must display one question at a time. |
| FR6  | The application must show four answer options (A, B, C, D). |
| FR7  | The application must allow the participant to select exactly one answer per question. |
| FR8  | The application must prevent the participant from progressing without selecting an answer. |
| FR9  | The application must move to the next question after an answer is submitted. |
| FR10 | The application must record all selected answers in order. |
| FR11 | The application must detect when the final question has been answered. |
| FR12 | The application must save the participant’s name, school, and answers to a CSV file. |
| FR13 | The application must create the results file with a header if it does not already exist. |
| FR14 | The application must append new results without overwriting previous entries. |
| FR15 | The application must show warnings for missing information or missing answers. |
| FR16 | The application must show a confirmation message when results are saved. |
| FR17 | The application must close the quiz window after completion. |

Non-Functional Requirements

| ID    | Requirement |
|-------|-------------|
| NFR1  | The interface must be simple and easy for non-technical users to understand. |
| NFR2  | All labels, buttons, and text fields must be clearly visible and readable. |
| NFR3  | The system must handle missing or malformed CSV files gracefully. |
| NFR4  | The system must not crash if the results file already exists. |
| NFR5  | Loading questions must be completed within one second. |
| NFR6  | Saving results must complete within one second. |
| NFR7  | The application must run on Windows systems with Python and Tkinter installed. |
| NFR8  | The application must not require internet access. |
| NFR9  | Pure logic functions must be separated from GUI code. |
| NFR10 | The system must allow unit tests to import functions without launching the GUI. |
| NFR11 | The system must use standard Tkinter widgets compatible with assistive technologies. |
| NFR12 | The system must avoid colour-only cues to ensure clarity for all users. |
| NFR13 | The system must store only name and school; no sensitive data. |
| NFR14 | All data must be stored locally and not transmitted externally. |


### Tech Stack Online 

- [Python 3](https://docs.python.org/3/) — Core programming language. Used for all application logic, file handling, and user interaction.
- [Tkinter](https://docs.python.org/3/library/tkinter.html) — Desktop graphical user interface. Provides the graphical interface for entering user details and navigating quiz questions.
- [csv](https://docs.python.org/3/library/csv.html) — Local data storage in CSV format. Stores quiz questions, answers and user data.
- [unittest](https://docs.python.org/3/library/unittest.html) — Automated unit testing. Used for smoke tests and functional checks of pure functions.

### Code Design Document
To do

