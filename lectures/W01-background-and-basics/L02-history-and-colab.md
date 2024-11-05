# CE 311K - L02 - Evolution of Programming and Overview of Google Colab
> January 15th, 2025

## Evolution of Programming

### Slide 3: 1800s - Early Computing
<details>
<summary><i>See More</i></summary>

#### Charles Babbage (1791 - 1871)
- Known as the "Father of the Computer" for designing the **Analytical Engine**.
- Introduced the idea of a programmable machine that could handle any calculation.
- Though it was never built, Babbage’s design included memory, a processor, and even control flow.

#### Ada Lovelace (1815 - 1852)
- Recognized as the "First Programmer" for writing an algorithm for Babbage’s machine.
- Envisioned that computers could process things beyond numbers, like text and music.
- She wrote an algorithm to compute **Bernoulli numbers**, showing the Analytical Engine's potential.

#### The Analytical Engine
- A mechanical computer design with modern-like components:
  - **Mill** = CPU, which performs calculations
  - **Store** = Memory, which holds data
  - **Reader/Printer** = Input/Output for data entry and results
- Featured early programming concepts like loops and conditionals, which allowed complex calculations.
- Punched card input/output influenced later computing technology.

</details>

### Slide 4: 1930s - 1940s
<details>
<summary><i>See More</i></summary>

#### Alan Turing
- Created the concept of the **Turing Machine**, a model for a universal computer.
- Showed that one machine could handle any task with the right programming.
- Worked on cracking the Enigma code in WWII, demonstrating computing’s real-world applications.

#### Z3
- Built by Konrad Zuse in 1941 as the first fully programmable digital computer.
- Used binary (0s and 1s), similar to today’s computers.
- The Z3 was initially used for complex engineering calculations, like airplane design.

#### ENIAC (Electronic Numerical Integrator and Computer)
- Completed in 1945, the ENIAC was the first fully electronic, general-purpose computer.
- Designed to compute artillery trajectories, it could calculate thousands of times faster than prior methods.
- This enormous machine used thousands of vacuum tubes and required a whole room.

</details>

### Slide 5: 1950s
<details>
<summary><i>See More</i></summary>

#### Assembly
- Translated machine code into readable instructions, simplifying hardware control.
- Used directly by early programmers to manage memory and hardware.
- Assembly is still important in low-level programming, like operating systems and device drivers.

#### FORTRAN
- The first high-level language, created for scientists and engineers.
- Allowed users to focus on math operations instead of hardware details.
- Still popular today for high-performance scientific computing.

#### LISP
- Created for artificial intelligence research, introducing recursion (self-calling functions).
- Used in tasks that involve logical reasoning and processing symbols.
- One of the oldest languages still used, especially in AI research.

</details>

### Slide 6: 1960s and 1970s
<details>
<summary><i>See More</i></summary>

#### 1964: BASIC
- Designed for beginners and widely used in schools.
- Made programming more accessible and helped popularize computing.
- Many early programmers started with BASIC on home computers.

#### 1969: UNIX Operating System
- Established standards for operating systems, including multitasking and multi-user capabilities.
- Basis for many modern systems like Linux and macOS.
- Set a foundation for system design that remains influential.

#### 1972: C Language
- Flexible language that could directly access memory, widely used for system software.
- Inspired many later languages, including C++, Java, and Python.
- Often used in OS development and embedded systems.

#### Structured Programming Movement
- Introduced modular coding, loops, and functions for better organization.
- Emphasized clean, readable code and reliable structures.
- Principles still used today for writing and organizing code.

#### 1974: Structured Query Language (SQL)
- Created for managing data in relational databases.
- Made it easier to store, retrieve, and manipulate large datasets.
- SQL remains essential in database management and business applications.

</details>

### Slide 7: 1980s
<details>
<summary><i>See More</i></summary>

#### IBM PC
- Released in 1981, making personal computing affordable and accessible.
- Sparked growth in software development for home and office use.
- Led to the expansion of computer use across industries.

#### OOP (Object-Oriented Programming)
- Concept of classes and objects, popularized by languages like **C++**.
- Made it easier to create complex, reusable code through concepts like inheritance.
- Forms the basis of most modern programming, used in software and app development.

#### Matlab
- Specialized in numerical computing and data visualization.
- Became popular in engineering and scientific fields for its ability to handle large datasets and calculations.
- Frequently used in research, especially for matrix and statistical operations.

</details>

### Slide 8: 1990s
<details>
<summary><i>See More</i></summary>

#### Web Languages
- HTML, CSS, and JavaScript allowed interactive, dynamic websites.
- Made it possible to share information and applications globally.
- Paved the way for the modern internet and web-based applications.

#### Platform Independence (Java)
- Java’s "Write once, run anywhere" approach made cross-platform development easier.
- Programs could run on any device with Java Virtual Machine (JVM).
- Became popular for web applications and enterprise systems.

#### Open Source Movement
- Linux (OS) and Python (language) led the charge for open-source collaboration.
- Encouraged free, community-driven software development.
- Revolutionized software by promoting shared innovation and accessibility.

</details>

### Slide 9: 2000s and On
<details>
<summary><i>See More</i></summary>

#### Data Science and Machine Learning
- Tools like **R** and **Python** made analyzing large datasets more accessible.
- Enabled predictive modeling and data-driven insights in fields from healthcare to marketing.
- Data science became essential for decision-making in various industries.

#### Cloud Computing
- Provided scalable data storage and computing power over the internet.
- Eliminated the need for physical hardware, enabling on-demand resources.
- Enabled big data applications and facilitated collaboration on a global scale.

#### Artificial Intelligence
- Advances in neural networks allowed machines to "learn" and adapt.
- Revolutionized areas like image recognition, natural language processing, and automation.
- AI became central to applications like autonomous vehicles and personal assistants.

</details>

## Getting Started with Colab

### Accessing Google Colab
1. Go to [https://colab.google.com](https://colab.google.com).
2. Sign in with your Google account if prompted.
3. Select **“New Notebook”** to create a new workspace.

Once created, your notebook will automatically save to your Google Drive, so you can access it anytime!

## Colab Interface Overview

### Key Elements in the Interface
- **Code Cells**: Where you enter Python code. You can run each code cell individually to see the output.
- **Text Cells**: For adding explanations or notes in Markdown. Text cells allow you to document your code and add headings, lists, and more.
- **Toolbar**: Contains options to save, download, add cells, and share the notebook.

### Adding Cells
- **To add a new cell**: Click on the **+ Code** or **+ Text** buttons at the top of the notebook.
- **To delete or move cells**: Use the three-dot menu on the left side of each cell.

## Running Code in Colab

1. **Enter Code**: Type `print("Hello, world!")` into a code cell.
2. **Run the Code**: Press **Shift + Enter** or click the **Play** button on the left side of the cell.

The output of your code will appear directly below the cell!

## Saving, Sharing, and Downloading Your Work

### Saving
Colab automatically saves your work to your Google Drive, so you don’t have to worry about manually saving. You can also manually save your progress by selecting **File > Save**.

### Sharing
To share your notebook with others:
1. Click the **Share** button in the top-right corner.
2. Adjust sharing permissions to allow others to view, comment, or edit your notebook.
   - **View**: Allows others to see your code and output but not make changes.
   - **Comment**: Allows others to add comments without modifying the content.
   - **Edit**: Allows others to collaborate and make changes to your notebook.

### Downloading
If you need to save a copy outside of Google Drive, you can download your notebook in various formats:
1. Go to **File > Download** and select your preferred format:
   - **.ipynb**: The default Jupyter Notebook format, which you can open in Colab or other Jupyter-compatible environments.
   - **.py**: A Python script file, useful if you want to run the code in a standard Python environment outside of Colab.
   - **PDF** or **HTML**: For static versions of your notebook, including both code and output, which is great for sharing final reports.

## Keyboard Shortcuts
Using keyboard shortcuts in Colab can speed up your workflow. Here are some of the most useful ones:

- **Run Cell**: `Shift + Enter`
- **Insert Code Cell Above**: `Ctrl + M` then `A`
- **Insert Code Cell Below**: `Ctrl + M` then `B`
- **Delete Cell**: `Ctrl + M` then `D`
- **Convert to Code Cell**: `Ctrl + M` then `Y`
- **Convert to Text Cell**: `Ctrl + M` then `M`
- **Move Cell Up**: `Ctrl + M` then `K`
- **Move Cell Down**: `Ctrl + M` then `J`

To view a full list of shortcuts, press **Ctrl + M, H** within Colab.

## Key Elements
- **Indentation Errors**: Python is sensitive to indentation. Make sure your code lines up correctly, especially with loops and functions.
- **Order of Execution**: Cells are executed in the order you run them. If you change a variable in one cell, remember to re-run cells that depend on that variable.
- **Variable Persistence**: Variables are “remembered” across cells, so you can use variables defined in one cell in other cells.

## Why We Use Colab
- **No Installation Required**: Colab runs in your browser, so there’s no need to install Python or additional libraries.
- **Pre-installed Libraries**: Colab comes with many popular Python libraries (like NumPy and Pandas), making it ready for engineering applications.
- **Cloud-Based**: Colab provides free access to cloud-based resources, meaning you don’t need a powerful computer to run complex code.
