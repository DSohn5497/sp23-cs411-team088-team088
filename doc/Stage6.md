1. Please list out changes in the directions of your project if the final project is different from your original proposal (based on your stage 1 proposal submission).
<br>
Originally, we were planning to describe the user’s “danger level” through some sort of heat map or a scale from 1-10 based on the user’s surroundings. However, we found that this would be very difficult to implement in our application, so we opted for a bit of a simpler solution. Instead of describing the “danger level” of the user, we give them an interface through which they can check the nearest crime closest to their location along with the probability of it happening using historical crime data in LA. We also wanted to have a function that would automatically alert the user when they enter a particularly dangerous area. However, this would require geo-fencing and due to time constraints we were not able to implement this feature either. Aside from these functions, though, the final project is pretty close to what we envisioned in the beginning of the semester.

2. Discuss what you think your application achieved or failed to achieve regarding its usefulness.
<br>
I think our application provides the most value to its users through its map visualization of the crimes that have occurred in LA. While locals may be more familiar with what routes/areas to avoid, for tourists/visitors, our app would be extremely informative as users can clearly see which areas are generally more concentrated with crimes. However, like we mentioned in question 1, we failed to create a notification system that automatically alerts users of high-risk areas. This was mainly due to the fact that our trigger was based on an insertion into our UserHistories table, so it made more sense to allow users to press a button that would set off the trigger and run our advanced queries. 

3. Discuss if you changed the schema or source of the data for your application.
<br>
We did not change the source of the data for the application, but we did change the schema from our original idea in stage 2. We actually created a whole new table called “NearestCrimes” that kept track of the user’s current location, the nearest crime to the user (determined using euclidean distances of latitude/longitude), along with the probability of that crime occurring relative to other crimes in our database. Furthermore, we switched around some foreign keys and removed redundant attributes from our Crimes, Locations, and Victims tables so that we could apply natural joins to them in our advanced queries. 
<br>
4. Discuss what you change to your ER diagram and/or your table implementations. What are some differences between the original design and the final design? Why? What do you think is a more suitable design? 
<br>
Like we stated in question 3, we changed the foreign keys of the Crimes, Locations, and Victims tables so that we could properly join them in our advanced queries. For example, in our original ER diagram, our crimes table actually didn’t have a locationID, so there was actually no way for us to recognize where each crime took place. This was a mistake in our original design, and we quickly recognized its issues as we tried to create the tables and apply our queries on them. We also created the new “NearestCrimes” table near the tail-end of our project so that we could use our stored procedure to retrieve information from the backend. Our final design is definitely not perfect, but it allowed us to effectively run our CRUD operations along with the trigger+stored procedure. 

5. Discuss what functionalities you added or removed. Why?
<br>
We described what functionalities we removed in question 1, such as the “heat map” of the danger levels of the users and the notification systems. We removed these functionalities due to practical limitations based on our time and experience/knowledge of SQL. Throughout the project, we learned that, although it is easy to write queries, it is hard to implement an interaction between the frontend and backend that invokes these queries in a streamlined manner. We also added the functionality of being able to query for the top 15 most crime-concentrated areas in LA, along with the most likely crimes to occur and their probabilities. Since we didn’t know all the requirements of the project in our original design, we didn’t think of adding this query functionality until we reached stage 3. 

6. Explain how you think your advanced database programs complement your application.
<br>
I think our 2 advanced queries from stage 3 really help to establish a link between the UI interface as well along with our real-life crime data. Not only can users visually see which areas are more risky, they can search up the most likely crimes to occur in these areas, which we believe is valuable information for being conscious of your safety. Also our trigger+stored procedure give users an even greater sense of awareness as they can receive information regarding the nearest crime to their current location. Although it would be nice if we could automate this process, for the sake of fulfilling the requirements, we give users an interface through which they can activate this function of our application. 

7. Each team member should describe one technical challenge that the team encountered.  This should be sufficiently detailed such that another future team could use this as helpful advice if they were to start a similar project or where to maintain your project. 
<br>
Karthik focused on the database design and implementation, and his main technical challenge was figuring out the way that tables could be entered into GCP in the most sensible way possible. Using the correct data and making the most logical decisions regarding what information should be shown to the users to make the application the most effective was the technical challenge. After deliberation we decided to use 1000 rows for the data as testing so that we can show crime codes and information about the crime that would help provide information about crimes in a user’s geographical vicinity. 

<br>
Aydan focused on the backend setup, namely getting the server running and connecting it with the SQL database too. While setting the server up was relatively straightforward, we ran into a lot of authentication issues with the SQL setup, since we had to use Google’s default authentication protocol. Additionally, there were issues with using SQLalchemy to push to 
<br>
Apoorva focused on the frontend - designing and implementing the screens and integrating the backend into the visual output. One issue that popped up was that there was there was no package for Google Maps in Flutter web that had implemented the user’s location, so we had to research, find and use an untested and unendorsed implementation of the user location API and thankfully that worked, however it took a while.There were also issues with passing data from the frontend to the backend API that we had created - more specifically, whenever we made a POST request, Flask didn't parse the data payload correctly and the request couldn’t be processed because of it. We fixed it by passing our data as query parameters in the request URL instead and that fixed the issue, however because of that we need to make sure that sensitive data like passwords is secure and encrypted.
<br>
David focused more on the big picture of the project such as refining schemas and relational diagrams, creating queries, and integrating more advanced database functions into the overall project. One challenge that arose was actually hosting our database on the GCP because our original schema definitions didn’t define foreign keys properly. Therefore, when we tried to create certain tables, the code would fail and not execute properly. Then further complications arose when we tried modifying the tables directly because of those foreign key dependencies. We ended up dropping our original tables and just creating the new tables from scratch. If we were to do a similar project in the future, we’d definitely spend more time ensuring that our ER diagrams/schemas are well-constructed before implementing them on GCP where it’s difficult to undo certain actions. 

8. Are there other things that changed comparing the final application with the original proposal?
<br>
I think we’ve discussed this pretty extensively at this point, but besides a couple of minor changes in the implementation of our database and the interface of the UI, our final application is pretty close to the original proposal we had in mind. 

9. Describe future work that you think, other than the interface, that the application can improve on.
<br>
I think we can improve the application by adding the geofencing functionality discussed above that would automatically alert users when they enter a location of a certain “danger level”. Furthermore, instead of simply calculating the probability of seeing a certain crime based only on location/area, we could also take into factor the user’s age/sex/other info to try and create a more accurate model of their safety. Also, since most of our information is already in a document-based format (and we use Json to relay information across the frontend/backend), we could create a NOSQL mongodb database that would allow us to perform aggregation functions for more complex/streamlined queries. We were also discussing this near the final stages of our project, but we wanted to give users the ability to report crimes whenever they see it so that the database would continue to stay up-to-date. However, we realized that this would be impractical as it would require verification with police records, and may lead to potential misuse of the application. Overall, though, we are very happy with our final product. 

10. Describe the final division of labor and how well you managed teamwork.
<br>
David - Coordinated team meetings, divided up work between members, created ER diagrams, wrote SQL/DDL code
<br>
Apoorva - Worked on the frontend of the application, set up Flutter and GoogleMaps API, connected frontend/backend with REST API
<br>
Aydan - Worked on the backend of the application, set up SQLAlchemy, connected frontend/backend with REST API
<br>
Karthik- Also worked on the frontend of the application, implemented database on GCP and helped with indexing/UI designs
<br>
Our team worked very well together. We understood our strengths and weaknesses, and worked hard to help each other in areas that we were lacking knowledge/experience in. Everyone was very cooperative, understanding, and put in an honest effort into every stage of the project. 
