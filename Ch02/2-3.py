"""
    날짜 : 2020/07/22
    이름 : 이태훈
    내용 : 파이썬 HADOOP 실습하기
"""

from pywebhdfs.webhdfs import PyWebHdfsClient as hadoop

# hadoop 접속
hdfs = hadoop(host='192.168.100.101', port='50070', user_name='root')

# hdfs 디렉터리 생성
hdfs.make_dir('./sample')

# hdfs 파일생성
text = 'Hello Hadoop! 반갑습니다.'
hdfs.create_file('./sample/test.txt', text.encode('utf-8'), overwrite=True)
print('프로그램 종료...')