import os
from bs4 import BeautifulSoup


####################################
# Compile every project .md to .html
####################################
for project_dir in sorted(os.listdir("./projects"), reverse=True):
    project_name = project_dir.split("_")[1]
    os.system("pandoc --template=project_html.template"
              " --from markdown --to html --mathjax"
              " --highlight-style breezedark -o {path}.html"
              " {path}.md".format(path="./projects/"+project_dir+"/"+project_name))


############################
# Scrape every project .html
############################
projects_dict = {}  # store data of interest
for project_dir in sorted(os.listdir("./projects"), reverse=True):
    project_name = project_dir.split("_")[1]
    file = open("{path}.html".format(path="./projects/" + project_dir +
                                     "/" + project_name), "r")
    soup = BeautifulSoup(file, "html.parser")
    title = soup.find(id="tituloProyecto").b.get_text()
    projects_dict[project_name] = {"title": title}
    file.close()


##############################################
# Write the html for the projects grid section
##############################################
project_div_template = r"""
  <div>
    <a href="./projects/{project_dir}/{project_name}.html">
      <div class="thumbnail">
        <div class="caption">
            <h3><b>{title}</b></h3>
            <br>
            <p>{date}</p>
        </div>
        <img class="img-responsive"
             src="./projects/{project_dir}/thumbnail.jpg"
             alt="imagen web"/>
      </div>
    </a>
  </div>
"""

projects_html = ""
for project_dir in sorted(os.listdir("./projects"), reverse=True):
    date = project_dir.split("_")[0]
    project_name = project_dir.split("_")[1]
    projects_html = projects_html + \
            project_div_template.format(project_dir=project_dir,
                                        project_name=project_name,
                                        title=projects_dict[project_name]["title"],
                                        date=date)


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
