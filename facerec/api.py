import requests
data = {
            'alamat': 'Coba Masukkan Tanggal Dengan Timeout',
            'jk': 'L',
            'jurusan': '1',
            'nama': '1',
            'nim': '1'
        }
api_url = "https://aldidwiferdian.000webhostapp.com/mahasiswa"
response = requests.post(api_url, data)
response.json()
api_url = "https://aldidwiferdian.000webhostapp.com/mahasiswa"
response = requests.post(api_url, data)
response.json()
        
print(response)