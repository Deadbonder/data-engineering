import pandas as pd
import sweetviz as sv
from sklearn.datasets import load_wine

df = load_wine(as_frame=True).frame  # 178 rows, 13 chemical features + target
report = sv.analyze(df)
report.show_html('report.html', open_browser=False)
