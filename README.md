
# Idea Title:Countdown Clock and Timer (Using gui and  functional programming )

a countdown timer in which the user can set a timer and then when the time is completed, the app will notify the user that the time has ended.



# Team Members (arabic name, english name, id)

Member1:(حسام خالد محمد ,hossam khaled mohamed , 20170178)

Member2:(أحمد عبدالرحمن ,Ahmed Abdelrhman , 20170044)

Member3:(حسن محمود عبدالغفار ,Hassan Mahmoud Abdelghaffar , 20170190)

Member4:(محمد طه  عبدالعليم ,mohamed taha abdelaleem , 20170450)

Member5:(احمد عبده موهوب , Ahmed Abdo mawhub , 20170048)



# Registration sheet, row number (38)
	

# Using Functional Programing Core Concept with Threading 
- Functional Programing exmple:
The code does not contain any loops just the recursion and Mutation Variables
```python
def coutdown(n):
    if n ==0:
        helper.setdata(n)
        return 0
    else:
       helper.setdata(n)        # Set Gui Data
       if helper.threadAport(): # Stop Thread
            return 0
       time.sleep(1)
       coutdown(n-1) 
```

# DEPLOYMENT
Desktop Application Using 
- Tkinter
- Pyinstaller : For  EXE File
- NSIS        : To Execute a Setup file (```installable```)  Link: https://drive.google.com/drive/folders/1a001WXDec_ZkT_XcQ2NO78sgV35bg3aj?usp=sharing
