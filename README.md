# kaggle_pll

## バックグラウンドでの動作
```
cd /notebooks
nohup ./pll_data_detection/do_notebook_by_cli.sh pll_data_detection/exp/exp001.ipynb &
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

