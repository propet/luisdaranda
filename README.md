A simple static personal website.

## Usage remainder
* Write any new project in markdown under _projects/\<year-month-day\>\_\<projectName\>/\<projectName\>.md_.
  * The file should begin with a title block such as 
  ```markdown
  % title
  ```
* Place any picture you like as _projects/\<year-month-day\>\_\<projectName\>/thumbnail.jpg_.
* Execute the make _make.py_ script to compile your markdown to html format using pandoc and update your main html.

## Requirements
* Pandoc
* Python3, BeautifulSoup
