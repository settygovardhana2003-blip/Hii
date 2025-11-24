import numpy as np
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 2, figsize=(10,6))
x=np.linspace(1,10,1000)
y=np.sin(x)
ax[0].plot(x, y)
ax[0].text(0.3, 0.4, 'Data: (0.3, 0.4)', transform=ax[0].transData)
ax[0].text(0.5, 0.5, 'Axes: (0.5, 0.5)', transform=ax[0].transAxes)
ax[0].text(0.8, 0.8, 'Figure: (0.3, 0.5)', transform=fig.transFigure)


ax[1].plot(x,y)

ax[1].text(0.3, 0.4, 'Data: (0.3, 0.4,)', transform=ax[1].transData)
ax[1].text(0.5, 0.5, 'Axes: (0.5, 0.5)', transform=ax[1].transAxes)
ax[1].text(0.8, 0.8, 'Figure: (0.3, 0.5,)', transform=fig.transFigure)
ax[1].set_xlim(-5,5)
ax[1].set_ylim(-2,2)

plt.show()

Question 1: Using Pandas Perform Merge and Join.
  
   import pandas as pd
   
   df1 = pd.DataFrame({
      'employee': ['Bob', 'Jake', 'Lisa', 'Sue'],
      'group': ['Accounting', 'Engineering', 'Engineering', 'HR']})
   
  df2 = pd.DataFrame({
     'name': ['Bob', 'Jake', 'Lisa', 'Sue'],
     'salary': [70000, 80000, 120000, 90000]})
  
  print("--- DataFrame 1 (df1) ---")
  print(df1)
  
  print("\n--- DataFrame 2 (df2) ---")
  print(df2)
  
  print("\n==================================================================")
  print("Merge using left_on='employee' and right_on='name'")
  merged_on_columns = pd.merge(df1, df2, left_on="employee", 
right_on="name").drop('name', axis=1)
  print(merged_on_columns)
  
  # Merge using 'left_index' and 'right_index'
  df3 = pd.DataFrame({
     'employee': ['Lisa', 'Bob', 'Jake', 'Sue'],
     'hire_date': [2004, 2008, 2012, 2014]
  })
  
  df1a = df1.set_index('employee')
  df2a = df3.set_index('employee')
  
  print("\n==================================================================")
  print("--- (df1a) ---")
  print(df1a)
  
  print("\n--- (df2a) ---")
  print(df2a)
  
  print("Merge using left_index=True and right_index=True")
  merged_on_index = pd.merge(df1a, df2a, left_index=True, right_index=True)
  print(merged_on_index)

 import pandas as pd
  data_x = {
     'A': ['A0', 'A1'],
     'B': ['B0', 'B1']
  }
  x = pd.DataFrame(data_x, index=[0, 1])
  data_y = {
 19/11/2025, 23:13 Code
 https://tarikjaber.github.io/Code-to-PDF/ 2/10
    'A': ['A2', 'A3'],
     'B': ['B2', 'B3']
  }
  y = pd.DataFrame(data_y, index=[2, 3])
  
 # Assign x's index to y's index (Duplicate Indices)
  y.index = x.index
  
 print("--- Original DataFrames ---")
  print("x:")
  print(x)
  print("\ny (now has duplicate indices [0, 1]):")
  print(y)
  
 print("\n" + "="*40)
  print("--- Result of pd.concat([x, y]) ---")
  print(pd.concat([x, y]))
  
 print("\n" + "="*40)
  print("--- Result of pd.concat([x, y], ignore_index=True) ---")
  print(pd.concat([x, y], ignore_index=True))



