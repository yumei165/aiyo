1, Def: An engine for executing programs written in PIG LATIN on top of Hadoop
http://pig.apache.org/

2, Example
find top 5 most used websites by age 18-25. 
Users = load ‘users’ as (name, age);
Fltrd = filter Users by age >= 18 and age <= 25;
Pages = load ‘pages’ as (user, url);
Jnd = join Fltrd by name, Pages by user;
Grpd = group Jnd by url;
Smmd = foreach Grpd generate group, COUNT(Jnd) as clicks;
Srtd = order Smmd by clicks desc;
Top5 = limit Srtd 5;
store Top5 into ‘top5sites’;
