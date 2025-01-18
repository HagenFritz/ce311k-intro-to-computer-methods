# Code Submission Process in Jupyter Notebook
This document outlines the process for capturing code and output from a Jupyter Notebook cell and submitting it to a Google Form for review. Below are the steps and code implementation.

## Google Form
You will create a Google Form that will function as your entrypoint and "database" for the submissions. 

### ✨ Create Google Form
You will need to create a Google Form from your drive. You will create a question for every input that you want to use. These inputs should be short or long paragraph answer options. Other options _might_ work, but I did not test those. Below shows a screenshot of including a "Name" entry field:

<img width="863" alt="Screenshot 2025-01-17 at 1 24 32 PM" src="https://github.com/user-attachments/assets/0fd2d786-02fd-48b9-9c45-c4a3ba61b06a" />

### ✏️ Obtain `entry` Field IDs
Follow the link to your Form like you were going to submit it. When you have it pulled up, right-click the page and choose the option for "Inspect":

<img width="239" alt="Screenshot 2025-01-17 at 1 29 50 PM" src="https://github.com/user-attachments/assets/a53c42bc-1a02-457f-ab36-5442c455f58f" />

On the right-hand side of your screen, you should see a lot of HTML. Hit `ctrl`+`F` (`cmd`+`F` on Mac) to open up the search feature. Type "entry" and your first hit should take you to the location you need. You should see some HTML like this:

```html
<input type="hidden" name="entry.26604604" value="">
<input type="hidden" name="entry.563413582" value="">
<input type="hidden" name="entry.1364507633" value="">
<input type="hidden" name="entry.2019513528" value="">
```

Each of these lines corresponds to one of the questions you defined in your form, corresponding to the order they appear in the form. In this example, I have four questions. You want the values in the `name` fields - copy those down.

### 🌐 Obtain POST URL
While still on the Form, submit it with whatever dummy data you want to include. Once you get to the "Successful Submission" screen, copy the full URL from your browser and save it somewhere for later. Your URL should look something like:

```
https://docs.google.com/forms/u/0/d/e/1FAIpQLSdBh0WXiUQvlcBdYwC5Mypdcj0RVF_YDOYJOo57vDqT4cJ1NA/formResponse
```

---

## Jupyter Notebook Setup
You will submit your code via a Google Colab notebook. You will need to import a few modules and then define two functions to help you.

### Cell 1: Import Necessary Libraries
You will need to import the `IPython` and `requests` libraries:
* `requests`: for making HTTP requests
* `IPython`: allows interaction with the notebook environment, including retrieving execution history

```python
from IPython import get_ipython
import requests
```

### Cell 2: Function to Retrieve Student Code and Output
The `get_student_code` function is designed to retrieve the content and output of the second-to-last executed cell in a Jupyter Notebook. We use the second-to-last cell because the last cell will correspond to the function used to submit, and the relevant code lies in the cell before it.

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

#### Key Steps in the Function

1. **Access the IPython Environment**
   ```python
   ipython = get_ipython()
   ```
   The function uses `get_ipython()` to access the interactive shell instance, enabling access to the execution history and variables.

2. **Retrieve Execution History**
   ```python
   history = list(ipython.history_manager.get_range(output=False))
   if len(history) < 2:
       return "", ""  # Not enough history to retrieve the second-to-last cell
   ```
   The `history_manager` fetches previously executed code. If there are fewer than two entries in the history, the function returns empty strings.

3. **Extract Code of the Second-to-Last Cell**
   ```python
   _, _, student_code = history[-2]
   ```
   The second-to-last cell’s code is extracted from the history list.

4. **Capture the Output of the Second-to-Last Cell**
   ```python
   exec_count = len(ipython.history_manager.input_hist_raw) - 2
   output = ipython.displayhook.shell.user_ns.get("Out", {}).get(exec_count, "")
   ```
   - `exec_count`: Determines the execution count of the second-to-last cell.
   - `Out`: Accesses the dictionary storing outputs of executed cells. If no output exists, an empty string is returned.

5. **Return Results**
   ```python
   return student_code, output
   ```
   The function returns a tuple containing:
   - `student_code`: The code executed in the second-to-last cell.
   - `output`: The corresponding output (if any).

### Cell 3: Function to Submit Data to Google Form
The `submit_answer` function is designed to send a code cell and its output from a Jupyter Notebook to a Google Form. This enables easy collection and review of submissions through an automated workflow.

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

#### Key Steps in the Function

1. **Define Submission Parameters**
   ```python
   student_name : str
   question_no : int
   ```
   These parameters collect the student's name and the corresponding question number for their submission.

2. **Fetch the Student's Code and Output**
   ```python
   code, output = get_student_code()
   ```
   The function calls `get_student_code` to retrieve the content and output of the relevant cell for submission.

3. **Map Parameters to Google Form Fields**
   ```python
   form_data = {
       "entry.26604604": student_name,  # Student Name field
       "entry.563413582": question_no,  # Question Number field
       "entry.1364507633": code,        # Code field
       "entry.2019513528": output       # Output field
   }
   ```
   The `form_data` dictionary maps the input parameters and retrieved data to the specific Google Form fields.

   ❗ You will need to input your own entry IDs that you copied down earlier

5. **Send Data via HTTP POST**
   ```python
   form_url = "https://docs.google.com/forms/u/0/d/e/1FAIpQLSdBh0WXiUQvlcBdYwC5Mypdcj0RVF_YDOYJOo57vDqT4cJ1NA/formResponse"
   ...
   response = requests.post(form_url, data=form_data)
   ```
   The function submits the data to the hardcoded Google Form URL using the `requests` library.

   ❗ You will need to input your own URL that you copied down earlier

7. **Handle the Submission Response**
   ```python
   if response.status_code == 200:
       print("Submission successful!")
   else:
       print(f"Submission failed with status code: {response.status_code}")
   ```
   Based on the HTTP response code, the function prints whether the submission was successful or encountered an error.

---

## Example Usage
1. Write and execute code in a Jupyter Notebook code cell.
2. Run a new cell that contains just the function `submit_answer` that contains the student name and question number as arguments.
3. Within `submit_answer`, we call the function `get_student_code` which captures the second-to-last executed cell's code and output and sends it to the Google Sheet connected to the Form you created

---

## Common Issues
1. **Execute Function Cells**
   - 
   
1. **Missing Output**
   - Make sure you run the correct cell
   - Ensure the code cell produces an evaluated result. A `print` statement shows the output but it isn't actually captured by the function.

3. **Google Form URL or Field ID Errors**:
   - Verify the form's POST URL and field IDs.

4. **Network Issues**:
   - Ensure the machine running the notebook has internet access to send requests to Google Forms.

---

### **Conclusion**
This setup allows students to submit their code and its output directly from a Jupyter Notebook to a Google Form, streamlining the submission and review process.
