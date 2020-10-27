"""
날짜 : 2020/08/18
이름 : 이태훈
내용 : 텐서플로 1.x HelloWorld 실습
"""
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

# 그래프 생성
a = tf.Variable(1, name='a')
b = tf.Variable(2, name='b')
c = a + b

# 세션생성
sess = tf.Session()

# 그래프 변수 초기화
sess.run(tf.global_variables_initializer())

# 그래프 실행
result = sess.run(c)
print(result)

# 텐서플로 그래프 시각화(텐서보드)
tf.summary.FileWriter('log_5-2', graph=sess.graph)

# 세션 종료
sess.close()