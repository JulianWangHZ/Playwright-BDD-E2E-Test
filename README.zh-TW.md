# TransGlobal 網頁自動化測試套件

> 🌐 本文件亦提供 [English version](README.md)。

一套採用 **Playwright** 與 **pytest-bdd** 技術棧構建的企業級端對端測試框架，專為確保 [TransGlobal](https://www.transglobalus.com/) 網頁平台的品質與可靠性而設計。本框架基於現代瀏覽器自動化原則，實作 Page Object Model 架構與行為驅動開發方法論，實現可維護、可擴展且穩健的測試自動化。框架充分運用 Playwright 的智慧型自動等待機制，有效消除不穩定測試，並提供與 Playwright MCP 的無縫整合，加速測試開發流程並支援互動式除錯工作流程。

---

## 📑 目錄

1. [專案概覽](#-專案概覽)
2. [架構設計](#-架構設計)
3. [技術棧](#-技術棧)
4. [核心功能](#-核心功能)
5. [快速開始](#-快速開始)
6. [安裝指南](#-安裝指南)
7. [執行測試](#-執行測試)
8. [Playwright MCP 整合](#-playwright-mcp-整合)
9. [開發指南](#-開發指南)
10. [最佳實踐](#-最佳實踐)
11. [故障排除](#-故障排除)

---

## 🎯 專案概覽

本測試自動化框架旨在確保 TransGlobal 網頁平台的品質與可靠性，涵蓋多項關鍵服務的使用者流程，包括房地產、貸款、保險、投資和稅務服務。

### 目標應用程式
- **網站**: [https://www.transglobalus.com/](https://www.transglobalus.com/)
- **測試重點**: 使用者介面驗證、跨瀏覽器相容性、響應式設計測試、關鍵業務流程

---

## 🏗️ 架構設計

### 設計模式
- **Page Object Model (POM)**: 封裝頁面特定邏輯與定位器
- **行為驅動開發 (BDD)**: 使用 Gherkin 語法撰寫測試情境
- **Fixture 基礎測試結構**: 可重用的測試 fixture 用於通用設定/清理
- **定位器管理**: 在專用類別中集中管理定位器定義

### 專案結構
```
Playwright-BDD-E2E-Test/
├── config/              # 配置與設備設定檔
│   ├── config.py        # 主要配置設定
│   └── devices/         # 設備模擬設定檔
├── locators/            # 頁面定位器定義
├── pages/               # Page Object 類別
│   └── base_actions/    # 基礎操作工具
├── features/            # BDD 功能檔案 (.feature)
├── tests/               # 測試步驟定義
│   └── steps/          # 步驟實作檔案
├── utils/               # 工具函數
├── conftest.py         # Pytest 配置與 fixtures
└── pytest.ini          # Pytest 設定
```

---

## 🛠️ 技術棧

| 組件 | 技術 | 版本 |
|------|------|------|
| **測試框架** | pytest | 8.0.2+ |
| **BDD 框架** | pytest-bdd | 6.1.1+ |
| **瀏覽器自動化** | Playwright | 1.40.0+ |
| **程式語言** | Python | 3.13+ |
| **測試報告** | pytest-html, allure-pytest | Latest |
| **平行執行** | pytest-xdist | 3.5.0+ |
| **重試機制** | pytest-rerunfailures | 12.0+ |

---

## ✨ 核心功能

### 1. **Playwright 驅動的自動化**
- **自動等待**: 自動元素等待機制消除不穩定的測試
- **多瀏覽器支援**: Chromium、Firefox 和 WebKit (Safari)
- **網路攔截**: 進階的網路請求/回應處理
- **截圖與錄影**: 失敗時自動截圖與錄影

### 2. **多設備測試**
- **設備設定檔**: 預設的桌面、平板和手機設備配置
- **自訂設備**: 輕鬆新增新的設備配置
- **視窗管理**: 自動視窗大小和使用者代理設定

### 3. **BDD 測試結構**
- **Gherkin 語法**: 人類可讀的測試情境
- **步驟重用**: 跨功能共享步驟定義
- **標籤執行**: 使用標籤組織和過濾測試

### 4. **專業測試基礎設施**
- **平行執行**: 使用 `pytest-xdist` 平行執行測試
- **重試機制**: 自動重試不穩定的測試
- **豐富報告**: 帶截圖的 HTML 和 Allure 報告
- **CI/CD 就緒**: 支援 headless 模式用於持續整合

### 5. **Playwright MCP 整合**
- **快速測試開發**: 使用 Playwright MCP 快速生成測試腳本
- **互動式除錯**: 即時瀏覽器互動進行故障排除
- **程式碼生成**: 直接從瀏覽器操作生成定位器和測試程式碼

---

## 🚀 快速開始

### 前置需求

- **Python**: 3.13 或更高版本
- **Node.js**: 18+ (用於 Playwright MCP 整合)
- **Playwright 瀏覽器**: 透過 `playwright install` 自動安裝

### 安裝步驟

1. **複製儲存庫**
```bash
git clone <repository-url>
cd Playwright-BDD-E2E-Test
```

2. **建立虛擬環境**
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

3. **安裝依賴套件**
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

4. **安裝 Playwright 瀏覽器**
```bash
playwright install
# 或安裝特定瀏覽器:
playwright install chromium firefox webkit
```

---

## 🎬 執行測試

### 基本測試執行

```bash
# 執行所有測試
pytest

# 執行特定標籤的測試
pytest -m "bdd"

# 執行特定測試檔案
pytest tests/test_home_page.py

# 詳細輸出模式
pytest -v
```

### 瀏覽器選擇

```bash
# 使用 Chromium (預設)
pytest --browser=chromium

# 使用 Firefox
pytest --browser=firefox

# 使用 WebKit (Safari)
pytest --browser=webkit
```

### 設備模擬

```bash
# 桌面 (預設)
pytest --device=desktop

# iPhone 17 Pro Max
pytest --device=iphone17promax

# iPhone 17
pytest --device=iphone17

# iPad Pro
pytest --device=ipadpro

# Google Pixel 9 Pro
pytest --device=pixel9pro
```

### 進階選項

```bash
# Headless 模式
pytest --headless

# 平行執行 (3 個工作進程)
pytest -n 3

# 重試失敗的測試 (2 次重試)
pytest --reruns 2

# 組合選項
pytest -m "bdd" \
  --browser=chromium \
  --device=iphone17 \
  --headless \
  --reruns=2 \
  -n 4 \
  -v
```

### 環境配置

```bash
# 設定環境 (dev, staging, prod)
pytest --env=staging

# 或使用環境變數
export ENV=staging
pytest
```

---

## 🎭 Playwright MCP 整合

### 設定

1. **安裝 Playwright MCP**
```bash
pnpm add -D @playwright/mcp
# 或
npm install --save-dev @playwright/mcp
```

2. **在 Cursor 中配置 MCP**
在 `~/.cursor/mcp.json` 中加入：
```json
{
  "playwright": {
    "command": "npx",
    "args": ["@playwright/mcp@latest"]
  }
}
```

### 使用指南

1. **測試開發流程**
   - 使用 Playwright MCP 互動式探索 TransGlobal 網站
   - 直接從瀏覽器操作生成定位器和測試程式碼
   - 在撰寫測試情境前驗證 UI 元素

2. **最佳實踐**
   - 在導航前說明目標網址和目的
   - 嚴格按照功能檔案中的步驟執行
   - 在關鍵操作後捕獲 UI 狀態
   - 以 `Navigate → Actions → Verification` 格式回報結果

### 官方資源

- [Playwright 文件](https://playwright.dev/)
- [Playwright GitHub](https://github.com/microsoft/playwright)
- [Cursor MCP 指南](https://cursor.sh/docs/mcp)

---

## 📚 開發指南

### 1. 新增設備設定檔

1. 在 `config/devices/` 建立新的設備類別：
```python
# config/devices/custom_device.py
from .base_device import BaseDevice

class CustomDevice(BaseDevice):
    def __init__(self):
        super().__init__()
        self.name = "自訂設備"
        self.width = 1920
        self.height = 1080
        self.pixel_ratio = 2.0
        self.user_agent = "Mozilla/5.0 ..."
```

2. 在 `conftest.py` 中註冊：
```python
def get_device_class(device_type: str) -> BaseDevice:
    devices = {
        # ... 現有設備
        "custom": CustomDevice
    }
```

### 2. 建立 Page Object

1. **定義定位器** (`locators/home_page_locators.py`):
```python
from playwright.sync_api import Page, Locator

class HomePageLocators:
    """TransGlobal 首頁定位器，使用 Playwright Locator 對象"""
    
    def __init__(self, page: Page):
        # 優先使用 Playwright 語義化定位器
        # 定位器屬性名稱使用大寫
        self.SERVICES_MENU = page.get_by_test_id('services-menu')
        self.CONTACT_BUTTON = page.locator('[data-testid="contact-button"]')
        self.LANGUAGE_SWITCHER = page.get_by_role('button', name='Language')
```

2. **建立 Page Object** (`pages/home_page.py`):
```python
from pages.base_actions.base_action import BaseAction
from locators.home_page_locators import HomePageLocators
from playwright.sync_api import Page

class HomePage(BaseAction):
    def __init__(self, page: Page):
        super().__init__(page)
        # 使用 page 實例初始化定位器 - 使用頁面特定名稱以提高可讀性
        self.home_locators = HomePageLocators(page)
    
    def navigate_to_services(self):
        # 使用 locators 實例 - 定位器屬性名稱使用大寫
        self.click_element(self.home_locators.SERVICES_MENU)
    
    def switch_language(self, language: str):
        self.click_element(self.home_locators.LANGUAGE_SWITCHER)
        # 語言選擇的額外邏輯
```

### 3. 撰寫 BDD 測試

1. **功能檔案** (`features/home_page.feature`):
```gherkin
Feature: TransGlobal 首頁
  作為使用者
  我想要瀏覽 TransGlobal 網站
  以便我可以存取各種服務

  @home_page @smoke
  Scenario: 使用者可以存取首頁
    Given 我導航到 TransGlobal 首頁
    When 我檢視頁面內容
    Then 我應該看到主要導航選單
    And 我應該看到服務區塊
```

2. **步驟定義** (`tests/test_home_page.py`):
```python
from pytest_bdd import given, when, then, scenarios
from pages.home_page import HomePage

scenarios("../features/home_page.feature")

@given("我導航到 TransGlobal 首頁")
def navigate_to_home_page(page):
    home_page = HomePage(page)
    home_page.open_url()
    home_page.wait_for_loaded()

@when("我檢視頁面內容")
def view_page_content(page):
    # 頁面已在先前步驟載入
    pass

@then("我應該看到主要導航選單")
def verify_navigation_menu(page):
    home_page = HomePage(page)
    assert home_page.is_navigation_menu_visible()

@then("我應該看到服務區塊")
def verify_services_section(page):
    home_page = HomePage(page)
    assert home_page.is_services_section_visible()
```

---

## 💡 最佳實踐

### 定位器策略
- **優先使用穩定選擇器**: 可用時使用 `data-testid` 屬性
- **語義定位器**: 利用 `get_by_role()`, `get_by_text()`, `get_by_label()`
- **集中管理**: 將所有定位器存放在 `locators/` 套件中
- **字串格式**: 使用前綴格式 (`test_id:`, `css:`, `xpath:`) 以提高清晰度

### 測試設計
- **每個測試一個斷言**: 保持測試專注且可維護
- **Page Object 模式**: 將頁面邏輯封裝在 Page Objects 中
- **可重用步驟**: 跨功能共享通用步驟定義
- **有意義的名稱**: 為測試和步驟使用描述性名稱

### Playwright 自動等待
- **利用自動等待**: 操作前無需明確等待
- **操作自動等待**: `click()`, `fill()`, `type()` 自動等待
- **讀取操作自動等待**: `inner_text()`, `input_value()` 等待可見性
- **狀態檢查**: 使用 `is_visible()` 進行立即檢查，`wait_for()` 用於斷言

### 程式碼品質
- **遵循 PEP8**: 保持一致的程式碼風格
- **DRY 原則**: 避免程式碼重複
- **SOLID 原則**: 設計可維護、可擴展的程式碼
- **文件**: 為所有公開方法包含文件字串

---

## 🔧 故障排除

### 常見問題

#### 1. 找不到瀏覽器
```bash
# 安裝缺少的瀏覽器
playwright install chromium
playwright install firefox
playwright install webkit
```

#### 2. 超時錯誤
- 在 `config/config.py` 中增加超時: `DEFAULT_TIMEOUT`
- 檢查與 TransGlobal 網站的網路連線
- 驗證元素定位器是否正確

#### 3. 找不到元素
- 使用 Playwright MCP 驗證定位器
- 檢查元素是否在 iframe 中 (使用 `frame_locator()`)
- 確保元素可見 (未被 CSS 隱藏)

#### 4. Headless 模式問題
- 某些功能在 headless 模式下可能行為不同
- 使用 `--headless=false` 進行除錯
- 檢查瀏覽器主控台日誌中的錯誤

### 除錯模式

```bash
# 使用除錯輸出執行
pytest --log-cli-level=DEBUG

# 使用 Playwright 除錯模式
PWDEBUG=1 pytest

# 執行特定測試並顯示詳細輸出
pytest tests/test_home_page.py::test_specific_scenario -v -s
```

### 截圖與錄影

測試失敗時會自動捕獲截圖並儲存到 `screenshots/` 目錄（可透過 config 中的 `SCREENSHOT_PATH` 配置）。

---

## 📊 測試執行範例

### 平行執行矩陣

| 情境 | 指令 |
|------|------|
| 平行執行所有 BDD 測試 | `pytest -m bdd -n 4` |
| 執行特定功能 | `pytest tests/test_home_page.py -n 2` |
| 關鍵字過濾 | `pytest -k "navigation" -n 3` |
| 瀏覽器 + 設備矩陣 | `pytest --browser=chromium --device=iphone17 -n 2` |
| 重試失敗測試 | `pytest --last-failed --reruns 2` |

### CI/CD 整合

```yaml
# GitHub Actions 工作流程範例
- name: 執行 E2E 測試
  run: |
    pip install -r requirements.txt
    playwright install --with-deps chromium
    pytest --headless -n 4 --html=report.html
```

---

## 📝 配置

### 環境變數

建立 `.env` 檔案 (參考 `.env.example`):

```env
# 瀏覽器配置
BROWSER=chromium
HEADLESS=false

# 超時設定
DEFAULT_TIMEOUT=20
POLL_FREQUENCY=0.5

# 環境
ENV=staging

# 日誌
LOG_LEVEL=INFO
SCREENSHOT_PATH=screenshots
```

### 命令列選項

```bash
# 瀏覽器選擇
--browser {chromium,firefox,webkit}

# 設備模擬
--device {desktop,iphone17promax,iphone17,ipadpro,pixel9pro}

# 執行模式
--headless          # Headless 模式執行
--env {dev,staging,prod}  # 設定環境

# 測試選擇
-m MARKER           # 執行帶有標籤的測試
-k KEYWORD          # 執行符合關鍵字的測試
```

---

## 📄 授權

本專案採用 MIT License 授權 - 詳見 [LICENSE](LICENSE) 檔案。

---

## 🙏 致謝

- [Playwright](https://playwright.dev/) - 現代瀏覽器自動化
- [pytest](https://docs.pytest.org/) - 測試框架
- [pytest-bdd](https://pytest-bdd.readthedocs.io/) - pytest 的 BDD

---

**祝測試順利！** 🚀

如有問題或問題，請在儲存庫中開啟 issue。
