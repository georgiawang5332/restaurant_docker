from rest_framework.viewsets import ModelViewSet
# 在你的 View 中，請確保已正確設定認證和權限。例如：
from rest_framework.permissions import IsAuthenticated
from .models import MenuItem
from .permissions import IsAdminOrReadOnly  # 👈 引入自訂權限 ;放在 permissions.py
from django.shortcuts import render

from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer, MenuItemSerializer  # 從 serializers 引用

# Create your views here.
class MenuItemViewSet(ModelViewSet): #ModelViewSet: 自動支援 GET/POST/PUT/DELETE 全部 API。
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly] # # 👈 用自訂權限 ; ✅ 有登入（JWT）才能存取 API ; IsAuthenticated代表這個 API 只能讓已登入的使用者（有 JWT token）存取。
    # ❌ 不需要再加 get_permissions()，因為 IsAdminOrReadOnly 已處理邏輯

def index(request):
    return render(request, 'restaurant/index.html')

def login_page(request):
    return render(request, 'restaurant/login.html')

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
'''
📝 附註：IsAuthenticated 的檢查也已內含在 IsAdminOrReadOnly 中（因為你只有登入後才有 request.user）。
如果你之後想再動態控制不同權限，可以再用 get_permissions()，但目前這樣寫最清楚乾淨。

細分權限:
| 動作            | 一般登入者 | 管理員（is\_staff） |
| ------------- | ----- | -------------- |
| 查看（GET）       | ✅ 可以  | ✅ 可以           |
| 新增（POST）      | ❌ 不行  | ✅ 可以           |
| 編輯（PUT/PATCH） | ❌ 不行  | ✅ 可以           |
| 刪除（DELETE）    | ❌ 不行  | ✅ 可以           |

✅「前後端登入 + 權限控管」學習進度表
| 功能項目                     | 狀態        | 說明                                           |
| -----------------------      | ------    | -------------------------------------------- |
| Django JWT 認證設定           | ✅ 完成   | 成功透過 `/api/token/` 登入並取得 token。              |
| JWT 寫入 localStorage         | ✅ 完成   | 前端成功把 token 存在 localStorage。                 |
| AJAX 自動帶入 Authorization   | ✅ 完成   | 使用 `$.ajaxSetup()` 自動帶入 `Bearer <token>`。    |
| 未登入導向 login 頁面          | ✅ 完成   | 若 localStorage 沒有 token，自動導回 `login.html`。   |
| 登入頁面 (login.html)         | ✅ 完成   | 可輸入帳密，登入成功後導回主頁。                             |
| Django 自動建立 API（DRF）     | ✅ 完成   | 使用 `ModelViewSet` 成功建立 CRUD API。             |
| 設定 API 權限限制 (登入者)     | ✅ 完成   | 設定 `permission_classes = [IsAuthenticated]`。 |
| 細分權限：讀者 vs 管理員       | ✅ 完成   | 自訂權限 `IsAdminOrReadOnly`，一般人可讀、管理員可寫。        |
| 權限邏輯獨立為 permissions.py  | ✅ 完成   | 把細分權限類別獨立為模組，乾淨有條理。                          |
| 前端限制功能顯示（如刪除鍵）    | 🧩 未完成 | 前端依角色顯示或隱藏按鈕（例如刪除/編輯按鈕）。                     |
| 使用者註冊系統                 | 🧩 未完成 | 目前無提供「註冊」功能（需自行建立使用者）。                       |
| 登入狀態 UI 顯示              | 🧩 未完成 | 顯示目前登入的帳號名稱或登出按鈕。                            |
| 登出功能                      | 🧩 未完成 | 清除 localStorage 並導回登入頁。                      |

✅ 下一步建議
你現在核心功能 已完成 70~80%，可以依照下面順序繼續：

🔒 前端控制按鈕（依照登入者權限，隱藏刪除/新增按鈕）

🔐 登出功能（清除 token 並導回 login）

🙋‍♀️ 註冊新使用者功能（可選）

完成上面後，我們就能 進入 Docker 階段：

把整個 Django + PostgreSQL + Redis + RabbitMQ 包成容器化專案！
'''







