__author__ = 'hwayoung kim'

import urllib.request
import urllib.parse
from time import sleep
import time
import os
import re

qr_height = 400
qr_width = 400

source_dir = os.getcwd() + "/source"

if __name__ == "__main__":

    # 현재 시간 출력
    # format : 20200612_180125 (년도, 월, 일 _ 시간, 분, 초)
    curr_datetime = time.localtime()
    timeString = "%04d%02d%02d_%02d%02d%02d" % (
        curr_datetime.tm_year, curr_datetime.tm_mon, curr_datetime.tm_mday,
        curr_datetime.tm_hour, curr_datetime.tm_min, curr_datetime.tm_sec
    )

    # 인식할 파일 정규식 표현 (*.txt)
    file_format = re.compile('.*[.]txt')

    # QR코드 출력 될 dir
    image_directory_name = 'dist/QRIMG_' + timeString

    # 크기 300 X 300으로 고정, 조정 가능
    qrcode_generator_url = "https://zxing.org/w/chart?" \
                           "cht=qr&" \
                           "chs=" + str(qr_width) + 'x' + str(qr_height) + "&chld=L&choe=UTF-8&chl="

    print('##########################################################')
    print('######          QR 코드 생성 텍스트 파일 탐색        #####')
    print('##########################################################')
    print('txt확장자 탐색 ... ')

    # 파일 리스트 조회
    file_list = os.listdir(source_dir)
    text_file_list = [file for file in filter(lambda x: file_format.match(x), file_list)]
    # for file in file_list:
    #     # 정규형에 맞는 파일 확인
    #     if file_format.match(file):
    #         print('Explored - ' + file)
    #         text_file_list.append(file)

    print()
    if len(text_file_list) == 0:
        print('대상파일이 없습니다. UTF-8 txt 파일을 생성하여 주십시오.')
        sleep(10)
    else:
        # DIR 생성
        try:
            if not (os.path.isdir(image_directory_name)):
                os.makedirs(os.path.join(image_directory_name))
        except OSError as e:
            print("Failed to create directory!!!!!")
        print()
        for text_file in text_file_list:
            # txt파일 명으로 dir 생성
            os.makedirs(os.path.join(image_directory_name + '/' + text_file))
            print('##########################################################')
            print('######          QR 코드 이미지 생성 준비중 ...       #####')
            print('##########################################################')

            print('fileName -- ' + text_file)
            print()
            fileIO = open(source_dir + "/" + text_file, mode='rt', encoding='utf-8')
            QRCodeList = fileIO.read().split('\n')
            fileIO.close()

            for QRCode in QRCodeList:
                if QRCode.strip() != '':
                    url = qrcode_generator_url + urllib.parse.quote(QRCode)

                    # 파일명에서 일부 특수문자 _로 replace (\, /, :, *, ?, ', ", >, <, |")
                    fileName = QRCode.replace('/', '_') \
                                   .replace('\\', '_') \
                                   .replace(':', '_') \
                                   .replace('*', '_') \
                                   .replace('?', '_') \
                                   .replace('\'', '_') \
                                   .replace('\"', '_') \
                                   .replace('>', '_') \
                                   .replace('<', '_') \
                                   .replace('|', '_') + '.png'

                    # 이미지 파일 URL로 다운로드 (상대경로)
                    urllib.request.urlretrieve(url, image_directory_name + '/' + text_file + '/' + fileName)
                    print('Create QRCode : ' + fileName)
            print()
        print('QR코드 생성이 완료되었습니다.')
        print('파일이름의 특수문자는 제거되었으나 QR코드는 정상적입니다.')
        sleep(5)
