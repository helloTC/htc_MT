import numpy as np
import nibabel as nib
import pandas as pd
import shutil
import scipy.io as sio

#This function is aim to calculate peak value of roi or stat picture and the peak value location
#Input
#type:'roi' or 'stat'
#pic_loc:file name
def htc_vox(type,pic_loc):
	#input image
	loc_ex='/nfs/j3/userhome/huangtaicheng/workingdir/parcellation_MT/BAA/results'
	loc=loc_ex+'/'+type+'/'+pic_loc+'.nii.gz'
	img = nib.load(loc)
	#calculate peak & peak value
	data = img.get_data()
	vox = np.unravel_index(data.argmax(),data.shape)
	return vox,data[vox]
	
#This function is aim to trasfer vox into MNI coordinates
#Input
#vox:vox coordinates
#size:resampled size
def htc_vox2MNI(vox,size):
	MNI=np.zeros(3)
	MNI[0]=(45-vox[0])*size
	MNI[1]=(vox[1]-63)*size
	MNI[2]=(vox[2]-36)*size
	return MNI
# Aim contrary to above
def htc_MNI2vox(MNI,size):
	vox = np.zeros(3)
	vox[0] = 45-(MNI[0]/size)
	vox[1] = 63+(MNI[1]/size)
	vox[2] = 36+(MNI[2]/size)
	return vox

#This function is aim to generate MPM picture
def htc_MPM(merge_pic,thre):
#Input
#merge_pic:merge pictures,pay attention the 1st dimension of merge picture 
#	   is zeros
#thre:thresholds
	img=nib.load(merge_pic)
	data=img.get_data()
	header=img.get_header()
	
	data[data<thre]=0
	data_new=np.argmax(data,axis=3)
	
	img_new=nib.Nifti1Image(data_new,None,header)
	nib.save(img_new,'MPM_p'+str(thre)+'.nii.gz')


def htc_cp(type):
	a=open('/nfs/j3/userhome/huangtaicheng/workingdir/parcellation_MT/doc/dfsf/sessid')
	line=a.readlines()
	type = type+'1'
	ori_loc = '/nfs/h2/fmricenter/volume/'
	aim_loc = '/nfs/j3/userhome/huangtaicheng/workingdir/parcellation_MT/BAA/SSR/'
	signal_ori = [ori_loc+line[i].replace('\n','')+'/mt.gfeat/'+'cope1.feat/'+'stats/'+type+'.nii.gz' for i in range(0,202)]
	signal_aim = [aim_loc+line[i].replace('\n','')+'/mt/'+'motion/' for i in range(0,202)]
	
	for i in range(0,202):
		shutil.copy(signal_ori[i],signal_aim[i])



# We want to calculate the reliability between two experts,by dice
# Input:
#	image4d1 & image4d2:4d files for comparison
# Output:
#	output:dice coefficients

# Pay attention:output is a subject_num * labelid_num matrix

def cal_dice(image4d1,image4d2,n):
	image1 = np.zeros([n,91,109,91])
	image2 = np.zeros([n,91,109,91])
	output = np.zeros([image4d1.shape[3],image1.shape[0]])
	for i in range(0,image4d1.shape[3]):
	        for j in range(0,image1.shape[0]):
			image1[j,:,:,:] = (np.abs((image4d1[:,:,:,i])-(j+1))<(10**-5))
			image2[j,:,:,:] = (np.abs((image4d2[:,:,:,i])-(j+1))<10**-5)
			dice_num = dice(image1[j,:,:,:],image2[j,:,:,:])
			output[i,j]=dice_num
	return output

def dice(image1,image2):
        image1_instead = image1
        image2_instead = image2
        image1_instead[image1_instead!=0]=1
        image2_instead[image2_instead!=0]=1
        overlap = image1*image2
        dice_num = 2*overlap.sum()/(image1.sum()+image2.sum())
        return dice_num

# produce peak/center/gcenter coordinate picture
def coordin_pic(areas,type):
	localdir = '/nfs/j3/userhome/huangtaicheng/workingdir/parcellation_MT/BAA/results/yang_test/sub201/data/results/'
	mat_name = localdir + '/' + type + '/' + type +'_'+ areas +'.mat'
	coor = sio.loadmat(mat_name)[type + '_' + areas]
	coorm = sio.loadmat(mat_name)['m'+type+'_'+areas]
	coorf = sio.loadmat(mat_name)['f'+type+'_'+areas]
	img = nib.load('/nfs/j3/userhome/huangtaicheng/workingdir/parcellation_MT/BAA/results/yang_test/sub201/data/probmaps/lMT.nii.gz')
	coor_vox = np.zeros([coor.shape[0],3])
	coorf_vox = np.zeros([coorf.shape[0],3])
	coorm_vox = np.zeros([coorm.shape[0],3])
	for i in range(0,coor.shape[0]):
		coor_vox[i,:] = htc_MNI2vox(coor[i,:],2)
        for i in range(0,coorm.shape[0]):        
		coorm_vox[i,:] = htc_MNI2vox(coorm[i,:],2)
	for i in range(0,coorf.shape[0]):
                coorf_vox[i,:] = htc_MNI2vox(coorf[i,:],2)
	coor_vox = np.int16(coor_vox)
        coorm_vox = np.int16(coorm_vox)
        coorf_vox = np.int16(coorf_vox)

	header = img.get_header()
	data = np.zeros([91,109,91])
	datam = np.zeros([91,109,91])
	dataf = np.zeros([91,109,91])
	for i in range(0,coor.shape[0]):
		data[coor_vox[i,0],coor_vox[i,1],coor_vox[i,2]]=data[coor_vox[i,0],coor_vox[i,1],coor_vox[i,2]]+1
	for i in range(0,coorm.shape[0]):
		datam[coorm_vox[i,0],coorm_vox[i,1],coorm_vox[i,2]]=datam[coorm_vox[i,0],coorm_vox[i,1],coorm_vox[i,2]]+1
	for i in range(0,coorf.shape[0]):	
		dataf[coorf_vox[i,0],coorf_vox[i,1],coorf_vox[i,2]]=dataf[coorf_vox[i,0],coorf_vox[i,1],coorf_vox[i,2]]+1

	img = nib.Nifti1Image(data,None,header)
	nib.save(img,type+areas+'.nii.gz')

        imgm = nib.Nifti1Image(datam,None,header)
        nib.save(imgm,'m'+type+areas+'.nii.gz')

        imgf = nib.Nifti1Image(dataf,None,header)
        nib.save(imgf,'f'+type+areas+'.nii.gz')

def maskfile(fileurl,maskurl,method):
# file and mask are all with 4D
	file = nib.load(fileurl)
	mask = nib.load(maskurl)
	file_data = file.get_data()
	mask_data = mask.get_data()
	maskvalue = np.zeros([4,file_data.shape[3]])
	
	for i in range(file_data.shape[3]):
		for j in range(4):
			if method == 'mean':
				maskvalue[j,i] = file_data[:,:,:,i]\
				[mask_data[:,:,:,i] == j+1].mean()
			elif method == 'peak':
				maskvalue[j,i] = file_data[:,:,:,i]\
		        	[mask_data[:,:,:,i] == j+1].max()
			else: 
		     		maskvalue[j,i] = file_data[:,:,:,i]\
		     		[mask_data[:,:,:,i] == j+1].mean()
	return maskvalue

