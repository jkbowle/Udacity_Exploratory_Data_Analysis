# Make Effective Data Visualization - Final Project
## Summary
>[This data visualization](http://bl.ocks.org/jkbowle/raw/73c5a7abdb0993a08972/ "final version") shows the growing trend in Major League Baseball to use more and more pitchers in a game.  This trend over time has dramatically increased the length of games in baseball.  I want to walk the reader through the growing trend year by year, but then open up the viz for the reader to explore and verify for themselves.

## Design
> The design is to make use of a scatter plot to show the relationship between average pitchers used in a season and the median length of a game.

> Initially I thought I would summarize this by year and team, but I ultimately decided against this as I thought it would add too much noise to the visualization.  The animation would come in as a show of how every year went up in both categories from 1950 to 2014.

> The final design had me opening up both axis to be selected by the reader to evaluate all the different relationships possible.  My first design had only the Y axis being updated but later after some feedback I added the X axis as being selectable as well.

### Change History
#### viz_sketch.jpg
> This is the initial design of the visualization that I sketched out.  I knew I wanted to show pitchers used on the Y axis and game length on the x axis, but I wasn't sure how the reader exploration would work.  In this design it would be to allow the reader to select up to 2 teams and replay the animation.  (ultimately decided against that)

#### index_start.html
> This is the first iteration of the visual which I was just trying to plot all games with pitchers used vs. game time. (this is before any rollup code was added).  Here my main goal was to get something working that I could show as a preliminary visualization to get the basics setup (i.e. read in the file, get the scales corrected, the sizing of the visualization, etc..)

#### index_pre_animation.html
> These two are the first iteration of the visualization after adding the rollup code to summarize the games for each year.  In this version I wanted to make sure I could correctly rollup the data for each year and display on a scatter plot.  I was pretty sure the chart would show the relationship that I expected, but this was the first time that it was verified for me.

#### index - year animation.html
> This file has the animation built in for the years showing up from 1950 to 2014 and then allowing the reader to explore the Y axis.  At this point I started seeking formal feedback, the prior versions I did show to colleagues to make sure they understood where I was going and explain how it would work.  This version was the first "shared for critism" file, which I also published to the discussion formums.

#### index.html
> Here is the final version of the file with the updatable X Axis and improved Heading.  (The heading needed to be more clear that I was intending the reader to see my "Ah Ha" moment, but allow them to explore as well.)  The changes here reflected the feedback that I got from the forums and from a Data Scientist at State Farm.  Also, while leaving feedback for peers in the forums, I noticed that most were doing some writeup with their visualization.  I decided to add that as well.

## Feedback
> I received 3 total feedback so far on my visualization:  
> > The first is one of the files added that I received from a colleage where I work. (Jay Herrman: RE.Feedback.for.final.viz.project.pdf)
>
> > The 2nd is shown here in the [forum](https://discussions.udacity.com/t/final-project-feedback-mlb-game-length/159600 "feedback")
>
> > The 3rd was by phone from a fellow Data Scientist at State Farm Insurance on Thursday, March 3rd around 3pm CST.  His feedback was that it wasn't immediately clear what I was trying to show in the visualization and that it should very easy for the reader to see this right away.  He also stated that he wasn't convinced that it was the pitchers used in a game that led to the overall length of the game.  He mentioned that pitches thrown per game would be nice to see (which I agree and if I had the data I would have used that to size the circle radius instead of runs scored).  

## Resources
> I found some good help for my tool tip at this [resource](http://bl.ocks.org/Caged/6476579 "Gist D3-Tip example")

> Found a cool way to add a little [animation to the tooltip](animation to the tooltip)

> Looking for some good fonts, I came across this [nice writeup](http://www.webdesigndev.com/16-gorgeous-web-safe-fonts-to-use-with-css/)

>  I really struggled with the legends until I found [this](http://d3-legend.susielu.com/ "D3 Legend") and figured out the correct way to use it.

> And countless examples from [Mr. Mike Bostock](https://bost.ocks.org/mike/)

## Data 
>This is a custom dataset pulled from [http://www.retrosheet.org/](http://www.retrosheet.org/ "http://www.retrosheet.org/").

>From their “game logs” section http://www.retrosheet.org/gamelogs/index.html, I pulled only games from 1950 to 2014 so as to keep my observations down to under 150K. A summary of the variables found in this dataset can be found [here](http://www.retrosheet.org/gamelogs/glfields.txt "game data fields"). For this analysis we’ll narrow it down to the following fields:
<strong>home_team,home_league,time_of_game,runs,SO,BB,AB,hits,GDP,pitchers_used,DP,year,WH,era</strong>
