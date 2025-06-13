import pandas as pd
import folium
import seaborn as sns
import matplotlib.pyplot as plt

# 데이터 불러오기
import pandas as pd
import matplotlib.pyplot as plt

# 데이터 불러오기
df = pd.read_csv('/mnt/data/1.0_week.csv')

# 시간 형식 변환
df['time'] = pd.to_datetime(df['time'])

# 1. 시간별 지진 횟수
df.set_index('time', inplace=True)
daily_quakes = df['mag'].resample('D').count()

# 시각화
daily_quakes.plot(kind='bar', title='일별 지진 발생 수', figsize=(10, 5))
plt.xlabel('날짜')
plt.ylabel('지진 횟수')
plt.tight_layout()
plt.show()

# 2. 규모 분포 분석
df['mag'].hist(bins=20, edgecolor='black')
plt.title('지진 규모 분포')
plt.xlabel('규모')
plt.ylabel('빈도수')
plt.tight_layout()
plt.show()

# 3. 지역별 상위 지진 발생 지역
top_places = df['place'].value_counts().head(10)
print("가장 많이 발생한 상위 10개 지역:")
print(top_places)
