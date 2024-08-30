# 使用說明

這個程式允許你設置自定義的按鍵組合。

## 安裝步驟

1. 安裝所需的 Python 套件：
   ```
   pip install pynput
   ```

## 使用方法

1. 下載 `skill2.py` 和 `Config.json` 文件，並將它們放在同一個文件夾中。

2. 根據你的需求編輯 `Config.json` 文件。你可以修改：
   - 觸發鍵（`trigger_key`）
   - 按鍵序列（`sequence`）
   - 組合名稱（`name`）
   - 延遲時間範圍（`delay`）

3. 運行 Python 腳本：
   ```
   python skill2.py
   ```

4. 程式運行後，按下你在 `Config.json` 中定義的觸發鍵，對應的按鍵序列就會自動執行。

## 配置文件說明

`Config.json` 文件的結構如下：

```json
{
  "combos": [
    {
      "name": "組合名稱",
      "trigger_key": "觸發鍵",
      "sequence": ["按鍵1", "按鍵2", "按鍵3", ...]
    },
    ...
  ],
  "delay": {
    "min": 最小延遲時間,
    "max": 最大延遲時間
  }
}
```

- `name`: 為你的按鍵組合取一個容易記住的名字
- `trigger_key`: 設置觸發這個組合的按鍵
- `sequence`: 定義要執行的按鍵序列
- `delay`: 設置按鍵之間的隨機延遲範圍（單位：秒）

## 注意事項

- 請確保不要將此程式用於違反遊戲規則或其他不當用途。
