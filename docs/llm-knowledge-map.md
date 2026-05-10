# 大模型知识地图

这份地图用来约束学习重点：我们不是为了“会调用 Whisper”，而是为了通过音频模型学习大模型的通用机制。

## 1. 数据如何进入模型

文本模型：

- 原始文本
- tokenizer
- token id
- embedding
- position embedding
- Transformer blocks

音频模型：

- 原始音频 waveform
- 重采样和切片
- STFT
- Mel filterbank
- log-Mel spectrogram
- audio encoder
- decoder 生成文本 token

关键问题：

- 为什么神经网络不能直接理解字符串或 wav 文件？
- token 和 embedding 解决了什么问题？
- 文本序列和音频帧序列有什么相同点？

## 2. 模型在学什么

语言模型常见目标：

- next-token prediction：给前文，预测下一个 token。
- masked language modeling：遮住一部分 token，再预测回来。
- seq2seq generation：给输入序列，生成输出序列。

Whisper 的目标更接近 seq2seq generation：

- 输入：音频特征序列。
- 输出：文本 token 序列，也可以包含语言、任务、时间戳等特殊 token。

关键问题：

- logits 是什么？
- softmax 后的概率代表什么？
- cross entropy 为什么能训练生成模型？
- teacher forcing 为什么能提高训练效率？

## 3. Transformer 的核心模块

必须掌握：

- embedding
- positional encoding 或 positional embedding
- self-attention
- multi-head attention
- causal mask
- padding mask
- residual connection
- LayerNorm
- MLP block
- cross-attention

理解顺序：

1. tensor shape
2. 单头 self-attention
3. 多头 attention
4. mask
5. Transformer block
6. 堆叠多个 block
7. decoder-only 和 encoder-decoder 的差异

## 4. 训练闭环

最小训练闭环：

1. 准备 batch
2. forward 得到 logits
3. 计算 loss
4. backward 计算梯度
5. optimizer 更新参数
6. 定期 eval
7. 保存 checkpoint

必须理解：

- batch size
- learning rate
- optimizer
- gradient
- overfitting
- validation loss
- checkpoint
- mixed precision

## 5. 推理和生成

基础生成方法：

- greedy decoding
- sampling
- temperature
- top-k
- top-p
- beam search

音频模型额外问题：

- 长音频如何切片？
- 多段识别结果如何合并？
- 时间戳如何生成？
- 如何处理静音和噪声？

## 6. 大模型工程问题

后续逐步学习：

- 数据清洗
- 数据配比
- tokenizer 训练
- 分布式训练
- 梯度累积
- 学习率调度
- 参数规模和数据规模
- 评估指标
- 推理加速
- 量化
- 部署

## 7. 与 Whisper 的对应关系

| 大模型概念 | Whisper 中的体现 |
| --- | --- |
| token | 文本 token、语言 token、任务 token、时间戳 token |
| embedding | decoder token embedding |
| sequence input | log-Mel spectrogram frame 序列 |
| encoder | 音频 encoder |
| decoder | 文本生成 decoder |
| self-attention | encoder 和 decoder 内部建模上下文 |
| cross-attention | decoder 读取 audio encoder 输出 |
| loss | 预测下一个文本 token 的 cross entropy |
| generation | greedy decoding 或 beam search |
| evaluation | WER / CER |

