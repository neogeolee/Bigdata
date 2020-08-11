"""
    날짜 : 2020/07/22
    이름 : 이태훈
    내용 : 파이썬 Hadoop 실습하기
"""

from pywebhdfs.webhdfs import PyWebHdfsClient as hadoop

# Hadoop 접속
hdfs = hadoop(host='192.168.100.101', port='50070', user_name='root')

# Local /home/bigdata/naver/naver-20-xx-xx 를 hadoop /naver/ 복사
hdfs.make_dir('./naver')
# Local의 /home/bigdata/naver/naver-20-xx-xx를 삭제
# 프로그램 종료