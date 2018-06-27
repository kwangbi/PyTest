# -*- coding: utf-8 -*-

from pyproj import Proj, transform
import numpy as np
import pandas  as pd

# Projection 정의
# UTM-K
proj_UTMK = Proj(init='epsg:5178') # UTM-K(Bassel) 도로명주소 지도 사용 중

# WGS1984
proj_WGS84 = Proj(init='epsg:4326') # Wgs84 경도/위도, GPS사용 전지구 좌표

# UTM-K -> WGS84 샘플
#x1, y1 = 961140.40958552,1946199.17184003
#x2, y2 = transform(proj_UTMK,proj_WGS84,x1,y1)
#print(x2,y2)

# WGS84 -> UTM-K 샘플
x1, y1 = 126.628998, 37.594590
x2, y2 = transform(proj_WGS84, proj_UTMK, x1, y1)

print(x2,y2)
