# MegaHan97K Dataset

* We introduce MegaHan97K, a mega-category, large-scale dataset that contains the largest 97,455 Chinese character categories.
* MegaHan97K includes Chinese characters of 97,455 categories, which significantly surpasses existing datasets with at least six times larger categories and holds the largest volume.
* MegaHan97K pioneers to support the latest Chinese GB18030-2022 standard, ensuring the most comprehensive coverage and compatibility with modern Chinese processing systems.
* MegaHan97K contains four distinct subsets: handwritten, mouse-written, historical, and synthetic. Each subset contains a greater number of character categories compared to existing datasets, resulting in remarkable scale and diversity advantages.
* MegaHan97K effectively mitigates long-tail distribution issues by providing a balanced and sufficient number of samples for each category, ensuring robust training and validation of CCR models.

![overview](/images/overview.png)

![example](/images/all_data.png)



## 🔥 Download
| **Setting**             | **Dataset** | **status** |
|-------------------------|----------------|------------|
| **General CCR**         | [GoogleDrive](https://drive.google.com/file/d/15rB6WE92RBB898kJoj3CFeSotPj_v3N-/view?usp=drive_link) / [BaiduYun:mbns](https://pan.baidu.com/s/1lBnBvisG-P-1ZYs2cZALzw?pwd=mbns) | Released |
| **Zero-Shot CCR**       | [GoogleDrive](https://drive.google.com/file/d/1UjmdeErr89L3AX5Yd95B8IWgesPyR2xT/view?usp=drive_link) / [BaiduYun:6pxi](https://pan.baidu.com/s/1E5WMLh64HThP1TIVGNijcQ?pwd=6pxi) | Released    |

## 🛠️ Usage

* Clone this repo:
```bash
git clone https://github.com/SCUT-DLVCLab/MegaHan97K.git
```

* Execute the following command to obtain example samples from the MegaHan97K dataset.
```python
python MegaHan_Dataloader.py
```

**Note: If you wish to access the entire dataset, please contact us via the email of the first author listed in the paper to obtain the decryption password.**
* To access the entire dataset, please first download it, update the ```data_root``` in the python ```MegaHan_Dataloader.py``` script and then execute
```python
python MegaHan_Dataloader.py
```


## 🌄 Gallery

<!-- * **Overview** -->


* **Illustration of the handwritten-original data in MegaHan97K**
![handwo](/images/handw.png)

* **Illustration of the handwritten-augmented data in MegaHan97K**
![handwa](/images/handw_rand.png)

* **Illustration of the M<sup>5</sup>HisDoc data in MegaHan97K**
![m5](/images/guji.png)

* **Illustration of the Kangxi dictionary data in MegaHan97K**
![kx](/images/kxzd.png)

* **Illustration of the mouse-written-original data in MegaHan97K**
![mwo](/images/mwrite.png)

* **Illustration of the mouse-written-augmented data in MegaHan97K**
![mwa](/images/mwrite_rand.png)

* **Illustration of the synthetic data in MegaHan97K**
![syn](/images/syn.png)

## 💙 Acknowledgement
- [M<sup>5</sup>HisDoc](https://github.com/HCIILAB/M5HisDoc)
- [FontDiffuser](https://github.com/yeungchenwa/FontDiffuser)

## License
MegaHan97K should be used and distributed under [Creative Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0) License](https://creativecommons.org/licenses/by-nc-nd/4.0/) for non-commercial research purposes.
## Copyright

- This repository can only be used for non-commercial research purposes.
- For commercial use, please contact Prof. Lianwen Jin (eelwjin@scut.edu.cn).
- Copyright 2024, [Deep Learning and Vision Computing Lab (DLVC-Lab)](http://www.dlvc-lab.net), South China University of Technology. 
