Check Spam Chat Indonesia
===
Menerima pesan atau chat adalah hal yang biasa, tetapi tetap harus perhatikan ketika menerima pesan terutama dari orang yang tidak dikenal. Sering kali pesan dari orang yang tidak dikenal berupa pesan penipuan yang sangat mengganggu sebagai spam chat. 

Program ini dibuat untuk **mengecek sebuah chat termasuk jenis *spam atau bukan***. Untuk proses mengecek spam chat tersebut menggunakan *algoritma KNN* dengan model dataset berasal dari kaggle yang telah ditambahkan beberapa pesan tambahan yang diterima secara pribadi.
>Terimaksih kepada [Gevabriel](https://www.kaggle.com/gevabriel) untuk model data set dari spam chat.

## Install & Dependence
- python
- pandas
- numpy
- matplotlib
- jupyter notebook
- scikit-learn

## Dataset
| Dataset | Download |
| ---     | ---   |
| Indonesia SMS Spam | [download](https://www.kaggle.com/datasets/gevabriel/indonesian-sms-spam) |

## Directory
```
|—— Model
|    |—— KNN_model.sav
|    |—— model_pesan.xlsx
|—— Train_Test
|    |—— KNN_model_train.sav
|    |—— test.py
|    |—— train.py
|—— example.exe
|—— main.py
|—— try.ipynb
```

## Use
> File dengan nama **example.exe** merupakan program yang telah dieksekusi menjadi aplikasi windows yang dapat langsung dijalankan

Sebelum mencoba menjalankan *program python*, **Pastikan telah menginstall package yang dibutuhkan**. Untuk menginstall package dapat dilakukan pada terminal secara langsung atau menggunakan [virtual environments](https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/) dengan menggunakan pip
  ```
  pip install pandas numpy matplotlib notebook scikit-learn openpyxl
  ```
  atau menggunkana file *requirements.txt*
  ```
  pip install -r requirements.txt
  ```
Untuk mencoba memahami proses pembuatan program yang saya latih dapat menggunakan file **try.ipynb** pada *Jupyter Notebook* dengan menjalankan perintah berikut pada terminal.
  ```
  jupyter notebook
  ```
>Pastikan terminal dibuka pada direktori tempat menyimpan program untuk mempermudah proses pencarian dan menjalankan file.

Jika ingin mencoba melakukan pelatihan program sendiri dapat melakukannya pada file **train.py** yang ada pada direktori *Train_Test* dengan menggunakan perintah
  ```
  python train.py
  ```
Kemudian, untuk menguji program yang telah dilatih sebelumnya dapat melakukannya pada file **test.py** yang ada pada direktori *Train_Test* dengan menggunakan perintah
  ```
  python test.py
  ```
>Setelah berhasil membuat model KNN yang dirasa sudah akurat dapat digunakan untuk mengubah file model yang digunakan pada program **main.py** dengan model latihan yang baru.

Pada **Program main.py** dapat digunakan dengan memanggil function *check_chat* untuk memeriksa status sebuah chat adalah spam atau bukan. Program ini dapat dikombinasikan menggunakan sistem API, seperti flask untuk digunakan sesuai kebutuhan yang diinginkan.
