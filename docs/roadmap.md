# 学习路线

## 总原则

这个项目的主目标是学习大模型知识，Whisper 只是一个很好的音频案例。不要一开始从零训练完整 Whisper，也不要只停留在调用现成模型。完整 Whisper 使用了约 68 万小时多语言、多任务音频数据，工程和算力规模都很大。更合理的路线是：

1. 先从文本 toy model 学会大模型训练闭环。
2. 再从零实现 Transformer 的关键模块。
3. 接着理解 encoder-decoder 架构。
4. 然后把输入从文本扩展到音频特征。
5. 最后再微调和复刻 mini-Whisper。

这样可以同时学到大模型的核心知识，也能保持每一步都有可运行结果。

## 第 0 阶段：工程和学习环境

目标：

- 建立工程目录。
- 保存学习路线和资源。
- 建立学习日志。
- 检查 Python 环境和关键依赖。

交付物：

- `README.md`
- `docs/roadmap.md`
- `docs/llm-knowledge-map.md`
- `docs/learning-log.md`
- `docs/resources.md`
- `scripts/check_env.py`

## 第 1 阶段：最小语言模型闭环

目标：

- 用很小的文本数据训练一个 toy language model。
- 理解大模型训练最小闭环：输入 token -> 模型预测 -> loss -> 反向传播 -> 参数更新。
- 先不追求模型效果，只追求每一步能解释清楚。

重点概念：

- token
- vocabulary
- embedding
- logits
- softmax
- cross entropy
- next-token prediction
- batch
- optimizer
- train/eval split
- generation

预期实验：

- 用字符级 tokenizer 训练一个极小模型。
- 输入一小段文本，模型能生成相似风格的短文本。
- 记录 loss 下降曲线和生成样例。

## 第 2 阶段：从零实现 Transformer

目标：

- 从零实现 decoder-only Transformer 的核心模块。
- 明白 attention 为什么能建模上下文。
- 明白 mask、position、残差、LayerNorm 的作用。

重点概念：

- self-attention
- multi-head attention
- causal mask
- positional embedding
- residual connection
- LayerNorm
- MLP block
- dropout
- parameter count
- context length

预期实验：

- 实现一个小型 GPT 风格模型。
- 对比无 attention、单头 attention、多头 attention 的效果。
- 能解释每个 tensor 的 shape。

## 第 3 阶段：encoder-decoder 和 seq2seq

目标：

- 从 decoder-only 过渡到 encoder-decoder。
- 理解翻译、摘要、语音识别这类输入输出长度不同的任务。
- 为理解 Whisper 架构做准备。

重点概念：

- encoder
- decoder
- cross-attention
- teacher forcing
- BOS/EOS token
- padding mask
- sequence-to-sequence
- greedy decoding
- beam search

预期实验：

- 实现一个 toy seq2seq 任务，例如字符串反转或字符级翻译。
- 画出 encoder 输出、decoder 输入、cross-attention 的数据流。

## 第 4 阶段：音频输入和 ASR 基础

目标：

- 学会读取 wav/mp3。
- 理解 waveform、STFT、Mel filterbank、log-Mel。
- 把音频特征看成一种序列输入。
- 理解 WER 和 CER。

重点概念：

- waveform
- sampling rate
- resampling
- STFT
- Mel scale
- log-Mel
- frame
- feature extractor
- WER
- CER

预期实验：

- 画出同一段音频的 waveform 和 Mel spectrogram。
- 对一组预测文本计算 WER/CER。
- 明确 Whisper 的 encoder 输入为什么是 log-Mel 序列。

## 第 5 阶段：mini-Whisper 和真实模型工程

目标：

- 自己实现一个小型 encoder-decoder Transformer ASR 模型。
- 用小数据集训练到能过拟合小样本，再扩展到小规模验证集。
- 再对比 Hugging Face 或 OpenAI Whisper 的真实实现。

建议设置：

- 输入：16kHz 音频
- 特征：80 维 log-Mel
- tokenizer：先用字符级 tokenizer
- encoder：2 到 4 层 Transformer
- decoder：2 到 4 层 Transformer
- hidden size：256 或 384
- 解码：先 greedy decoding，再 beam search

重点概念：

- dataset split
- data collator
- mixed precision
- checkpoint
- evaluation
- model scaling
- overfitting small batch
- inference

预期实验：

- 先在极小数据上过拟合。
- 再训练一个可用的 toy ASR。
- 最后微调 `whisper-tiny` 或 `whisper-small` 做对照。

## 第 6 阶段：扩展和优化

目标：

- 长音频切片和合并。
- 时间戳。
- 多语言任务 token。
- 噪声增强。
- 推理速度优化。

重点概念：

- chunking
- VAD
- timestamp token
- multilingual token
- SpecAugment
- quantization
- streaming inference
