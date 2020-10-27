from collections import Counter
from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import numpy as np
from PIL import Image
import matplotlib
import pandas as pd
matplotlib.rcParams['font.family'] = "Maulgun Gothic"
font_path="C:/Windows/Fonts/NanumGothic.ttf"

instagram_tags = pd.read_csv('insta.csv')

stop_words = ['맞팔' , '주짓수', '부산대주짓수', '부산', '부산대']
instagram_tags = [word for word in instagram_tags if word not in stop_words]

count = Counter(instagram_tags)
common_tag_200 = count.most_common(200)

denne_mask = np.array(Image.open('cloud.png'))

wc = WordCloud(font_path=font_path, background_color="white", width=800, height=600, mask = denne_mask)
cloud = wc.generate_from_frequencies(dict(common_tag_200))
plt.figure(figsize = (20, 16))
plt.axis('off')
plt.imshow(cloud)


