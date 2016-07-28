# tbl_ConnectLog | 游戏连接Log

|NUM|COLUM NAME|DATA TYPE|NULL|DEFAULT|KEY|NOTE|
| :--- | :---: | --- | --- | --- | :---: | :--- |
|1|idx|INT|not null|identity(1,1)|PK|数据顺序值|
|2|LogTime|datetime|not null|getdate()||Log生成时间|
|3|UserNum|int|not null|||用户固有编号|
|4|ClubID|bigint|not null|||生成俱乐部固有编号|
|5|GameCode|smallint|not null|||用户Channel Code|
|6|ServerCode|smallint|not null|||用户连接服务器Code|
|7|LogType|tinyint|not null|||LogType（0：Login，1：Logout，3：连接中）|
|8|Lv|smallint|not null|||俱乐部等级|
|9|exp|bigint|not null|||俱乐部经验值|
|10|reputation|int|not null|||俱乐部声望|
|11|money|bigint|not null|||俱乐部拥有资金|
|12|win|int|not null|||俱乐部总胜利|
|13|lost|int|not null|||俱乐部总败绩|
|14|draw|int|not null|||俱乐部总平局|
|15|PCBang|tinyint|not null|||网吧连接与否（0：普通连接，1：网吧连接）|
|16|UserIP|varchar(15)|not null|||用户连接IP|
