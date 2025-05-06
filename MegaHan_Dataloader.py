
import os
import torch
from torch.utils.data import Dataset
import torchvision.transforms as transforms
import lmdb, cv2, six, sys
from PIL import Image
from PIL import Image
import numpy as np
import torchvision


class LMDBDataset(Dataset):
    def __init__(self, root=None, img_size=(96,96), transform=None):
        
        self.env = lmdb.open(
            root,
            max_readers=1,
            readonly=True,
            lock=False,
            readahead=False,
            meminit=False,
            map_size=1099511627776)

        
        if not self.env:
            print('cannot creat lmdb from %s' % (root))
            sys.exit(0)
        with self.env.begin(write=False) as txn:
            
            nSamples = int(txn.get('num-samples'.encode()).decode())
            self.nSamples = nSamples

        self.root = root
        self.transform = transform
        self.img_size = img_size
        self.toTensor = transforms.ToTensor()

    def __len__(self):
        return self.nSamples

    def __getitem__(self, index):
        assert index <= len(self), 'index range error'
        index += 1
        with self.env.begin(write=False) as txn:
            
            img_key = 'image-%09d' % index
            label_key = 'label-%09d' % index
            imgbuf = txn.get(img_key.encode())
            buf = six.BytesIO()
            buf.write(imgbuf)
            buf.seek(0)
            try:
                img = Image.open(buf).convert('RGB')
            except IOError:
                print('Corrupted image for %d' % index)
                return self[index + 1]

            label = str(txn.get(label_key.encode()).decode())
            

        img = np.asarray(img)
        img = cv2.resize(img, self.img_size, interpolation=cv2.INTER_AREA) #cv2.INTER_AREA
        if self.transform:
            img = self.transform(img)
        label = int(label)

        return (img, label)
    
    
if __name__ == '__main__':
    data_root = 'MegaHan_Example'
    megahan_codebook = 'MegaHan_codebook.txt'
    save_path = 'images'
    

    if not os.path.exists(save_path):
        os.makedirs(save_path)
    codebook = open(megahan_codebook, "r", encoding='utf-8').readlines()
    codebook_dict = {}
    for i, codes in enumerate(codebook):
        char = codes.replace('\n', '')
        codebook_dict[i] = char.split(':')[0]
    
    data_transform = transforms.ToTensor()
    dataset = LMDBDataset(
        root=data_root,
        transform=data_transform,
    )
    train_loader = torch.utils.data.DataLoader(dataset, 
                                               batch_size=1, 
                                               sampler=None, 
                                               drop_last=True, 
                                               num_workers=0, 
                                               shuffle=True,
    )
    dataset_size = len(dataset) 
    print('The number of images = %d' % dataset_size)
    for i, data in enumerate(train_loader):

        img, label = data
        label = codebook_dict[int(label)]
        torchvision.utils.save_image(img, f'{save_path}/{label}_{i}.jpg', normalize=True)
        
