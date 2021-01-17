# import modules
import numpy as np
import os
os.chdir(r'C:\Users\USER\PycharmProjects\untitled1\ProfProject\SavedFiles')
# load strong keywords 2001 to 2016
CM01 = np.load('CIKM2001AKWhi.npy',allow_pickle=True).tolist()
CM02 = np.load('CIKM2002AKWhi.npy',allow_pickle=True).tolist()
CM03 = np.load('CIKM2003AKWhi.npy',allow_pickle=True).tolist()
CM04 = np.load('CIKM2004AKWhi.npy',allow_pickle=True).tolist()
CM05 = np.load('CIKM2005AKWhi.npy',allow_pickle=True).tolist()
CM06 = np.load('CIKM2006AKWhi.npy',allow_pickle=True).tolist()
CM07 = np.load('CIKM2007AKWhi.npy',allow_pickle=True).tolist()
CM08 = np.load('CIKM2008AKWhi.npy',allow_pickle=True).tolist()
CM09 = np.load('CIKM2009AKWhi.npy',allow_pickle=True).tolist()
CM10 = np.load('CIKM2010AKWhi.npy',allow_pickle=True).tolist()
CM11 = np.load('CIKM2011AKWhi.npy',allow_pickle=True).tolist()
CM12 = np.load('CIKM2012AKWhi.npy',allow_pickle=True).tolist()
CM13 = np.load('CIKM2013AKWhi.npy',allow_pickle=True).tolist()
CM14 = np.load('CIKM2014AKWhi.npy',allow_pickle=True).tolist()
CM15 = np.load('CIKM2015AKWhi.npy',allow_pickle=True).tolist()
CM16 = np.load('CIKM2016AKWhi.npy',allow_pickle=True).tolist()
# create list of strong keywords
MKW = CM01 + CM02 + CM03 + CM04 + CM05 + CM06 + CM07 + CM08 + CM09 + CM10 + CM11 + CM12 + CM13 + CM14 + CM15 + CM16
MKW = list(set(MKW))
MKW.sort()
# load LWRM from 2001 to 2016
dR01 = np.load('CIKM2001LWRM.npy',allow_pickle=True)
dR02 = np.load('CIKM2002LWRM.npy',allow_pickle=True)
dR03 = np.load('CIKM2003LWRM.npy',allow_pickle=True)
dR04 = np.load('CIKM2004LWRM.npy',allow_pickle=True)
dR05 = np.load('CIKM2005LWRM.npy',allow_pickle=True)
dR06 = np.load('CIKM2006LWRM.npy',allow_pickle=True)
dR07 = np.load('CIKM2007LWRM.npy',allow_pickle=True)
dR08 = np.load('CIKM2008LWRM.npy',allow_pickle=True)
dR09 = np.load('CIKM2009LWRM.npy',allow_pickle=True)
dR10 = np.load('CIKM2010LWRM.npy',allow_pickle=True)
dR11 = np.load('CIKM2011LWRM.npy',allow_pickle=True)
dR12 = np.load('CIKM2012LWRM.npy',allow_pickle=True)
dR13 = np.load('CIKM2013LWRM.npy',allow_pickle=True)
dR14 = np.load('CIKM2014LWRM.npy',allow_pickle=True)
dR15 = np.load('CIKM2015LWRM.npy',allow_pickle=True)
dR16 = np.load('CIKM2016LWRM.npy',allow_pickle=True)
# create years array
Yt = list(np.arange(2001,2017))
# create empty numpy array for storing maximum negative log word rank movements
ndR = np.zeros((len(MKW), len(Yt)))
# find maximum negative log word rank movements
for m in range(len(MKW)):
	# 2001
	dRm01max = 0.0
	for n in range(len(dR01)):
		if MKW[m] in dR01[n]:
			if -1.0*dR01[n][MKW[m]] > dRm01max:
				dRm01max = -1.0*dR01[n][MKW[m]]
	ndR[m,0] = dRm01max
	# 2002
	dRm02max = 0.0
	for n in range(len(dR02)):
		if MKW[m] in dR02[n]:
			if -1.0*dR02[n][MKW[m]] > dRm02max:
				dRm02max = -1.0*dR02[n][MKW[m]]
	ndR[m,1] = dRm02max
	# 2003
	dRm03max = 0.0
	for n in range(len(dR03)):
		if MKW[m] in dR03[n]:
			if -1.0*dR03[n][MKW[m]] > dRm03max:
				dRm03max = -1.0*dR03[n][MKW[m]]
	ndR[m,2] = dRm03max
	# 2004
	dRm04max = 0.0
	for n in range(len(dR04)):
		if MKW[m] in dR04[n]:
			if -1.0*dR04[n][MKW[m]] > dRm04max:
				dRm04max = -1.0*dR04[n][MKW[m]]
	ndR[m,3] = dRm04max
	# 2005
	dRm05max = 0.0
	for n in range(len(dR05)):
		if MKW[m] in dR05[n]:
			if -1.0*dR05[n][MKW[m]] > dRm05max:
				dRm05max = -1.0*dR05[n][MKW[m]]
	ndR[m,4] = dRm05max
	# 2006
	dRm06max = 0.0
	for n in range(len(dR06)):
		if MKW[m] in dR06[n]:
			if -1.0*dR06[n][MKW[m]] > dRm06max:
				dRm06max = -1.0*dR06[n][MKW[m]]
	ndR[m,5] = dRm06max
	# 2007
	dRm07max = 0.0
	for n in range(len(dR07)):
		if MKW[m] in dR07[n]:
			if -1.0*dR07[n][MKW[m]] > dRm07max:
				dRm07max = -1.0*dR07[n][MKW[m]]
	ndR[m,6] = dRm07max
	# 2008
	dRm08max = 0.0
	for n in range(len(dR08)):
		if MKW[m] in dR08[n]:
			if -1.0*dR08[n][MKW[m]] > dRm08max:
				dRm08max = -1.0*dR08[n][MKW[m]]
	ndR[m,7] = dRm08max
	# 2009
	dRm09max = 0.0
	for n in range(len(dR09)):
		if MKW[m] in dR09[n]:
			if -1.0*dR09[n][MKW[m]] > dRm09max:
				dRm09max = -1.0*dR09[n][MKW[m]]
	ndR[m,8] = dRm09max
	# 2010
	dRm10max = 0.0
	for n in range(len(dR10)):
		if MKW[m] in dR10[n]:
			if -1.0*dR10[n][MKW[m]] > dRm10max:
				dRm10max = -1.0*dR10[n][MKW[m]]
	ndR[m,9] = dRm10max
	# 2011
	dRm11max = 0.0
	for n in range(len(dR11)):
		if MKW[m] in dR11[n]:
			if -1.0*dR11[n][MKW[m]] > dRm11max:
				dRm11max = -1.0*dR11[n][MKW[m]]
	ndR[m,10] = dRm11max
	# 2012
	dRm12max = 0.0
	for n in range(len(dR12)):
		if MKW[m] in dR12[n]:
			if -1.0*dR12[n][MKW[m]] > dRm12max:
				dRm12max = -1.0*dR12[n][MKW[m]]
	ndR[m,11] = dRm12max
	# 2013
	dRm13max = 0.0
	for n in range(len(dR13)):
		if MKW[m] in dR13[n]:
			if -1.0*dR13[n][MKW[m]] > dRm13max:
				dRm13max = -1.0*dR13[n][MKW[m]]
	ndR[m,12] = dRm13max
	# 2014
	dRm14max = 0.0
	for n in range(len(dR14)):
		if MKW[m] in dR14[n]:
			if -1.0*dR14[n][MKW[m]] > dRm14max:
				dRm14max = -1.0*dR14[n][MKW[m]]
	ndR[m,13] = dRm14max
	# 2015
	dRm15max = 0.0
	for n in range(len(dR15)):
		if MKW[m] in dR15[n]:
			if -1.0*dR15[n][MKW[m]] > dRm15max:
				dRm15max = -1.0*dR15[n][MKW[m]]
	ndR[m,14] = dRm15max
	# 2016
	dRm16max = 0.0
	for n in range(len(dR16)):
		if MKW[m] in dR16[n]:
			if -1.0*dR16[n][MKW[m]] > dRm16max:
				dRm16max = -1.0*dR16[n][MKW[m]]
	ndR[m,15] = dRm16max
print(len(MKW))
# save data
np.save('CIKMMKWhindR.npy', ndR)
np.save('CIKMMKW.npy',MKW)
