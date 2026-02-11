# digital-education-competency-quiz
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

Below is my User Persona Map. I have created six personas that can be broadly applied to individuals working across the education sector. The names have been selected carefully to avoid implying bias related to gender, age or ethnicity. Each persona includes an overarching tagline and a more detailed description. Developing this User Persona Map is valuable because it helps shape the design of my application and can support the DfE in planning future training and guidance for schools.

<img src="https://github.com/niletingham-web/digital-education-competency-quiz/blob/237b9464b24df1495259df6ae7c79f8a94849508/doc_assets/User_Personas.png" alt="User Personas" width="300">

Personas Matrix:

The next item is the User Persona Matrix. This takes the personality profiles from the map and plots how my application, alongside a wider training and guidance package, could support the development of each persona. The horizontal axis represents confidence, while the vertical axis represents actual capability. Each persona is shown using an emoji placed at the point that best reflects their current position, with an arrow indicating the direction in which they could develop in the short to medium term. The overall aim is to move more personas toward higher levels of confidence and capability. This approach also recognises the gap that can exist between perceived and actual ability. For example, the “Cautious User” is highly capable but unlikely to reach the highest levels of confidence due to their naturally cautious disposition. Similarly, the “Confident Collaborator” appears to lose confidence as capability increases; this reflects the idea that greater expertise often brings greater awareness of risk, tempering overconfidence.

<img src="https://github.com/niletingham-web/digital-education-competency-quiz/blob/237b9464b24df1495259df6ae7c79f8a94849508/doc_assets/Persona_Matrix.png" alt="User Personas" width="1500">




