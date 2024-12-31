# Getting Started with Colab

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
