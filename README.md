# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Institut merupakan salah satu institusi pendidikan tinggi yang telah berdiri sejak tahun 2000 dan dikenal telah mencetak banyak lulusan berprestasi. Namun, di balik keberhasilan tersebut, masih terdapat masalah signifikan yaitu tingginya tingkat dropout (siswa yang tidak menyelesaikan pendidikan).

Tingkat dropout yang tinggi tidak hanya berdampak pada reputasi institusi, tetapi juga menghambat misi utama institusi dalam mencetak lulusan berkualitas. Oleh karena itu, penting bagi Jaya Jaya Institut untuk melakukan deteksi dini terhadap siswa yang berpotensi dropout agar dapat diberikan intervensi atau bimbingan khusus sejak awal.

### Permasalahan Bisnis
- Tingginya jumlah siswa yang melakukan dropout.
- Insitut kurang memahami faktor-faktor yang memengaruhi performa siswa.
- Tidak adanya sistem monitoring performa siswa berbasis data.
- Ketiadaan sistem deteksi dini untuk mengidentifikasi siswa berisiko tinggi.

### Cakupan Proyek
- Melakukan eksplorasi dan preprocessing data siswa yang disediakan oleh institusi.
- Membangun model machine learning untuk memprediksi status siswa (Dropout, Enrolled, Graduate).
- Menyusun dashboard interaktif untuk membantu pihak manajemen memahami performa siswa.
- Membuat prototype aplikasi prediksi berbasis web yang dapat digunakan untuk memantau dan mengantisipasi potensi dropout.
- Menyediakan sistem monitoring model ML dengan Prometheus dan Grafana.

### Persiapan

Sumber data : [Github Dicoding Jaya Jaya Student Performance ](https://github.com/dicodingacademy/dicoding_dataset/tree/main/students_performance)

Setup environment:
```
conda create --name JayaMajuHR python=3.9
conda activate JayaMajuHR
pip install -r requirements.txt
```
#### Instalasi dependensi:
```
pip install -r requirements.txt
```
#### Setup Environment - Metabase
```
mkdir -p ~/metabase-data
docker run -d -p 3000:3000 --name metabase \
  -v ~/metabase-data:/metabase.db \
  metabase/metabase
```

## Business Dashboard
Link Dashboard : [Dashboard](http://localhost:3000/public/dashboard/f33f6bed-d92f-435b-bc3c-655f334c2872)
Email: leonardo.fajar.mardika-2020@ftmm.unair.ac.id
Password: KomboUA22
Dashboard ini saya buat dengan memasukkan dataset student performance. Dalam dashboard ini tab dimana yang berkaitan kondisi status siswa, hubungan status dengan keadaan siswa, hubungan status dengan nilai siswa, dan hubungan status dengan keadaan ekonomi.
Dashboard diawali dengan memiliki beberapa filter seperti:
- Age enrollment : Umur pelajar/siswa masuk
- Status : Status siswa saat ini
- Course : Bidang yang diambil siswa
- Gender : Jenis Kelamin
- Nacionality : Kewarganegaraan

Pada tab 1 terdapat beberapa tabel seperti:

| Tabel                                              | Deskripsi                                                                                  |
|----------------------------------------------------|--------------------------------------------------------------------------------------------|
| Student Count                                      | Jumlah total siswa yang terdaftar di Jaya Jaya Institut                                   |
| Dropout Count                                      | Jumlah siswa yang keluar (dropout) dari institusi                                         |
| Percentage Dropout                                 | Persentase siswa yang melakukan dropout dibandingkan total siswa                          |
| Average of Curricular 1st Grade                    | Rata-rata nilai kurikulum semester pertama                                                |
| Count by Scholarship_holder                        | Jumlah siswa yang menerima beasiswa                                                       |
| Count by Tuition_fees_up_to_date                   | Jumlah siswa yang membayar uang kuliah tepat waktu                                        |
| Count by Daytime_evening_attendance                | Jumlah siswa berdasarkan keikutsertaan dalam kelas siang atau malam                       |
| Average of Previous_qualification_grade by Status  | Rata-rata nilai kualifikasi sebelumnya (sebelum masuk) berdasarkan status dropout/aktif   |
| Average of Curricular_units_credited by Status     | Rata-rata jumlah mata kuliah yang dikonversi kreditnya berdasarkan status dropout/aktif   |
| Average of Curricular_unit_enrolled by Status      | Rata-rata jumlah mata kuliah yang diambil siswa berdasarkan status dropout/aktif          |
| Average of Curricular_units_evaluations by Status  | Rata-rata jumlah evaluasi kurikulum yang diikuti siswa berdasarkan status dropout/aktif   |
| Average of Curricular_units_approved by Status     | Rata-rata jumlah mata kuliah yang lulus berdasarkan status dropout/aktif                  |
| Average of Curricular_units_without_evaluations by Status | Rata-rata jumlah mata kuliah tanpa evaluasi berdasarkan status dropout/aktif         |
| Average of Curricular_units_1st and 2nd_grade by Status | Rata-rata nilai semester 1 dan 2 berdasarkan status dropout/aktif                    |
| Inflation_rate and Status                          | Korelasi antara tingkat inflasi saat itu dengan status siswa (aktif/dropout)              |
| Unemployment_rate and Status                       | Korelasi antara tingkat pengangguran dengan status siswa (aktif/dropout)                  |
| GDP and Status                                     | Korelasi antara kondisi ekonomi (GDP) dengan status siswa (aktif/dropout)                 |
| Status and Debtor                                  | Jumlah siswa dengan status berhutang (debtor) berdasarkan status dropout/aktif            |


## Menjalankan Sistem Machine Learning
Menjalankan Prediksi Streamlit dengan app.py 
- Pastikan file app.py dan folder model berada dalam direktori yang sama.
- Jalankan script:
    #### Running app Streamlit:
    ```
    streamlit run app.py
    ```
Atau bisa langsung menggunakan link yang suda dideploy berikut: [Streamlit](https://studentperformance123.streamlit.app/)


## Conclusion
Dari hasil analis dapat disimpulkan bahwa:
#### Faktor penyebab utama siswa dropout:
- Siswa yang memiliki nilai rendah pada awal semester
- Kekuatan finansial siswa yang kurang baik
- Mayoritas laki-laki yang melakukan dopout
#### Karakteristik umum karyawan yang keluar:
- Nilai awal semester yang kurang baik.
- Tidak memiliki kemampuan untuk membayar uang studi
- Memiliki debt/hutang yang harus dibayarkan
- Cenderung hadir di kelas malam dan berasal dari daerah dengan tingkat pengangguran atau inflasi yang tinggi.

#### Business dashboard yang dibangun (Metabase) memvisualisasikan:
- Distribusi status siswa (dropout, enrolled, graduate) berdasarkan faktor-faktor penting seperti gender, usia saat mendaftar, beasiswa, status keuangan, kehadiran kelas, dan faktor ekonomi makro (inflasi, pengangguran, GDP).
- KPI utama seperti total jumlah siswa, total dropout, persentase dropout, serta rata-rata nilai akademik semester awal dan kredit kurikuler.

#### Prediksi menggunakan model Machine Learning (Random Forest):
- Model dilatih pada data performa siswa dan mampu memprediksi status suwa dengan akurasi >80%.
- Model dapat dideploy dengan run python app atau dengan link [streamlit](https://studentperformance123.streamlit.app/) yang telah disiapkan untuk mempermudah inferensi terhadap siswa baru atau aktif.

### Rekomendasi Action Items
Berikan beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka.
- Lakukan monitoring akademik ketat di semester awal untuk mendeteksi murid berisiko.
- Berikan program remedial atau tutoring bagi mahasiswa dengan nilai rendah
- Tingkatkan layanan konseling dan bimbingan akademik secara proaktif
- Sediakan bantuan keuangan seperti cicilan SPP dan dana darurat untuk siswa.
