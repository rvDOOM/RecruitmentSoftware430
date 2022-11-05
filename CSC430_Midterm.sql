#DROP DATABASE CSC430_Midterm;
CREATE DATABASE CSC430_Midterm;

USE CSC430_Midterm;
CREATE USER 'api'@'localhost' IDENTIFIED WITH caching_sha2_password BY "password";
GRANT ALL PRIVILEGES ON mydb.* TO 'api'@'localhost' WITH GRANT OPTION;

CREATE TABLE Candidate(
	uName CHAR(20) NOT NULL,
    currentJobTitle CHAR(30),
    employeed BOOL,
    PRIMARY KEY (uName)
);

# ALL COMPANIES, EVEN THE ONES THAT CANDIDATES HAVE WORKED FOR IN THE PAST
CREATE TABLE Company(
	cName CHAR(30) NOT NULL PRIMARY KEY,
    industrySector CHAR(30) NOT NULL
);

CREATE TABLE PreviousJobs(
	uName CHAR(20) NOT NULL,
	jobPosition CHAR(30),
    cName CHAR(30),
	FOREIGN KEY (uName) REFERENCES Candidate (uName),
    FOREIGN KEY (cName) REFERENCES Company (cName)
);


CREATE TABLE Recruiter(
	aName CHAR(30) NOT NULL PRIMARY KEY,
    company CHAR(30)NOT NULL,
	FOREIGN KEY (company) REFERENCES Company (cName) #Maybe 
);

CREATE TABLE JobPosition(
	pName CHAR(30) NOT NULL,
    positionID INT   PRIMARY KEY,
    numOfOpenings INT,
    totalFilled INT,
    recruiter CHAR(30) NOT NULL,
    agency CHAR(30) NOT NULL,
    
    FOREIGN KEY (recruiter) REFERENCES Recruiter (aName)
	#FOREIGN KEY (positionID) REFERENCES Agency(positionID)
);
#COMAPNY THAT IS ACTIVELY HIRING IS AN AGENCY
CREATE TABLE Agency(
	cName CHAR(30) NOT NULL PRIMARY KEY,
    industrySector CHAR(30) NOT NULL,
    jobPositionName CHAR(30) NOT NULL,
    positionID int,

   FOREIGN KEY (positionID) REFERENCES JobPosition(positionID)
);

#Filling in example data 
INSERT INTO Candidate (uName, currentJobTitle,  employeed) VALUES ('William','Analyst', '1');
INSERT INTO Candidate (uName, currentJobTitle,  employeed) VALUES ('Charles','Retail', '0');

INSERT INTO Company (cName, industrySector) VALUES ('Google', 'Tech');
INSERT INTO Company (cName, industrySector) VALUES ('Meta', 'Tech');
INSERT INTO Company (cName, industrySector) VALUES ('Apple', 'Tech');

INSERT INTO PreviousJobs (uName, jobPosition, cName) VALUES ('William', 'Retail', 'Apple'); 

INSERT INTO Recruiter(aName, company) VALUES ('John', 'Google');
INSERT INTO Recruiter(aName, company) VALUES ('Gemma', 'Meta');
INSERT INTO Recruiter(aName, company) VALUES ('Sabrina', 'Apple');

INSERT INTO JobPosition (pName, positionID, numOfOpenings, totalFilled, recruiter, agency) VALUES 
('Programmer', '3', '5', '0', 'Gemma', 'SomeAgency');

INSERT INTO Agency (cName, industrySector, jobPositionName, positionID) VALUES ('SomeJobAgency', 'Tech', 'Programmer', '3');

SELECT* from Recruiter; #Grabs the entire Recruiter table
SELECT* from JobPosition; #Grabs the entire JobPosition table
SELECT* from Candidate; #Grabs the entire Candidate table

#positionID is the primary key
#foreign key positionID is how we map the position in the agency to the position in the Agency table 
#positionID is how we can query the positions that are open for a company


#adding the foreign key to table JobPosition so we can use the hashmap data here for Agency -- to map a position to agency
ALTER TABLE JobPosition ADD CONSTRAINT FOREIGN KEY (agency) REFERENCES Agency (cName);


#DROP TABLE Candidate;
#DROP TABLE Company;
#DROP TABLE AGENCY;
#DROP TABLE RECRUITER;
#DROP TABLE JOBPOSIITON;
#DROP DATABASE CSC430_Midterm;