## 【説明】
コンテキストメニューに機能を追加します。
本ツールを使用することで任意のファイルに日付、日付と時間を追加することができます。

## 【手順】
### 1. レジストリエディタに情報を追加
以下ファイルをクリックし、レジストリエディタに情報を追加します。

- AddDateToFile.reg
- AddDateTimeToFile.reg

※ "情報を追加すると、..." と表示されるが、「はい(Y)」を押して続行します。

### 2. レジストリエディタに情報を修正
以下の場所に新しいキーが作成されていることを確認します。
```HKEY_CLASSES_ROOT\*\shell```

- AddDateToFile
- AddDateTimeToFile

各キーの (既定) を以下のように修正します。

- AddDateToFile：
```ファイル名に日付を追加```

- AddDateTimeToFile
```ファイル名に日付と時間を追加```


各キーの下にコマンドキー ```command``` の (既定) を以下のように修正します。

- AddDateToFile：
```"C:\path\to\add_date_to_filename.exe" "%1"```

- AddDateTimeToFile
```"C:\path\to\add_date_to_filename.exe" "%1" --time```

※ ```C:\path\to\add_date_to_filename.exe``` は配布された .exe ファイルのフルパスに置き換えが必要です。


### 3. 動作確認
任意のファイルを右クリックし、「ファイル名に日付を追加」をクリックします。
ファイル名が変更されることが確認できます。
```例: example.txt → 20250122_example.txt```

※ 複数ファイルに対しても実行可能です。
