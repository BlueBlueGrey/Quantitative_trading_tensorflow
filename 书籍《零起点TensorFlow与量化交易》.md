# 第2章

## 2.1 金融数据源

CCXT

Https://github.com/cctxt/ccxt

《CCXT:神器级的数字货币万能API接口》 http://www.topquant.viip?p=394

### 2.1.1 TopDat金融数据集

### 量化分析与试错成本

## 2.2 OHLC金融数据格式

国际上，股票、期货等金融数据采用

格式  get_h_data函数返回

- 交易日期
- 开盘价
- 最高价
- 收盘价
- 最低价
- 成交量
- 成交金额

get_k_data 函数返回

- date
- open
- close
- high
- low
- volumn 成交量
- code 证券代码

## 2.3 K线图

## 2.4Tick数据格式

Tick Data 是指每一只股票的每一笔交易的数据。

调用TuShare中get_tick_data函数

- time 时间
- price 成交价格
- Change 价格变动
- volume 成交手
- amount 成交总金额
- type 买卖类型

### 2.4.1 Tick data 与分时数据装换

使用问题

- 数据过多
- 缺乏统一时间戳

有人尝试研究秒级的分时数据

在进行实盘分析时，一般需要先合成Tick数据，然后再转换成分时数据。

## 2.5 离线金融数据集

与前两小节一样

## TopDat 金融数据集的Tick数据

输出 True,表示存在数据文件，从文件当中的最后日期开始追加数据；如果为False,则表示数据文件不存在，从A股建市时即1994-01-01日期开始下载数据。

## 2.6.2 Tick数据与实时数据



# 第三章 无数据不量化（下）

## 3.1 均值优先

## 3.2多因子策略和泛因子策略

### 3.2.1多因子策略

### 3.2.2范因子策略

多因子策略结合更多的衍生数据扩展策略

通常使用dropnil命令清理掉NaN 无用的数据



价格曲线图，avg均值曲线，时间周期越长，曲线越平滑

## 3.3 “25日神定理”



每月25号以后，不参与任何交易。

### 案例3-3：时间因子

介绍如何拆分时间数据，把单一的时间数据扩展成更加专业的数据集。 扩展成更加专业的时间因子。

## 3-4 TA_Lib 金融指标

（多平台的金融市场）技术指标分析函数库。指数很多，用到在看吧

## 3.5 TQ智能量化回溯系统

## 3.6 全内存计算

## 3.7 股票池

## 3.8 TQ_bar全局变量类

## 3.9大盘指数

## 3.10TDS 数据集

P96 对数据集进行了介绍，



xavg(n) 次日均值 Y  

ma_(n)  移动平均线



Python df。max https://blog.csdn.net/tz_zs/article/details/81252710?utm_medium=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.channel_param&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.channel_param

### 3-14：TDS金融数据集的制作

### 3-15：TDS金融数据集2.0

# 第4章

## 4.1 TFLearn 简化接口

## 4.2 人工智能与统计关联度分析

## 4.3关联分析函数corr

```python
corr(DataFrame,P/K/S,min_periods=None)

```

- Perason 皮尔逊，https://blog.csdn.net/qq_30142403/article/details/82350628

  ![image-20201008152259161](/Users/bluegrey/Library/Application Support/typora-user-images/image-20201008152259161.png)

- ？ Spearman 斯伯曼 相关系数？

- ？ Kendall 肯德尔相关系数

## 4.4 open(开盘价)关联性分析

神经网络预测算法的本质，就是计算当前数据与未来数据的关联度。

预测n+1

### 4-1： open 关联度分析

介绍Pandas的关联分析函数corr,对OHLC数据进行关联性分析。



Pandas shift https://www.cnblogs.com/liulangmao/p/9301032.html





### 4-5 数值预测与趋势预测

eg: 把大盘、个股指数分为上涨、下跌和停滞三种状态，根据历史数据建立模型，然后将模型应用到模拟盘、实盘数据中，分析股票、个股的未来走势，至于具体的数值分析，通常可以使用回归算法模型。

#### 4.5.1数值预测

预测价格，提高投资策略的收益率。

传统预测算法：

- 简易平均法
- 移动平均法
- 指数平滑法
- 线性回归法



？ 不清楚数据表示



#### 4.5.2 趋势预测

预测上涨/下跌



### 案例4-2： ROC 股票变动率



ROC: 当天股价与一定的天数之前的某一天的股价比较变动速度的大小，来反映股票市场变动的快慢程度。





TA-Lib金融函数库zpd_talib.py 中已经有编写好的ROC函数

![image-20201010214400444](/Users/bluegrey/Library/Application Support/typora-user-images/image-20201010214400444.png)



python  diff 差

shift n-1 天前价格



- 交易日期
- 开盘价
- 最高价
- 收盘价
- 最低价
- 成交量
- 成交金额





%matplotlib inline 在 jupter notebook 里面画图



Axis=1 行模式，默认采用列模式



#### 4-3：ROC与交易数据分类

3.1 二选1



大于101 对应1上涨，否则0下跌

```python
df['ktype2']=df['price_change'].apply(zt.iff2type,d0=101,v1=1,v0=0) 
print(df['ktype2'].value_counts())
```

随机策略，未来10天价格会上涨1%,这个幅度对于短线交易而言已经很高了。不过，这并不代表这种策略会稳定获利。因为最终利润还需要考虑上涨、下跌的幅度，进行更加专业的回溯分析，才能获得最终的投资回报率计算结果。



4-