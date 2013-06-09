1, Def: An engine for executing programs written in PIG LATIN on top of Hadoop
http://pig.apache.org/
http://www.ibm.com/developerworks/cn/linux/l-apachepigdataquery/

2, Data types
Atom: Integer, String, etc
Tuple: each field can be any type
Bag: collection of tuples, duplicated allowed
Map: string literal keys mapped to any type
Example:
t  =    <1, {<2,3>,<4,6>,<5,7>}, ['apache':'search']>
Tuple f1:Atom     f2:Bag               f3:Map
$0   #result: 1
f2   #Bag{<2,3>,<4,6>,<5,7>}
f2.$0  #Bag{2,4,5}
f3#'apache'  #Atom"search"
sum(f2.$0)  #11

3， Functions
Load:
  A = LOAD 'myfile.txt' USING PigStorage('t') AS (f1,f2,f3);
FILTER:
  Y = FILTER A BY f1 == '8';
GROUP:
  X = GROUP A BY f1;
DISTINCT:
  Y = DISTINCT A
FOREACH:
  X = FOREACH A GENERATE f0, f1+f2;
  Y = GROUP A BY f1;
  Z = FOREACH X GENERATE group, X.($1, $2);
FLATTEN:
Y = GROUP A BY f1;
Z = FOREACH X GENERATE group, FLATTEN(X);
COGROUP: getting data together
  C = COGROUP A BY f1, B BY $0;
JOIN: a special case of cogroup
  C = JOIN A BY $0, B BY $0;
STORE,UNION,CROSS,DUMP,ORDER


4, Example
#find top 5 most used websites by age 18-25. 
Users = load ‘users’ as (name, age);
Fltrd = filter Users by age >= 18 and age <= 25;
Pages = load ‘pages’ as (user, url);
Jnd = join Fltrd by name, Pages by user;
Grpd = group Jnd by url;
Smmd = foreach Grpd generate group, COUNT(Jnd) as clicks;
Srtd = order Smmd by clicks desc;
Top5 = limit Srtd 5;
store Top5 into ‘top5sites’;

#find traffic info of specified ip address
A = LOAD ‘traffic.dat’ AS (ip, time, url);
B = GROUP A BY ip;
C = FOREACH B GENERATE group AS ip,
COUNT(A);
D = FILTER C BY ip IS ‘192.168.0.1’
OR ip IS ‘192.168.0.0’;
STORE D INTO ‘local_traffic.dat’;

