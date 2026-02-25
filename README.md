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

### User Personas:

**Figure 1:** Below is my User Persona Map. I have created six personas that can be broadly applied to individuals working across the education sector. The names have been selected carefully to avoid implying bias related to gender, age or ethnicity. Each persona includes an overarching tagline and a more detailed description. Developing this User Persona Map is valuable because it helps shape the design of my application and can support the DfE in planning future training and guidance for schools.

<img src="doc_assets/User_Personas.png" alt="Figure 1: A User Persona Map showing 6 fictional personas designed to replicate typical school capabilities" width="400">

**Figure 1:** User Persona Map


### Personas Matrix:

**Figure 2:** The next item is the User Persona Matrix. This takes the personality profiles from the map and plots how my application, alongside a wider training and guidance package, could support the development of each persona. The horizontal axis represents confidence, while the vertical axis represents actual capability. Each persona is shown using an emoji placed at the point that best reflects their current position, with an arrow indicating the direction in which they could develop in the short to medium term. The overall aim is to move more personas toward higher levels of confidence and capability. This approach also recognises the gap that can exist between perceived and actual ability. For example, the “Cautious User” is highly capable but unlikely to reach the highest levels of confidence due to their naturally cautious disposition. Similarly, the “Confident Collaborator” appears to lose confidence as capability increases; this reflects the idea that greater expertise often brings greater awareness of risk, tempering overconfidence.

<img src="doc_assets/Persona_Matrix.png" alt="Figure 2: A Persona Matrix, plotting typical confidence vs capability, along with trends for improvement" width="1500">

**Figure 2:** User Persona Matrix


### GUI Prototyping

**Figure 3:** A wireframe was produced during the initial planning phase to outline how users would move through the quiz. It maps the sequence of interactions, beginning with entering name and school, progressing through each question, and concluding with the submission confirmation. Included in the design are indicative error-handling prompts.

Its purpose was to organise the arrangement of screens, identify where validation should occur, and establish the overall navigation logic before any coding took place. The wireframe focuses purely on flow and interaction rather than visual styling, acting as a structural guide rather than a final design

[Link to live Figma prototype](https://www.figma.com/proto/mCGgaxD7YMgP6cBQVEi0pv/EdTech-Quiz-Prototype?t=HrJ1jBI9K3BsOJIG-1&scaling=min-zoom&content-scaling=fixed&page-id=0%3A1&node-id=1-6&starting-point-node-id=1%3A6) — An interactive prototype quiz application, created in Figma

<img src="doc_assets/EdTech_Quiz_Prototype.png" alt="Figure 3: A prototype wireframe demonstrating user journey for completion of the EdTech Quiz" width="1386">

**Figure 3:** Wireframe


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
| FR18 | The application must support keyboard-only navigation. |
| FR19 | The application must show a clear, non-colour-focused outline for input areas. |
| FR20 | The application must have clear screen-reader-friendly text. |
| FR21 | The application must not impose time-based restrictions. |

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
| NFR15 | The application must use minimum contrast ratios compliant with WCAG AA standards. |
| NFR16 | Minimum font sizes must meet accessibility guidelines for readability on standard displays. |
| NFR17 | The system must be tested with at least one major screen reader. |
| NFR18 | All warnings and errors must be written in age-appropriate plain English.  |
| NFR19 | Spacing and alignment must remain consistent across all screens to reduce cognitive load. |
| NFR20 | The documentation must include a section describing available accessibility features. |

### Accessibility Assessment

The functional and non-functional requirements work together to create an experience that is accessible, predictable, and inclusive for a wide range of users. Many of the functional requirements directly reduce cognitive load and support assistive technologies. For example, collecting only essential information (FR1–FR3) keeps the onboarding process simple, while a single-question presentation (FR5) and enforced answer selection (FR7–FR8) help users focus on one task at a time. Keyboard-only navigation (FR18), clear input outlines (FR19), and screen reader-friendly text (FR20) ensure that participants who rely on assistive tools can interact with the quiz without barriers. The absence of time limits (FR21) is particularly important for users with processing, motor, or attention-related needs, allowing them to work at their own pace. Clear warnings and confirmations (FR15–FR16) also support users who benefit from explicit feedback or who may struggle with ambiguity.

The non-functional requirements reinforce this foundation by ensuring the interface remains readable, consistent, and compatible with accessibility standards. Readable labels and minimum contrast ratios (NFR2, NFR15–NFR16) support users with low vision, while avoiding colour-only cues (NFR12) ensures that information is not lost for colour blind participants. Compatibility with standard Tkinter widgets (NFR11) and testing with a screen reader (NFR17) help guarantee that assistive technologies can interpret the interface reliably. Requirements such as simple design (NFR1), consistent spacing (NFR19), and plain-English warnings (NFR18) reduce cognitive load and make the quiz approachable for younger users or those with learning differences. Local data storage (NFR13–NFR14) also protects privacy by limiting the amount and sensitivity of information collected. Together, these requirements create a quiz environment that is accessible by design rather than as an afterthought.

### Tech Stack Online 

- [Python 3](https://docs.python.org/3/) — Core programming language. Used for all application logic, file handling, and user interaction.
- [Tkinter](https://docs.python.org/3/library/tkinter.html) — Desktop graphical user interface. Provides the graphical interface for entering user details and navigating quiz questions.
- [csv](https://docs.python.org/3/library/csv.html) — Local data storage in CSV format. Stores quiz questions, answers and user data.
- [unittest](https://docs.python.org/3/library/unittest.html) — Automated unit testing. Used for smoke tests and functional checks of pure functions.

### Code Design Document

The conceptual UML Class Diagram below demonstrates the overall structure of the quiz application. At its centre is the edtech_quiz class, which manages the quiz flow, user interface state, and user inputs. It holds the questions, the Tkinter window, and the variables that track the user’s name, school, and answer choices. Its methods represent the lifecycle of the quiz, from starting it to showing each question, moving forward, and finally completing the session.

Supporting this main class are two focused helper classes: QuestionLoader, responsible for retrieving or preparing the questions, and ResultSaver, which handles storing or exporting the final results. The diagram shows that the quiz class depends on these helpers but does not inherit from them, emphasising a clean separation of responsibilities. The diagram demonstrates a well‑structured, maintainable design where each class has a clear purpose, and the main controller orchestrates the quiz experience.

<img src="doc_assets/class_diagram.png" alt="Figure 4: A Conceptual UML Class Diagram" width="196">

**Figure 4:** Conceptual UML Class Diagram

## Development Section

In this section, include relevant code blocks using triple backticks (```) to format your code clearly. Explain how your application works by describing the main parts of your code, such as important functions, classes, or modules. Provide enough detail to demonstrate your understanding of how each part contributes to the overall functionality. There is no word limit; focus on clarity and completeness.

1. Importing Modules

```
import csv
import tkinter as tk
from tkinter import messagebox
```

- csv module is used to read the questions and write the results
- tkinter module provides the GUI framework
- messagebox module is used for pop‑up warnings and confirmation messages

These modules form the foundation of the application.

2. Loading Questions

```
def load_questions(filename):
    with open(filename, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))
```

- Opens a CSV file containing quiz questions
- Uses csv.DictReader to convert each row into a dictionary
- utf-8 tells Python what character format to use when reading the file
- Returns a list of question dictionaries

This allows you to store questions externally and update them without changing the Python code.

3. Saving Results

```
def save_results(filename, name, school, answers):
    header = ["name", "school"] + [f"Q{i+1}" for i in range(len(answers))]

    try:
        with open(filename, "x", newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(header)
    except FileExistsError:
        pass

    with open(filename, "a", newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([name, school] + answers)
```

- Creates a header row the first time the file is created
- Error handling prevents deletion of previous results
- Appends each user’s name, school, and answers to the CSV file

This ensures quiz results are stored persistently and can be analysed later.

4. Starting the Quiz

```
def start_quiz():
    name = name_var.get().strip()
    school = school_var.get().strip()

    if name == "" or school == "":
        messagebox.showwarning("Missing info", "Please enter your name and school.")
        return

    show_question(0, [])
```


- Retrieves the user’s name and school
- Validates that both fields are filled
- Starts the quiz by calling show_question() with:
- 0 → first question
- [] → empty answer list

This ensures all neccessary information is captured and displays a message prompting the user when incomplete.

5. Displaying a Question

```
def show_question(question_number, answers_so_far):
    for widget in root.winfo_children():
        widget.destroy()

    question = questions[question_number]

    tk.Label(
        root,
        text=f"Question {question_number + 1}: {question['question']}",
        wraplength=1000,
        justify="left"
    ).pack(anchor="w")

    choice_var.set("")

    for option in ["a", "b", "c", "d"]:
        text = f"{option.upper()}: {question[option]}"
        tk.Radiobutton(
            root,
            text=text,
            variable=choice_var,
            value=option,
            wraplength=950,
            justify="left"
        ).pack(anchor="w")

    tk.Button(
        root,
        text="Next",
        command=lambda: next_question(question_number, answers_so_far)
    ).pack(pady=10)
```

- Clears the window so each question appears on a fresh screen
- Displays the question text
- Creates four radio buttons for answer choices
- Adds a Next button

This function controls the main quiz interface and ensures each question is shown cleanly and consistently.

6. Moving to the Next Question
```
def next_question(question_number, answers_so_far):
    selected = choice_var.get()

    if selected == "":
        messagebox.showwarning("No answer", "Please select an answer.")
        return

    new_answers = answers_so_far + [selected]

    if question_number + 1 < len(questions):
        show_question(question_number + 1, new_answers)
    else:
        finish_quiz(new_answers)
```

- Ensures the user has selected an answer
- Adds the selected answer to the list
- Either: Loads the next question, or ends the quiz

7. Finishing the Quiz

```
def finish_quiz(all_answers):
    save_results("results.csv", name_var.get(), school_var.get(), all_answers)
    messagebox.showinfo("Done", "Your answers have been saved.")
    root.destroy()
```

- Saves the user’s answers
- Shows a confirmation message
- Closes the application

8. Building the Main Window

```
root = tk.Tk()
root.title("EdTech Quiz")
root.geometry("1000x350")
root.configure(bg="#FFFFFF")

root.option_add("*Background", "#FFFFFF")
root.option_add("*Foreground", "#B60000")
root.option_add("*Font", "Sans-Serif 16")
```

- Creates the main Tkinter window
- Sets:
- Window size
- Background colour
- Default text colour
- Default font

This ensures a consistent visual style.

9. Welcome Screen and User Inputs

```
tk.Label(
    root,
    text="Welcome to the EdTech Quiz!\n\nPlease enter your name and school below, then click the Start Quiz button.\nYou will then be asked six questions, select one answer per question and confirm by clicking Next.",
    wraplength=950,
    justify="center"
).pack(pady=20)

tk.Label(root, text="Enter your name:").pack()
tk.Entry(root, textvariable=name_var).pack()

tk.Label(root, text="Enter your school:").pack()
tk.Entry(root, textvariable=school_var).pack()

tk.Button(root, text="Start Quiz", command=start_quiz).pack(pady=10)
```

- Displays a welcome message and instructions for completion
- Provides input fields for name and school
- Adds a button to begin the quiz

This is the first screen the user sees.

10. Main Loop

```
root.mainloop()
```

- Starts Tkinter’s event loop
- Keeps the window open and responsive


## Testing Section

Explain your approach to testing your digital product, demonstrating a systematic and strategic approach. Address the following topics:
1.	Testing strategy and methodology (summarise and justify different methods of testing you have used, for example, manual and automated unit testing)
2.	Outcomes of application testing:
2.1.	The outcome of manual tests (should be presented in a tabular format).
2.2.	Unit testing outcome (should include screenshots of tests running - passing or failing).


## Documentation Section

User documentation should explain how end users, such as staff within your organisation, can interact with the quiz application, whereas technical documentation should outline steps such as running tests locally and explain parts of the code.

## Evaluation Section

The evaluation section should explain what went well during the development of the project and what could have been improved. The evaluation section should be written in a genuine, reflective tone. As the README follows the conventions of software documentation, hyperlinks should be used for references instead of Harvard referencing.
