#   第2章

## 2.1 金融数据源

CCXT

Https://github.com/cctxt/ccxt

《CCXT:神器级的数字货币万能API接口》 http://www.topquant.viip?p=394

### 2.1.1 TopDat金融数据集

### 

A股目录： cn/day/

A股指数目录： cn/xday

A股索引参数文件目录：inx/

A股分时目录： min/

A股Tick 目录：tick/

A股实时数据目录： real



### 2.1.2 量化分析与试错成本



## 2.2 OHLC金融数据格式

国际上，股票、期货等金融数据采用

使用Tushare数据软件下载  get_h_data函数返回

- data  交易日期
- open  开盘价
- high 最高价
- close 收盘价
- low 最低价
- volume 成交量
- amount 成交金额

get_k_data 函数返回,方便获取日、周、月的低频数据，也可以获取5、15、30和60分钟等分时数据

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

ztq.tick2x(df,ktim='1T')   1T/ 1min/1D/30S/15min 参数

## 2.5 离线金融数据集

与前两小节一样



zdat，数据根目录

cn, A股日线数据

cn/day 股票日线数据

cn/xday, 指数日线数据

Inx, 常用指数，股票代码参数目录

min,分时数据，包括5，15，30，60分钟分时数据

tick,分笔数据，按月建立子目录



## 2.6 TopDown金融数据下载

专门用于下载A股历史数据和实盘数据的开源程序



tdown_cnSTK.py 股票日线数据下载程序

tdown_real.py 股票实时数据下载程序

tdown_cnSTK_inx.py 指数日线数据下载程序

tdown_cnSTK_base.py 股票基础数据下载程序,股票代码，分类，新数据保存在tmp目录中

tdown_cnMin.py 股票分时数据下载程序，默认是5分钟分时数据，。Tushare新版本中的k函数接口使用腾讯服务器，只能提供最近40天左右的分时数据，需要每个月定时更新。

tdown_cnTick.py 股票Tick数据下载程序。使用原来新浪服务器，会定时屏蔽，所以意义不大



MTrd， winPyhton,我还没试

#### 案例2-7：更新单一A股日线数据

下载数据是通过 ztools_datadown 模块的 down_stk010函数完成的。

#### 案例2-8 ： 批量更新A股日线数据

#### 案例2-9： 更新单一A股分时数据

#### 案例2-10：批量更新分时数据

本书案例把全部股票代码列表文件stk_code.csv换成了自定义的股票池索引文件stk_pool.csv

## TopDat 金融数据集的Tick数据

输出 True,表示存在数据文件，从文件当中的最后日期开始追加数据；如果为False,则表示数据文件不存在，从A股建市时即1994-01-01日期开始下载数据。

## 2.6.2 Tick数据与实时数据

#### 案例2-11：更新单一实时数据

下载所有的指数实数数据，股票实时数据

![image-20201021215906853](/Users/bluegrey/Library/Application Support/typora-user-images/image-20201021215906853.png)

![image-20201021215915109](/Users/bluegrey/Library/Application Support/typora-user-images/image-20201021215915109.png)





![image-20201021215938052](/Users/bluegrey/Library/Application Support/typora-user-images/image-20201021215938052.png)

# 第三章 无数据不量化（下）

## 3.1 均值优先

在很多金融量化传统分析工程中也面临类似的抉择，通常都是使用close (收盘价)作为价格数据的。不过对于神经网络以及量化实盘分析而言，avg（均价）可能更有参考价值。

### 案例3-1：均值计算与价格曲线图

#计算avg均值数据 每一行均值

df['avg']=df[zsys.ohlcLst].mean(axis=1).round(2)

## 3.2多因子策略和泛因子策略

### 3.2.1多因子策略

多因子模型的关键是提供数据分析，找到因子与收益之间的关联性。

### 3.2.2范因子策略

多因子策略结合更多的衍生数据扩展策略

#### 案例3-2：均线因子

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

### 案例3-5：增强版指数索引

![image-20201021221454685](/Users/bluegrey/Library/Application Support/typora-user-images/image-20201021221454685.png)

![image-20201021221500769](/Users/bluegrey/Library/Application Support/typora-user-images/image-20201021221500769.png)



感觉这里bug  id字段



### 案例3-6：AI版索引数据库

介绍如何修改股票代码文件stk_code.csv,生成一个增强版本的股票数据文件。

![image-20201021221749920](/Users/bluegrey/Library/Application Support/typora-user-images/image-20201021221749920.png)

![image-20201021221838141](/Users/bluegrey/Library/Application Support/typora-user-images/image-20201021221838141.png)

id 字段应该有bug



## 3.7 股票池



### 案例3-7：股票池的使用

主要介绍股票池的使用，以及相关的实用编程技术。



## 3.8 TQ_bar全局变量类

为了简化编程，TopQuant采用All-in-One 编程模式，定义了一个TQ_bar全局变量类，用于交换全程各种数。

### 案例3-8：TQ_bar 初始化

### 案例3-9：TQ版本日线数据

## 3.9大盘指数

收集24种指数数据。

![image-20201021222748185](/Users/bluegrey/Library/Application Support/typora-user-images/image-20201021222748185.png)

### 案例3-10： 指数日线数据

### 案例3-11： TQ版本指数K线图

### 案例3-12： 个股和指数曲线对照图



## 3.10 TDS金融数据集

P96 对数据集进行了介绍，



xavg(n) 次日均值 Y  

ma_(n)  移动平均线



Python df.max https://blog.csdn.net/tz_zs/article/details/81252710?utm_medium=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.channel_param&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.channel_param

### 案例3-13:TDS衍生数据

### 案例3-14：TDS金融数据集的制作

### 案例3-15：TDS金融数据集2.0

### 案例3-16：读取TDS金融数据集



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

## 4.6 n+1 大盘指数预测



在前面案例4-1中已经知道当天的收盘价与第二天的开盘价关联度最大，大盘指数也是类似。也可用大盘指数计算其中的关联度数据。

### 4.6.1 线性回归模型

线性回归模型是最简单的模型，也是最古老的算法模型，其原理是基于二元一次回归方程。

#### 案例4-4：上证指数n+1的开盘价预测

使用Tensorflow简化接口TFLearn，建立线性回归模型来分析历史数据，预测n+1的上证指数的Open。



？ 了解线性回归模型



### 案例4-5：预测数据评估

介绍如何读取预测数据文件，并对模型的预测效果进行评估。

### 4.6.2 效果评估函数

介绍了 ai_acc_xed2ext() 函数

### 4.6.3 常用的评测指标

P138

- SSE
- $R^2$
- Adjusted R-square,修正确定系数。
- Precision,准确率
- Recall，R指标，召回率
- ....
- 

## 4.7 n+1大盘指数趋势预测

前面的案例误差精读为 3% ~5%时，模型准确度高达95%以上，但是没有任何实盘价值。对于股市大盘指数，日线的波动一般都在3%以内。案例中的3%~5% 上下波动可高达10%，没有意义。对波动精度要求为千分之一、万分之一，外汇日内交易更是要求十万分之一的波动精度。

### 案例4-6：涨跌趋势归一化分类

第二天开盘价和当天收盘价之比

### 案例4-7：经典版涨跌趋势归一化分类

第二天收盘价与开盘价进行比较



## 4.8 One-Hot

Pandas get_dummies()

## 4.9 DNN 模型

### 案例4-9：DNN 趋势预测



# 第五章 单层神经网络预测股价

## 5.1 Keras 简化接口

介绍了一下keras优点

## 5.2 单层神经网络



感知机 https://www.cnblogs.com/xym4869/p/11282469.html

### 5-2: 可视化神经网络模型

- summary

- Plot_model

- TensorBoard  

  # ? Mac 怎么用zwpython

### 案例5-3: 模型读写

需要对模型和相关权重数据进行保存。

- TensorFlow提供了一个Saver类，用于在训练完一个模型之后，保存训练结果。
- Python的pickle模块支持二进制数据和程序的一体化存储，是非常理想的机器学习模型存储工具。
- SKLearn模块中内置了高效的模型持久化模块joblib
- Keras的model模块

代码5-3主要介绍了Keras神经网络模型保存和读取的具体方法。



书籍页面缺失16页，在pdf 196页



案例5-4：参数调优入门

```python
# 调用 ztools_tq 模块中的ai_mx_tst_epochs 函数，测试不同参数的准确度，并绘制相关的图形。
# 测试轮数  每批数量规模   不同误差精度
df2=ztq.ai_mx_tst_epochs(fmx,ftg,df_train,df_test,kepochs=100,nsize=128,ky0=5)
#df2=ztq.ai_mx_tst_bsize(fmx,ftg,df_train,df_test,nepochs=300,ksize=8,ky0=5)
#df2=ztq.ai_mx_tst_kacc(fmx,ftg,df_train,df_test,nepochs=300,nsize=128)


```

# 第六章 MLP与股价预测

## 6.1 MLP

MLP多层感知器，又称多层神经网络。

# ？ 与感知机关系？DNN关系？与上一章什么关系？



### 案例6-1：MLP价格预测模型



## 6.2 神经网络模型应用四大环节

读取数据 -》 调用模型 -》 训练模型 -》 模型预测

![image-20201014213325804](/Users/bluegrey/Library/Application Support/typora-user-images/image-20201014213325804.png)

### 案例6-2：MLP模型评估

案例6-1并没有对模型进行评估



### 案例6-3：优化MLP价格预测模型



多了一个初始化参数：

# ？ Kernel_initializer='normal' ,使得完全一样的模型的准确度从不足50%,提高到97.59%



### 案例6-4： 优化版MLP模型评估



# 第7章RNN与趋势预测

## 7.1 RNN

循环神经网络，通常指的是时间递归神经网络，也叫递归数据网络。

![image-20201014224250332](/Users/bluegrey/Library/Application Support/typora-user-images/image-20201014224250332.png)



## 7.2 IRNN 与预势预测

初始化循环神经网络模型， 它是RNN模型的衍生模型。

# ？ 深度学习三巨头



对金融数据进行处理：

- 把股票价格、波动幅度转化为上涨、下跌、平稳类型
- 分类后的数据作为标签y结果，并且转化我One-hot（独热码）格式



### 案例7-1: RNN趋势预测模型

###  案例7-2：RNN模型评估

### 案例7-3：RNN趋势预测模型2

###  案例7-4：RNN模型2评估

# 第八章 LSTM与量化分析





## 8.1 LSTM模型

 LSTM算法具有RNN算法的各种优点，但因为LSTM模型有更好的记忆能力，所以效果更佳。

本文的模型结构通常都在10层以内。而在实际应用中，所使用的神经网络模型要复杂的多，神经网络层往往超过100层。所需的数据也庞大得多，通常有上百甚至上千个数据字段，



### 8.1.1 数值预测

#### 案例8-1：LSTM价格预测模型

#### 案例8-2：LSTM价格预测模型评估

### 8.1.2 趋势预测

未来市场价格走向上涨还是下跌进行

#### 案例8-3：LSTM股价趋势预测模型

#### 案例8-4：LSTM趋势模型评估

## 8.2 LSTM量化回溯分析

### 8.2.1构建模型

#### 案例8-5：构建模型

介绍在量化回溯系统中LSTM模型的构建方法。

数据zz500  2017年1月以前的所有股票数据作为训练数据，2017 1-9月作为测试数据

使用量化回溯测试进行数据分析



### 8.2.2 数据整理

arr.shape    # (a,b)
arr.reshape(m,-1) #改变维度为m行、d列 （-1表示列数自动计算，d= a*b /m ）
arr.reshape(-1,m) #改变维度为d行、m列 （-1表示行数自动计算，d= a*b /m ）

清理无效数据，格式转换

#### 案例8-6：数据整理

在TopQuant极宽智能量化系统中，策略函数采用组合函数模式 即一个数据预处理函数dataPre和一个策略函数sta

同时充分利用Pandas 、NumPy等的矢量化高速运算函数，提高量化分析的整体性能。

书P251详细介绍

ztq.tq_pools_call(qx,qx.preFun)

即通过股票池主调用函数tq_pools_call,调用数据预处理函数preFun，对相关数据进行处理。



### 8.2.3 回溯分析

BackTest  就是使用过去的历史数据，对投资策略进行测试，以检验投资策略是不是有效；或者通过参数优化，调整投资策略的细节。

#### 案例8-7：回溯分析



qx.trdLib是交易记录表，它共有4个字段。

- time ——时间
- ID——用户的交易订单编码，按日期归组
- Cash——当天的现金总额，已扣除当天的交易金额。
- UserPools——用户交易股票池数据
  - 字典key值——股票代码
  - Num9——持有该股票的总数额
  - dnum——当天交易数额，正数为买入，负数为卖出  

![image-20201022124744141](/Users/bluegrey/Library/Application Support/typora-user-images/image-20201022124744141.png)



第6.2组代码

合并用户交易数据

- data——时间

- inx——大盘指数当天的价格数据

- cash——当天持有的现金总额

- tatal——资产总值

- 000001等——股票代码字段，对应相关股票当天的价格数据

  

第6.3组代码

增加字段

- xcod ——股票代码名称
- xcod_num——该代码股票的持有量
- xcod_money——该代码股票的出游金额
- stk-val——当天用户持有的股票总值

### 8.2.4 专业回报分析

ROI(投资回报率)

#### 案例8-8：量化交易回报分析



第二组

增加了两个字段， inx total

数据源使用的是回溯测试的结果数据



## 8.3 完整的LSTM量化分析程序

#### 案例8-9：LSTM量化分析程序



### 8.3.1 数据整理

### 8.3.2 量化回溯



# 第9章 日线数据回溯分析



## 9.1数据整理

- 数据更新
- 数据清理
- 参数设置

### 案例9-1：数据更新

