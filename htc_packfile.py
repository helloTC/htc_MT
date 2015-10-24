# This program has a goal to rearrange mroi.mat
import scipy.io as sio
import os

mroi_loc = '/nfs/j3/userhome/huangtaicheng/workingdir/parcellation_MT/BAA/results/yang_test/sub/data/mroi.mat'
data = sio.loadmat(mroi_loc)['mroi']

lMT = data['lMT'][0,0]
rMT = data['rMT'][0,0]
lV3 = data['lV3'][0,0]
rV3 = data['rV3'][0,0]

global gender
gender = lMT['subj'][0,0]['sex'][0,0]

def htc_repack(area,para):
        if not(cmp(para,'psc')):
                para_all = data[area][0,0]['mag'][0,0]['rb'][0,0]
        else: para_all = data[area][0,0]['geo'][0,0][para][0,0]
        if not(cmp(para,'size')):
		para_all = para_all.T
	mpara = para_all[gender[0].T==1]
        fpara = para_all[gender[0].T==0]
        return para_all,mpara,fpara
	

if __name__ == '__main__':
	[peak_lMT,mpeak_lMT,fpeak_lMT] = htc_repack('lMT','peak')
	[peak_rMT,mpeak_rMT,fpeak_rMT] = htc_repack('rMT','peak')
	[peak_lV3,mpeak_lV3,fpeak_lV3] = htc_repack('lV3','peak')
	[peak_rV3,mpeak_rV3,fpeak_rV3] = htc_repack('rV3','peak')

	[size_lMT,msize_lMT,fsize_lMT] = htc_repack('lMT','size')
	[size_rMT,msize_rMT,fsize_rMT] = htc_repack('rMT','size')
	[size_lV3,msize_lV3,fsize_lV3] = htc_repack('lV3','size')
	[size_rV3,msize_rV3,fsize_rV3] = htc_repack('rV3','size')

	[gcenter_lMT,mgcenter_lMT,fgcenter_lMT] = htc_repack('lMT','gcenter')
	[gcenter_rMT,mgcenter_rMT,fgcenter_rMT] = htc_repack('rMT','gcenter')
	[gcenter_lV3,mgcenter_lV3,fgcenter_lV3] = htc_repack('lV3','gcenter')
	[gcenter_rV3,mgcenter_rV3,fgcenter_rV3] = htc_repack('rV3','gcenter')

	[center_lMT,mcenter_lMT,fcenter_lMT] = htc_repack('lMT','center')
	[center_rMT,mcenter_rMT,fcenter_rMT] = htc_repack('rMT','center')
	[center_lV3,mcenter_lV3,fcenter_lV3] = htc_repack('lV3','center')
	[center_rV3,mcenter_rV3,fcenter_rV3] = htc_repack('rV3','center')

	[psc_lMT,mpsc_lMT,fpsc_lMT] = htc_repack('lMT','psc')
	[psc_rMT,mpsc_rMT,fpsc_rMT] = htc_repack('rMT','psc')
	[psc_lV3,mpsc_lV3,fpsc_lV3] = htc_repack('lV3','psc')
	[psc_rV3,mpsc_rV3,fpsc_rV3] = htc_repack('rV3','psc')

	subjdice_lMT = lMT['geo'][0,0]['subj_dice'][0,0]
	subjdice_rMT = rMT['geo'][0,0]['subj_dice'][0,0]
	subjdice_lV3 = lV3['geo'][0,0]['subj_dice'][0,0]
	subjdice_rV3 = rV3['geo'][0,0]['subj_dice'][0,0]

	path = '/nfs/j3/userhome/huangtaicheng/workingdir/parcellation_MT/BAA/results/yang_test/sub/'
	os.mkdir(os.path.join(path,'results'))
	
	os.mkdir(os.path.join(path,'results','peak'))
	sio.savemat(os.path.join(path,'results','peak')+'/peak.mat',{'peak_lMT':peak_lMT,'mpeak_lMT':mpeak_lMT,'fpeak_lMT':fpeak_lMT,'peak_rMT':peak_rMT,'mpeak_rMT':mpeak_rMT,'fpeak_rMT':fpeak_rMT,'peak_lV3':peak_lV3,'mpeak_lV3':mpeak_lV3,'fpeak_lV3':fpeak_lV3,'peak_rV3':peak_rV3,'mpeak_rV3':mpeak_rV3,'fpeak_rV3':fpeak_rV3})

	os.mkdir(os.path.join(path,'results','size'))
        sio.savemat(os.path.join(path,'results','size')+'/size.mat',{'size_lMT':size_lMT,'msize_lMT':msize_lMT,'fsize_lMT':fsize_lMT,'size_rMT':size_rMT,'msize_rMT':msize_rMT,'fsize_rMT':fsize_rMT,'size_lV3':size_lV3,'msize_lV3':msize_lV3,'fsize_lV3':fsize_lV3,'size_rV3':size_rV3,'msize_rV3':msize_rV3,'fsize_rV3':fsize_rV3})

        os.mkdir(os.path.join(path,'results','gcenter'))
        sio.savemat(os.path.join(path,'results','gcenter')+'/gcenter.mat',{'gcenter_lMT':gcenter_lMT,'mgcenter_lMT':mgcenter_lMT,'fgcenter_lMT':fgcenter_lMT,'gcenter_rMT':gcenter_rMT,'mgcenter_rMT':mgcenter_rMT,'fgcenter_rMT':fgcenter_rMT,'gcenter_lV3':gcenter_lV3,'mgcenter_lV3':mgcenter_lV3,'fgcenter_lV3':fgcenter_lV3,'gcenter_rV3':gcenter_rV3,'mgcenter_rV3':mgcenter_rV3,'fgcenter_rV3':fgcenter_rV3})

        os.mkdir(os.path.join(path,'results','center'))
        sio.savemat(os.path.join(path,'results','center')+'/center.mat',{'center_lMT':center_lMT,'mcenter_lMT':mcenter_lMT,'fcenter_lMT':fcenter_lMT,'center_rMT':center_rMT,'mcenter_rMT':mcenter_rMT,'fcenter_rMT':fcenter_rMT,'center_lV3':center_lV3,'mcenter_lV3':mcenter_lV3,'fcenter_lV3':fcenter_lV3,'center_rV3':center_rV3,'mcenter_rV3':mcenter_rV3,'fcenter_rV3':fcenter_rV3})

        os.mkdir(os.path.join(path,'results','psc'))
        sio.savemat(os.path.join(path,'results','psc')+'/psc.mat',{'psc_lMT':psc_lMT,'mpsc_lMT':mpsc_lMT,'fpsc_lMT':fpsc_lMT,'psc_rMT':psc_rMT,'mpsc_rMT':mpsc_rMT,'fpsc_rMT':fpsc_rMT,'psc_lV3':psc_lV3,'mpsc_lV3':mpsc_lV3,'fpsc_lV3':fpsc_lV3,'psc_rV3':psc_rV3,'mpsc_rV3':mpsc_rV3,'fpsc_rV3':fpsc_rV3})

        os.mkdir(os.path.join(path,'results','dice'))
	sio.savemat(os.path.join(path,'results','dice')+'/subj_dice.mat',{'subjdice_lMT':subjdice_lMT,'subjdice_rMT':subjdice_rMT,'subjdice_lV3':subjdice_lV3,'subjdice_rV3':subjdice_rV3})

	sio.savemat(os.path.join(path,'results')+'/gender.mat',{'gender':gender})
