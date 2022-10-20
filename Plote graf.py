import pandas as pd
import matplotlib.pyplot as plt

# get input data
df = pd.read_csv(r"C:\Users\47994\Documents\Cell 2.csv")

### Oppgave 1 ####

#Celle 1

df1 = pd.read_csv(r"C:\Users\47994\Documents\Cell-11.csv",sep=';')
df1.drop(df1[df1['Cycle Index'] <= 5].index, inplace = True)

column1 = df1["Voltage (V)"]
max_value1 = column1.max()
min_value1 = column1.min()

#Celle 2

df2 = pd.read_csv(r"C:\Users\47994\Documents\Cell 2.csv")
df2.drop(df2[df2['Cycle Index'] <= 5].index, inplace = True)

column2 = df2["Voltage (V)"]
max_value2 = column2.max()
min_value2 = column2.min()

#Celle 3

df3 = pd.read_csv(r"C:\Users\47994\Documents\Cell 3.csv")
df3.drop(df3[df3['Cycle Index'] <= 5].index, inplace = True)

column3 = df3["Voltage (V)"]
max_value3 = column3.max()
min_value3 = column3.min()

#Celle 4

df4 = pd.read_csv(r"C:\Users\47994\Documents\Cell 4.csv")
df4.drop(df4[df4['Cycle Index'] <= 5].index, inplace = True)

column4 = df4["Voltage (V)"]
max_value4 = column4.max()
min_value4 = column4.min()




### Oppgave 2 ####

df_op2 = pd.read_csv(r"C:\Users\47994\Documents\Cell 2.csv")
df_op2.drop(df_op2[df_op2['Cycle Index'] == 6].index, inplace = True)
ax = df_op2.plot(x='Test Time (s)', y=['Charge Capacity (Ah)', 'Discharge Capacity (Ah)'])


### Oppgave 3 ###

df_op3 = pd.read_csv(r"C:\Users\47994\Documents\Cell 2.csv")
df_op3.drop(df_op3[df_op3['Cycle Index'] <= 5].index, inplace = True)


### Oppgave 4 ###

df_op4_c2 = pd.read_csv(r"C:\Users\47994\Documents\Cell 2.csv")
df_op4_c3 = pd.read_csv(r"C:\Users\47994\Documents\Cell 2.csv")
df_op4_c4 = pd.read_csv(r"C:\Users\47994\Documents\Cell 2.csv")
df_op4_c5 = pd.read_csv(r"C:\Users\47994\Documents\Cell 2.csv")


#Cycel 2
df_op4_c2.drop(df_op4_c2[df_op4_c2['Cycle Index'] >= 3].index, inplace = True)
df_op4_c2.drop(df_op4_c2[df_op4_c2['Cycle Index'] <= 1].index, inplace = True)

#Cycel 3
df_op4_c3.drop(df_op4_c3[df_op4_c3['Cycle Index'] >= 4].index, inplace = True)
df_op4_c3.drop(df_op4_c3[df_op4_c3['Cycle Index'] <= 2].index, inplace = True)

#Cycel 4
df_op4_c4.drop(df_op4_c4[df_op4_c4['Cycle Index'] >= 5].index, inplace = True)
df_op4_c4.drop(df_op4_c4[df_op4_c4['Cycle Index'] <= 3].index, inplace = True)

#Cycel 5
df_op4_c5.drop(df_op4_c5[df_op4_c5['Cycle Index'] >= 6].index, inplace = True)
df_op4_c5.drop(df_op4_c5[df_op4_c5['Cycle Index'] <= 4].index, inplace = True)


### Oppgave 5 ###
# Celle 3 og Celle 1 er NMC



df_op5 = pd.read_csv(r"C:\Users\47994\Documents\Cell 3.csv")


 

fig, axes = plt.subplots(nrows=2, ncols=1)

df_op5.plot(ax=axes[0], x='Test Time (s)', y=['Voltage (V)'])
df_op5.plot(ax=axes[1], x='Test Time (s)', y=['Current (A)'], style='r')
for ax in axes:
    ax.axvline(51001, color='purple', linestyle='dashed')
    ax.axvline(233751, color='orange', linestyle='dashed')
    ax.axvline(419369, color='green', linestyle='dashed')
    ax.legend(loc='center left')



#axes.axvline(100000, linestyle= ':', color = 'g')
#plt.axvline(ax=axes[0], x = 100000, linestyle= ':', color = 'g')
#df_op5_c.plot(x='Test Time (s)', y=['Current (A)'])
#df_op5_s.plot(x='Test Time (s)', y=['Voltage (V)'])

#ax = df_op5.plot(x='Test Time (s)', y=['Current (A)'])
plt.show()



### Oppgave 6 ###

# Celle 3 og Celle 1 er NMC
df_op6_NMC = pd.read_csv(r"C:\Users\47994\Documents\Cell 3.csv")
df_op6_NMC.drop(df_op6_NMC[df_op6_NMC['Cycle Index'] >= 6].index, inplace = True)
df_op6_NMC.drop(df_op6_NMC[df_op6_NMC['Cycle Index'] <= 4].index, inplace = True)
ax = df_op6_NMC.plot(x='Discharge Capacity (Ah)', y='Voltage (V)')
plt.show()

# Celle 4 og Celle 2 er LFP
df_op6_LFP = pd.read_csv(r"C:\Users\47994\Documents\Cell 2.csv")
df_op6_LFP.drop(df_op6_LFP[df_op6_LFP['Cycle Index'] >= 6].index, inplace = True)
df_op6_LFP.drop(df_op6_LFP[df_op6_LFP['Cycle Index'] <= 4].index, inplace = True)
ax = df_op6_LFP.plot(x='Discharge Capacity (Ah)', y='Voltage (V)')
plt.show()





#Ekstra
#ax = df.plot(x='Test Time (s)', y=['Current (A)','Voltage (V)', 'Power (W)', 'Charge Capacity (Ah)', 'Discharge Capacity (Ah)', 'Charge Energy (Wh)', 'Discharge Energy (Wh)', 'ACR (Ohm)', 'dV/dt (V/s)', 'Internal Resistance (Ohm)', 'dQ/dV (Ah/V)', 'dV/dQ (V/Ah)'])



