create table book(
bnum char(20) NOT NULL,
bclass varchar(50),
bname varchar(50),
publisher varchar(50),
year int,
author varchar(20),
price decimal(7,2),
total int,
collection int,
primary key(bnum)
);

create table card
(cnum char(10) NOT NULL, -- 校卡卡号长度为 10
name varchar(20),
department varchar(40),
type char(1),
numbers int,
primary key(cnum),
check(type in ('T','S'))
);

create table borrow
(cnum char(10),
bnum char(20),
btime datetime,
rtime datetime,
times int, -- 用于记录可续借的次数
primary key(cnum,bnum),
foreign key(cnum) references card(cnum),
foreign key(bnum) references book(bnum)
);