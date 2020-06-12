__author__ = 'hwayoung kim'

import urllib.request
import urllib.parse
from time import sleep
import time
import os
import re

if __name__ == "__main__":
    now = time.localtime()
    timeString = "%04d%02d%02d_%02d%02d%02d" % (
        now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
    p = re.compile('.*[.]txt')

    imgForderName = 'QRIMG_' + timeString



    qrGenderUrl = "https://zxing.org/w/chart?cht=qr&chs=300x300&chld=L&choe=UTF-8&chl="

    fileList = os.listdir(os.getcwd())
    textFileList = []
    # print(fileList)
    print('##########################################################')
    print('######          QR 코드 생성 텍스트 파일 탐색        #####')
    print('##########################################################')
    print('txt확장자 탐색 ... ')
    for file in fileList:
        if p.match(file):
            print('Explored - ' + file)
            textFileList.append(file)

    print()
    if len(textFileList) == 0:
        print('대상파일이 없습니다. UTF-8 txt 파일을 생성하여 주십시오.')
        sleep(10)
    else :
        try:
            if not(os.path.isdir(imgForderName)):
                os.makedirs(os.path.join(imgForderName))
        except OSError as e:
            print("Failed to create directory!!!!!")
        print()
        for textFile in textFileList:
            os.makedirs(os.path.join(imgForderName + '/' + textFile))
            print('##########################################################')
            print('######          QR 코드 이미지 생성 준비중 ...       #####')
            print('##########################################################')
            print('fileName -- ' + textFile)
            print()
            f = open(textFile, mode='rt', encoding='utf-8')
            QRCodeList = f.read().split('\n')
            f.close()

            for QRCode in QRCodeList:
                if QRCode.strip() != '':
                    url = qrGenderUrl + urllib.parse.quote(QRCode)
                    fileName = QRCode.replace('/', '_').replace('\\', '_').replace(':', '_').replace('*', '_').replace(
                        '?', '_').replace('\'', '_').replace('\"', '_').replace('>', '_').replace('<', '_').replace('|', '_') + '.jpg'
                    urllib.request.urlretrieve(url, imgForderName + '/' + textFile + '/' + fileName)
                    print('Create QRCode : ' + fileName)
            print()
        print('QR코드 생성이 완료되었습니다.')
        print('파일이름의 특수문자는 제거되었으나 QR코드는 정상적입니다.')
        sleep(5)
