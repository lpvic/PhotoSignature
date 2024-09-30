from pathlib import Path
from photosignature import sign_svg


sign_svg(Path(r'aaaaa.svg'), Path(r'DSC_3165.JPG'), title='Berrea 2024', signature='Luis Pedro Vicente Matilla',
         color='000000')
