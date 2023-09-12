
## DDL Commands:

* Crimes Table
```sql
CREATE TABLE Crimes (
    crimeID INT, 
    crimeCode INT, 
    timeOccurred DATETIME, 
    weaponID INT,
    PRIMARY KEY (crimeID), 
    FOREIGN KEY (crimeCode) REFERENCES CrimeCodes(crimeCode), 
    FOREIGN KEY (weaponID) REFERENCES Weapons(weaponID)
);
```

* Weapons Table
```sql
CREATE TABLE Weapons (
    weaponID INT,
    description VARCHAR(max),
    PRIMARY KEY (crimeID)
);
```

* Victims Table
```sql
CREATE TABLE Victims (
    victimID INT,
    age INT,
    sex CHAR(1), 
    descent CHAR(1),
    crimeID INT,
    PRIMARY KEY (victimID),
);
```

* Locations Table
```sql
CREATE TABLE Locations (
    locationID INT, 
    latitiude REAL, 
    longitude REAL, 
    area VARCHAR(max), 
    street VARCHAR(max), 
    PRIMARY KEY (locationID)
);
```

* UserHistories Table
```sql
CREATE TABLE UserHistories (
    userID INT, 
    locationID INT, 
    currentTime DATETIME, 
    FOREIGN KEY (userID) REFERENCES Users (userID), 
    FOREIGN KEY (locationID) REFERENCES Locations (locationID)
);
```

* Users Table
```sql
CREATE TABLE Users (
      userID INT, 
      name VARCHAR(max), 
      age INT, 
      sex CHAR(1), 
      descent CHAR(1),
      email VARCHAR(max), 
      password VARCHAR(max), 
      PRIMARY KEY(userID)
 );
 ```

* CrimeCodes Table
```sql
CREATE TABLE CrimeCodes (
      crimeCode INT, 
      description VARCHAR(max), 
      PRIMARY KEY (crimeCode)
 );
```
* AffectedBy Table
```sql
CREATE TABLE AffectedBy (
	victimID INT,
	crimeID INT,
	FOREIGN KEY (victimID) REFERENCES Victims(victimID),
	FOREIGN KEY (crimeID) REFERENCES Crimes(crimeID)
);
```
* VictimizedAt Table
```sql
CREATE TABLE VictimizedAt (
	victimID INT,
	locationID INT,
	FOREIGN KEY (victimID) REFERENCES Victims(victimID),
	FOREIGN KEY (locationID) REFERENCES Locations(locationID)
);
```

## Advanced SQL Queries
This query searches for the top 15 locations with the highest crime occurrences. 
```sql
SELECT Crimes.CrimeCode, CrimeCodes.description, COUNT(*)/(SELECT COUNT(*) FROM Crimes) AS probability
FROM Crimes JOIN CrimeCodes ON (Crimes.crimeCode  = CrimeCodes.crimeCode)
GROUP BY CrimeCode
ORDER BY probability DESC
LIMIT 15;
```



This query generates which crimes are the most probable. 
```sql
SELECT Area, COUNT(*) 
FROM Locations JOIN VictimizedAt ON (Locations.locationID = VictimizedAt.locationID) JOIN Victims ON (VictimizedAt.victimID = Victims.victimID)
GROUP BY area
ORDER BY count(*) DESC
LIMIT 15;
```

Connecting to GCP:
![commandLine](https://user-images.githubusercontent.com/92744600/223779157-0996a9cd-3b07-4115-97fc-7ca36da644d4.png)


Count of 4 tables from our database:
![CountRows](https://user-images.githubusercontent.com/92744600/223265357-1dcde327-6075-4e96-a4b9-22b20abdbeec.png)

Top 15 rows of 1st query:
![1stQResults](https://user-images.githubusercontent.com/92744600/223266770-d8a5777d-32a7-429d-91e4-c201dba8639f.png)

Top 15 rows of 2nd query:
![2ndQResults](https://user-images.githubusercontent.com/92744600/223267252-33468151-66e5-49c6-83d9-4642e4b043eb.png)



## Indexing

1st Query:

Before indexing: ![BeforeIdx(1stQ)](https://user-images.githubusercontent.com/92744600/223243047-b8eac9e1-c8e9-4253-bc2b-0eb01019ca9e.png)

(`CREATE INDEX crimeIdx ON Crimes(CrimeID);`)
After Indexing (unclustered/primary): ![AfterIdx(2ndQ)](https://user-images.githubusercontent.com/92744600/223243096-fb8ea779-8e28-4eed-a871-bfe101220332.png)

We chose to index on the primary key because it made the most sense logically. We wanted to try an unclustered index, to speed up search operations. As you can see in the pictures above, even though the query iterated through the same number of rows, the time to perform the operation was faster after using unclustered indexing as we expected. 

(`CREATE INDEX idx_CriimeCode ON Crimes(CrimeCode);`)
After Indexing (unclusered/primary): <img width="1216" alt="image" src="https://user-images.githubusercontent.com/49540156/223621089-93c22af3-5a66-4c60-8ef4-2b5074d2a027.png"> 

We chose to index on this key because it was one of the main keys in the query - we perform a join based on the crimeCode, so indexing based off this key may potentially help when it comes to performing the join. Our intuition was right, since we took a lesser amount of time to perform our nested inner join!

(`CREATE INDEX idx_CrimeDesc ON Crimes(CrimeDesc);`)
<img width="1202" alt="image" src="https://user-images.githubusercontent.com/49540156/223621564-4681e9fc-e0c5-4b69-b909-736786436ae1.png">

We chose to index on the crimeDesc because we perform a select on the crime description - to this means, indexing by the crime description would potentially allow us to perform this select faster. Note that this approach was actually efficient, because it means that our table lookup turned into an index scan, which cut our time in half.

2nd Query:


Before Indexing:![BeforeIdx(2ndQ)](https://user-images.githubusercontent.com/92744600/223245168-515bd676-f72a-4ea8-8ce9-bfd2dde82720.png)

(CREATE INDEX locationIdx ON Locations(locationID);)
After Indexing:![AfterIdx(2ndQ2)](https://user-images.githubusercontent.com/92744600/223245199-b0f89c5f-d215-4e7d-9ac7-73cfd8e500cf.png)

Once again, we chose to index on the primary key because it would allow us to divide up the data nicely. We wanted to try an unclustered index, to speed up search operations. As you can see in the pictures above, even though the query iterated through the same number of rows, the time to perform the operation was faster after using unclustered indexing as we expected. 



(CREATE INDEX areaIdx on Locations(area);)
After Indexing: ![after2ndIdx(2ndQ)](https://user-images.githubusercontent.com/92744600/223775651-7423e79d-c748-4149-bbb6-ef466bbce847.png)

This time, since our advanced query was specifically grouping the results by the different areas in LA, we thought that it would be efficient to index on the area atttribute. Our intuition was correct, and this index design provided the fastest runtime results, as the indexing structure was directly correlated to the output of the query. This sped up the time it took to perform the nested inner loop join and improved the overall runtime.


(CREATE INDEX locIdx ON Locations(latitude, longitude);)
After Indexing: ![After3rdIdx(2ndQ)](https://user-images.githubusercontent.com/92744600/223776398-65441a3c-99d1-4008-9439-bbe96bd5c638.png)

Lastly, we wanted to try indexing on two different non-primary attributes to see if it would provide any optmiziations. Though it performed slighly faster than before the indexing, it was not as much of an improvement as the 2nd index design. We believe that because we were using two attributes to index, it would take up more space and time in the Btree to store all of our records, thereby causing the query's performance to increase only slightly. 
