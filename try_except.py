# -*-coding:utf-8-*-
# @Time       :2018/12/24 6:30
# @Autor      :DA BAI CAI
# @Email      :icewong401@163.com
# @File       :try_except.py
# @Software   :PyCharm
# 1、为了处理英文字符，产生了ASCII码
# 2、为了处理中文字符，产生了GB2312
# 3、为了处理各国字符，产生了unicde
# 4、为了提高Unicode存储和传输性能，产生了UTF-8，他是Unicode的一种实现形
# 式5\操作系统是unicode编码，内容，需要.encode(编码)才可以
s="柠檬班12期"
print(s.encode('gbk').decode('gbk').encode('utf-8'))
print(s.encode('gbk'))
print(s.encode('gbk').decode('gbk'))
L=[98,7,77,1,5]#[1,5,7,77,98
#比较n-1伦，元素之间 两两比较
for i in range(len(L)-1):#0,1,2,3 控制次数
    for j in range(0,len(L)-1-i):#减一防止越界,两两比较元素,-i最后一个元素不用比较
        if L[j]>L[j+1]:
            L[j],L[j+1]=L[j+1],L[j]
print(L)

file=open('python12.txt','w+')
print(file.closed)#判断文件是否关闭
file.close()#关闭文件
print(file.closed)
print('---------------------------------------------')
#上下文管理器
with open('python12.txt','w+',encoding='utf-8') as file:#file相当于别名，在里面不会关，出去文件自动关闭
    s=['A组的组长是谁！\n','B组的组长是谁！\n',]
    file.writelines(s)
    print('在上下文管理器中的文件状态',file.closed)
print("在上下文管理器外面的文件状态",file.closed)

print("-------------------try-------------except------------")

#读取地方，数据交换地方，抓到异常，然后做出相关处理
try:#报警并处理，可以保证下面的代码执行
    with open('python12.txt','w+',encoding='utf-8')as file:
        file.write('python666666666666666')
except Exception as e:
    raise e
    # print("chucuo")
try:
    a=10
    print(a+b)
    # raise e
except NameError as e:
    print('nemeerror',e)
    # print(e)
except Exception as e:
    print('expecton',e)
finally:
    print(a)#不管是否报错都要执行,如果是else，要try没有问题
    # 才会执行else，如果有问题就不执行，finally是无论如何都会执行的