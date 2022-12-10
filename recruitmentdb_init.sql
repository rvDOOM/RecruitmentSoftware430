CREATE DATABASE IF NOT EXISTS recruitmentdb;


CREATE TABLE Company(
	name CHAR(30) PRIMARY KEY,
    industrySector CHAR(30) NOT NULL,
    numOfEmployees INT
);

CREATE TABLE Candidate(
	firstName CHAR(30) NOT NULL,
    lastName CHAR(30) NOT NULL,
	phoneNumber CHAR(10) NOT NULL,
    address CHAR(50) NOT NULL,
    email CHAR(50) NOT NULL,
	CONSTRAINT PK_Candidate
		PRIMARY KEY (firstName, lastName)
);


CREATE TABLE Recruiter(
	firstName CHAR(30),
    lastName CHAR(30),
    CONSTRAINT PK_Recruiter
		PRIMARY KEY(firstName, lastName)
);


CREATE TABLE Reqs(
	name CHAR(40),
    annualPay INT NOT NULL,
    numOf INT NOT NULL,
    fullTime BIT NOT NULL,
    companyName CHAR(30) NOT NULL,
    recruiterFirstName CHAR(50),
    recruiterLastName CHAR(30),
    FOREIGN KEY (companyName) 
		REFERENCES Company(name),
	FOREIGN KEY (recruiterFirstName, recruiterLastName)
		REFERENCES Recruiter(firstName, lastName),
	CONSTRAINT
		PRIMARY KEY(name, companyName)
);


CREATE TABLE WorkHistory(
	candidateFirstName CHAR(30),
    candidateLastName CHAR(30),
    companyName CHAR(30),
    yoe int NOT NULL,
    FOREIGN KEY (candidateFirstName, candidateLastName)
		REFERENCES Candidate(firstName, lastName),
	FOREIGN KEY (companyName)
		REFERENCES Company(name),
	CONSTRAINT PK_WorkHistory
		PRIMARY KEY (candidateFirstName, candidateLastName, companyName)
);


CREATE TABLE Interviews(
	candidateFirstName CHAR(30),
    candidateLastName CHAR(30),
    reqName CHAR(40),
    companyName CHAR(30),
    dateOf DATE,
    timeOf TIME,
    FOREIGN KEY (candidateFirstName, candidateLastName)
		REFERENCES Candidate(firstName, lastName),
	FOREIGN KEY (reqName, companyName)
		REFERENCES Reqs(name, companyName),
	CONSTRAINT PK_Interviews
		PRIMARY KEY (candidateFirstName, candidateLastName, reqName, companyName)
);


INSERT INTO Company
VALUES
("Grant Associates", "Recruitment", 550),
("Google", "Tech", 10200),
("Uber", "Tech", 1550),
("Walmart", "Retail", 572754),
("Microsoft", "Tech", 198087),
("The Home Depot", "Retail", 151157),
("JPMorgan Chase", "Financial services", 127202),
("Lowe's", "Retail", 96250 ),
("State Farm", "Financials", 82407),
("Intel", "Technology", 79024);


INSERT INTO Candidate 
VALUES 
("Richard", "Valerio", 3474963211, "319 Vaughan St, Staten Island, NY 10305", "rv91@gmail.com"),
("Alyssa", "Pena", 9174589652, "402 West Hanover Ave., Woodside, NY 11377", "ap32@yahoo.com"),
("Michael", "Sanchez", 3478546985, "7954 Valley Farms St, Buffalo, NY 14215", "flakes44@playfuny.com"),
("Rayed", "Rashed", 9174523216, "7879 S. Edgefield Street, Middletown, NY 10940", "susl231192@gmailvn.net"),
("Angela", "Liu", 7185423685, "593 Deerfield Street, Fairport, NY 14450", "aaccaaa@uhpanel.com"),
("Ramon", "Diaz", 9178459632, "450 East Street, Bronx, NY 10461", "bronce896@gmailpro.ml"),
("Christopher", "Muniz", 3474125521, "19 State Street, New York, NY 10024", "dput8dra@sepican.website"),
("Brooke", "Davis", 9296587854, "58 Thatcher Drive, Brooklyn, NY 11221", "katie71@mailcuk.com"),
("Dwayne", "Carter", 9297539512, "14 Whitemarsh Street, New York, NY 10027", "s0v3e2t@bomukic.com"),
("Raul", "Nunez", 7184523215, "234 Marvon Dr., Flushing, NY 11354", "redkooo@pianoxltd.com"),
("James", "Gandolfini", 9178423125, "91 Beechwood Rd., New York, NY 10033", "martagonzalez21@mailsupply.net");


INSERT INTO Recruiter
VALUES
("Shauna", "Huang"),
("Inaaya", "Aguilar"),
("Presley", "Lozano"),
("Harvey", "Bryan"),
("Calvin", "Jackson"),
("Mari", "Mercer");


INSERT INTO Reqs
VALUES
("Account Manager", 70000, 4, 1, "Grant Associates", "Shauna", "Huang"),
("Career Advisor", 55000, 2, 1, "Grant Associates", "Inaaya", "Aguilar"),
("Director", 115000, 1, 1, "Grant Associates", "Presley", "Lozano"),
("Office Assistant", 40000, 2, 0, "Grant Associates", "Shauna", "Huang"),
("Software Engineer", 210000, 5, 1, "Google", "Presley", "Lozano"),
("Program Manager", 218000, 2, 1, "Google", "Harvey", "Bryan"),
("Business Analyst", 158000, 3, 1, "Google", "Inaaya", "Aguilar"),
("Software Engineer", 187000, 2, 1, "Uber", "Inaaya", "Aguilar"),
("Driver", 47000, 24, 1, "Uber", "Inaaya", "Aguilar"),
("Senior Software Engineer", 214000, 1, 1, "Uber", "Shauna", "Huang"),
("Data Scientist", 187000, 2, 1, "Uber", "Presley", "Lozano"),
("Dept. Manager", 54000, 2, 1, "Walmart", "Harvey", "Bryan"),
("Sales Associate", 40681, 13, 0, "Walmart", "Harvey", "Bryan"),
("Overnight Stocker", 40681, 11,0, "Walmart", "Shauna", "Huang"),
("Software Engineer", 142000, 3, 1, "Microsoft", "Calvin", "Jackson"),
("Data and Applied Scientist", 179000, 1, 1, "Microsoft", "Harvey", "Bryan"),
("Support Engineer", 135000, 3, 1, "Microsoft", "Mari", "Mercer"),
("Sales Associate", 46448, 12, 0, "The Home Depot", "Mari", "Mercer"),
("Customer Service Representative", 37000, 15, 0, "The Home Depot", "Shauna", "Huang"),
("Supervisor", 49000, 3, 1, "The Home Depot", "Calvin", "Jackson"),
("Cashier", 135000, 11, 1, "The Home Depot", "Mari", "Mercer"),
("Financial Analyst", 83592, 11, 1, "JPMorgan Chase", "Calvin", "Jackson");

INSERT INTO WorkHistory
VALUES
("Richard", "Valerio", "Grant Associates", 5),
("Richard", "Valerio", "JPMorgan Chase", 2),
("Richard", "Valerio", "State Farm", 5),
("Alyssa", "Pena", "Uber", 6),
("Alyssa", "Pena", "Microsoft", 2),
("Michael", "Sanchez", "State Farm", 2),
("Rayed", "Rashed","Grant Associates", 4),
("Rayed", "Rashed","Intel", 2),
("Rayed", "Rashed","Walmart", 1),
("Angela", "Liu","Grant Associates",3),
("Ramon", "Diaz", "Uber", 1),
("Ramon", "Diaz", "Intel", 2),
("Ramon", "Diaz", "Microsoft", 4),
("Christopher", "Muniz","The Home Depot",2),
("Brooke", "Davis","Grant Associates", 1),
("Dwayne", "Carter","Lowe's", 4),
("Raul", "Nunez","Walmart",1);

INSERT INTO Interviews
VALUES
("Richard", "Valerio", "Account Manager", "Grant Associates", '2022-12-31', '12:31:00'),
("Alyssa", "Pena", "Account Manager", "Grant Associates", '2022-12-25', '05:30:00');






SELECT * FROM Company;
SELECT * FROM Candidate;
SELECT * FROM Recruiter;
SELECT * FROM Reqs;
SELECT * FROM Interviews;

#DROP TABLE WorkHistory;
#DROP TABLE Reqs;
#DROP TABLE Recruiter;
#DROP TABLE Company;
#DROP TABLE Candidate;
#DROP TABLE Interviews;