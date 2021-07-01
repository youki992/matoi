drop database if exists c_scan;
use c_scan;
create table result(
	id varchar(30) primary key,
	ip varchar(20),
	C_ip varchar(20),
	response varchar(1000))
	default charset=utf8;
drop database if exists craw_result;
use craw_result;
create table result(
	id varchar(30) primary key,
	title varchar(50),
	link varchar(1000),
	zhuangtai int)
	default charset=utf8;
drop database if exists port_scan;
use port_scan;
create table result(
	id varchar(90) primary key,
	ip varchar(20),
	port int)
	default charset=utf8;
drop database if exists subdomain;
use subdomain;
create table result(
	id varchar(30) primary key,
	subdomain varchar(50),
	ips varchar(400))
	default charset=utf8;