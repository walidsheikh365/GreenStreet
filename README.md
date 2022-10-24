![Logo Image](Images/Logo.png)

# Coursework 1
## Technical information

### Set-up instructions
Installed Packages:
* matplotlib
* pandas
* openpyxl
* numpy

## 1.0 Introduction
This project examines the open space areas in London, such as parks, play grounds, and churchyards to name a few, as 
well as the canopy cover by trees. This data is examined on a borough level, as well as overall for London. Using 
publicly available data, analyses are conducted on how each borough performs in these indicators of open spaces and 
canopy cover. This project explains the methodology used in section 2, the business need in section 3, followed by 
the manipulation of the data in section 4, and the weekly progress reports in section 5. 

## 2.0 Selection of project methodology

The development methodology chosen for the project has a significant impact on the time required as well as the ultimate
outcome. Development methodologies are split into data science, software engineering.

### 2.1 Selection criteria and justification of selection

Given the business need, the composition of the GreenStreet team, and the target audience, key factors or criteria for
the development methodology were narrowed down. These are as follows:

* __Level of volatility of the requirements:__ the base requirements influenced by the business need are unlikely to
  change. However, it is possible and probable that new requirements will be added as the potential from the dataset is
  fully understood.
* __Size of project team:__ the GreenStreet team is small in composition, with each team member encompassing a wide
  range of responsibilities.
* __Experience of the team in particular methods:__ the team members have yet to experience the breadth of possibilities
  in the software engineering world and are relatively new to the field. As such, the learning process with this dataset
  is also extensive for the team.
* __Timeframe of the project:__ the project may not be urgent, but it will guide policy and planning, which is quite
  vital for any local authority. Therefore, it will be assumed that the timeframe is fixed, and some results are 
necessary in the end.
* __Ease of access to the client:__ the typical client persona in this case is a big organization (local/municipal
  authorities or boroughs) which does not lend itself to easy communication given the scale of work occupying the 
  client. Therefore, the needs defined by the client early on will not deviate significantly, there communication with 
  the client can be kept low.
* __Business criticality of the project:__ As mentioned, the outcome of the project can have a marked impact on future
  planning and policy when it comes to greening, being able to reduce long-term costs through better maintenance and
  upfront planning and greenery selection.

### 2.2 Selected Methodology & Justification

The popular scrum technique, based on iterative and incremental phases was chosen when evaluated against the
aforementioned criteria, the process of which is shown in the Figure 1.

![Scrum Method image](Images/Scrum%20method.png)

*Figure 1. Scrum Methodology Processes Diagram (SlideModel, n.d.)*

The scrum method's versatility suits this project, and this reason among others is summarised in the justification from
the point of view of each aforementioned criterion.

#### Level of volatility of the requirements:

The scrum technique can be adjusted quite well for any changes in the requirements, as is characteristic of agile
methods. This is also contingent on regular communication with the client, usually bi-weekly (the typical timeframe of a
scrum sprint), where the changed or new requirements can make it onto the product backlog.

#### Size of project team:

A scrum team has defined roles in the form of a product owner, scrum master, and specialist developers. The developers
can vary from 2-5 people in an ideal scrum team, as is suitable for the scope and of the project. Since the scrum
technique hinges on close collaboration, this team size works well (Van der Hoek, 2021). In addition, scrum teams also
function without a hierarchical system.

#### Experience of the team in particular methods:

The scrum method is quite heuristic, and team members evolve and learn through regular appraisals due to fluctuating
factors. It is an acknowledgement that the team members will not know it all at the commencement of a project, and the
short cycles or sprints will allow knowledge and experience to be adapted (Drummond, n.d.). This will allow team members
with less experience to catch up at a quick rate with their more experienced counterparts.

#### Timeframe of the project:

Since the scrum technique relies on a number of sprints, with each sprint lasting anywhere from 1-4 weeks, the technique
can be molded for large projects over a lengthy period as well as smaller projects. If any changes require the timeframe
to be prolonged, it is possible to just increase the number of sprints for this, and since the length of each sprint is
not especially lengthy, it’s significantly easier to avoid large delays in the project timeframe (Drummond, n.d.).

#### Ease of access to the client:

The scrum methodology does require the client to be an active participant during the process, making any entries or
adjustments to the product backlog, with the meetings at the end of each sprint being an opportunity to properly define
any changes in requirements. This involvement can be passive during a sprint, but a client’s presence at a sprint
meeting at the end is quite vital for the project (BrightHub PM, n.d.).

#### Business criticality of the project:
Scrum has been successful in a diverse range of projects. Although the project does not have a strict deadline as the
addition and maintenance of open spaces and trees is a continuous process, scrum can still provide value in delivering 
the project without a high chance of delays. 

### 2.3 Comparison to Other Methodologies

The same criteria were evaluated against the waterfall method, a sequential development process where each phase is
dependent on the delivery of the previous phases (Waterfall Methodology, n.d.)(see Figure 2).

![Waterfall Method image](Images/Waterfall%20method.jpg)

*Figure 2. Waterfall Methodology Diagram (Bowes, 2014)*

Although very structured, this can have a negative impact on the project due to the following reasons from each
criterion's perspective.

#### Cons of Waterfall Method for the Criteria:

#### Level of volatility of the requirements:
Not suitable for this, as the waterfall method due to its cascading effect does not allow iterative change if required,
as requirements must be strictly defined, and the following steps must be executed with extreme precision (Waterfall
Methodology, n.d.).

#### Size of project team:
Does not specify, however it is reasonable to assume that the team will be expansive enough to allow experts in each
area the project requires, so that each requirement can be carefully considered and followed through.

#### Experience of the team in particular methods:
Since the waterfall method is quite different from the others in that no change is implemented and there is no
re-iterative process, team members will feel it necessary to triple-check every step, which may slow down the project.

#### Timeframe of the project:
The waterfall method seems better for projects that may have shorter timeframes, in that there are fewer chances of 
major interruptions disrupting the project and ultimately causing it to be derailed as it isn’t flexible enough. On the 
other hand, each must be completed before the next one can begin, therefore any delay can be major (Waterfall 
Methodology, n.d.).

#### Ease of access to the client:
Since the requirements are assumed to be well-defined in the beginning of the project, it is assumed that there will be
little or no interaction with the client after that period. Therefore, this method is useful for uncommunicative clients
or clients that don’t tend to interfere in the development process (Waterfall Methodology, n.d.).

#### Business criticality of the project:
Although the project does not have a strict deadline since adding and maintaining open spaces is a continuous process 
for a local authority, the waterfall method can fail if one phase in the process is held up, increasing the chances for 
a delay or the project being scrapped.

## 3.0 Definition of the business need

### 3.1 Problem definition
The Greater London Authority wants to undertake a re-evaluation of its outdoor spaces, after much derision during the 
pandemic about how lacking in greenery and openness some areas of the city felt. The issue was felt mostly in the West 
End and the City of London, areas which historically have been devoid of green spaces. The residents felt the lack of 
green space detrimental to their quality of life, and several neighbourhood forums have begun calling for more funding 
for greening practices (FitzWest, n.d.). The benefits of additional green or open for public use are numerous, with a 
key one being that people living close to it reported higher levels of satisfaction (Houlden et al., 2019).

The Greater London Authority wants to use an app/website which can pinpoint and recommend areas for improvement in that 
regard. The purpose of the app ideally would be to compare the area dedicated to open space and tree canopy cover in a 
borough, two factors that influence outdoor physical activity. An additional requirement is to be able to compare the 
types of open spaces in Greater London overall and in each borough by percentages, to influence decisions about which 
types of open spaces should be made in the future.

GreenStreet would examine publicly available datasets by Breadboard Labs and Greenspace Information for Greater 
London(GiGL) to examine each borough within Greater London and conclude where greenery (in terms of tree planting for 
canopy cover) and/or open spaces could be added. 

### 3.2 Target audience
The target audience for GreenStreet's app would be a local authority or government organisation with the responsibility 
to develop and maintain greenery and open spaces in an urban or even rural environment, though the main target is the 
former. Profiles of typical customers have been linked below:

[Customer Profile (City of Westminster)](PDF Files/City of Westminster.pdf)

[Customer Profile (Tower Hamlets)](PDF Files/Tower Hamlets.pdf)

### 3.3 Questions to be answered using the dataset
The dataset provided by Breadboard Labs can answer several key questions:
1. What is the canopy cover percentage for each borough, and how does it compare to overall canopy cover in London?
2. What is the open space area percentage for each borough and how does it compare to overall open space area in London?
3. Is there a correlation between open space area and canopy cover in a borough?
4. What is the percentage breakdown of open space area use in each borough and in London overall?

### 3.4 Suggested web app
In terms of developing a web application or dashboard, since the user will be a large organisation and not a lay person,
the interface does not have to be simple enough, but it should display relevant information in a concise manner along 
with the relevant recommendations for the user(a London borough). 

Ideally, there would be information about canopy cover for each borough, and how it compares to other boroughs with a 
similar profile, and to Greater London as a whole. Recommendations for increasing canopy cover will consider the type of
trees required(ornamental, forestry, flowering, fruiting, etc.) by the borough authority. It will also consider if the 
borough wants to increase canopy cover near a water body, where more water-thirsty trees will do well, or trees for an 
urban streetscape that have to deal with street compaction. 

Dealing with open spaces, the app will compare the borough's open space area and primary use percentages to boroughs 
with similar profiles and nearby boroughs, and then offer recommendations on that. It could recommend having an open 
space area type that is not present in neighbouring boroughs as a way to maximise users, for example. 

## 4.0 Data preparation and exploration

### 4.1 Data preparation

[Data Preparation](Data_Preparation.py)

For data preparation, there was some work done in organising and making the data more readible for both given data set 
files. 

For the canopy cover file, canopy cover was measured in smaller, arbitrary areas for each borough, and this information 
had to be displayed in a way that could be more useful for the dashboard. The following steps were taken to prepare the 
canopy cover file:
1. Columns were named to more suitable names for better understanding
2. File was sorted alphabetically by borough name
3. Missing values were checked for(but as this returned 0, this step was later removed)
4. Borough canopy cover areas was summed for each and sorted alphabetically by each borough
5. All values were rounded to 2 decimal places
6. The open space area for each borough was concatenated to the data frame

The following steps were taken for the open space area data set file:
1. Columns were renamed to more suitable names
2. Units were converted from hectares to square meters
3. File was sorted alphabetically by borough name
4. Missing values were checked for(but as this returned 0, this step was later removed)
5. Open spaces areas that were shared between multiple boroughs were divided equally between the boroughs, using an
indexing method for ';' in the borough column strings
6. The redundant rows with the open space area assigned to multiple boroughs were removed
7. Open space areas not in Greater London were removed
8. Borough open spaces were summed by borough and the primary use
9. Borough open spaces were also summed by just borough for later exploration with canopy cover
10. All values were rounded to 2 decimal places
11. Total borough open space data was concatenated to the canopy cover data frame
### 4.1.1 Prepared data set

[Original data set 1](CanopyCover.csv)
[Original data set 2](OpenSpace.csv)

[Prepared data set 1](Prepared_Data1.csv)
[Prepared data set 2](Prepared_Data2.csv)
### 4.2 Data exploration

[Data Exploration](Data_Exploration.py)

To explore the data using the two prepared data sets, the main method was to compare percentages for open spaces and 
canopy cover area in each borough in London and in London as a whole. The data was mainly explored by calculating these 
percentages from the total open space area in a borough, the total canopy cover in a borough, and the total open space 
area in London. This information was made into 4 plots, and were used to provide a template in how the web app could 
function in a basic state. 

Figure 1 shows the correlation between open space area and canopy cover percentages in London boroughs, and the 
correlation, using Pearson's correlation coefficient, was determined to be positive.

![Correlation between canopy cover and open space area in London boroughs](Images/Open%20Space%20and%20Canopy%20Correlation.png)

*Figure 1. Correlation between canopy cover and open space area in London boroughs*

Figure 2 shows the percentage of each open space area primary use type in London

![London open space area primary use percentages](Images/Open%20Space%20Primary%20Use%20Percentages.png)

*Figure 2. London open space area primary use percentages*

Figure 3 shows the percentage of canopy cover and open space area for each London borough, as a method of visual
comparison. Note the low percentages for both in City of London.

![Canopy cover and open space areas percentages in London boroughs](Images/Open%20Space%20and%20Canopy%20Boroughs.png)

*Figure 3. Canopy cover and open space areas percentages in London boroughs*

Figure 4 shows an example output of open space primary use percentage breakdown within a borough, with Westminster used 
as an example.

![Percentage of open space areas in Westminster by primary use](Images/Westminster%20Open%20Spaces.png)

*Figure 4. Percentage of open space areas in Westminster by primary use*

## 5.0 Weekly progress reports
### Report 1
What I did in the last week:
As for progress over the past week, a lot of it went into looking into possibilities for the project and the type of 
method I should implement in executing it. I have settled on the Scrum method for now as it seems the most suitable, 
with enough flexibility and its inherent design allowing for iterations and communication during different phases of the
project with the client, allowing changes to be made. 

As for the project itself, I looked into being able to estimate the tree age based on canopy cover. However, this can be
tricky because tree species in London are quite diverse, being from around the world, and have different growth rates 
and the maximum sizes they can reach. For example, conifer trees like cedars will tend to grow tall rather than wide and
this will not allow their age to be properly estimated in comparison to various deciduous trees. 

What I plan to do in the next week:
For next week, I will continue to look into the Scrum method a bit more and how its limitations might affect my project.
I also need to look at all the data in the given data sets since it is quite extensive. Another thing I want to look 
into is marking various species or notable trees on the map (rare and/or old trees) on a map and how this data can be 
collected through the data set. 

I also need to begin cleaning the data and develop a convention of naming variables or characteristics that will be 
suitable for the python environment and this course as required. 

The Business need/problem statement is another thing that needs to be hashed out as I'm not quite sure who I will be 
setting my target audience as. 

Issues blocking my progress (state ‘None’ if there are no issues):
So far, the given data set (13) has some issues as it is only 94% accurate as is stated by its developers. For example, 
some football pitches or marshes are incorrectly picked up as canopy cover. This will hopefully be resolved during the 
cleaning process in the coming weeks.

### Report 2
What I did in the last week:
This week, I drafted a problem statement, looked at some questions that could be answered from the data set given the 
nature of the problem statement, and made some potential personas. 

What I plan to do in the next week:
For next week, I would like to begin coding and preparing the data, and finalising the app features that I can possibly 
do, given my skill level and the remaining time. 

Issues blocking my progress (state ‘None’ if there are no issues):
None

### Report 3
What I did in the last week:
This week, the focus was on starting a draft proposal document for Coursework 1, with the business need and methodology 
being finalised, and also setting up the structure of the document. The other goal was to prepare the data, but due to 
an issue with PyCharm was put on hold. 

What I plan to do in the next week:
Next week, the goal or the hope is that there will be a workaround for the PyCharm issue through another coding 
environment (i.e. Replit). The data will be prepared if so and the necessary manipulations and computations required 
will have been coded, and, the proposal document would be ready for submission during the weekend of next week. 

Issues blocking my progress (state ‘None’ if there are no issues):
There is this recurring issue in PyCharm for me, where pandas is unable to be installed due to the pip version, even 
though the pip version is fully up-to-date in all python interpreters. The error log shows pycharm looking for Visual 
C++ 14.0 or more, and even though it is installed on my system it is unable to find it. Until then, I will try to set 
up Replit and try to make some progress there. 

### Report 4
What I did in the last week:
For this week, the methodology and business need were finalised, and some brainstorming for data preparation and exploration was done after resolving the PyCharm pandas issue. 

What I plan to do in the next week:
Next week will be mostly focused on data preparation and exploration, as the business need, methodology and other writing in the markdown file for the coursework is finished.

Issues blocking my progress (state ‘None’ if there are no issues):
None

## 6.0 References

Bowes, Jim. (2014). *Agile vs Waterfall: Comparing project management methods*. Retrieved from: https://manifesto.co.uk/agile-vs-waterfall-comparing-project-management-methodologies/

Breadboard Labs (2018). *Measurement & spatial analysis of
London’s tree canopy cover: 2018 methodology report*. Retrieved from: https://airdrive-secure.s3-eu-west-1.amazonaws.com/london/dataset/curio-canopy/2018-11-16T10%3A59%3A02/curio-%20tree-canopy-cover-methodology-report-nov-2018.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAJJDIMAIVZJDICKHA%2F20211026%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20211026T164546Z&X-Amz-Expires=300&X-Amz-Signature=1dec6afcc86a3b436e3bde403a05e4bfb6e36704aa187af52a06d930e79ddd0c&X-Amz-SignedHeaders=host

BrightHub PM. (2009). *Scrum Methodology: What is the Client’s Role?*. Retrieved from: https://www.brighthubpm.com/agile/33844-scrum-methodology-what-is-the-clients-role/

City of Westminster. (2018). *City of Westminster Profile*. Retrieved from: https://www.westminster.gov.uk/media/document/city-of-westminster-profile

Drummond, Claire. (n.d.). *Scrum*. Retrieved from: https://www.atlassian.com/agile/scrum

FitzWest. (n.d.). *Greening Project for FitzWest*. Retrieved from: https://www.fitzwest.org/category/greening/

Houlden et al. (2019). *A spatial analysis of proximate greenspace and mental wellbeing in London*. Retrieved from: https://www.sciencedirect.com/science/article/pii/S0143622818312384

SlideModel.(n.d.). *Software Diagrams for PowerPoint*. Retrieved from: https://slidemodel.com/templates/software-diagrams-powerpoint/

Tower Hamlets. (2020). *Borough Profile 2020 Chapter 1: Population*. Retrieved from: https://www.towerhamlets.gov.uk/Documents/Borough_statistics/Research-briefings/BoroughProfilePopulation.ppt

Van der Hoek, Jasper. (2021). *How to Structure an Agile Development Scrum Team*. Retrieved from: https://www.mendix.com/blog/the-road-to-adopting-scrum-team-composition/

*Waterfall Methodology* (n.d.). Retrieved from: https://www.workfront.com/en-gb/project-management/methodologies/waterfall
