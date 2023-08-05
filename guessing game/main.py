import tkinter as tk
from tkinter import messagebox
import random

# Define the questions and their options with correct answers
questions = {
    "What is the capital of France?": {
        'options': ['A. London', 'B. Paris', 'C. Rome', 'D. Madrid'],
        'answer': 'B'
    },
    "Which planet is known as the Red Planet?": {
        'options': ['A. Venus', 'B. Mars', 'C. Jupiter', 'D. Saturn'],
        'answer': 'B'
    },
    "Who painted the Mona Lisa?": {
        'options': ['A. Vincent van Gogh', 'B. Pablo Picasso', 'C. Leonardo da Vinci', 'D. Claude Monet'],
        'answer': 'C'
    },
  "Which module is used to create graphical user interfaces in Python?": {
        'options': ['A. tkinter', 'B. pygui', 'C. pyui', 'D. guilib'],
        'answer': 'A'
    },
    "Which tkinter widget is used to display a simple text message?": {
        'options': ['A. Label', 'B. Button', 'C. Entry', 'D. Text'],
        'answer': 'A'
    },
    "What does the 'pack()' method do for a tkinter widget?": {
        'options': ['A. Aligns the widget vertically', 'B. Packs the widget into a frame', 'C. Sets the widget size', 'D. Aligns the widget horizontally'],
        'answer': 'B'
    },
    "Which geometry manager is used to create a flexible grid-like layout in tkinter?": {
        'options': ['A. grid', 'B. pack', 'C. place', 'D. flex'],
        'answer': 'A'
    },
    "What does the 'mainloop()' function do in tkinter?": {
        'options': ['A. Starts the main application window', 'B. Ends the application', 'C. Handles events and updates the display', 'D. Sets the main window title'],
        'answer': 'C'
    },
    "Which tkinter widget is used to display multiple lines of text with scrollbars?": {
        'options': ['A. Label', 'B. Button', 'C. Entry', 'D. Text'],
        'answer': 'D'
    },
    "Which method is used to add a new item to a tkinter Listbox widget?": {
        'options': ['A. insert()', 'B. add()', 'C. append()', 'D. new_item()'],
        'answer': 'C'
    },
    "What is the purpose of the 'command' parameter in a tkinter Button widget?": {
        'options': ['A. Sets the widget size', 'B. Sets the widget color', 'C. Defines the function to execute when the button is clicked', 'D. Sets the button label'],
        'answer': 'C'
    },
    "Which tkinter widget is used to input single-line text?": {
        'options': ['A. Label', 'B. Button', 'C. Entry', 'D. Text'],
        'answer': 'C'
    },
    "What does the 'config()' method do in tkinter?": {
        'options': ['A. Sets the widget color', 'B. Sets the widget size', 'C. Configures widget properties', 'D. Adds a new widget'],
        'answer': 'C'
    },
    "Which tkinter widget is used to display images in a window?": {
        'options': ['A. ImageBox', 'B. ImageView', 'C. ImageDisplay', 'D. Canvas'],
        'answer': 'D'
    },
    "What is the purpose of the 'bind()' method in tkinter?": {
        'options': ['A. Binds a function to a widget event', 'B. Sets the widget size', 'C. Configures widget properties', 'D. Adds a new widget'],
        'answer': 'A'
    },
    "Which tkinter widget is used to create dropdown menus?": {
        'options': ['A. Listbox', 'B. OptionMenu', 'C. Combobox', 'D. Menu'],
        'answer': 'B'
    },
    "What does the 'Canvas' widget do in tkinter?": {
        'options': ['A. Provides a text editing area', 'B. Displays images', 'C. Creates a drawing area for lines, shapes, and images', 'D. Adds buttons'],
        'answer': 'C'
    },
    "What is the purpose of the 'messagebox' module in tkinter?": {
        'options': ['A. Creates text labels', 'B. Displays images', 'C. Handles events', 'D. Shows popup message boxes'],
        'answer': 'D'
    },
    "Which tkinter geometry manager allows precise positioning and sizing of widgets?": {
        'options': ['A. grid', 'B. pack', 'C. place', 'D. flex'],
        'answer': 'C'
    },
    "What is the output of 'print(tkinter.TkVersion)'?": {
        'options': ['A. 1', 'B. 8', 'C. 2.7', 'D. 8.6'],
        'answer': 'D'
    },
    "Which tkinter widget is used to display HTML content?": {
        'options': ['A. HTMLViewer', 'B. WebView', 'C. Text', 'D. None of the above'],
        'answer': 'D'
    },
    "What is the correct way to set the window title in tkinter?": {
        'options': ['A. app.title', 'B. root.title', 'C. window.title', 'D. title'],
        'answer': 'B'
    },
    "Which method is used to close the tkinter main application window?": {
        'options': ['A. quit()', 'B. close()', 'C. exit()', 'D. stop()'],
        'answer': 'A'
    },
    "What is the primary purpose of an operating system?": {
        'options': ['A. Run applications', 'B. Manage hardware resources', 'C. Control data flow', 'D. Connect to the internet'],
        'answer': 'B'
    },
    "What does LAN stand for in computer networking?": {
        'options': ['A. Local Area Network', 'B. Long Area Network', 'C. Large Access Network', 'D. Linked Application Node'],
        'answer': 'A'
    },
    "Which technology allows communication between nearby devices without using wires?": {
        'options': ['A. Bluetooth', 'B. Wi-Fi', 'C. NFC', 'D. GPS'],
        'answer': 'A'
    },
    "What is the process of encoding data in such a way that only authorized parties can read it?": {
        'options': ['A. Decryption', 'B. Encoding', 'C. Encryption', 'D. Compression'],
        'answer': 'C'
    },
    "Which data structure follows the Last In, First Out (LIFO) principle?": {
        'options': ['A. Queue', 'B. Stack', 'C. Linked List', 'D. Tree'],
        'answer': 'B'
    },
    "What is the basic unit of digital information?": {
        'options': ['A. Byte', 'B. Kilobyte', 'C. Bit', 'D. Megabyte'],
        'answer': 'C'
    },
    "Which technology is used for short-range communication between devices by touching them together?": {
        'options': ['A. Bluetooth', 'B. Wi-Fi', 'C. NFC', 'D. GPS'],
        'answer': 'C'
    },
    "What is the process of copying data from a computer's memory to a storage device called?": {
        'options': ['A. Upload', 'B. Download', 'C. Backup', 'D. Download'],
        'answer': 'C'
    },
    "Which search engine is known for its I am Feeling Lucky button?": {
        'options': ['A. Bing', 'B. Yahoo', 'C. Google', 'D. DuckDuckGo'],
        'answer': 'C'
    },
    "Which web programming language is used to create interactive and dynamic web pages?": {
        'options': ['A. HTML', 'B. CSS', 'C. JavaScript', 'D. Python'],
        'answer': 'C'
    },
    "Which component of a computer is responsible for executing instructions of a computer program?": {
        'options': ['A. CPU', 'B. RAM', 'C. GPU', 'D. HDD'],
        'answer': 'A'
    },
    "Which type of software provides a platform for other software to run on?": {
        'options': ['A. Operating System', 'B. Application Software', 'C. Utility Software', 'D. System Software'],
        'answer': 'A'
    },
    "What does DNS stand for in computer networking?": {
        'options': ['A. Data Network Service', 'B. Domain Name System', 'C. Dynamic Network Service', 'D. Digital Network System'],
        'answer': 'B'
    },
    "Which cloud computing service provides on-demand computing resources over the internet?": {
        'options': ['A. Amazon Web Services (AWS)', 'B. Google Drive', 'C. Microsoft Office 365', 'D. Dropbox'],
        'answer': 'A'
    },
    "Which technology is used to record data on optical discs like CDs and DVDs?": {
        'options': ['A. Laser Printing', 'B. Inkjet Printing', 'C. Blu-ray Technology', 'D. Solid-State Drive (SSD)'],
        'answer': 'C'
    },
    "What is the process of converting analog signals to digital signals?": {
        'options': ['A. Modulation', 'B. Demodulation', 'C. Encoding', 'D. Decoding'],
        'answer': 'C'
    },
    "Which component of a computer is responsible for displaying visual output?": {
        'options': ['A. GPU', 'B. CPU', 'C. RAM', 'D. HDD'],
        'answer': 'A'
    },
    "Which type of software helps in creating, editing, and formatting documents?": {
        'options': ['A. Spreadsheet Software', 'B. Presentation Software', 'C. Database Software', 'D. Word Processing Software'],
        'answer': 'D'
    },
    "What is the protocol used for sending and receiving emails over the internet?": {
        'options': ['A. HTTP', 'B. FTP', 'C. SMTP', 'D. TCP'],
        'answer': 'C'
    },
    "What does the acronym GUI stand for in computing?": {
        'options': ['A. Graphical User Interface', 'B. General Utility Interface', 'C. Global User Interaction', 'D. Graphic Utilization Interface'],
        'answer': 'A'
    },
    "What is the primary purpose of an operating system?": {
        'options': ['A. Run applications', 'B. Manage hardware resources', 'C. Control data flow', 'D. Connect to the internet'],
        'answer': 'B'
    },
    "What does LAN stand for in computer networking?": {
        'options': ['A. Local Area Network', 'B. Long Area Network', 'C. Large Access Network', 'D. Linked Application Node'],
        'answer': 'A'
    },
    "Which technology allows communication between nearby devices without using wires?": {
        'options': ['A. Bluetooth', 'B. Wi-Fi', 'C. NFC', 'D. GPS'],
        'answer': 'A'
    },
    "What is the process of encoding data in such a way that only authorized parties can read it?": {
        'options': ['A. Decryption', 'B. Encoding', 'C. Encryption', 'D. Compression'],
        'answer': 'C'
    },
    "Which data structure follows the Last In, First Out (LIFO) principle?": {
        'options': ['A. Queue', 'B. Stack', 'C. Linked List', 'D. Tree'],
        'answer': 'B'
    },
    "What is the basic unit of digital information?": {
        'options': ['A. Byte', 'B. Kilobyte', 'C. Bit', 'D. Megabyte'],
        'answer': 'C'
    },
    "Which technology is used for short-range communication between devices by touching them together?": {
        'options': ['A. Bluetooth', 'B. Wi-Fi', 'C. NFC', 'D. GPS'],
        'answer': 'C'
    },
    "What is the process of copying data from a computer's memory to a storage device called?": {
        'options': ['A. Upload', 'B. Download', 'C. Backup', 'D. Download'],
        'answer': 'C'
    },
  
    "Which web programming language is used to create interactive and dynamic web pages?": {
        'options': ['A. HTML', 'B. CSS', 'C. JavaScript', 'D. Python'],
        'answer': 'C'
    },
    "Which component of a computer is responsible for executing instructions of a computer program?": {
        'options': ['A. CPU', 'B. RAM', 'C. GPU', 'D. HDD'],
        'answer': 'A'
    },
    "Which type of software provides a platform for other software to run on?": {
        'options': ['A. Operating System', 'B. Application Software', 'C. Utility Software', 'D. System Software'],
        'answer': 'A'
    },
    "What does DNS stand for in computer networking?": {
        'options': ['A. Data Network Service', 'B. Domain Name System', 'C. Dynamic Network Service', 'D. Digital Network System'],
        'answer': 'B'
    },
    "Which cloud computing service provides on-demand computing resources over the internet?": {
        'options': ['A. Amazon Web Services (AWS)', 'B. Google Drive', 'C. Microsoft Office 365', 'D. Dropbox'],
        'answer': 'A'
    },
    "Which technology is used to record data on optical discs like CDs and DVDs?": {
        'options': ['A. Laser Printing', 'B. Inkjet Printing', 'C. Blu-ray Technology', 'D. Solid-State Drive (SSD)'],
        'answer': 'C'
    },
    "What is the process of converting analog signals to digital signals?": {
        'options': ['A. Modulation', 'B. Demodulation', 'C. Encoding', 'D. Decoding'],
        'answer': 'C'
    },
    "Which component of a computer is responsible for displaying visual output?": {
        'options': ['A. GPU', 'B. CPU', 'C. RAM', 'D. HDD'],
        'answer': 'A'
    },
    "Which type of software helps in creating, editing, and formatting documents?": {
        'options': ['A. Spreadsheet Software', 'B. Presentation Software', 'C. Database Software', 'D. Word Processing Software'],
        'answer': 'D'
    },
    "What is the protocol used for sending and receiving emails over the internet?": {
        'options': ['A. HTTP', 'B. FTP', 'C. SMTP', 'D. TCP'],
        'answer': 'C'
    },
    "What does the acronym GUI stand for in computing?": {
        'options': ['A. Graphical User Interface', 'B. General Utility Interface', 'C. Global User Interaction', 'D. Graphic Utilization Interface'],
        'answer': 'A'
    },

}

total_questions = 0
score = 0

def check_answer():
    global total_questions, score
    user_answer_index = answer_var.get()
    if user_answer_index > 0:
        total_questions += 1
        user_answer = chr(ord('A') + user_answer_index - 1)  # Convert index to corresponding letter (A, B, C, or D)
        correct_answer = questions[question]['answer']
        if user_answer == correct_answer:
            score += 1
            messagebox.showinfo("Result", "Correct! Great job.")
        else:
            messagebox.showinfo("Result", "Sorry, that's incorrect.")
        show_score()
        generate_question()
    else:
        messagebox.showinfo("Result", "Please select an option.")

def generate_question():
    global question
    question = random.choice(list(questions.keys()))
    question_label.config(text=question)
    for i, option in enumerate(questions[question]['options']):
        option_buttons[i].config(text=option, value=i+1)  # Set value for each option button

def show_score():
    score_label.config(text=f"Score: {score}/{total_questions}")

# Create the main application window
app = tk.Tk()
app.title("Quiz Game")
app.geometry("650x350+400+200")

# Variables
answer_var = tk.IntVar()

# Question label
question_label = tk.Label(app, text="", font=("Arial", 12, "bold"))
question_label.pack(pady=10)

# Option buttons
option_buttons = []
for i in range(4):
    option_button = tk.Radiobutton(app, text="", font=("Arial", 10), width=30, variable=answer_var, value=0, indicator=0)
    option_button.pack(pady=5)
    option_buttons.append(option_button)

# Next question button
next_button = tk.Button(app, text="Next Question", font=("Arial", 12, "bold"), command=generate_question)
next_button.pack(pady=10)

# Check answer button
check_button = tk.Button(app, text="Check Answer", font=("Arial", 12, "bold"), command=check_answer)
check_button.pack(pady=10)

# Score label
score_label = tk.Label(app, text="Score: 0/0", font=("Arial", 12, "bold"))
score_label.pack(pady=10)

# Start the quiz by generating the first question
generate_question()

# Start the Tkinter main loop
app.mainloop()
