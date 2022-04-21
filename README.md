pythonOS
---
[![GitHub Stars](https://img.shields.io/github/stars/Iemane291/pythonOS.svg)](https://github.com/Iemane291/pythonOS/stargazers)
[![GitHub pull requests](https://img.shields.io/github/issues/Iemane291/pythonOS.svg)](https://github.com/Iemane291/pythonOS/issues)
[![GitHub Wiki](https://img.shields.io/badge/project-wiki-ff69b4.svg)](https://github.com/Iemane291/pythonOS/wiki/Home)
[![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/Iemane291/pythonOS/master/LICENSE)
[![Github All Releases](https://img.shields.io/github/downloads/Iemane291/pythonOS/total.svg?maxAge=2592000)](https://github.com/Iemane291/pythonOS/releases)
[![The support server](https://shields.io/discord/943449399307157604)](https://discord.gg/mz3HmzP5ac)
[![version](https://img.shields.io/badge/version-0.0.6a-blue)](https://github.com/Iemane291/pythonOS/releases)


pythonOS is based off of [ChungOS](https://github.com/ArezalGame89/ChungOS), pythonOS is the more better and optimized version of [ChungOS](https://github.com/ArezalGame89/ChungOS).

pythonOS features:
- Lua script support using [lupa](https://pypi.org/project/lupa)
- Easy to use, fast and colorful interface using [colorama](https://pypi.org/project/colorama)   and [rich](https://pypi.org/project/rich)
- Changeable options that change your experience to your likings.
- A [support](https://discord.gg/m2x7MUTe3B) server incase you want to suggest something, or you encountered an issue.
- Much, much more (is yet to come).


## Getting Started

### As a first-time user:
So what you'll need to install is:

- [Python 3.10.0](https://python.org/downloads/) or a higher version.
- [Git-scm](https://git-scm.com/download)


Then open the terminal and change the directory to where you want pythonOS to be installed and then just type `git clone https://github.com/Iemane291/pythonOS.git` and it should start installing.

Once it has finished installing, you can do `cd pythonOS` in the terminal and do one of these commands depending on what operating system you use.

Windows: `py -m pip install -r requirements.txt`

Mac: `python3 -m pip install -r requirements.txt`

Linux: `python3 -m pip install -r requirements.txt`

> The Linux command is untested.

Then it should install all the libraries (view the libraries in the requirements.txt file if you are suspicious of what libraries are installed) you need.

Once that is finished, you can finally run one of these commands depending on what operating system you use.

Windows: `py main.py`

Mac: `python3 main.py`

Linux: `python3 main.py`

> The Linux command is untested.

And that is it!

### As a user

Assuming you have everything installed (if not, please read the As a first-time user section) You can just open the terminal, change the directory to where the pythonOS folder is located and then do one of these commands depending on what operating system you use:

Windows: `py main.py`

Mac: `python3 main.py`

Linux: `python3 main.py`

> The Linux command is untested.

### As a developer

Assuming you use an IDE, here's what you can do to easily run pythonOS.

Run one of these commands depending on what IDE you use.

Visual Studio Code: Assuming you have the Python extension installed, you can click the run (the play button looking one) button and it should run in the integrated terminal.

Sublime Text: Assuming Sublime has an integrated terminal & you've already installed what you need (if you don't know what to install, read the As a first-user section), you can just do one of these commands in the integrated terminal.

Windows: `py main.py`

Mac: `python3 main.py`

Linux: `python3 main.py`

## Options
This section is based on the changeable options (if you are a developer, there is a settings.json located in the data folder so you can edit settings)

All of these settings can be changed by doing `change <setting_name> <new_value>` or running the `pyconf` command to open an application to easily change your settings through a graphical user interface.

An option's possible values are called boolean values if their possible values are `true`, `on`, `off` and `false`

These settings are not categorized (if they will be, they will not be categorized in the settings.json file) but I plan to categorize them when I think of more settings to add.

### input-color

**NOTE: THIS OPTION WILL STILL WORK EVEN IF YOU HAVE THE COLORS OPTION DISABLED**

The possible values for this are:
- `red`
- `blue`
- `green`
- `yellow`
- `magenta`
- `white`

This changes the `cwd >` color. Just like how you can with any terminal (that I know)

### colors

This is a boolean value.

This toggles if you have colors enabled or not.

> I heavily recommend to turn this off if you're colorblind or if colors cause eyestrain for you.

### edit-warning

This is a boolean option.

This toggles if a warning will be shown everytime you run the edit command (even if an error occured).

### security

This is a boolean value.

This will make pythonOS not show the computer information like current working directory and also prevents pythonOS from opening new webbrowser tabs.

### git-installed

This is a boolean value.

When you run the `update` command, this decides if pythonOS will ask you if you have git installed.

If this option is enabled, then pythonOS will not ask you if you have Git installed and it will update.

Else, it will ask again.

This option is automatically turned on when pythonOS asks you if you have Git installed and you answer `y`

### use-size-settings

This is a boolean value.

This will change the command window size (on a restart using the `restart` command) to `size-columns` for the columns and `size-lines` for the lines.

### size-lines

This is the lines for the command window.

### size-columns

This is the columns for the command window.


### language

This chooses the language for pythonOS.

**NOTE: IF A LANGUAGE ENDS WITH `-gt` IT MEANS IT WAS GOOGLE TRANSLATED**

Possible languages are:
- `spanish-gt`
- `english`


## FAQ
### Q: Why do I get a list index out of range error?
A: Likely because you haven't provided the argument for that command.

## Credits

- [Mini](https://twitter.com/minilol69) - Creator, Programmer

### Special Thanks

- [Arezal](mailto:aradytfa@gmail.com) -  Made a good PR & created ChungOS.
