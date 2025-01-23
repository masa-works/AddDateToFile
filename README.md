## 【説明】
コンテキストメニューに機能を追加します。  
本ツールを使用することで任意のファイルに日付、日付と時間を追加することができます。

## 【手順】
### 1. レジストリエディタに情報を追加
以下ファイルをクリックし、レジストリエディタに情報を追加します。

- AddDateToFile.reg
- AddDateTimeToFile.reg
- AddDateToFolder.reg
- AddDateTimeToFolder.reg

※ "情報を追加すると、..." と表示されるが、「はい(Y)」を押して続行します。

### 2. レジストリエディタに情報を修正
レジストリエディタを開きます。  
Win + R を押して ```regedit``` と入力して Enter を押します。

以下の場所に新しいキーが作成されていることを確認します。  
```HKEY_CLASSES_ROOT\*\shell```  
- AddDateToFile
- AddDateTimeToFile

```HKEY_CLASSES_ROOT\Directory\shell```  
- AddDateToFolder
- AddDateTimeToFolder

各キーの (既定) に以下のような文字列が登録されていることを確認します。  
※ 任意の文字列に変更が可能です。

```HKEY_CLASSES_ROOT\*\shell```  
- AddDateToFile：
```ファイル名に日付を追加```
- AddDateTimeToFile
```ファイル名に日付と時間を追加```

```HKEY_CLASSES_ROOT\Directory\shell```  
- AddDateToFolder
```フォルダ名に日付を追加```
- AddDateTimeToFolder
```フォルダ名に日付と時間を追加```

各キーの下にコマンドキー ```command``` の (既定) を以下のように修正します。

```
C:\path\to\add_date_to_filename.exe
↓
配布された .exe ファイルのフルパスに置き換える

例: C:\Users\username\Downloads\AddDateToX\main.exe
```

```HKEY_CLASSES_ROOT\*\shell```  
- AddDateToFile：
```"C:\path\to\add_date_to_filename.exe" "%1"```
- AddDateTimeToFile
```"C:\path\to\add_date_to_filename.exe" "%1" --time```

```HKEY_CLASSES_ROOT\Directory\shell```  
- AddDateToFolder
```"C:\path\to\add_date_to_filename.exe" "%1" --folder```
- AddDateTimeToFolder
```"C:\path\to\add_date_to_filename.exe" "%1" --folder --time```

### 3. 動作確認
任意のファイル/フォルダを右クリックし、「ファイル名に日付を追加」/「フォルダ名に日付を追加」をクリックします。
ファイル/フォルダ名が変更されることが確認できます。
```
例: example.txt → 20250122_example.txt
    example_folder → 20250122_example_folder
```

※ 複数ファイル/フォルダに対しても実行可能です。
