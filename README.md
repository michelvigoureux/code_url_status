### 📝 Description
This script checks the status codes of a list of URLs. It's useful for SEO tasks to ensure that web pages are accessible and returning the expected status codes. It reads URLs from an input.txt file, processes them to get their HTTP status codes, and then writes the results to an output.csv file.

#### 🔧 Requirements
Python 3
Requests library
tqdm library
To install the required libraries, run:

```
Copy code
pip install requests tqdm

```
### 🚀 How to Use
#### 📂 Input File

Prepare an input.txt file with one URL per line.
Example:
arduino
Copy code
https://www.example.com/
https://www.example.com/page1
https://www.example.com/page2

### 🏃‍♂️ Run the Script

```
Copy code
python seo_script.py

```

As the script runs, it will show a progress bar thanks to the tqdm library.
### 📊 Output

Once the script finishes processing all the URLs, you'll find an output.csv file in the same directory.
The CSV file will have two columns: URL and Status Code.
If there's an error accessing a particular URL, the error message will be logged in the Status Code column.

#### ⚠️ Note
*** Ensure that the script has the necessary permissions to read from input.txt and write to output.csv.
The script uses the requests library to fetch the status codes and tqdm to show a progress bar. Ensure you're not violating any terms of service when sending multiple requests to websites. ***
