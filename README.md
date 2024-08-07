Prerequisites

    Git installed on your system.
    Python installed on your system.

1. Cloning the Repository

First, you need to clone the repository to your local machine. Open your terminal and run the following command:

git clone https://github.com/MarcoPolo987/Librarydtb.git

This will create a directory named OnlineFoodStore in your current directory.
2. Navigating to the Project Directory

Change to the project directory:

cd Library

3. Creating a Virtual Environment

Create a virtual environment in the project directory:

python -m venv venv

This command creates a new directory named venv where the virtual environment files are stored.
4. Activating the Virtual Environment

Activate the virtual environment. The command varies depending on your operating system:
On Windows:

.\venv\Scripts\activate

On Mac:

source venv/bin/activate

You should now see (venv) in your terminal prompt, indicating that the virtual environment is active.
5. Installing Dependencies

Install the required dependencies using the requirements.txt file:

pip install -r requirements.txt

This command will install all the packages listed in requirements.txt with their specified versions.
6. Running the application

To run the website. make sure you are still in the project directory

cd Library
once you are in here you can type

python3 app.py

and you will be prompted with a link to the website hosted locally
