# 学习路线

## 总原则

不要一开始从零训练完整 Whisper。完整 Whisper 使用了约 68 万小时多语言、多任务音频数据，工程和算力规模都很大。更合理的路线是：

1. 先用现成模型做推理。
2. 再微调小模型。
3. 最后从零实现一个小型版本。

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
- `docs/learning-log.md`
- `docs/resources.md`
- `scripts/check_env.py`

## 第 1 阶段：跑通 Whisper 推理

目标：

- 安装 `openai-whisper` 或 Hugging Face `transformers`。
- 准备一段短音频。
- 跑通音频转文字。
- 观察模型输入输出。

重点概念：

- ASR
- 采样率
- 音频切片
- log-Mel spectrogram
- encoder-decoder Transformer
- decoder 生成文本

预期实验：

- 使用 `whisper-tiny` 或 `whisper-base` 转写一段 10 到 30 秒音频。
- 保存原始音频、转写结果和命令。

## 第 2 阶段：音频和 ASR 基础

目标：

- 学会读取 wav/mp3。
- 理解 waveform、STFT、Mel filterbank、log-Mel。
- 手写或调用 torchaudio 生成 spectrogram。
- 理解 WER 和 CER。

重点概念：

- waveform
- sampling rate
- resampling
- STFT
- Mel scale
- log-Mel
- WER
- CER

预期实验：

- 画出同一段音频的 waveform 和 Mel spectrogram。
- 对一组预测文本计算 WER/CER。

## 第 3 阶段：微调 Whisper 小模型

目标：

- 选择一个小数据集。
- 使用 `whisper-tiny` 或 `whisper-small` 做微调。
- 记录训练 loss、验证集 WER/CER 和推理结果。

可选数据集：

- 英文：LibriSpeech
- 多语言：Common Voice
- 中文普通话：AISHELL-1

重点概念：

- dataset split
- feature extractor
- tokenizer
- data collator
- teacher forcing
- mixed precision
- checkpoint
- evaluation

预期实验：

- 用 1 到 10 小时数据跑一个小型微调实验。
- 比较微调前后的识别效果。

## 第 4 阶段：从零实现 mini-Whisper

目标：

- 自己实现一个小型 encoder-decoder Transformer ASR 模型。
- 用小数据集训练到能过拟合小样本，再扩展到小规模验证集。

建议设置：

- 输入：16kHz 音频
- 特征：80 维 log-Mel
- tokenizer：先用字符级 tokenizer
- encoder：2 到 4 层 Transformer
- decoder：2 到 4 层 Transformer
- hidden size：256 或 384
- 解码：先 greedy decoding，再 beam search

重点概念：

- positional encoding
- self-attention
- cross-attention
- causal mask
- padding mask
- sequence loss
- greedy decoding
- beam search

预期实验：

- 先在极小数据上过拟合。
- 再训练一个可用的 toy ASR。

## 第 5 阶段：扩展和优化

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

