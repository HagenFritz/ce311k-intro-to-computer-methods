# Code Submission Process in Jupyter Notebook
This document outlines the process for capturing code and output from a Jupyter Notebook cell and submitting it to a Google Form for review. Below are the steps and code implementation.

---

# Prerequisites

### Google Form
You will need to create a Google Form from your drive. You will create a question for every input that you want to use. These inputs should be short or long paragraph answer options. Other options _might_ work, but I did not test those. Below shows a screenshot of including a "Name" entry field:

<img width="863" alt="Screenshot 2025-01-17 at 1 24 32 PM" src="https://github.com/user-attachments/assets/0fd2d786-02fd-48b9-9c45-c4a3ba61b06a" />

### Obtain `entry` Field IDs
Follow the link to your Form like you were going to submit it. When you have it pulled up, right-click the page and choose the option for "Inspect":

<img width="239" alt="Screenshot 2025-01-17 at 1 29 50 PM" src="https://github.com/user-attachments/assets/a53c42bc-1a02-457f-ab36-5442c455f58f" />

On the right-hand side of your screen, you should see a lot of HTML. Hit `ctrl`+`F` (`cmd`+`F` on Mac) to open up the search feature. Type "entry" and your first hit should take you to the location you need. You should see some HTML like this:

```html
<input type="hidden" name="entry.26604604" value="">
<input type="hidden" name="entry.563413582" value="">
<input type="hidden" name="entry.1364507633" value="">
<input type="hidden" name="entry.2019513528" value="">
```

Each of these lines corresponds to one of the questions you defined in your form, following the order they appear in the form. In this example, I have four questions. You want the values in the `name` fields - copy those down.

### Obtain POST URL
While still on the Form, submit it with whatever dummy data you want to include. Once you get to the "Successful Submission" screen, copy the full URL from your browser and save it somewhere for later. Your URL should look something like:

```
https://docs.google.com/forms/u/0/d/e/1FAIpQLSdBh0WXiUQvlcBdYwC5Mypdcj0RVF_YDOYJOo57vDqT4cJ1NA/formResponse
```





---

### **Code Implementation**

#### **Cell 1: Import Necessary Libraries**
```python
# Import necessary libraries
from IPython import get_ipython
import requests
```

#### **Cell 2: Function to Retrieve Student Code and Output**
```python
def get_student_code():
    """Retrieve the second-to-last executed cell's content (the last will be the submission code)."""
    ipython = get_ipython()
    # Get the history of executed code
    history = list(ipython.history_manager.get_range(output=False))
    if len(history) < 2:
        return "", ""  # Not enough history to retrieve the second-to-last cell

    _, _, student_code = history[-2]  # Get second-to-last cell code

    # Get the output of the second-to-last cell
    exec_count = len(ipython.history_manager.input_hist_raw) - 2
    output = ipython.displayhook.shell.user_ns.get("Out", {}).get(exec_count, "")

    return student_code, output
```

#### **Cell 3: Function to Submit Data to Google Form**
```python
def submit_answer(student_name, question_no):
    """
    Submit the student's code to a Google Form.

    Parameters
    ----------
    student_name : str
      The student's name.
    question_no : int
      Number for the question submitting for

    Returns
    -------
    <str> : str
      Output of successful or unsuccessful submission
    """
    # Hardcoded Google Form URL
    form_url = "https://docs.google.com/forms/u/0/d/e/1FAIpQLSdBh0WXiUQvlcBdYwC5Mypdcj0RVF_YDOYJOo57vDqT4cJ1NA/formResponse"
    # Get code and output
    code, output = get_student_code()
    # Map field IDs to input params
    form_data = {
        "entry.26604604": student_name,  # Student Name field
        "entry.563413582": question_no,  # Question Number field
        "entry.1364507633": code,        # Code field
        "entry.2019513528": output       # Output field
    }

    # Send the POST request
    response = requests.post(form_url, data=form_data)
    if response.status_code == 200:
        print("Submission successful!")
    else:
        print(f"Submission failed with status code: {response.status_code}")
```

---

### **Example Usage**

#### **Code**
```python
# Example of submitting data
name = "John Doe"
submit_answer(student_name=name, question_no=0)
```

#### **Execution Steps**
1. Students write and execute their code in a Jupyter Notebook cell.
2. The function `get_student_code` captures the second-to-last executed cell's code and output.
3. The `submit_answer` function sends the captured data to the Google Form.

---

### **Google Form Field Mapping**
| Field Description    | Google Form Field ID |
|----------------------|----------------------|
| Student Name         | `entry.26604604`    |
| Question Number      | `entry.563413582`   |
| Code                | `entry.1364507633`  |
| Output              | `entry.2019513528`  |

---

### **Output Handling**
- **Code:** Captures the exact code the student wrote.
- **Output:** Retrieves both printed and evaluated outputs from the executed cell.

---

### **Common Issues**
1. **Missing Output**:
   - Ensure the student's code produces either an evaluated result or a `print` statement.
   - If no output is generated, the output field will be empty.

2. **Google Form URL or Field ID Errors**:
   - Verify the form's POST URL and field IDs.

3. **Network Issues**:
   - Ensure the machine running the notebook has internet access to send requests to Google Forms.

---

### **Conclusion**
This setup allows students to submit their code and its output directly from a Jupyter Notebook to a Google Form, streamlining the submission and review process.
