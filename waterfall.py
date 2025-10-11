# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt

my_green = '#6a994e'
my_red = '#bc4749'

# 1. 读数据
df = pd.read_csv('data.csv')
df['gain'] = df['Price'] * df['Weight']

# 2. 累计收益
df['cum'] = df['gain'].cumsum()
df.reset_index(inplace=True)

# 3. 画图
plt.figure(figsize=(10, 6))
colors = [my_red if g >= 0 else my_green for g in df['gain']]

# 关键：left=前一累计，高度=当前gain
left = df['cum'] - df['gain']
plt.bar(df['index'], df['gain'], bottom=left,
        color=colors, edgecolor='black', linewidth=0.3)

# 4. 零轴
plt.axhline(0, color='black', linewidth=1)

# 5. 顶部大标题：总收益 or 总亏损
total = df['gain'].sum()
tag = "Totall Profit" if total >= 0 else "Total Loss"
plt.text(0.5, 0.5, f"{tag}: {total:+.2f} CNY", transform=plt.gca().transAxes,
         ha='center', va='top', fontsize=24, fontweight='bold',
         color=my_red if total >= 0 else my_green)

# 6. 收尾
plt.xlabel("Transaction Index")
plt.ylabel("Cumulative Gain")
# plt.title("Revenue Waterfall  (Price × Weight)")
plt.grid(axis='y', linestyle='--', alpha=0.4)
plt.tight_layout()
plt.savefig("waterfall.png", dpi=300)
plt.show()
