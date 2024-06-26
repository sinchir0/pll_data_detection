# kaggle_pll

```
# 不要なファイルを削除
rm -rf pll_data_detection/log

# S3へ避難する
ls /datasets/pii_bucket
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
ssh-keygen -t ed25519 -C "<YOUR_EMAIL_ADDRESS>"
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
git config --global user.email "<YOUR_EMAIL_ADDRESS>"
```

## git add, commit, push

```
git add -u
git config --global user.email "<YOUR_EMAIL_ADDRESS>"
git commit -m "add"
git push origin main
```

## メモリの確認
```
vmstat -t 2
```

### Ref
https://docs.github.com/ja/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent

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
