# 📁 How to Access Files from Google Drive in Google Colab
When working in **Google Colab**, you can read and write files stored in your **Google Drive**. This is useful for loading data, saving results, and working across multiple sessions.


### 🔹 Step 1: Mount Google Drive

Before you can access any files in your Drive, you need to **mount** it:

```python
from google.colab import drive
drive.mount('/content/gdrive')
```

🟡 This will prompt you to authorize Colab to access your Google Drive.  

🔐 Follow the link, log in, and paste the authorization code.

Once mounted, the **root** of your Drive is available at:  
```plaintext
/content/gdrive/MyDrive/
```

### 🔹 Step 2: Define the File Path
Now that your Drive is mounted, you can create a variable that points to your file using its path. You must match the folder structure in your Drive.

##### ✅ Example 1: File directly in MyDrive

If your file is in the root of your Drive:

```python
file_path = "/content/gdrive/MyDrive/data.txt"
```

##### ✅ Example 2: File inside a subfolder
To access a file inside a subfolder called `ce311k`:

```python
file_path = "/content/gdrive/MyDrive/ce311k/data.txt"
```

##### ✅ Example 3: Writing to a new file in a subfolder
🗂️ You can create subfolders in Drive just like on your computer. Use the exact folder and file name in the path string.

```python
save_path = "/content/gdrive/MyDrive/ce311k/output.json"

with open(save_path, "w") as f:
    f.write("Hello from Colab!")
```

## Tip: Use Tab Completion

Once Drive is mounted, you can use **tab completion** in Colab to browse file paths:

- Type: `/content/gdrive/MyDrive/`  
- Then press `Tab` to see available folders and files!