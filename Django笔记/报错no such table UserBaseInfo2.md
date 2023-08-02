在进行Django重定向时，报错

```
Exception Type:	OperationalError
Exception Value:	
no such table: UserBaseInfo2
```

原因：

* 可能是没有进行数据库迁移

```
python manage.py makemigrations
python manage.py migrate
```

运行之后还不行，可能因为您的模型和数据库表之间存在差异，执行以下命令，将数据库表和模型同步：

```
python manage.py migrate --fake myapp2 zero
python manage.py migrate myapp2
```

可能继续报错：

![image-20230802115452792](https://s2.loli.net/2023/08/02/LuydTlVtrsm3iNf.png)

是因为没有手动在项目setting.py文件中注册应用，添加应用名称

![image-20230802120103251](https://s2.loli.net/2023/08/02/RwLg3kADZhEpiKX.png)