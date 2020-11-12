/*  FCP Part 3 - GROUP 07
 SUBMITTED BY: PRECIOUS OGHENERURIE, NICHOLAS SMALL, LAKSHMI SANDEEP
 SUBMISSION TITLE : FCP_3_Group07 */ 

CREATE TABLE G07_OLAP.dim_area (
	fips_id_SK SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
	fips_NK SMALLINT NOT NULL,
    area_name VARCHAR(20) UNIQUE,
    PRIMARY KEY (fips_id_SK));
    
CREATE TABLE G07_OLAP.dim_congress (
		cong_id_SK SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
		cong_id_NK SMALLINT NOT NULL,
        cong_name CHAR(5) NOT NULL UNIQUE,
        PRIMARY KEY (cong_id_SK));
        
CREATE TABLE G07_OLAP.dim_industry (
        ind_id_SK SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
		ind_id_NK SMALLINT NOT NULL,
        naics CHAR(6) NOT NULL UNIQUE,
        ind_desc VARCHAR(75),
        PRIMARY KEY (ind_id_SK));

CREATE TABLE G07_OLAP.dim_flag (
		flag_id_SK SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
		code_NK CHAR(1) NOT NULL,
        flag_desc TEXT,
        PRIMARY KEY (flag_id_SK));
        
CREATE	TABLE G07_OLAP.dim_congressional_district (
		cd_id_SK INT UNSIGNED NOT NULL AUTO_INCREMENT,        
        cong_id_SK SMALLINT UNSIGNED,
        cd_id_NK INT NOT NULL,
        dist_num VARCHAR(3),
        PRIMARY KEY	(cd_id_SK),
		CONSTRAINT congress_fk FOREIGN KEY (cong_id_SK)
		REFERENCES G07_OLAP.dim_congress (cong_id_SK)
		ON DELETE NO ACTION ON UPDATE NO ACTION);
        
CREATE TABLE G07_OLAP.dim_date  (
    date_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    year    YEAR NOT NULL,
    quarter tinyint,
    PRIMARY KEY(date_id));
            
CREATE TABLE G07_OLAP.fact_business_pattern (
fact_bus_pattern_SK INT UNSIGNED NOT NULL AUTO_INCREMENT,
	cd_id_SK INT UNSIGNED NOT NULL,
    ind_id_SK SMALLINT UNSIGNED NOT NULL,
    fips_id_SK SMALLINT UNSIGNED NOT NULL,
    empl_flag_id_SK SMALLINT UNSIGNED,
    q1_pr_flag_id_SK SMALLINT UNSIGNED,
    yr_pr_flag_id_SK SMALLINT UNSIGNED,
    date_id INT UNSIGNED,
    num_est INT UNSIGNED,
    num_empl INT UNSIGNED,    
    q1_pr INT UNSIGNED,    
    yr_pr INT UNSIGNED,
    PRIMARY KEY (fact_bus_pattern_SK),
    CONSTRAINT congressional_district_fk FOREIGN KEY (cd_id_SK)
		REFERENCES G07_OLAP.dim_congressional_district (cd_id_SK)
		ON DELETE NO ACTION ON UPDATE NO ACTION,
	CONSTRAINT industry_fk FOREIGN KEY (ind_id_SK)
		REFERENCES G07_OLAP.dim_industry (ind_id_SK)
		ON DELETE NO ACTION ON UPDATE NO ACTION,
	CONSTRAINT area_fk FOREIGN KEY (fips_id_SK)
		REFERENCES G07_OLAP.dim_area (fips_id_SK)
		ON DELETE NO ACTION ON UPDATE NO ACTION,
	CONSTRAINT EMPL_F_fk FOREIGN KEY (empl_flag_id_SK)
		REFERENCES G07_OLAP.dim_flag (flag_id_SK)
		ON DELETE NO ACTION ON UPDATE NO ACTION,
	CONSTRAINT Q1_PR_F_fk FOREIGN KEY (q1_pr_flag_id_SK)
		REFERENCES G07_OLAP.dim_flag(flag_id_SK)
		ON DELETE NO ACTION ON UPDATE NO ACTION,
	CONSTRAINT YR_PR_F_fk FOREIGN KEY (yr_pr_flag_id_SK)
		REFERENCES G07_OLAP.dim_flag (flag_id_SK)
		ON DELETE NO ACTION ON UPDATE NO ACTION,
	CONSTRAINT date_fk FOREIGN KEY (date_id)
		REFERENCES G07_OLAP.dim_date (date_id)
		ON DELETE NO ACTION ON UPDATE NO ACTION);
        
        
INSERT INTO G07_OLAP.dim_area(fips_NK,area_name)
SELECT fips,area_name FROM G07_OLTP.area ;

INSERT INTO G07_OLAP.dim_congress(cong_id_NK,cong_name)
SELECT cong_id,cong_name from G07_OLTP.congress;

INSERT INTO G07_OLAP.dim_flag (code_NK,flag_desc) 
SELECT code, flag_desc FROM G07_OLTP.flag;

INSERT INTO G07_OLAP.dim_industry (ind_id_NK,naics,ind_desc) 
Select DISTINCT ind_id,naics,ind_desc FROM G07_OLTP.industry;

INSERT INTO G07_OLAP.dim_date(year)
SELECT distinct year from G07_OLTP.district_industry;
UPDATE G07_OLAP.dim_date SET quarter = 1 where date_id IS NOT NULL;

INSERT INTO G07_OLAP.dim_congressional_district(cong_id_SK,cd_id_NK,dist_num)
SELECT DISTINCT dim.cong_id_SK,cd.cd_id,cd.dist_num FROM G07_OLTP.congressional_district cd
JOIN G07_OLAP.dim_congress dim ON dim.cong_id_NK=cd.cong_id;

INSERT INTO G07_OLAP.fact_business_pattern (cd_id_SK,ind_id_SK,fips_id_SK,empl_flag_id_SK,q1_pr_flag_id_SK,yr_pr_flag_id_SK,date_id,num_est,num_empl,q1_pr,yr_pr)
SELECT dimcd.cd_id_SK,dimi.ind_id_SK, dima.fips_id_SK,dimf1.flag_id_SK,dimf2.flag_id_SK,dimf3.flag_id_SK,dimd.date_id,
di.num_est,di.num_empl,di.q1_pr,di.yr_pr from G07_OLTP.district_industry di 
JOIN G07_OLTP.congressional_district cd ON cd.cd_id = di.cd_id
JOIN G07_OLAP.dim_congressional_district dimcd ON dimcd.cd_id_NK=di.cd_id
JOIN G07_OLAP.dim_industry dimi ON dimi.ind_id_SK=di.ind_id
JOIN G07_OLAP.dim_area dima ON dima.fips_NK = cd.fips
JOIN G07_OLAP.dim_date dimd ON dimd.year = di.year
LEFT JOIN G07_OLAP.dim_flag dimf1 ON dimf1.code_NK = di.empl_flag_id 
LEFT JOIN G07_OLAP.dim_flag dimf2 ON dimf2.code_NK = di.q1_pr_flag_id
LEFT JOIN G07_OLAP.dim_flag dimf3 ON dimf3.code_NK = di.yr_pr_flag_id;

