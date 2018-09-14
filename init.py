from google_drive_downloader import GoogleDriveDownloader  as gdd
import os, json, glob
import pickle
import pdb

def batch_download(keys, file_dir):
	# download the dataset
	for key in keys:
		folder = '/'.join(key.split('/')[0:-1])+'/'
		if not os.path.exists(folder):
			os.mkdir(folder)
		if not os.path.isfile(key):
			gdd.download_file_from_google_drive(
				file_id=file_dir[key]['file_id'],
				dest_path=key,
				unzip=True)

	return 

# inidicate the hardware or trans_render one wants to download
flat_flg = 'kinect'
list_flgs = ['test']

# create the local folder for the dataset
folder = './FLAT_test/'
if not os.path.exists(folder):
	os.mkdir(folder)

# load the directory list of the flat dataset
file_dir_name = 'file_dir.pickle'
with open(file_dir_name, 'rb') as f:
	file_dir = pickle.load(f)

os.chdir(folder)
lists = []
# download the certain list indicated by the flg
for i in range(len(list_flgs)):
	folder_dir = './'+flat_flg+'/list/'
	filename = folder_dir+list_flgs[i]+'.txt'
	batch_download([filename],file_dir)

	# load the file, and read stuffs
	f = open(filename,'r')
	message = f.read()
	files = message.split('\n')
	data_list = files[0:-1]

	# download the images in the list folder
	filename = filename[:-4]+'/'
	keys = [key for key in file_dir.keys() if filename in key]
	batch_download(keys, file_dir)

	# download the files in the datafolder
	keys = [key for key in file_dir.keys() \
		if (key.split('/')[-1] in data_list) \
		and (key.split('/')[1] == flat_flg)
	]
	batch_download(keys, file_dir)


# download the modules


pdb.set_trace()
