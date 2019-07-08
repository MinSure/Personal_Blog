from django.db import models

# Create your models here.

#定义实体类，映射到数据库中的表
class Dept(models.Model):
    #属性会映射成表中的字段
    deptno=models.AutoField(primary_key=True) #主键自动增长
    dname=models.CharField(max_length=50)#部门名称，字符型，最大50
    loc=models.CharField(max_length=50)#部门所在地
    pass