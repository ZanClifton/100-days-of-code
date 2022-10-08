<img src="https://github.com/ZanClifton/100-days-of-code/blob/main/images/100-days-code.png" width=250px align=right alt="100 Days of Code"/>

# 100 Days of Code Log

This project is a refactor of the [100 Days Log](https://github.com/ZanClifton/100-days-log) specifically for 100 Days of Code. It is a basic log and reflective diary. While the original was created with the SQLite module in Python, this version makes use of [ElephantSQL](https://www.elephantsql.com/) to run a PostgreSQL database.

Adding two optional fields to an entry, one for a link to the repo and the other for a link to a demo, if they are available, this version is closer to the 100 Days of Code format than the first log I created. Some of the prompts have been made clearer, too.

## A Copy on Replit

There is a version of this log on [Replit](https://replit.com/@ZanClifton/my-100-days-of-code-1?v=1) where you can fork the project to create your own log.

### ✔️ 1. FORK THE REPL

![Replit](https://img.shields.io/badge/Replit-DD1200?style=for-the-badge&logo=Replit&logoColor=white)

Following the link above to [the project](https://replit.com/@ZanClifton/my-100-days-of-code-1?v=1), and on the top right hand side of the screen, there is an option called "Fork Repl". Select it, and in the popup, name your fork, provide a description if you like, and click the "Fork Repl" button on the popup window.

### ✔️ 2. SET UP YOUR REPL

![Replit](https://img.shields.io/badge/Replit-DD1200?style=for-the-badge&logo=Replit&logoColor=white)

You will need to sign up with [ElephantSQL](https://www.elephantsql.com/) and create your own instance. You don't need to do any complicated configuration to make it work, just sign up and create a free instance (named anything you like) on the [Tiny Turtle](https://www.elephantsql.com/plans.html) plan. Once you have created this, go to the details page and copy the URL.

#### ✅ A: Secrets

Navigate to the 'Secrets' section on the left hand side of your new repl, and it will prompt you for a key/value pair. The URL you copied from ElephantSQL is the `value` here. You will also need to add the key provided below.

| KEY          | VALUE                               |
| :----------- | :---------------------------------- |
| DATABASE_URI | The URL you copied from ElephantSQL |

You do not need to add anything else to 'Secrets'.

#### ✅ B: Packager

Above 'Secrets' there is 'Packager'. Navigate here and search for the following:

| Package         | Version |
| :-------------- | :------ |
| psycopg2-binary | 2.9.4   |
| python-dotenv   | 0.21.0  |

Add them both to your project.

Your project is now set up and ready to use.

### ✔️ 3. ONLINE USAGE

![Replit](https://img.shields.io/badge/Replit-DD1200?style=for-the-badge&logo=Replit&logoColor=white)

By default, the version in Replit is 'read only' and all the writable functionality has been commented out. Using it this way, you can't add an entry, but you can read all the entries and even find entries by day or by date. You can make the changes below so that you can write to your log from Replit directly if you would like.

In main.py, find line 74. 

<img src="https://user-images.githubusercontent.com/96394256/194715665-3f37a322-b4ff-4175-a9b2-eb6388b9afe1.png" width=400px alt="A picture showing a screenshot demonstrating the below instructions."/>

Remove the `#` at the beginning of the line. Add a `#` at the beginning of the line below. This section should now look like this:

<img src="https://user-images.githubusercontent.com/96394256/194715698-2f778016-86c6-46dc-bbe5-fe4d269dd60f.png" width=400px alt="An image showing the hash symbol has  been deleted on line 74 and a hash symbol has been added to the beginning of line 75."/>

#

**N.B. If you choose to make the above changes, please be aware that anyone who accesses your repl will also be able to write changes to your log. This means that they may be able to add new entries which other people can also read.**

If you want to keep your log safe from random edits and additions, follow the instructions below to create and run a local copy, rather than enabling write access on your repl.

#

<img src="https://user-images.githubusercontent.com/96394256/194716168-5adfde85-762f-4068-b0fe-76d4466e2d75.png" width=400px align=right alt="A picture showing a screenshot demonstrating the below instructions."/>

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

You will need to sign up with [ElephantSQL](https://www.elephantsql.com/) and create your own instance. You don't need to do any complicated configuration to make it work, just sign up and create a free instance (named anything you like) on the [Tiny Turtle](https://www.elephantsql.com/plans.html) plan. Once you have created this, go to the details page and copy the URL.

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
