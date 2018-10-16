# First Lesson
## 字符串
### string.title() 单词首字母大写
### string.strip() 去除变量两侧的空白符
空白符包括空格、换行、制表符等，包括两个相同的方法：
- `string.lstrip()` 去除左侧的空白符
- `string.rstrip()` 去除右侧的空白符

## 列表
列表由一系列按特定顺序排列的元素组成。用方括号`[]`表示列表。
### `list.append(item)` 在列表尾部插入元素
### `list.insert(index)` 在列表任何位置插入元素
### `del list[index]` 从列表中删除某个元素
### `list.pop(index?)` 从列表尾部弹出某个元素
可以使用`list.pop()`删除列表中最后一项的元素，但是，可以传入位置参数，这样可以删除列表任何位置的元素。和del的区别是，这个弹出会返回弹出的元素，可以访问到，而del语句是直接删除。
### `list.remove(item)` 根据元素删除list的项
当不知道元素在list中的索引的时候，就可以使用remove来根据列表元素来删除。
### `list.sort()` 永久排序 `list.sorted()` 临时排序
默认按照字母顺序排序，可以传入`reserve=True`来反转顺序。两者的差别是排序的作用对象：
- `list.sort()` 是永久排序，列表本身被替换为排序后的列表。
- `list.sorted()` 是临时排序，返回排序后的列表。列表本身不受影响。

### `list.reverse()` 倒序排列列表
倒序排列列表，作用于本身，不做排序，只是顺序的反向。
### `len(list)` 获得列表的长度
### `for ... in` 遍历列表
`for ... in`循环建立临时变量，从列表中拿取当前的值放入临时变量中，以冒号开始循环体，以缩进结束循环体：
```python
bicycles = ['trek', 'redBic', 'canNodale']

print('start')

for item in bicycles:
    print('item:' + str(item) + '\n')

print('end')
```
## Number数字
### `range()` 生成一系列数字
调用参数：`range(start, stop[, step])`，需要传递初始值、结束值、步长（默认为1）。
```python
for value in range(1, 50, 10):
    print('\tvalue: ' + str(value) + '\n')
# 1 11 21 31 41
```


