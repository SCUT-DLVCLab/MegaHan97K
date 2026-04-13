<div align=center>

# MegaHan97K: A Large-Scale Dataset for Mega-Category Chinese Character Recognition with over 97K Categories

</div>

![Megahan97K_LOGO](images/logo.png) 

<div align="center">


<!-- <a href="https://www.sciencedirect.com/science/article/abs/pii/S0031320325004170"> <b>Pattern Recognition (PR), 2025</b> </a> -->

[![SCUT DLVC Lab](https://img.shields.io/badge/SCUT-DLVC_Lab-327FE6?logo=Academia&logoColor=white)](http://dlvc-lab.net/lianwen/)
[![Pattern Recognition](https://img.shields.io/badge/Pattern_Recognition-2025-FF6C37?logo=Elsevier&logoColor=white&labelColor=0C2340)](https://www.sciencedirect.com/science/article/abs/pii/S0031320325004170)
[![arXiv preprint](http://img.shields.io/badge/arXiv-2506.04807-b31b1b)](https://arxiv.org/abs/2506.04807) 
[![Code](https://img.shields.io/badge/Code-MegaHan97K-yellow)](https://github.com/SCUT-DLVCLab/MegaHan97K)

</div>

* We introduce **MegaHan97K**, a mega-category, large-scale dataset that contains the largest 97,455 Chinese character categories.
* MegaHan97K includes Chinese characters of 97,455 categories, which significantly surpasses existing datasets with at least six times larger categories and holds the largest volume.
* MegaHan97K pioneers to support the latest Chinese GB18030-2022 standard, ensuring the most comprehensive coverage and compatibility with modern Chinese processing systems.
* MegaHan97K contains three distinct subsets: handwritten, historical, and synthetic. Each subset contains a greater number of character categories compared to existing datasets, resulting in remarkable scale and diversity advantages.
* MegaHan97K effectively mitigates long-tail distribution issues by providing a balanced and sufficient number of samples for each category, ensuring robust training and validation of CCR models.

![overview](/images/overview.png)

<!-- ![example](/images/all_data.png) -->

## Important Note
The original data of the dataset is sourced from public channels such as the Internet, and its copyright shall remain with the original providers. The collated and annotated dataset presented in this case is for non-commercial use only and is currently licensed to universities and research institutions. To apply for the use of this dataset, please fill in the corresponding application form in accordance with the requirements specified on the dataset’s official website. The applicant must be a full-time employee of a university or research institute and is required to sign the application form. For the convenience of review, it is recommended to affix an official seal (a seal of a secondary-level department is acceptable).



## 🔥 Download
| **Setting**             | **Dataset** | **status** |
|-------------------------|----------------|------------|
| **General CCR**         | [Baiduyun:k4ch](https://pan.baidu.com/s/1LwIS-K812Q0LjBajpvQeVw?pwd=k4ch)/[OneDrive](https://1drv.ms/u/c/d3b0ec8fe3491f94/EYi4e5_dtLBMmFl9I669KjEBr2PqPWEd7VLxeIzHDlKhgg?e=YXrQEO) | Released |
| **Zero-Shot CCR**       | [Baiduyun:bxde](https://pan.baidu.com/s/1tKhrIZK7zmpQq3NNCo5Edw?pwd=bxfe)/[OneDrive](https://1drv.ms/u/c/d3b0ec8fe3491f94/ETsFnx-i6sRJvrVrgnvO3h4BMugmO2TUObjD9ddz3xfEmw?e=IoUcXq) | Released |

## 🛠️ Usage

* Clone this repo:
```bash
git clone https://github.com/SCUT-DLVCLab/MegaHan97K.git
```

* Execute the following command to obtain example samples from the MegaHan97K dataset.
```python
python MegaHan_Dataloader.py
```

**Note:**
- The MegaHan97K dataset can only be used for non-commercial research purposes. For scholar or organization who wants to use the MegaHan97K dataset, you can apply through either of the following two options:

  **Option A: Apply Online**
  Submit your application through our online platform: 👉 [Apply Here](http://121.41.49.212:9000/)

  **Option B: Apply via Email**
  Please first fill in this [Application Form](./application-form/Application-Form-for-Using-MegaHan97K.docx) and sign the [Legal Commitment](./application-form/Legal-Commitment.docx) and email them to us ([eelwjin@scut.edu.cn](mailto:eelwjin@scut.edu.cn), cc: [lianwen.jin@gmail.com](mailto:lianwen.jin@gmail.com)). When submitting the application form to us, please list or attached 1-2 of your publications in the recent 6 years to indicate that you (or your team) do research in the related research fields of handwriting analysis and recognition, document image processing, and so on.

- We will give you the decompression password after your application has been received and approved.
- All users must follow all use conditions; otherwise, the authorization will be revoked.

* To access the entire dataset, please first download it, update the ```data_root``` in the python ```MegaHan_Dataloader.py``` script and then execute
```python
python MegaHan_Dataloader.py
```

## ☎️ Contact
If you have any questions, feel free to contact [Yuyi Zhang](https://github.com/ZZXF11) at [yuyi.zhang11@foxmail.com](yuyi.zhang11@foxmail.com)

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

* **Illustration of the handwritten-original data in MegaHan97K**
![mwo](/images/mwrite.png)

* **Illustration of the handwritten-augmented data in MegaHan97K**
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
- Copyright 2025, [Deep Learning and Vision Computing Lab (DLVC-Lab)](http://www.dlvc-lab.net), South China University of Technology.

## ⭐ Star Rising
[![Star Rising](https://api.star-history.com/svg?repos=SCUT-DLVCLab/MegaHan97K&type=Timeline)](https://star-history.com/#SCUT-DLVCLab/MegaHan97K&Timeline)
