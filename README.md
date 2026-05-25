# DATA201-FinalPrj-AKM Project Report

Data collection and Data Types
Data is collected within the three weeks. One dataset include routine informations and the other include external events happened withtin the threee weeks

Collected Data include:
2 weeks record (Rountines).csv
- Date - MM/DD/YYYY
- Activity - Types of general activties that I do (Sleep, Social,Study, Class,Chores, Screen Time)
- Hour - the amount of hours spent on the activity
- Efficiency_score - subjective scoring (0 to 5) based upon how much I felt accomplished, learnt or satisfied within the activity
- Exam_Week - Boolean values that indicate whether the week is final week filled with exams and assignments, or not
- Week_no - numerical value to separate the weeks for analysis.

2 weeks record (Events).csv
- Date - MM/DD/YYYY
- Electricity_cuts - categorical values stating whether the electricity cuts are 'Normal' (scheduled cuts), or 'Severe' (no scheduled with long cuts)
- Connection_problem - categorical values also stating the coonection is 'Normal' (Low disturbance) or 'Severe' (long connection lost time)
- Min, Avg, Max Tmeperatures (celsius) - temperature data of my home town collected from public weather records.

Story overview

I have collected three weeks worth of data to analyze my general routines efficiency and how the external factor can impact me. Also I would like to know how am I managing my time.
First week can be the normal week without exam and electrical problems. Showing my laid back study patterns
Second week have external factors disrupting my routines
Third week is the exam week. I can analyse how I manage my studies in exam week.
I chose this topic to know, how I am doing and how to improve myself.

Key Findings

- First finding is that my average efficiency score in overall activities rise in exam week. My conclusion is that I must have more focus on study matters as exams are near. Raising efficiency in overall tasks.
- Second finding is that, significant amount of time is allocated to Screen Time and Sleep. Indicating I wasting a lot of my time on Screen rather than being productive. Procrastination effects can be seen by the sharp rise in avg study hours and reduced screen time.
- Third finding is that external factors impacts more than I think. Lowering efficiency to a significant level in study and noticeable amount in overall.

Future Decision making

- Scheduling Study time and other important activities: To increase efficiency in my routines and be able to face electricity cuts and connection problems.
- Adjusting Screen Time: reducing screen time will be helpful since it take majority of the time of the days. And extra time could be allocated to other activities such as study in non-exam week to avoid last minute preparations

Ethical Discussion

Privacy Statement

- What data is included?: Non-sensitive data such as general activity (eg. screen time, sleep) and public data such as electricity cuts.
- What is anonymized?: Information such as my name, exact details on the activity (such as who I socialise with) are excluded. So, there is no identifiable information in the data set.

Bias & Limitation Disclosure

- Memory bias: Some data input(such as electricity problems and hours before May 10th) are from memory. So, the data may slight over or under represent the exact activities happened.
- Subjective Scoring: The data set include efficiency score which is scored subjectively from how I felt during that activity on that day. It is not a standard metric.
- Small Dataset: The dataset is relatively small (only 3 week worth of data), it might not fully describe my activities and events across the year

Visualization Justification

- Line Chart for Avg Efficiency Trend: As I would like to show trend, I think line chart is the most clear choice since it can show ups and downs clearly.

- Line Chart for Hours spend on Activity: Even though it looks crowded on default, it can show clear trends when filtered. Similar to the previous reason.

- Pie Chart for actvities per rweek: As I would like to show the distribution of activity time in the weeks and the categories are not many, I chose pie chart to represent the data.

- Correlation Heat Map for factors and Avg efficienc: To show the correlation cleary to the audience, heat map is used instead of scatter plot.

- Bar Chart for impact on avg efficiency: To compare the impact of external factors, I chose bar chart since it can show the difference clearly and simple to read.

- Risk: Correlation heat map can be hard to interpret for general audience. It can cause misinterpretation. And since the data are daily trends the sharp spikes can look more exaggerated.

Responsible Decision

- Limitation on Decision: Since the data set is relatively small (Time-wise and Variable-wise). There can be more factors that can interfere with my activities. This limit my decision to be set upon conditions that available in the dataset.
🤖 AI usage
Gemini 3 Flash is used in the creation of the dashboard and visualization templates. Insights, EDA and Visualizations are done by human.
