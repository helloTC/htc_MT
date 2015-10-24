import numpy as np
from scipy import stats
import xlrd
import matplotlib.pyplot as plt

# behaviour analysis
excelpath = '/nfs/j3/userhome/huangtaicheng/workingdir/parcellation_MT/doc/motion&form/'

data_form = xlrd.open_workbook(excelpath + 'Global Form.xlsx')
table_form = data_form.sheets()[0]
acc_form = table_form.col_values(2)
acc_form.pop(0)
rt_form = table_form.col_values(3)
rt_form.pop(0)

# Gform acc vs rt
slope_form,intercept_form,rvalue_form,pvalue_form,slopestderr_form = stats.linregress(acc_form,rt_form)

predict_form = intercept_form + slope_form * np.array(acc_form)
plt.figure()
plt.plot(acc_form,rt_form,'o')
plt.plot(np.array(acc_form),predict_form,'k-')
plt.xlabel('acc_gform')
plt.ylabel('rt_gform')
plt.show()


data_motion = xlrd.open_workbook(excelpath + 'Global Motion.xlsx')
table_motion = data_motion.sheets()[0]
acc_motion = table_motion.col_values(2)
acc_motion.pop(0)
rt_motion = table_motion.col_values(3)
rt_motion.pop(0)

#Gmotion acc vs rt
slope_motion,intercept_motion,rvalue_motion,pvalue_motion,slopestderr_motion = stats.linregress(acc_motion,rt_motion)

predict_motion = intercept_motion + slope_motion * np.array(acc_motion)
plt.figure()
plt.plot(acc_motion,rt_motion,'o')
plt.plot(np.array(acc_motion),predict_motion,'k-')
plt.xlabel('acc_gmotion')
plt.ylabel('rt_gmotion')
plt.show()


#Gform acc vs Gmotion acc
slope_acc,intercept_acc,rvalue_acc,pvalue_acc,slopestderr_acc = stats.linregress(acc_form,acc_motion)
predict_acc = intercept_acc + slope_acc * np.array(acc_form)
plt.plot(acc_form,acc_motion,'o')
plt.plot(np.array(acc_form),predict_acc,'k-')
plt.xlabel('acc_gform')
plt.ylabel('acc_gmotion')
plt.show()
#Gform rt vs Gmotion rt
slope_rt,intercept_rt,rvalue_rt,pvalue_rt,slopestderr_rt = stats.linregress(rt_form,rt_motion)
predict_rt = intercept_rt + slope_rt * np.array(rt_form)
plt.plot(rt_form,rt_motion,'o')
plt.plot(np.array(rt_form),predict_rt,'k-')
plt.xlabel('rt_gform')
plt.ylabel('rt_gmotion')
plt.show()


