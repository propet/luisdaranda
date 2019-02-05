% This very same portfolio
%
% 2019-01-22

[_Take a look at the repo_](https://github.com/propet/luisdaranda)


**Motivation**
--------------

I need to proof the things I say I'm capable of. 

Traditionally that means showing some title expended by a trusted institution (e.g. a college degree). But nowadays most conventional teaching centers have become costly and obsolete. And that I believe will never change, universities are beyond repair. Because new technologies, not so new, present themselves as a much better alternative to the oldschool kind of lecture done until this point in time. Would you rather keep taking notes on paper or write them down in an easy to store, searchable, and convenient text file? Would you rather ask for whatever it was just said, or simply go down the video timeline to the point you missed something?. Sure, getting to know the facts from an expert in the field in a face-to-face fashion is such an invaluable experience, but that usually never happens, what really takes place it's a face-to-mob _conversation_. Even if you could afford a teacher for every 3 or 4 pupils, does it even make sense to be constantly on top of them? Let the students learn on their own, since that is gonna be their most valuable asset for the rest of their lives. You don't even require an expert to solve whatever doubts come up, a community of learners habitually does the trick just as well. Look at [stackoverflow](https://stackoverflow.com/) for instance, where you'll find answers for any software related thing troubling you. Schools and high-schools also suffer from the same issue, but I'm afraid they serve the purpose of a kindergarden for more grown up kids, and it won't be so easy to replace them unless the fabric of society is significantly modified (i.e. never).

So in the last years we've seen a lot of new course platforms coming up on the internet. Just to name a few: EDX, Coursera, Udacity, or Udemy. They host a bunch of courses, or related series of them in the form of _specializations_ also called _mini-masters_. And whoever wants to do them, needs to digest their content, pass some tests or do some exercises, and then obtains the blessing from the platform for a price. Very much the same as in the previous system, but supposedly cheaper, you can study in your own time, and the content is frequently of a higher quality than you would get in a classroom, always available 24/7. This makes much more sense to me. I don't want to fund research at the expense of my education, neither do the researcher wants to give the same lecture year after year like a broken record.

At the end of the day, the reason you should be studying something at all, is because of the things that will allow you to **do**. What better way to proof your knowledge than showing off the things you've already done using those insights you claim to be in possession of. Would you rather hire the guy with a piece of paper that says he's good enough to build a car, or the guy who has built his own last year?. Okay, building a car from scratch might be stretching the idea too far, but you get my point, we should be aiming towards the end results. And any institution or company in the middle gets in the way of that goal.

That's why I believe a proper portfolio should be the backbone of any resume. This is why I'm doing mine, on my personal website, and now I'll tell you how I did it.


**A static website**
--------------------

I don't really need that much, just to serve some html files and a couple of css files for styling. I don't mess around with any database like a dynamic website would do, I don't need to.

Writing everything in html would do just fine. However I quickly got fed up with all the hassle and ceremony required to write something as simple as a plain line break:
```html
<br/>
```
It just doesn't roll off the tongue. I would also like to separate the content from the html file it is embedded into. Finally, I figured I would like to:

* Write the content in markdown.
* Convert that to html.
* Update my index (home) page with the new content so it's addressable.

The conversion step is done using [pandoc](http://pandoc.org/), a quite powerful command line utility written in haskell. And the _updatting_ proccess is taken care of by a simple script in python which barely reaches 50 LOC's. It calls the pandoc command to convert every markdown file it finds under the _projects_ directory and specifies a common html template for all projects

```python
####################################
# Compile every project .md to .html
####################################
for project in os.listdir("./projects"):
    os.system("pandoc --template=project_html.template"
              " --from markdown --to html --mathjax"
              " --highlight-style breezedark -o {path}.html"
              " {path}.md".format(path="./projects/"+project+"/"+project))
```

then it scrapes the produced html files for the title and date with the BeautifulSoup library

```python
############################
# Scrape every project .html
############################
projects_dict = {}  # store data of interest
for project in os.listdir("./projects"):
    file = open("{path}.html".format(path="./projects/" + project +
                                     "/" + project), "r")
    soup = BeautifulSoup(file, "html.parser")
    title = soup.find(id="tituloProyecto").b.get_text()
    date = soup.find(id="fechaProyecto").get_text()
    projects_dict[project] = {"title": title, "date": date}
    file.close()

```


and finally writes the contents for the index html which will display a grid with all the available projects

```python
##############################################
# Write the html for the projects grid section
##############################################
project_div_template = r"""
  <div>
    <a href="./projects/{project_name}/{project_name}.html">
      <div class="thumbnail">
        <div class="caption">
            <h3><b>{title}</b></h3>
            <br>
            <p>{date}</p>
        </div>
        <img class="img-responsive"
             src="./projects/{project_name}/thumbnail.jpg"
             alt="imagen web"/>
      </div>
    </a>
  </div>
"""

projects_html = ""
for project in os.listdir("./projects"):
    projects_html = projects_html + \
            project_div_template.format(project_name=project,
                                        title=projects_dict[project]["title"],
                                        date=projects_dict[project]["date"])

#####################
# Update project grid
#####################
index_template = open("index_template.html", 'r')
index_template_data = index_template.read()
index_template.close()

index_prueba_newdata = index_template_data.replace("__PROJECT_DIVS__",
                                                   projects_html)
index = open("index.html", 'w')
index.write(index_prueba_newdata)
index.close()
```

So whenever I feel like writing about something I recently did, I just need to write a markdown file, add a nice thumbnail picture, and run _make.py_ to do its wonders. Employing a framework for just these two operations feels like an overkill. While I can't promise I won't change my mind in the near future, I must say I'm very happy with the way things are actually working right now.


**Domain and hosting**
----------------------

In addittion, one of the biggest selling points about a static website is that I get free hosting on [github pages](https://pages.github.com) or [gitlab pages](https://about.gitlab.com/product/pages/), even with a custom domain. At the time of this writing I'm using [luisdomingoaranda.com](luisdomingoaranda.com).

And since I was already moderately familiarized with AWS, I got my domain name from them for 10 bucks a year, along with a small monthly fee for the routing service.

![Administration console](./images/instanciaAmazon.jpg)
