# 高温ガス炉
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
print("abaaaaan")
def plot_rmse_order(input_file, sheet_name, row_range, col_range, output_file):
    # Excelファイルを読み込む（pandasで）
    df = pd.read_excel(input_file, sheet_name=sheet_name, engine="openpyxl")
    subset = df.iloc[row_range[0]:row_range[1], col_range[0]:col_range[1]]
    
    # NumPy配列に変換
    data = subset.to_numpy()
    print(data.shape)

    # 行番号をX軸に使う
    x = np.arange(data.shape[0])
    markers = ['o', '^', 'x']

    # 散布図を描く（各列を別々の系列として）
    for i in range(data.shape[1]):
        plt.scatter(x, data[:, i], label=f"Case{i+1}", marker=markers[i])

    plt.xlabel("order of expansion [-]", fontsize=14)
    plt.ylabel("RMSE [%]", fontsize=14)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)

    plt.grid(True, linewidth=0.5, color='gray', alpha=0.5)

    plt.legend(fontsize=12)
    plt.savefig(output_file)
    plt.close()

# 1回目のプロット
plot_rmse_order(
    input_file="C:/Users/urase-PC/Documents/epsilon.xlsx",
    sheet_name="epsilon",
    row_range=(22, 52),
    col_range=(7, 10),
    output_file="C:/Users/urase-PC/documents/GENESIS/HTTR/10%/9g/r2/rpv/POWER/RMSE_order.png"
)

# 2回目のプロット
plot_rmse_order(
    input_file="C:/Users/urase-PC/Documents/epsilon.xlsx",
    sheet_name="epsilon",
    row_range=(64, 94),
    col_range=(7, 10),
    output_file="C:/Users/urase-PC/documents/GENESIS/HTTR/lr/10%/9g/r2/rpv/POWER/RMSE_order.png"
)

# def plot_rmse_detector(input_file, sheet_name, row_range, col_range, output_file):
#     # Excelファイルを読み込む（pandasで）
#     df = pd.read_excel(input_file, sheet_name=sheet_name, engine="openpyxl")
#     subset = df.iloc[row_range[0]:row_range[1], col_range[0]:col_range[1]]
    
#     # NumPy配列に変換
#     data = subset.to_numpy()
#     print(data.shape)

#     # 行番号をX軸に使う
#     x = np.arange(data.shape[0])
#     markers = ['o', 's', 'x']

#     # 散布図を描く（各列を別々の系列として）
#     for i in range(data.shape[1]):
#         plt.scatter(x, data[:, i], label=f"Case{i+1}", marker=markers[i])

#     plt.xlabel("number of detector [-]")
#     plt.ylabel("RMSE [%]")
#     plt.grid(True)
#     plt.legend()
#     plt.savefig(output_file)
#     plt.close()
    
# # 1回目のプロット
# plot_rmse_detector(
#     input_file="C:/Users/urase-PC/Documents/epsilon.xlsx",
#     sheet_name="epsilon",
#     row_range=(55, 58),
#     col_range=(6, 10),
#     output_file="C:/Users/urase-PC/documents/GENESIS/HTTR/10%/9g/r2/rpv/POWER/RMSE_detector.png"
# )

# # 2回目のプロット
# plot_rmse_detector(
#     input_file="C:/Users/urase-PC/Documents/epsilon.xlsx",
#     sheet_name="epsilon",
#     row_range=(97, 100),
#     col_range=(6, 10),
#     output_file="C:/Users/urase-PC/documents/GENESIS/HTTR/lr/10%/9g/r2/rpv/POWER/RMSE_detector.png"
# )


def plot_rmse_detector(input_file, sheet_name, row_range, col_range, output_file):
    # Excelファイルを読み込む（pandasで）
    df = pd.read_excel(input_file, sheet_name=sheet_name, engine="openpyxl")
    subset = df.iloc[row_range[0]:row_range[1], col_range[0]:col_range[1]]
    
    # NumPy配列に変換
    data = subset.to_numpy()
    print(data)

    # 横軸（X軸）をデータセットの1列目に設定
    x = data[:, 0]  # 1列目（検出器の数）

    # 縦軸（Y軸）をデータセットの2列目以降に設定
    markers = ['o', '^', 'x']  # マーカーの種類

    # 散布図を描く（各列を別々の系列として、1列目はX軸、2列目以降はY軸）
    for i in range(1, data.shape[1]):  # 2列目から4列目まで処理
        plt.scatter(x, data[:, i], label=f"Case{i}", marker=markers[i-1])  # i-1 でマーカーを指定

    plt.xlabel("number of detector [-]", fontsize=14)
    plt.ylabel("RMSE [%]", fontsize=14)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    
    plt.xlim(left=0)

    # 薄いグリッド線
    plt.grid(True, linewidth=0.5, color='gray', alpha=0.5)

    # 凡例
    plt.legend(fontsize=12)
    
    # グラフの保存
    plt.savefig(output_file)
    plt.close()




# 1回目のプロット
plot_rmse_detector(
    input_file="C:/Users/urase-PC/Documents/epsilon.xlsx",
    sheet_name="epsilon",
    row_range=(54, 57),
    col_range=(2, 6),
    output_file="C:/Users/urase-PC/documents/GENESIS/HTTR/10%/9g/r2/rpv/POWER/RMSE_detector.png"
)

# 2回目のプロット
plot_rmse_detector(
    input_file="C:/Users/urase-PC/Documents/epsilon.xlsx",
    sheet_name="epsilon",
    row_range=(95, 98),
    col_range=(1, 5),
    output_file="C:/Users/urase-PC/documents/GENESIS/HTTR/lr/10%/9g/r2/rpv/POWER/RMSE_detector.png"
)

# def plot_rmse_k(input_file, sheet_name, row_range, col_range, output_file):
#     # Excelファイルを読み込む（pandasで）
#     df = pd.read_excel(input_file, sheet_name=sheet_name, engine="openpyxl")
#     subset = df.iloc[row_range[0]:row_range[1], col_range[0]:col_range[1]]
    
#     # NumPy配列に変換
#     data = subset.to_numpy()
#     print(data)

#     # 横軸（X軸）をデータセットの1列目に設定
#     x = data[:, 0]  # 1列目（検出器の数）

#     # 縦軸（Y軸）をデータセットの2列目以降に設定
#     markers = ['o', '^', 'x']  # マーカーの種類

#     # 散布図を描く（各列を別々の系列として、1列目はX軸、2列目以降はY軸）
#     for i in range(1, data.shape[1]):  # 2列目から4列目まで処理
#         plt.scatter(x, data[:, i], label=f"Case{i}", marker=markers[i-1])  # i-1 でマーカーを指定

#     plt.xlabel("normalization constant k [-]", fontsize=14)
#     plt.ylabel("RMSE [%]", fontsize=14)
#     plt.xticks(fontsize=12)
#     plt.yticks(fontsize=12)
print("A")
#     plt.xscale('log')
    
#     plt.xlim(left=0)

#     # 薄いグリッド線
#     plt.grid(True, linewidth=0.5, color='gray', alpha=0.5)

#     # 凡例
#     plt.legend(fontsize=12)
    
#     # グラフの保存
#     plt.savefig(output_file)
#     plt.close()

def plot_rmse_k_with_errorbars(input_file, sheet_name, row_range, col_range, output_file):
    # Excelからデータ読み込み
    df = pd.read_excel(input_file, sheet_name=sheet_name, engine="openpyxl")
    subset = df.iloc[row_range[0]:row_range[1], col_range[0]:col_range[1]]

    data = subset.to_numpy()
    print(data)

    # 値行と誤差行に分割（前半が値、後半が誤差）
    n_rows = data.shape[0] // 2
    values = data[:n_rows, :]
    errors = data[n_rows:, :]

    x = values[:, 0]
    y_values = values[:, 1:]
    y_errors = errors[:, 1:]

    markers = ['o', '^', 'x', 's', 'D']
    num_cases = y_values.shape[1]

    # シフト量（logスケールなので、乗算で調整）
    delta = 0.07  # x を ±3% ずらす（logスケールでもOKなように）

    for i in range(num_cases):
        shift = (i - (num_cases - 1)/2) * delta * x  # 中央を起点に±ずらす
        x_shifted = x + shift

        plt.errorbar(
            x_shifted, y_values[:, i], yerr=y_errors[:, i],
            fmt=markers[i % len(markers)], label=f"Case{i+1}", capsize=5
        )

    plt.xlabel("normalization constant k [-]", fontsize=14)
    plt.ylabel("RMSE [%]", fontsize=14)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.xscale('log')
    plt.xlim(left=0)

    plt.grid(True, linewidth=0.5, color='gray', alpha=0.5)
    plt.legend(fontsize=12)

    plt.savefig(output_file)
    plt.close()
    
# 1回目のプロット
plot_rmse_k_with_errorbars(
    input_file="C:/Users/urase-PC/Documents/epsilon.xlsx",
    sheet_name="epsilon2",
    row_range=(118, 126),
    col_range=(6, 10),
    output_file="C:/Users/urase-PC/documents/GENESIS/HTTR/10%/9g/r2/rpv/POWER/RMSE_k.png"
)

# 2回目のプロット
plot_rmse_k_with_errorbars(
    input_file="C:/Users/urase-PC/Documents/epsilon.xlsx",
    sheet_name="epsilon2",
    row_range=(101, 109),
    col_range=(6, 10),
    output_file="C:/Users/urase-PC/documents/GENESIS/HTTR/lr/10%/9g/r2/rpv/POWER/RMSE_k.png"
)

