--------------------------------------------------------
--  File created - Thursday-April-07-2011   
--------------------------------------------------------
--------------------------------------------------------
--  DDL for Sequence SEQ_AUTHOR
--------------------------------------------------------

   CREATE SEQUENCE  "SEQ_AUTHOR"  MINVALUE 0 MAXVALUE 9999999999999999999999999999 INCREMENT BY 1 START WITH 120 CACHE 20 NOORDER  NOCYCLE ;
--------------------------------------------------------
--  DDL for Sequence SEQ_PUBLISHER
--------------------------------------------------------

   CREATE SEQUENCE  "SEQ_PUBLISHER"  MINVALUE 0 MAXVALUE 9999999999999999999999999999 INCREMENT BY 1 START WITH 20 CACHE 20 NOORDER  NOCYCLE ;
--------------------------------------------------------
--  DDL for Sequence SEQ_SRESOURCE
--------------------------------------------------------

   CREATE SEQUENCE  "SEQ_SRESOURCE"  MINVALUE 0 MAXVALUE 9999999999999999999999999999 INCREMENT BY 1 START WITH 5440 CACHE 20 NOORDER  NOCYCLE ;
--------------------------------------------------------
--  DDL for Sequence SEQ_VENUE
--------------------------------------------------------

   CREATE SEQUENCE  "SEQ_VENUE"  MINVALUE 0 MAXVALUE 9999999999999999999999999999 INCREMENT BY 1 START WITH 580 CACHE 20 NOORDER  NOCYCLE ;
--------------------------------------------------------
--  DDL for Table COMMUNITY
--------------------------------------------------------

  CREATE TABLE "COMMUNITY" 
   (	"COMMUNITY_ID" NUMBER, 
	"COMMUNITY_NAME" VARCHAR2(100), 
	"GROUP_NAME" VARCHAR2(100)
   ) ;
--------------------------------------------------------
--  DDL for Table COMMUNITY_JOURNAL
--------------------------------------------------------

  CREATE TABLE "COMMUNITY_JOURNAL" 
   (	"COMMUNITY_ID" NUMBER, 
	"JOURNAL_ID" NUMBER
   ) ;
--------------------------------------------------------
--  DDL for Table COMMUNITY_PERSON
--------------------------------------------------------

  CREATE TABLE "COMMUNITY_PERSON" 
   (	"PERSON_ID" NUMBER, 
	"COMMUNITY_ID" NUMBER
   ) ;
--------------------------------------------------------
--  DDL for Table JOURNAL
--------------------------------------------------------

  CREATE TABLE "JOURNAL" 
   (	"JOURNAL_ID" NUMBER, 
	"JOURNAL_NAME" VARCHAR2(2000)
   ) ;
--------------------------------------------------------
--  DDL for Table RATING
--------------------------------------------------------

  CREATE TABLE "RATING" 
   (	"RATER_ID" NUMBER, 
	"RATED_PERSON_ID" NUMBER, 
	"RATING" FLOAT(63), 
	"RESEARCH_ROLE_ID" NUMBER
   ) ;
--------------------------------------------------------
--  DDL for Table RESEARCH_ROLE
--------------------------------------------------------

  CREATE TABLE "RESEARCH_ROLE" 
   (	"RESEARCH_ROLE_ID" NUMBER, 
	"RESEARCH_ROLE_NAME" VARCHAR2(100)
   ) ;
--------------------------------------------------------
--  DDL for Table SURVEY
--------------------------------------------------------

  CREATE TABLE "SURVEY" 
   (	"SURVEY_ID" NUMBER, 
	"SURVEY_NAME" VARCHAR2(100), 
	"SURVEY_URL" VARCHAR2(2000)
   ) ;

---------------------------------------------------
--   DATA FOR TABLE COMMUNITY
--   FILTER = none used
---------------------------------------------------
REM INSERTING into COMMUNITY
Insert into COMMUNITY (COMMUNITY_ID,COMMUNITY_NAME,GROUP_NAME) values (1,'ICST - Algorithms Engineering','ICST');

---------------------------------------------------
--   END DATA FOR TABLE COMMUNITY
---------------------------------------------------


---------------------------------------------------
--   DATA FOR TABLE COMMUNITY_JOURNAL
--   FILTER = none used
---------------------------------------------------
REM INSERTING into COMMUNITY_JOURNAL

---------------------------------------------------
--   END DATA FOR TABLE COMMUNITY_JOURNAL
---------------------------------------------------


---------------------------------------------------
--   DATA FOR TABLE COMMUNITY_PERSON
--   FILTER = none used
---------------------------------------------------
REM INSERTING into COMMUNITY_PERSON

---------------------------------------------------
--   END DATA FOR TABLE COMMUNITY_PERSON
---------------------------------------------------


---------------------------------------------------
--   DATA FOR TABLE JOURNAL
--   FILTER = none used
---------------------------------------------------
REM INSERTING into JOURNAL

---------------------------------------------------
--   END DATA FOR TABLE JOURNAL
---------------------------------------------------


---------------------------------------------------
--   DATA FOR TABLE RATING
--   FILTER = none used
---------------------------------------------------
REM INSERTING into RATING

---------------------------------------------------
--   END DATA FOR TABLE RATING
---------------------------------------------------


---------------------------------------------------
--   DATA FOR TABLE RESEARCH_ROLE
--   FILTER = none used
---------------------------------------------------
REM INSERTING into RESEARCH_ROLE
Insert into RESEARCH_ROLE (RESEARCH_ROLE_ID,RESEARCH_ROLE_NAME) values (1,'author');
Insert into RESEARCH_ROLE (RESEARCH_ROLE_ID,RESEARCH_ROLE_NAME) values (2,'reviewer');

---------------------------------------------------
--   END DATA FOR TABLE RESEARCH_ROLE
---------------------------------------------------


---------------------------------------------------
--   DATA FOR TABLE SURVEY
--   FILTER = none used
---------------------------------------------------
REM INSERTING into SURVEY

---------------------------------------------------
--   END DATA FOR TABLE SURVEY
---------------------------------------------------








--------------------------------------------------------
--  DDL for Index COMMUNITY_JOURNAL_PK
--------------------------------------------------------

  CREATE UNIQUE INDEX "COMMUNITY_JOURNAL_PK" ON "COMMUNITY_JOURNAL" ("COMMUNITY_ID", "JOURNAL_ID") 
  ;
--------------------------------------------------------
--  DDL for Index COMMUNITY_PERSON_PK
--------------------------------------------------------

  CREATE UNIQUE INDEX "COMMUNITY_PERSON_PK" ON "COMMUNITY_PERSON" ("PERSON_ID", "COMMUNITY_ID") 
  ;
--------------------------------------------------------
--  DDL for Index COMMUNITY_PK
--------------------------------------------------------

  CREATE UNIQUE INDEX "COMMUNITY_PK" ON "COMMUNITY" ("COMMUNITY_ID") 
  ;
--------------------------------------------------------
--  DDL for Index JOURNAL_PK
--------------------------------------------------------

  CREATE UNIQUE INDEX "JOURNAL_PK" ON "JOURNAL" ("JOURNAL_ID") 
  ;
--------------------------------------------------------
--  DDL for Index RATING_PK
--------------------------------------------------------

  CREATE UNIQUE INDEX "RATING_PK" ON "RATING" ("RATER_ID") 
  ;
--------------------------------------------------------
--  DDL for Index RESEARCH_ROLE_PK
--------------------------------------------------------

  CREATE UNIQUE INDEX "RESEARCH_ROLE_PK" ON "RESEARCH_ROLE" ("RESEARCH_ROLE_ID") 
  ;
--------------------------------------------------------
--  DDL for Index SURVEY_PK
--------------------------------------------------------

  CREATE UNIQUE INDEX "SURVEY_PK" ON "SURVEY" ("SURVEY_ID") 
  ;






