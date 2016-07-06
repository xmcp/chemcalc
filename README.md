# ChemParser
计算原子量的有力工具 *（非清真）*

## 使用方法
用 chemparser 解释化学式：
```python
>>> import chemparser
>>> chemparser.parser.parse('Fe2(SO4)3')
<chemparser.Materials object at 0x02BC70D0>
>>> _.mats
{'S': 3, 'O': 12, 'Fe': 2}
```

用 chemcalc 计算分子量（支持带括号的四则运算）
```python
>>> import chemcalc
>>> chemcalc.parser.parse('304 * [Fe] / [FeSO4]')
112.0
```

## 附赠：良心™计算器
`LXcalc.py`

![screenshot](https://cloud.githubusercontent.com/assets/6646473/16622426/c2536d70-43cc-11e6-9440-801c87ce3819.png)

