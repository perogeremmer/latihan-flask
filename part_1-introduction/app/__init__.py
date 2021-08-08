from flask import Flask # Memanggil library Flask

app = Flask(__name__) # Untuk menjelaskan nama modul yang digunakan, sehingga ketika folder lain memanggil folder app akan otomatis teridentifikasi.

from app import routes # Memanggil file routes (akan segera dibuat)