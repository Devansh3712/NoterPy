# NoterPy

NoterPy is a task management and notes taking program, made using `Python` and the database is managed using `MySQL`

<img src="https://img.shields.io/badge/python%20-%2314354C.svg?&style=for-the-badge&logo=python&logoColor=white"/> <img src="https://camo.githubusercontent.com/4524c09f8c821218b3c602e3e5a222ce00c290c2f87e264b40f398a6b486bd91/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6d7973716c2d2532333030303030662e7376673f267374796c653d666f722d7468652d6261646765266c6f676f3d6d7973716c266c6f676f436f6c6f723d7768697465"/>

## Installation

### Clone

Clone this repository to your local machine or download it as a zip file 

```console
git clone https://github.com/Devansh3712/NoterPy.git
```

### Setup

Before using `noterpy`, install the required modules using `pip`, mentioned in `requirements.txt`

> Windows
```console
pip install -r requirements.txt
```

> Linux
```console
pip3 install -r requirements.txt
```

> If any error arises for `mysqlclient` or `PyAudio`, refer to the following sites and download the `whl` file according to your Python version and system and install using `pip install "path to the downloaded .whl file"`
> - `mysqlclient`: https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient
> - `PyAudio`: https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio


Before running `noterpy`, change the `MySQL` user credentials in `user_db.py` file according to your user setup

```python
try:
	import mysql.connector as mc
	connectMySQL = mc.connect(host='localhost', user='user_name', password='user_password')
except:
	print('module for mysql not setup\n')
	exit()
```

## Usage

To run `noterpy` on your system, either directly run `noter.py` file or

> Windows
```console
python noter.py
```

> Linux
```console
python3 noter.py
```

## License

MIT License
