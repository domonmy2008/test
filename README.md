# 计算器项目

一个简单的Python计算器模块，提供基本的数学运算功能。

## 功能特性

这个计算器模块支持以下运算：

- **加法** (`add`) - 两个数相加
- **减法** (`subtract`) - 两个数相减
- **乘法** (`multiply`) - 两个数相乘
- **除法** (`divide`) - 两个数相除（包含除零检查）
- **幂运算** (`power`) - 计算a的b次方
- **模运算** (`modulo`) - 计算两个数相除的余数（包含除零检查）
- **平方根** (`sqrt`) - 计算一个数的平方根（包含负数检查）

## 项目结构

```
.
├── calculator.py          # 计算器模块实现
├── test_calculator.py     # 单元测试
└── README.md             # 项目说明文档
```

## 如何使用

### 导入模块

```python
from calculator import add, subtract, multiply, divide, power, modulo, sqrt

# 使用示例
result = add(10, 5)        # 15
result = subtract(10, 5)   # 5
result = multiply(10, 5)   # 50
result = divide(10, 5)     # 2.0
result = power(2, 3)       # 8
result = modulo(10, 3)     # 1
result = sqrt(16)          # 4.0
```

## 运行测试

确保你已经安装了Python 3，然后在项目目录下运行：

```bash
python3 test_calculator.py
```

或者使用pytest（如果已安装）：

```bash
pytest test_calculator.py -v
```

## 测试覆盖

测试文件 `test_calculator.py` 包含了所有函数的单元测试，包括：

- 基本运算的正确性测试
- 边界条件测试（如零值、负数）
- 异常处理测试（如除零错误）

所有测试应该全部通过。

## 环境要求

- Python 3.6 或更高版本
- 标准库依赖：`unittest`（测试）、`math`（平方根运算）

## 许可证

本项目仅用于学习和测试目的。
