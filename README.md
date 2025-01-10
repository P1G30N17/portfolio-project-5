# Software Engineer Job Market Analysis

## Dataset Content
The dataset used for this project is a survey of software engineers done by stack overflow. The dataset contains over 65000 results submitted by software engineers from around the world, regarding all their information pertaining to a career in said field. Such data includes: role, salary, years of experience, qualifications, gender, ethnicity and so forth. The dataset was found at: https://survey.stackoverflow.co/ and a summary of their results can be found at: https://survey.stackoverflow.co/2024


## Business Requirements
As a Freelance Data Analyst I have been approached by a close friend, from hereon referred to as the client, to help them make an informed decision about the future of their career and family living. The client has recently completed a bootcamp in software development and engineering and is looking to change career paths as they are no longer happy with their current job due to various factors, including toxic work environment, long work hours keeping them from their family and bad pay. The client has made me aware that they are willing to immigrate to a new country (they currently reside in South Africa) for work, if the job market and pay is worthwhile (currently the client earns 324000 *South African Rands* per annum, the equivalent, as of 01/01/2025, to 17082.25 *United States Dollars*). Other factors the client has included are that they hold dual nationality for South Africa and Great Britain, inferring that work visas for countries covered by those nationalities are not needed, giving me a bias in country choice, unless the salary range for them is greatly below what the client is currently earning. 

- 1 - The client is interested in having a study to investigate the best location (Country with most jobs) for a potential job in the software engineering market
- 2 - The client is interested in determining whether experience in the software engineering industry affects potential salary
- 3 - The client wishes to be able to predict their potential salary based off of their qualification, years of experience and where they would be able to live(Country).


## Hypothesis and how to validate?
We suspect that a higher level of education and years of experience both positively effect software engineers and their salary. Job location is also another factor that can affect salary, countries deemed as '1st world' tend to have higher salaries on offer as opposed to others. 

We will attempt to validate this hypothesis by looking at the best guess factors influencing salary(Factors Influencing Salary from a google search returned: Experience, Education, Location, Industry, and others unnecessary for our project scope) within the Software Engineering Industry. These could be summarised as the following for the scopre of this project:
- Location of job (Country)
- Qualification
- Years of experience
- Salary earned

From this we will attempt to look for any correlation and attempt to extrapolate upon this, looking at the mean salary earned as we manipulate the corresponding correlated data. We will also attempt to see if there is a correlation between salary and experience and if location has a noticeable difference in average salaries earned per country.


## The rationale to map the business requirements to the Data Visualizations and ML tasks
- **Business Requirement 1**: Job Market Density / Job Availability 

  - We will display the total number of jobs within each country from the dataset.
  - We will display a graph clearly showing the proportions of software engineering jobs per country with the highest jobmarket saturation (the project assumption for this is that the more jobs within a country the higher the job availability), we have set the cutoff from the dataset at 100 jobs or more per country so as to be able to get a better training set for our model.
  - We will display a graph showing the distribution of average salary per country.

- **Business Requirement 2**: Industry experience effect on salary
  - We will investigate the effect experience has on a software engineer's salary and report the findings.
  - We will display a graph showing these findings and extrapolate upon them.

- **Business Requirement 3**: Salary Predictor
  - We want to predict the clients potential salary given their inputs of location, years of experience within the industry and their qualification.
  - We will build an app page to handle this task specifically.
  - We will build a regressor model to predict the clients salary.


## ML Business Case
### Salary Predictor
- We want an ML model to predict the clients potential salary given their inputs of location, years of experience within the industry and their qualification.
- Our ideal outcome is to be able to give the client the necessary information to make an informed decision about a career change that would be hugely impactful to their life, and that of their family.
- We would like a average descrepancy of no more than $35000 or lower.
- The model output is a predicted salary based off the user input variables.
- Heuristics: The app requires minimal technical user input to use, however the client will be cautioned that this project is still only an analysis and in no way guarantees them a job at the estimated salary level predicted, so any life changing choices must be undertaken with this awareness.
- The training data to fit the model came from a [survey](https://survey.stackoverflow.co/2024) done by *StackOverFlow* of 65000 software engineers.


## Dashboard Design
### Project Summary Page

- Project summary
  - General Information
    - The Software industry is a global booming market, it would only be fair to assume that jobs within this market would be too. This project aims to give a brief insight into this growing market with an investiagtion into the availability of Software Engineering jobs, their associated salary and which countries have the most jobs (This is an assumption off the current number of people employed within the field).
  - Dataset
    - The dataset used was taken from a survey of 65000 people done by StackOverflow as of 2024, and gives an incredibly detailed list of variables all pertaining to aspects of Software Engineers and their experiences within the current job market.
  - Link to additional information
  - Business requirements
    - The client is interested in having a study to investigate the best location(Country with most jobs) for a potential job in the software engineering market
    - The client is interested in determining whether experience in the software engineering industry affects potential salary
    - The client wishes to be able to predict their potential salary based off of their qualification, years of experience and where they would be able to live(Country).

### Predict Salary Page

- Salary Predictor
    - Business Requirement 3: "The client wishes to be able to predict their potential salary based off of their qualification, years of experience and where they would be able to live(Country)."
    - Widgets to adjust the user input for the corresponding fields (Years of experience, Qualification, Location)
    - A Predict Salary button which will take in the user variables and make a salary prediction.
        - Once clicked the predicted salary will be displayed.

### Explore Page

- Project exploration
    - Business requirement 1: The client is interested in having a study to investigate the best location (Country with most jobs) for a potential job in the software engineering market
        - A Donut chart and relevant explanation of the distribution of jobs by country.
        - A bar chart and relevant explanation of the average salary per country.
    - Business requirement 2: The client is interested in determining whether experience in the software engineering industry affects potential salary
        - A line chart showing the average salary by years of experience.
    - Conclusion summarising the various findings from the project.

### Project Hypothesis Page

- A block describing the project hypothesis as described in the hypothesis subsection.
- A block with the project hypothesis verdict.


## Unfixed Bugs
* None


## Deployment
### Heroku

* The App live link is: https://YOUR_APP_NAME.herokuapp.com/ 
* Set the runtime.txt Python version to a [Heroku-24](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.


## Main Data Analysis and Machine Learning Libraries

### Linear Regression
- We want an ML model to predict average salary per annum. We consider a linear regression model, which is supervised and uni-dimensional.
- As stated earlier we want a deviation of no more than $35000, however this was not the case and so we attempted a different model.

### Decision Tree Regression
- We want an ML model to predict average salary per annum. We consider a decision tree regression model, which is supervised and has a continuos output.
- The deviation was within the set acceptable amount however not by much, so we wished to see if we could get a lower results from other models.

### Random Forest Regression
- We want an ML model to predict average salary per annum. We consider a random forest regression model, every decision tree has high variance, but when we combine all of them in parallel then the resultant variance is low, in the case of a regression problem, the final output is the mean of all the outputs.
- The deviation again was within the acceptable amount, however not lower than that of the decision tree regressor.

### Grid Search with Cross Validation
- We try to fine tune the model using GridSearchCV, GridSearchCV implements a “fit” and a “score” method, the parameters of the estimator used to apply these methods are optimized by cross-validated grid-search over a parameter grid.
- We can see the best estimator model would be the Decision Tree Regressor method with a max depth of 10. So we get those parameters by using the gs.best_estimator_ and apply that to our model.
- As we see the deviation is higher than the lowest we have obtained earlier in the decision tree step, however we will still use this best method with said parameters as it could be due to random variables even though we set the random state to 0.

## Credits 

* In this section, you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials, however, it is important to be very specific about these sources to avoid plagiarism. 
* You can break the credits section up into Content and Media, depending on what you have included in your project. 

### Content 

- The text for the Home page was taken from Wikipedia Article A
- Instructions on how to implement form validation on the Sign-Up page were taken from [Specific YouTube Tutorial](https://www.youtube.com/)
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media

- The photos used on the home and sign-up page are from This Open-Source site
- The images used for the gallery page were taken from this other open-source site



## Acknowledgements (optional)
* Thank the people who provided support through this project.

