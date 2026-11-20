# Intelligent Timetable Generator (Turbo Prolog)

A rule-based timetable generator built in **Turbo Prolog 2.0** (running via DOSBox). It uses constraint satisfaction, recursion, and backtracking to schedule lectures without teacher or classroom clashes.

## 🎥 Video Explanation
Watch the full step-by-step code walkthrough and demo here:  
👉 **https://youtu.be/DJ8OL5Lqywg?si=E1TjlNrKxE9NUhd-**

## ✨ Features
- **Knowledge Base:** Models 3 subjects (`AI`, `Python`, `DBMS`), 3 teachers, 2 classrooms (`Room 101`, `Room 102`), and 5 time slots.
- **Clash Prevention (`check_clash`):** Uses a dynamic `database` (`scheduled`) to ensure no teacher or room is double-booked in the same slot.
- **Recursive Allocation (`assign_lecture`):** Assigns the exact number of required lectures per subject and locks valid choices using the cut (`!`) operator.
- **Backtracking Loops:** Uses Prolog's `fail` mechanism to iterate through all subjects and print the final schedule.

## 🚀 How to Run
1. Open **DOSBox** and mount your Turbo Prolog directory:
   ```dos
   mount c c:\TurboProlog
   c:
   cd prolog
   prolog

2.Press F3 in the Turbo Prolog IDE to load WORK.PRO.

3.Press Alt + R to compile and run the timetable generator.
