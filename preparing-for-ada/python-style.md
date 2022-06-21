# Python Coding Style

<iframe src="https://adaacademy.hosted.panopto.com/Panopto/Pages/Embed.aspx?id=90f1f6c3-d359-4dc4-960a-acb5001eb0ef&autoplay=false&offerviewer=true&showtitle=true&showbrand=false&start=0&interactivity=all" height="405" width="720" style="border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe>

The style in our code is just as important as the code itself. Programmers use code standards along with company style guides to ensure that all programmers are using the same style. Code with good style is easy to read, understand, and modify.

At Ada, we will be using the [PEP8](https://www.python.org/dev/peps/pep-0008/) coding style guide. 

We encourage you to look it over and your instructors will be referring to it when we make comments on your coding style.

Some highlights include:

* **[4-space indentation](https://www.python.org/dev/peps/pep-0008/#id17)** - Use 4 spaces per indentation level.
  * Use spaces not tabs to indent
    * Note that this is the recommendation in the [PEP8 coding style guide](https://peps.python.org/pep-0008/#tabs-or-spaces). However, one reason we may chose not to follow this guideline is accessibility. Folks who need to display the text larger will find that spaces can consume a great deal of horizontal space, and thus may prefer a tab that can be adjusted by the editor.
  * Continuation lines should align wrapped elements either vertically using Python's implicit line joining inside parentheses, brackets and braces, or using a hanging indent. When using a hanging indent the following should be considered; there should be no arguments on the first line and further indentation should be used to clearly distinguish itself as a continuation line:
* **[Maximum line length = 79 characters](https://www.python.org/dev/peps/pep-0008/#id19)**  - You should have no more than 79 characters on a single line.
* **[Imports should be on separate lines](https://www.python.org/dev/peps/pep-0008/#id23)** 
* **[Function & variable names](https://www.python.org/dev/peps/pep-0008/#id45)** - Function & variable names should be lower case with each word separated by underscores.

## Why Worry About Style?

Unlike how programming is depicted in hollywood, software development is usually a team activity.  It is very important to have code that our team can read, follow and when needed modify.  To that end, we will focus at Ada on writing readable, maintainable and efficient code.

