#!/bin/bash
pip install runnb

# 引数として受け取ったファイル名を確認
filename=$1

# ファイル名から接頭辞 'ipynb/' を削除
# base_name=${filename#ipynb/}

# ファイル名から拡張子を削除
# base_name=${base_name%.*}

# ファイル名を取得
base_name=$(basename "$filename" .ipynb)

# 実行
(time runnb --allow-not-trusted --to=${filename} ${filename}) > pll_data_detection/output_log/${base_name}-$(TZ=JST-9 date +"%Y%m%d%H%M%S").txt 2>&1
# (time runnb --allow-not-trusted --to=${filename} ${filename}) > output_log/tst.txt 2>&1