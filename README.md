# Digital Tools for Finance - Project

**The repository is structured as follows:**<br />
The "main" branch is used for the final resarch project mentioned below. Additionally, there is a branch "midterm" where the weekly homeworks are stored. The branch "feature-1" was created for the git collab exercises.

**Research Topic:**<br />
What is the effect of the U.S. Real GDP on different S&P500 sector indices' market capitalizations

**Methods:**<br />
We regress the S&P500 sector indices' average market capitalizations on the U.S. Real GDP, instrumenting for other macroeconomic factors. The programming language used will be Python.

**Data:**<br />
Quarterly data is used for a time span of 14 years. Data is taken from Bloomberg and FRED.\

Data can be downloaded via FRED API. For this a personal api key must be requested and stored in an environmental variable called FRED_API_KEY. The code to run for downloading macro data lies in the folder ./data/interim. Before running the code make sure to have the package "fredapi" installed. Otherwise run "conda install fredapi" or "pip install fredapi". \
Otherwise, one can use the stored data in the ./data/processed folder.


### Reproducibility Remarks:
Unfortunately the creation of a container did not work as planned. Hence the usage of docker is not possible. 

main.ipnby has to be run from a jupyter notebook.\
To be able launch the application, the package "voila" must be installed manually, since otherwise docker would have handled this.\
Run "pip install voila" or "conda install voila".

There is an interactive plot at the end of the code. Unfortunately, this interactivity only works within the notebook and not in the application.\
Further, this interactive dropdown menu only works as long as the application is not running.

To run the server application, the last code snippet containing the command "!voila main.ipynb" must be uncommented and run.

### Project Organization: 
    .
    ├── README.md
    ├── data
    │   ├── interim
    │   ├── processed
    │   └── raw (ignored)
    ├── notebooks
    ├── reports
        └── figures


<br /><br />

### Group Members
Jonas Neller, 21-730-676 <br />
Lorena Tassone, 18-700-237 <br />
Naomi Huser, 17-056-201 <br />
