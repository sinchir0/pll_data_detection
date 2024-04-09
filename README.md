# kaggle_pll

```
# 不要なファイルを削除
rm -rf pll_data_detection/log

# S3へ避難する
cp -r /notebooks/pll_data_detection/trained_models /datasets/pii_bucket
```

## バックグラウンドでの動作
```
cd /notebooks
# 単発
nohup ./pll_data_detection/do_notebook_by_cli.sh pll_data_detection/exp/exp001.ipynb &
# 複数個(あらかじめ、mutiple_run.sh内に実行したいnotebookを記載する)
nohup ./pll_data_detection/multiple_run.sh &
```

## 動作確認
```
cd /notebooks
./pll_data_detection/do_notebook_by_cli.sh pll_data_detection/exp/exp001.ipynb
```

## 動いているかの確認
```
ps aux | grep python
```

## GitHubからのpull
```
cd pll_data_detection/
ssh-keygen -t ed25519 -C "s-saito@chic.ocn.ne.jp"
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
cat ~/.ssh/id_ed25519.pub
```

```
以下のリンクで、New SSH Keyを行う,keyの名前はpaperspace_YYMMDD
https://github.com/settings/keys
```

```
git pull origin main
# commitをする場合は以下も追加
git config --global user.email "s-saito@chic.ocn.ne.jp"
```

## git add, commit, push

```
git add -u
git config --global user.email "s-saito@chic.ocn.ne.jp"
git commit -m "add"
git push origin main
```

## メモリの確認
vmstat -t 2

### Ref
https://docs.github.com/ja/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent

## 実験管理のために
- 問題点: 日付が空くと何をしていたか忘れる、一度やった実験を何度もやってしまう
- 解決策
  - 1Notebook1実験(1要素しか変更しない)
  - ipynbのファイル名の最初に[ToDO], [Now], [Done]をつける
  - Notebookの最初に、このNotebookでの目的は何で、結果はどうなったかを書く

## 外部データセット
external_pii_dataset.csv
https://www.kaggle.com/competitions/pii-detection-removal-from-educational-data/discussion/469493

### punctuationを修正したバージョン
pii_dataset_fixed.csv
moredata_dataset_fixed.csv
https://www.kaggle.com/code/valentinwerner/fix-punctuation-tokenization-external-dataset/output

## nbconvertで変換した際に、ログに残るかどうか
- printで出力したものは残る
- notebookの一番最後に実行し、Notebookの機能で出力したものは残らない

## kaggle cliの利用方法

### 準備
```
mkdir -p ~/.kaggle/
cp /notebooks/pll_data_detection/kaggle.json ~/.kaggle/
chmod 600 ~/.kaggle/kaggle.json
```

```
pip install kaggle
```
