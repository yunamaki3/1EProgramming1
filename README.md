# 1EProgramming1 Info
<br>
## Kadai1**
**課題1 入力した整数が自然数か否かを判定するプログラムを作成せよ。**
入力値は整数であることから、入力値は整数型(int)となり、以下のコードが記述できる。
```python:Kadai1-1
#変数numに入力値のinputを整数型intに変換した値を代入する
num = int(input())
```
自然数（入力された値が1以上）か否かを判定すればいいのでif文を使用すればよい。
```python:Kadai1-2
#入力値変数numの値が1以上ならTrue、それ以外（0以下)ならFalseと出力する
if num>1:
  print("True")
else:
  print("False")
```
