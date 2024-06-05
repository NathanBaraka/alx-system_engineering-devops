Reddit API Project
This project involves querying the Reddit API to retrieve various information about subreddits. It includes three main tasks: retrieving the number of subscribers for a subreddit, getting the top ten hot posts of a subreddit, and recursively fetching all hot posts of a subreddit.

Requirements
Operating System: Ubuntu 20.04 LTS
Python Version: Python 3.4.3
Editors: vi, vim, emacs
Style Guidelines: PEP 8
General Rules
File Format:

All files should end with a new line.
The first line of all Python files should be #!/usr/bin/python3.
Libraries:

Imported libraries must be organized in alphabetical order.
Documentation:

Each module should have documentation accessible via python3 -c 'print(__import__("module_name").__doc__)'.
Executability:

All Python files must be executable.
File Length:

File lengths will be tested using wc.
HTTP Requests:

The Requests module must be used for sending HTTP requests to the Reddit API.
Tasks
Task 0: How Many Subs?
Write a function that queries the Reddit API and returns the number of subscribers for a given subreddit. If the subreddit is invalid, the function should return 0.

Prototype
python
Copy code
def number_of_subscribers(subreddit)
Requirements
If not a valid subreddit, return 0.
Do not follow redirects for invalid subreddits.
Example Usage
shell
Copy code
wintermancer@lapbox ~/reddit_api/project $ python3 0-main.py programming
756024
wintermancer@lapbox ~/reddit_api/project $ python3 0-main.py this_is_a_fake_subreddit
0
Task 1: Top Ten
Write a function that queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit.

Prototype
python
Copy code
def top_ten(subreddit)
Requirements
If not a valid subreddit, print None.
Do not follow redirects for invalid subreddits.
Example Usage
shell
Copy code
wintermancer@lapbox ~/reddit_api/project $ python3 1-main.py programming
Firebase founder's response to last week's "Firebase Costs increased by 7000%!"
How a 64k intro is made
...
PyCon 2017 Talk Videos
wintermancer@lapbox ~/reddit_api/project $ python3 1-main.py this_is_a_fake_subreddit
None
Task 2: Recurse It!
Write a recursive function that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit. If no results are found, return None.

Prototype
python
Copy code
def recurse(subreddit, hot_list=[])
Requirements
If not a valid subreddit, return None.
Do not follow redirects for invalid subreddits.
Function must use recursion, not loops.
Example Usage
shell
Copy code
wintermancer@lapbox ~/reddit_api/project $ python3 2-main.py programming
932
wintermancer@lapbox ~/reddit_api/project $ python3 2-main.py this_is_a_fake_subreddit
None
Directory Structure
GitHub Repository: alx-system_engineering-devops
Project Directory: 0x16-api_advanced
File Descriptions
0-subs.py: Contains the function for Task 0.
1-top_ten.py: Contains the function for Task 1.
2-recurse.py: Contains the function for Task 2.
Usage
Each task can be executed by running the corresponding main script with the subreddit name as an argument. For example:

shell
Copy code
python3 0-main.py <subreddit_name>
python3 1-main.py <subreddit_name>
python3 2-main.py <subreddit_name>
Contributing
Follow the general and style guidelines mentioned above.
Ensure your code is well-documented and tested.
Submit a pull request for any enhancements or bug fixes.
