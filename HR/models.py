from django.db import models
from datetime import date

# Create your models here.

class Person(models.Model):
    """
    人员信息，包含基本信息属性
    """
    # verbose_name = "员工详细信息"
    #第一个参数表示字段的自述名称，或者使用verbose_name="XXXX"，但是OneToOneField第一个参数被占用了
    # staff = models.OneToOneField(auth.user, primary_key=True, verbose_name="员工姓名")
    #staff = models.OneToOneField(User, primary_key=True, verbose_name="员工姓名")
    #员工姓名
    userName = models.CharField("姓名", max_length=15, default="无名氏")
    #公司工号
    workNo = models.CharField("公司工号", max_length=15)
    #华为工号
    workNoExt = models.CharField("华为工号", max_length=15, null=True)
    #手机号码
    mobilePhone = models.CharField("手机号码", max_length=15, default="00000000000")
    #身份证号码
    IDNo = models.CharField("身份证", max_length=18)
    #电子邮箱
    email = models.EmailField("电子邮箱", max_length=50, null=True)
    #华为电子邮箱
    emailExt = models.EmailField("华为邮箱", max_length=50, null=True)

    #性别字段只能是0或1的值，元组第一位表示保存的值，第二位表示显示的值
    sex = models.CharField("性别", max_length=1, choices=(("0", "女"), ("1", "男")), default="1")
    # 岗位级别
    levelList = (
        ("00", "00"),
        ("1B", "1B"), ("1A", "1A"), ("2B", "2B"), ("2A", "2A"),
        ("3B", "3B"), ("3A", "3A"), ("4B", "4B"), ("4A", "4A"),
        ("5B", "5B"), ("5A", "5A"), ("6B", "6B"), ("6A", "6A"),
        ("7B", "7B"), ("7A", "7A"), ("8B", "8B"), ("8A", "8A"),
        ("9B", "9B"), ("9A", "9A"), ("10B", "10B"), ("10A", "10A"),
        ("11B", "11B"), ("11A", "11A"), ("12B", "12B"), ("12A", "12A")
    )
    level = models.CharField("岗位级别", max_length=4, choices=levelList, default="00")
    # 到岗日期/入职日期
    entryDate = models.DateField("入职日期", default=date.today)
    # 部门
    depart = models.CharField("部门", max_length=10, default="0", null=True)
    # 业务线
    productUnit = models.CharField("产品线", max_length=10, default="0",null=True)
    # 项目组
    projectName = models.CharField("项目组名", max_length=20, default="0",null=True)
    # 籍贯省
    provinceBirth = models.CharField("籍贯省份", max_length=20,null=True, default="江苏省")
    # 籍贯市
    cityBirth = models.CharField("籍贯市", max_length=20,null=True, default="南京市")
    # 出生日期
    birthDay = models.DateField("出生日期", null=True,default=date.today)
    # 婚姻状况
    maritalStatus = models.CharField("婚姻状况", max_length=1, 
        choices=(('0','未婚'), ('1','已婚'), ('2','离异')), default="0")
  
    #员工住址 ，第一个参数表示字段的自述名称，或者使用verbose_name="XXXX"
    address = models.CharField("住址", max_length=200, null=True)
    # 毕业院校
    graduatedSchool = models.CharField("毕业学校", max_length=20, null=True,default="大学")
    # 学历
    education = models.CharField("学历", max_length=1,
    choices=(('0', '小学'), ('1', '初中'), ('2', '高中'), ('3', '大专'), ('4', '本科'), ('5', '研究生')),null=True, default="4")
    # 大学专业名称
    profession = models.CharField("专业", max_length=20, null=True, default="")
    # 毕业时间
    graduatedDay = models.DateField("毕业日期", null=True,default=date.today)

  

    def get_absolute_url(self):
        from django.urls import reverse
        # return reverse('PersonListView', kwargs={'pk': self.pk})
        return reverse('PersonListView')

    class Meta:
        ordering = ["-entryDate"]
    def __str__(self):
        return self.userName

#从公司的花名册表单中读取员工数据，更新到数据库中
def import_data_excel(fileName):
    pass
class Salary(models.Model):
    """
    员工薪资调整的详细数据
    """
    #员工
    person = models.ForeignKey(Person,on_delete=models.CASCADE , verbose_name="员工")
    #调薪日期
    adjustDate = models.DateField("调薪日期", default=date.today)
    #调薪幅度
    adjustRange = models.IntegerField("调薪幅度", default=0)
    #调整后薪资
    salaryFinal = models.IntegerField("调整后薪资", default=0)
    #备注
    notes = models.CharField("备注", max_length=200, blank=True, null=True)
    #此处表示表名字
    verbose_name = "薪资调整数据"
    def __str__(self):
        return self.person
