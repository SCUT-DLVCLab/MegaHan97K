<h1 align="center">MegaHan97K Dataset</h1>

<div align="center">

<a href="https://www.sciencedirect.com/science/article/abs/pii/S0031320325004170"> <b>MegaHan97K: A Large-Scale Dataset for Mega-Category Chinese Character Recognition with over 97K Categories</b> </a>

<b>Pattern Recognition (PR), 2025</b>

</div>

* We introduce MegaHan97K, a mega-category, large-scale dataset that contains the largest 97,455 Chinese character categories.
* MegaHan97K includes Chinese characters of 97,455 categories, which significantly surpasses existing datasets with at least six times larger categories and holds the largest volume.
* MegaHan97K pioneers to support the latest Chinese GB18030-2022 standard, ensuring the most comprehensive coverage and compatibility with modern Chinese processing systems.
* MegaHan97K contains three distinct subsets: handwritten, historical, and synthetic. Each subset contains a greater number of character categories compared to existing datasets, resulting in remarkable scale and diversity advantages.
* MegaHan97K effectively mitigates long-tail distribution issues by providing a balanced and sufficient number of samples for each category, ensuring robust training and validation of CCR models.

![overview](/images/overview.png)

<!-- ![example](/images/all_data.png) -->



## 🔥 Download
| **Setting**             | **Dataset** | **status** |
|-------------------------|----------------|------------|
| **General CCR**         | [Baiduyun:k4ch](https://pan.baidu.com/s/1LwIS-K812Q0LjBajpvQeVw?pwd=k4ch) | Released |
| **Zero-Shot CCR**       | [Baiduyun:bxde](https://pan.baidu.com/s/1tKhrIZK7zmpQq3NNCo5Edw?pwd=bxfe) | Released |

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
- The MegaHan97K dataset can only be used for non-commercial research purposes. For scholar or organization who wants to use the MegaHan97K dataset, please first fill in this [Application Form](./application-form/Application-Form-for-Using-MegaHan97K.docx) and sign the [Legal Commitment](./application-form/Legal-Commitment.docx) and email them to us. When submitting the application form to us, please list or attached 1-2 of your publications in the recent 6 years to indicate that you (or your team) do research in the related research fields of handwriting analysis and recognition, document image processing, and so on.
- We will give you the decompression password after your application has been received and approved.
- All users must follow all use conditions; otherwise, the authorization will be revoked.

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
