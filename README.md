# kaggle_pll

## バックグラウンドでの動作
```
nohup ./do_notebook_by_cli.sh exp/exp001.ipynb &
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

### Ref
https://docs.github.com/ja/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent

## 実験管理のために
- 問題点: 日付が空くと何をしていたか忘れる、一度やった実験を何度もやってしまう
- 解決策
  - 1Notebook1実験(1要素しか変更しない)
  - ipynbのファイル名の最初に[ToDO], [Now], [Done]をつける
  - Notebookの最初に、このNotebookでの目的は何で、結果はどうなったかを書く
