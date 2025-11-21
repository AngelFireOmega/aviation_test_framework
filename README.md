# Python API 測試框架範例

## 總覽

本專案是一個使用 `pytest` 和頁面物件模型（POM）模式的 Python API 測試框架範例。它示範了如何建構可擴展和可維護的自動化測試。
此專案的部分程式碼與文件由 Google Gemini 輔助生成

此框架包含針對以下 API 的測試套件：
- **Aviationstack API**：用於獲取航空和機場數據，特別是機場列表。

## 功能特性

- **結構化測試**：使用 API 客戶端類別（一種頁面物件模型）將測試邏輯與 API 請求的實作細節分離。
- **可讀性強的測試**：`pytest` 的 fixtures 和描述性的測試函數名稱使測試案例清晰易懂。
- **可維護性**：API 端點、URL 和參數都集中在各自的客戶端類別中，使未來的更新和維護更加容易。
- **擴充性**：此結構可以輕鬆地為其他 API 端點或服務新增客戶端類別和測試檔案。

## 專案結構

```
aviation_test_framework/
├── api/
│   ├── __init__.py
│   └── aviationstack_api.py
├── .env
├── requirements.txt
├── test_aviation.py
└── test_stock_price.py
```

## 設定與安裝

1.  **複製儲存庫**
    ```bash
    git clone <你的儲存庫位址>
    cd aviation_test_framework
    ```

2.  **建立虛擬環境 (推薦)**
    ```bash
    # Windows
    python -m venv venv
    .\venv\Scripts\activate

    # macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **安裝依賴套件**
    從 `requirements.txt` 檔案安裝所有必需的套件。
    ```bash
    pip install -r requirements.txt
    ```

## 如何執行測試

要執行所有測試並在終端機中查看詳細的 `print` 輸出，請從專案的根目錄執行以下命令：

```bash
pytest -s
```

## 已實作的測試案例

本框架包含以下針對 Aviationstack API 的測試案例：

| 測試檔案 | 測試案例 | 描述 |
| :--- | :--- | :--- |
| `test_aviation.py` | `test_get_airports_returns_200` | 驗證對 `/airports` 端點的請求。檢查 API 是否回傳 200 OK 狀態碼，並斷言回應中包含 100 個機場，且第一個機場為 "Anaa"。 |
| `test_aviation.py` | `test_get_countries_returns_100_with_200_ok` | 驗證對 `/countries` 端點的請求。檢查 API 是否回傳 200 OK 狀態碼，並斷言回應中包含 100 個國家，且第一個國家為 "Andorra"。 |
| `test_aviation.py` | `test_get_request_with_invalid_api_key` | 驗證當使用錯誤的 API 金鑰時，API 是否回傳 'invalid_access_key' 錯誤和 401 狀態碼。 |

---

