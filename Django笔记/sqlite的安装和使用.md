# 1.安装

到 [官网]: https://www.sqlite.org/download.html 去下载对应系统版本，这里以win为例

需要下载两个文件

![image-20230812200629893](https://s2.loli.net/2023/08/12/pIl9mgJFWRKEhwa.png)

下载解压后放入同一个文件夹中

![image-20230812200659783](https://s2.loli.net/2023/08/12/ZRh2f1zLcHTa3SY.png)

将路径加入到系统变量Path中

打开命令行，验证是否安装成功：输入sqlite3

![image-20230812200744673](https://s2.loli.net/2023/08/12/CQnAVihP2pvoZOl.png)

即成功



# 2.使用

SQLite 是一个自包含的、零配置的 SQL 数据库引擎，相对于其他的 SQL 数据库，它比较轻巧且易于使用。

直接使用sql语句进行数据库操作

```
sqlite> CREATE TABLE UserBaseInfo2(
(x1...> id INT NOT NULL,
(x1...> NAME VARCHAR(200),
(x1...> creatDate VARCHAR(200)
(x1...> );
sqlite>
```

分号代表结束

![image-20230812204627960](https://s2.loli.net/2023/08/12/xRkYrIbCThyfjPq.png)





## 2.1 退出sqlite模式 

在 SQLite 命令行模式下，想要退出 SQLite，可以输入 `.quit` 命令，然后按下回车键即可退出。还可以使用 `.exit` 命令，也可以直接使用快捷键 `Ctrl + D` 退出 SQLite。

![image-20230812200931605](https://s2.loli.net/2023/08/12/bpdUf6So8zZju2c.png)

