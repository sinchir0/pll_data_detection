# kaggle_pll

## バックグラウンドでの動作
```
nohup ./do_notebook_by_cli.sh ipynb/finetuning-mpnet-tripletloss-10man.ipynb &
```

## 動いているかの確認
```
ps aux | grep python
```

## 実験管理のために
- 問題点: 日付が空くと何をしていたか忘れる、一度やった実験を何度もやってしまう
- 解決策
  - 1Notebook1実験(1要素しか変更しない)
  - ipynbのファイル名の最初に[ToDO], [Now], [Done]をつける
  - Notebookの最初に、このNotebookでの目的は何で、結果はどうなったかを書く
