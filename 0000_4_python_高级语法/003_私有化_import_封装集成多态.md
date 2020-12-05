## 私有化

- xx： 共有变量
- _x: 单前置下划线，私有化属性或者方法， import 禁止导入，类对象和子类可以访问
- __xx: 双前置下划线，避免与子类中的属性命名冲突，无法在外部直接访问（名字重合所以访问不到）
- __xx__: 双前后下划线，用户名字空间的魔法对象或者属性，例如 __init__,不要自己发明这样的名字
- xx_: 单后置下划线，用于避免与python关键词冲突


## import

```python3
from xxx import yyy
import xxx
from xxx import *
import xxx,zzz
from xxx import yyy, zzz
import xxx as XYZ
```
### 重新导入(在不停止服务的情况下，重新启动)
```python3
from imp import reload

reload(somemodule)
```

## 多模块import注意的点

如果是全局变量，那么使用import module这么导入
如果使用from module import xxx, yyy, zzz 那么需要使用global

## 封装、继承、多态
