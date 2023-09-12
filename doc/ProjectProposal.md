Describe what data is stored in the database. (Where is the data from, and what attributes and information would be stored?) 

In terms of storing data, we’ll be using the “Crime in Los Angeles Data From 2020 To Present” dataset. This dataset should contain most of the crime data in Los Angeles, which we will extrapolate to identify dangerous areas that users might be in. At a high level, we’ll have the following categories of data: location-based, time-based, and severity-based. 

Given a potential user’s location, we can take advantage of their location and time to find data that is most similar to the current conditions. Given that data, we can return the severity of the situation, and potentially provide the user with useful information.

What are the basic functions of your web application? (What can users of this website do? Which simple and complex features are there?)

Naturally, the most important feature of our application is to give the users an accurate depiction of the danger of their surroundings. To this means, the most important feature is to take in the location and time as input (which we can simply do with permissions), and then return the severity of the location. While this itself feels simple, it has a lot of potential to be complicated - for instance, if we do add in integrations that are user-based (i.e. setting emergency contacts or saved paths), then we would also need to work around authentication/authorization. This has the potential to drag down our project, and we need to ensure that we focus on the main features first.

What would be a good creative component (function) that can improve the functionality of your application? (What is something cool that you want to include? How are you planning to achieve it?) 

A few creative (and daring) modifications that we want to include are: 
Real-time location so that the user can identify which parts of the city are currently present in. We plan to use the Google Maps API and the real time GPS functionality present in most computers and mobile devices.
Notifications to the web/mobile app so that if the user is walking through a dangerous part of the city where multiple crimes have been committed that the current user is more susceptible to based on historical data and the user’s information such as age, sex, etc. Using either client side local notifications or Firebase Cloud Messaging, we should be able to give the user notifications when they enter a dangerous region. This feature will require real-time user location to have been implemented.
(Not planned for the MVP) Navigation to give the user the fastest path out of a dangerous part of the city. We would need to use the Google Maps API for this too or develop our own search algorithm to find the nearest relatively safe location.

Project Title:  Daringly Detailed Danger Mapper in LA

Project Summary: 

Our project will be a web and/or mobile application that uses the historical crime data of the city of LA to identify dangerous regions of areas of the city and visualize that on a map based on the severity and number of crimes using heat maps and markers. We also want to provide the user real-time information about the area in their current vicinity by using the real-time location of the user, displaying that on the map too, and also take into account their demographics so that the severity of the danger is personalized to the user.

Description of an application of your choice. State as clearly as possible what you want to do. What problem do you want to solve, etc.? 

We are going to implement a web and/or mobile application that uses the database containing data of the historical crime rate in various regions in LA to identify and display dangerous and volatile areas to avoid. Using the available data, we are going to allow all users to view and update both crime-ridden and relatively safe areas within LA for other people to recognize potential dangers in their current locations and to take an effective course of action to extract themselves from that situation. We will use existing APIs and GPS functionality to maintain cohesiveness in our project’s technical development so that all platforms can access our application. To ensure peak usage and functionality in the application, we will employ live notifications based on user inputs and trends to ensure that people are constantly aware of criminal events in their vicinity. We will also have an easy user interface for users to view such that each output from our application can be clearly viewed. Considering this application development avenue would provide relevant and accurate insights for users to maintain their safety, this application will have a lot of use cases and can be extrapolated to many more geographical regions or technical purposes. Many crimes in the United States, especially in LA, happen to tourists who are unaware of the region or their location, and I believe that our application would help minimize these occurrences if not eliminate them altogether. 

Usefulness. Explain as clearly as possible why your chosen application is useful.  Make sure to answer the following questions: Are there any similar websites/applications out there?  If so, what are they, and how is yours different? 
Crime is an ever present problem in the United States, especially in metropolitan areas with high densities of people. With crime on the rise, it is important for people to make sure they know which areas are safer than others. Tourists from across the world come to Los Angeles due to its various attractions, and knowing where to go to enjoy nightlife without risking their lives or their belongings is essential towards making a good community. With an application like ours, it helps people avoid these very dangerous issues and enjoy their time in Los Angeles.
Apps similar to ours include CrimeReports, NextDoor, and NeighborhoodScout, but they all serve different functions with different data. CrimeReports has real time data that allows users to understand if an area is dangerous when they are active. NextDoor has neighborhood specific events that allow users to understand potential and actual criminal events in their vicinity. NeighborhoodScout allows users to view criminal data when it comes to real estate applications. Because our app will give historical data of criminal issues associated to each region of Los Angeles independent of specific use cases, it shows that this app has a different overall functionality than the others. Our app will be unique in that each data point will have a strong historical data-based perspective on the danger level of each region in Los Angeles and can incorporate real time updates based on individual user updates.  

Realness.  Describe what your data is and where you will get it.

We decided to use the dataset about crime history in LA since 2020 to present day in order to create an application that will help the users offer a sense of security as well as caution about their current location and time. The dataset itself comes from Kaggle and is transcribed from original crime reports from LA. However, the address fields are only provided to the nearest hundredth block as the creator of the dataset wanted to maintain anonymity for the residents in LA. Therefore, our application won’t be able to make street-by-street predictions on the user’s current threat level, but we will be able to make zones across LA that still provide accurate information. 
Some of the data includes the time and date at which the crime was committed, which LAPD stations were called, what crime was actually committed (using crime codes that the police use), victim’s age, gender, race, location, as well as perpetrator information. Using this data, we will be able to create a visualization of LA and its most dangerous areas. We could also allow users to self-report crime, add their information into the database, and update the appropriate locations and their associated danger levels. It’s also important to note that the user’s threat levels will change according to their age, gender, ect. So our application will take all of this into account, along with the known history of crime to best predict what kind of threats the user may be exposed to at certain times and locations. 

Description of the functionality that your website offers:
 
Our website will allow users to input their real-time location, along with their personal information (based on how comfortable they are with sharing it) and display a numerical threat level that we will determine using the data set of previous crime history in the city of LA. Although users can omit certain information about themselves, the application will provide more accurate feedback if the user fills out all the information. In addition, the website will constantly keep track of the user’s nearest LAPD, in order to keep the user vigilant and able to find help when needed. There will also be specific danger zones that the website will recommend the users avoid as they were typically hotspots for crimes in the past. Different users can use the application, update their information as necessary, which would also update the feedback that the website provides. Users will most likely not be able to delete entries from the dataset, as these were all real-life crimes that already occurred in the past. However, they will be able to self-report crime and add more data to the database. 

UI mockup:![IMG_0032](https://user-images.githubusercontent.com/92744600/216855642-7ebb00b5-3e13-4ee0-b448-cdc5b9c2f1ae.png)


Project work distribution: We will develop the backend of the application first, as that is the focus of this project. Aydan and Karthik will lead this portion as they are more experienced with SQL and handling real life data sets. As we near stage 4 of the project, we hope to be done with the overall framework of the backend portion, so that we could integrate it with our frontend. Apoorva and David will be responsible for developing an easy to use, friendly, and intuitive interface for the user to interact with. Due to the nature of the application, the backend will be more focused on defining clear relationships between schemas as well as creating/reading data. On the other hand, the frontend team will focus more on making updates to the database as well as querying for specific information, as that is most relevant for the users. As a team, we will ensure a smooth integration among these major components. In addition, as with any coding project, we will create our own branches from the git repository as we write our code. We will make sure to use pull requests and have everyone review the changes/edits before merging into the main branch. We will keep each other accountable and maintain communication through Discord as we work on this project. 
