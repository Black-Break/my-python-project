# my-python-project

一个用于演示 **GitHub Actions 自动化单元测试** 的最小 Python 项目。

## 项目结构

```
my-python-project/
├── .github/
│   └── workflows/
│       └── ci.yml          # GitHub Actions 工作流:推送/提PR时自动跑 pytest
├── calculator.py           # 被测试的代码(纯函数)
├── test_calculator.py      # pytest 单元测试
├── requirements.txt        # 项目依赖
├── .gitignore
└── README.md
```

## 本地运行测试

```bash
pip install -r requirements.txt
pytest -v
```

预期输出结尾会看到:

```
========================= 8 passed =========================
```

## 自动化测试工作流

`.github/workflows/ci.yml` 会在以下事件触发:

- `push`(推送到任意分支)
- `pull_request`(创建或更新 PR)

工作流共 4 步:

| 步骤 | 说明 |
| --- | --- |
| 检出代码 | `actions/checkout@v4` 把仓库代码拉到 runner |
| 设置Python | `actions/setup-python@v5` 配置 Python 3.11 环境(带 pip 缓存) |
| 安装依赖 | 升级 pip 并按 `requirements.txt` 安装 pytest |
| 运行测试 | 执行 `pytest -v`,任一用例失败则整体失败 |

## 如何判断结果

**测试通过 ✅**

- 仓库首页 / Actions 标签页显示绿色对勾
- 日志中出现 `===== PASSED =====` 与 `8 passed`

**测试失败 ❌**

- 状态显示红色叉号
- 日志中出现 `===== FAILED =====`,并指出失败用例名与断言差异
- 点击步骤可展开完整 traceback

## 演示:让测试失败

把 `calculator.py` 中的 `add` 故意写错:

```python
def add(a, b):
    return a * b   # 错误实现!
```

提交并推送后,工作流会变红,`test_add` 断言 `add(2, 3) == 5` 失败。
改回 `a + b` 再推送,即可恢复绿色对勾。