# Github_Parser

A Github Parser written in Python3 which accepts username as input and shows various statistics of the user.

# The Working Procedure: 

1. The user is prompted for username on github when the program **scraper.py** is run.

2. With the given username, the parser extracts the user data from github and shows the number of repositories created/forked by the user.

<img width="562" alt="parser2 1" src="https://user-images.githubusercontent.com/43088920/65906294-e7579680-e3df-11e9-82dc-919b40b02fef.png">

3. Then, the parser provides the user with the choice of parsing any repository present in the list.

<img width="567" alt="parser2 3" src="https://user-images.githubusercontent.com/43088920/65906491-51703b80-e3e0-11e9-8bbe-06271acb84c0.png">

4. Now as the repository is being parsed the corresponding directories are simultaneously created in the same folder as the one in which **parser.py** is being run.

<img width="309" alt="parser2 4" src="https://user-images.githubusercontent.com/43088920/65907001-20dcd180-e3e1-11e9-8601-5dea3229fc43.png">

* **ScreenShot from the projects folder in atom**
  * Here you can see that the folder OOP has been created all subsequent directories and files in the form of a **tree like structure**

5. Now, in the terminal you get a output on the basis of language depicting number of programs written in each language in the chosen repo.

<img width="569" alt="parser2 2" src="https://user-images.githubusercontent.com/43088920/65907295-c55f1380-e3e1-11e9-9e2f-b4ade07d3108.png">

## PIE-CHART using plotly (Opens in Browser)

* **Using plotly.graph_objects** ( This is of another repo so don't get confused due to the mismatch with the above image :) )

<img width="999" alt="scraper2 5" src="https://user-images.githubusercontent.com/43088920/65908324-db6dd380-e3e3-11e9-94a3-b8cd2c06eeec.png">


## More with analysis with Seaborn and Matplotlib coming soon........

# Technologies used to make the project:-

1. Web Parsing using **Requests** Python Library (Use command **pip3 install requests** to download the library)

2. Web Scraping using **Beautiful Soup** (Use command **pip3 install bs4** to download the library)

3. String Matching using **Regular Expressions** (a.k.a **regex**)

4. Python data visualization using **Pyplot** Python Library (Use command **pip3 install pyplot** to download the library)

5. Directories Creation using **OS** module (Use command **pip3 install os** to download the module)

6. Directory Tree deletion using **SHUTIL** module

