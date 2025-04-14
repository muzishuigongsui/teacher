from tkinter import *
from tkinter.messagebox import *


import service,datautil
import openpyxl
from PIL import Image, ImageTk
class StartMenu():
    def __init__(self):
        self.startmenu=Tk()
        self.startmenu.geometry('1480x880+150+50')
        self.startmenu.title('学生成绩管理系统')
        self.startmenu.wm_resizable(False,False)
        image=ImageTk.PhotoImage(file='./image/startmenu.png')
        Label(self.startmenu,image=image).place(x=0,y=0,width=1480,height=880)
        # 三个按钮
        Button(self.startmenu, text='教师注册', bg='yellowgreen', fg='white',
               font=16, command=lambda : TeacherRegister(self.startmenu)).place(x=500, y=500, width=100, height=40)

        Button(self.startmenu, text='教师登录', bg='yellowgreen', fg='white',
               font=16,command=lambda :TeacherLogin(self.startmenu)).place(x=610, y=500, width=100, height=40)

        Button(self.startmenu, text='教师退出', bg='yellowgreen', fg='white',
               font=16, command=self.startmenu.destroy).place(x=720, y=500, width=100, height=40)

        self.startmenu.mainloop()

class TeacherRegister():
    def __init__(self,startmenu):
        self.startmenu=startmenu
        self.startmenu.withdraw()
        self.teacherreg=Toplevel()
        self.teacherreg.geometry('1480x880+150+50')
        self.teacherreg.title('学生成绩管理系统-教师注册')
        self.startmenu.resizable(False, False)
        image=ImageTk.PhotoImage(file='./image/teacherreg.png')
        Label(self.teacherreg,image=image).place(x=0,y=0,width=1480,height=880)
        # 页面布局
        Label(self.teacherreg, text='输入账号', bg='#F0F4CF', font=16, anchor='w').place(x=50,y=300,width=80,height=40)
        self.teachername=Entry(self.teacherreg,font=16)
        self.teachername.place(x=140,y=300,width=300,height=40)

        #密码
        Label(self.teacherreg, text='输入密码', bg='#F0F4CF', font=16, anchor='w').place(x=50, y=360, width=80,
        height=40)
        self.teacherpwd = Entry(self.teacherreg, font=16, show='*')
        self.teacherpwd.place(x=140, y=360, width=300, height=40)

        #确认账号
        Label(self.teacherreg, text='确认密码', bg='#F0F4CF', font=16, anchor='w').place(x=50, y=420, width=80,
        height=40)
        self.comteacherpwd = Entry(self.teacherreg, font=16, show='*')
        self.comteacherpwd.place(x=140, y=420, width=300, height=40)

        # 两个按钮
        Button(self.teacherreg, text='确定', bg='yellowgreen', fg='white', font=16,command=self.register).place(x=260,y=480,width=80,height=40)
        Button(self.teacherreg, text='返回', bg='yellowgreen', fg='white', font=16,command=self.closewin).place(x=350,y=480,width=80,height=40)

        self.teacherreg.bind('<Destroy>',self.closewin2)
        self.teacherreg.mainloop()

    def register(self):
        if self.teachername.get()=='' or self.teacherpwd.get()=='':
            showwarning('警告','账号或密码不允许为空')
            return False
        if self.teacherpwd.get()!=self.comteacherpwd.get():
            showwarning('警告','密码与确认密码不一致')
            return False
        sql='select * from teacher_login where loginname=%s'
        mysqlobj=service.PyMySQLUtils()
        result=mysqlobj.fetchall(sql,self.teachername.get())
        if len(result)>0:
            showwarning('警告','账号重复')
            return False
        sql1='INSERT INTO teacher_login (loginname,loginpwd) VALUES (%s,%s);'
        result1=mysqlobj.execute(sql1,(self.teachername.get(),self.teacherpwd.get()))
        if result1>0:
            showinfo('提示','教师账号注册成功')
            self.teacherreg.destroy()
        else:
            showwarning('错误','教师注册失败，请联系管理员')
            self.teachername.delete(0,END)
            self.teacherpwd.delete(0,END)
            self.comteacherpwd.delete(0,END)


    def closewin(self):
        self.teacherreg.destroy()
        self.startmenu.deiconify()

    def closewin2(self,event):
        self.closewin()

class TeacherLogin():
    def __init__(self,startmenu):
        self.startmenu=startmenu
        self.startmenu.withdraw()
        self.teacherlogin=Toplevel()
        self.teacherlogin.geometry('1480x880+150+50')
        self.teacherlogin.title('学生成绩管理系统-教师登录')
        self.teacherlogin.resizable(False,False)
        image = ImageTk.PhotoImage(file='./image/teacherlogin.png')
        Label(self.teacherlogin, image=image).place(x=0, y=0, width=1480, height=880)

        # 页面布局
        # 账号
        Label(self.teacherlogin, text='账号:', bg='#F0F4CF', font=16, anchor='w').place(x=560, y=320, width=80,
              height=40)
        self.teachername=Entry(self.teacherlogin,font=16,
                               highlightbackground='black',highlightthickness=1,relief='flat')
        self.teachername.place(x=640,y=320,width=300,height=40)

        # 密码
        Label(self.teacherlogin, text='密码:', bg='#F0F4CF', font=16, anchor='w').place(x=560, y=400, width=80,
              height=40)
        self.teacherpwd = Entry(self.teacherlogin, font=16,show='*',
                                 highlightbackground='black', highlightthickness=1, relief='flat')
        self.teacherpwd.place(x=640, y=400, width=300, height=40)

        # 按钮
        Button(self.teacherlogin,text='确定',bg='yellowgreen',fg='white',font=16,
               command=self.login).place(x=770,y=480,width=80,height=40)

        Button(self.teacherlogin, text='返回', bg='yellowgreen', fg='white', font=16,
               command=self.closewin).place(x=860, y=480, width=80, height=40)

        self.teacherlogin.bind('<Destroy>',self.closewin2)
        self.teacherlogin.mainloop()

    def login(self):
        if self.teachername.get()=='' or self.teacherpwd.get()=='':
            showwarning('警告','账号或密码不可为空')
            return False
        sql='select * from teacher_login where loginname=%s and loginpwd=%s;'
        sqlobj=service.PyMySQLUtils()
        result=sqlobj.fetchall(sql,self.teachername.get(),self.teacherpwd.get())
        if len(result)>0:
            self.teachername.delete(0, END)
            self.teacherpwd.delete(0, END)
            TeacherMenu(self.teacherlogin)
            # showinfo('提示','登录成功')

        else:
            showinfo('错误','账户或密码错误')

    def closewin(self):
        self.teacherlogin.destroy()
        self.startmenu.deiconify()

    def closewin2(self,event):
        self.closewin()

class TeacherMenu():
    def __init__(self,teacherlogin):
        self.teacherlogin=teacherlogin
        self.teacherlogin.withdraw()
        self.teachermenu=Toplevel()
        self.teachermenu.geometry('1480x880+150+50')
        self.teachermenu.title('学生成绩管理系统-学生成绩管理')
        self.teachermenu.resizable(False,False)
        image = ImageTk.PhotoImage(file='./image/score.png')
        Label(self.teachermenu,image=image).place(x=0,y=0,width=1480,height=880)
        # 页面布局
        # 学号
        Label(self.teachermenu, text='学号:', bg='#F0F4CF', font=16, anchor='w').place(x=160, y=170, width=80,
              height=40)
        self.stuno=Entry(self.teachermenu,font=16,highlightbackground='black',highlightthickness=1,relief='flat')
        self.stuno.place(x=250,y=170,width=90,height=40)
        # 姓名
        Label(self.teachermenu, text='姓名:', bg='#F0F4CF', font=16, anchor='w').place(x=470, y=170, width=80,
              height=40)
        self.stuname = Entry(self.teachermenu, font=16, highlightbackground='black', highlightthickness=1, relief='flat')
        self.stuname.place(x=560, y=170, width=90, height=40)
        # 院系
        Label(self.teachermenu, text='院系:', bg='#F0F4CF', font=16, anchor='w').place(x=160, y=240, width=80,
              height=40)
        self.college = Entry(self.teachermenu, font=16, highlightbackground='black', highlightthickness=1, relief='flat')
        self.college.place(x=250, y=240, width=90, height=40)
        # 课程成绩
        Label(self.teachermenu, text='课程成绩:', bg='#F0F4CF', font=16, anchor='w').place(x=430, y=240, width=120,
              height=40)
        self.score = Entry(self.teachermenu, font=16, highlightbackground='black', highlightthickness=1, relief='flat')
        self.score.place(x=560, y=240, width=90, height=40)
        # 考试平均成绩
        Label(self.teachermenu, text='考试平均成绩:', bg='#F0F4CF', font=16, anchor='w').place(x=100, y=310, width=140,
              height=40)
        self.avgscore = Entry(self.teachermenu, font=16, highlightbackground='black', highlightthickness=1,
                              relief='flat')
        self.avgscore.place(x=250, y=310, width=90, height=40)
        # 任课教师评分
        Label(self.teachermenu, text='任课教师评分:', bg='#F0F4CF', font=16, anchor='w').place(x=410, y=310, width=140,
              height=40)
        self.teacher_rating = Entry(self.teachermenu, font=16, highlightbackground='black', highlightthickness=1,
                              relief='flat')
        self.teacher_rating.place(x=560, y=310, width=90, height=40)
        # 综合测评总分
        Label(self.teachermenu, text='综合测评总分:', bg='#F0F4CF', font=16, anchor='w').place(x=100, y=400, width=140,
              height=40)
        self.total_score = Entry(self.teachermenu, font=16, highlightbackground='black', highlightthickness=1,
                              relief='flat')
        self.total_score.place(x=250, y=400, width=90, height=40)

        # 按钮
        Button(self.teachermenu, text='添加', bg='yellowgreen', fg='white', font=16,
               command=self.insert).place(x=250, y=490, width=80, height=40)
        Button(self.teachermenu, text='修改', bg='orange', fg='white', font=16,
               command=self.update).place(x=340, y=490, width=80, height=40)
        Button(self.teachermenu, text='查询', bg='#5b9bd5', fg='white', font=16,
               command=self.query).place(x=430, y=490, width=80, height=40)
        Button(self.teachermenu, text='删除', bg='red', fg='white', font=16,
               command=self.delete).place(x=250, y=540, width=80, height=40)
        Button(self.teachermenu, text='清空', bg='gray', fg='white', font=16,
               command=self.clear).place(x=340, y=540, width=80, height=40)
        Button(self.teachermenu, text='保存', bg='green', fg='white', font=16,
               command=self.save).place(x=430, y=540, width=80, height=40)
        # 右侧是Treeview
        lst=['stuno','stuname','college','score','avgscore','teacher_rating','total_score']
        lst_name=['学号','姓名','院系','课程成绩','平均分','任课教师评分','综合测评总分']
        self.tv=datautil.tv(self.teachermenu,lst,lst_name)
        self.tv.place(x=680,y=180,width=760,height=400)
        self.query()
        # 排序按钮
        Button(self.teachermenu,text='综合测评总分各项排序',font=16,
               bg='#5d9bd5',fg='white',command=self.tree_sort_column).place(x=1240,y=590,width=200,height=40)
        self.teachermenu.bind('<Destroy>',self.closewin2)

        self.teachermenu.mainloop()

    def save(self):
        sqlobj=service.PyMySQLUtils()
        sql='select * from student_sore'
        result=sqlobj.fetchall(sql)
        try:
            wb=openpyxl.Workbook()
            sheet=wb.create_sheet('sheet1')
            sheet.append(['学号','姓名','院系','课程成绩','平均分','任课教师评分','综合测评总分'])
            for item in result:
                sheet.append(item)
            wb.save('./student_score.xlsx')
            showinfo('提示','保存学生信息成功')
        except Exception as e:
            showerror('错误','保存数据失败，请联系管理员')


    def tree_sort_column(self):
        sql='select * from student_sore order by total_score desc'
        sqlobj=service.PyMySQLUtils()
        result=sqlobj.fetchall(sql)
        datautil.tv_data(self.tv,result)

    def delete(self):
        sqlobj = service.PyMySQLUtils()
        if self.stuno.get() == '':
            showwarning('警告', '请先输入要删除的学生学号')
            return False
        self.query()
        if self.stuno.get()!='':
            answer=askyesno('提示','确定要删除吗')
            if answer:
                sql='delete from student_sore where stuno=%s'
                result=sqlobj.execute(sql,self.stuno.get())
                if result>0:
                    showinfo('提示','删除成功')
                    self.clear()
                    self.query()
                else:
                    showerror('错误','删除失败，请联系管理员')


    def update(self):
        sqlobj=service.PyMySQLUtils()
        if self.stuno.get() == '':
            showwarning('警告', '请先选择一名学生成绩')
            return False
        if self.stuname.get() == '':
            showwarning('警告', '请先查询学生信息')
            return False
        sql='update student_sore set stuname=%s,college=%s,score=%s,avgscore=%s,teacher_rating=%s,total_score=%s where stuno=%s'
        values=(self.stuname.get(),self.college.get(),self.score.get(),
                self.avgscore.get(),self.teacher_rating.get(),
                self.total_score.get(),self.stuno.get())
        result=sqlobj.execute(sql, values)
        if result>0:
            showinfo('提示','修改学生信息成功')
            self.clear()
            self.query()
        else:
            showerror('错误','修改学生信息失败，请联系管理员')


    def insert(self):
        sqlobj=service.PyMySQLUtils()
        if self.stuno.get()=='' or self.stuname.get()=='':
            showwarning('警告','学号或姓名不允许为空')
            return False
        sql='select * from student_sore where stuno=%s'
        result=sqlobj.fetchall(sql,self.stuno.get())
        if len(result)>0:
            showwarning('警告','学号不允许重复')
            return False
        sql='insert into student_sore values (%s,%s,%s,%s,%s,%s,%s)'
        values=(self.stuno.get(),self.stuname.get(),self.college.get(),
                self.score.get(),self.avgscore.get(),self.teacher_rating.get(),
                self.total_score.get())
        result2=sqlobj.execute(sql, values)
        if result2>0:
            showinfo('提示','新增学生成绩成功')
            self.clear()
            self.query()
        else:
            showerror('错误','新增学生成绩失败，请联系管理员')
            self.clear()

    def query(self):
        sqlobj=service.PyMySQLUtils()
        if self.stuno.get()=='':
            self.clear()
            sql='select * from student_sore'
            result=sqlobj.fetchall(sql)
        else:
            sql='select * from student_sore where stuno=%s'
            result=sqlobj.fetchall(sql,self.stuno.get())
            if len(result)>0:
                self.clear()
                self.stuno.insert(0,result[0][0])
                self.stuname.insert(0,result[0][1])
                self.college.insert(0,result[0][2])
                self.score.insert(0,result[0][3])
                self.avgscore.insert(0,result[0][4])
                self.teacher_rating.insert(0,result[0][5])
                self.total_score.insert(0,result[0][6])

        if len(result)!=0:
            datautil.tv_data(self.tv,result)
        else:
            showinfo('提示','该学生成绩信息不存在')
            self.clear()

    def clear(self):
        self.stuno.delete(0,END)
        self.stuname.delete(0,END)
        self.college.delete(0,END)
        self.score.delete(0,END)
        self.avgscore.delete(0,END)
        self.teacher_rating.delete(0,END)
        self.total_score.delete(0,END)

    def closewin2(self,event):
        self.teachermenu.destroy()
        self.teacherlogin.deiconify()


if __name__ == '__main__':
    StartMenu()

















