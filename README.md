# Concept_CountdownTimer
a countdown timer in which the user can set a timer and then when the time is completed, the app will notify the user that the time has ended.

# Using Functional Programing Core Concept with Threading 
- Functional Programing exmple:
The code does not contain any loops just the recursion
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

