# 100 Days of Code Log

This project is a refactor of the [100 Days Log](https://github.com/ZanClifton/100-days-log) specifically for 100 Days of Code. It is a basic log and reflective diary. While the original was created with the SQLite module in Python, this version makes use of [Elephant SQL](https://www.elephantsql.com/) to run a PostgreSQL database.

Adding two optional fields to an entry, one for a link to the repo and the other for a link to a demo, if they are available, this version is closer to the 100 Days of Code format than the first log I created. Some of the prompts have been made clearer, too.

## Creating A Local Copy

### ✔️ 1. CLONE THE REPO

![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white) ![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white) ![PyCharm](https://img.shields.io/badge/pycharm-143?style=for-the-badge&logo=pycharm&logoColor=black&color=black&labelColor=green)

Terminal Commands:

```
$ git clone https://github.com/ZanClifton/100-days-of-code.git
$ cd 100-days-of-code/log
```

### ✔️ 2. ELEPHANTSQL AND DOTENV

<img height=25 width=60 src="https://github.com/ZanClifton/shrelly-mail-api/blob/main/env.png">

It is recommended that you sign up with [ElephantSQL](https://www.elephantsql.com/) and create your own instance. You don't need to do any complicated configuration to make it work, just sign up and create a free instance (named anything you like) on the [Tiny Turtle](https://www.elephantsql.com/plans.html) plan. Once you have created this, go to the details page and copy the URL.

To be able to run this project locally you'll need to create a file in the main directory:

```
.env
```

You can rename the `.env.example` file to `.env` if you like.

Your `.env` file should contain the following:

```
DATABASE_URI=
```

Paste your url directly after the `=` sign. You will not need to add anything else.

In the terminal at the root of the project folder run the following command:

```
$ pip install python-dotenv
```

Your local copy should now be set up and ready to use.

### ✔️ 3. USAGE

![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white) ![PyCharm](https://img.shields.io/badge/pycharm-143?style=for-the-badge&logo=pycharm&logoColor=black&color=black&labelColor=green)

Ideally, to edit the environment variables or make changes to the code you will need an IDE. I recommend VS Code or PyCharm.

In your terminal, if you have not already, navigate into the project folder:

```
$ cd 100-days-of-code/log
```

Run the script in the terminal:

```
$ python3 main.py
```

#

### Python 3.8

This project was created using Python 3.8 and requires it to run. Please ensure you have updated Python to the latest available version.
