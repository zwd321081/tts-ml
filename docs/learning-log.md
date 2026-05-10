# 学习日志

## 2026-05-10：第 0 次记录，建立工程

### 今天做了什么

- 新建 `audio-llm-lab` 工程。
- 保存从 Whisper 入手学习音频大模型的路线。
- 建立 `docs/roadmap.md`、`docs/resources.md` 和本学习日志。
- 准备最小 Python 项目骨架和环境检查脚本。
- 确认 Python 依赖管理使用 `uv`，项目固定使用 Python 3.11。

### 关键概念

- Whisper 是一个自动语音识别模型，也可以做多语言转写、语音翻译和语言识别。
- Whisper 的核心链路是：音频切片 -> log-Mel spectrogram -> encoder -> decoder -> 文本 token。
- 完整 Whisper 的数据和算力规模很大，学习时不应只从调用模型开始，而应先理解大模型训练闭环，再迁移到音频模型。

### 问题和待确认

- 本机 Python、PyTorch、torchaudio、transformers 等依赖是否已安装。
- `uv sync --extra dev` 是否能顺利安装 PyTorch 和音频相关依赖。
- 后续优先学习英文 ASR、中文 ASR，还是二者都做。
- 是否使用 GPU、Apple Silicon MPS，还是 CPU 先跑小模型。

### 下一步

1. 运行 `uv sync --extra dev` 安装依赖。
2. 运行 `uv run python scripts/check_env.py` 检查环境。
3. 做第一个实验：字符级 tokenizer + 最小语言模型训练闭环。
4. 记录 token、embedding、logits、loss、generation 的观察。

## 2026-05-10：调整学习方向，大模型机制优先

### 今天做了什么

- 将路线从“先跑 Whisper 推理”调整为“先学大模型核心机制，再进入音频模型”。
- 新增 `docs/llm-knowledge-map.md`，记录大模型知识地图。
- 将第 1 阶段改为最小语言模型闭环。

### 关键概念

- Whisper 是学习案例，不是第一目标。
- 大模型基础应先掌握：token、embedding、Transformer、loss、optimizer、generation。
- 音频模型和文本模型的共同点是：都把输入变成序列，再用神经网络建模序列关系。

### 下一步

1. 创建第一个实验 `experiments/2026-05-10-tiny-lm/`。
2. 用字符级 tokenizer 做一个最小训练数据集。
3. 写一个能训练、评估、生成文本的 tiny LM。

## 2026-05-10：学习约定，术语中英对照

### 今天做了什么

- 增加学习约定：后续关键术语使用“中文（English）”格式。
- 例子：张量（tensor）、标量（scalar）、嵌入（embedding）、损失（loss）、反向传播（backpropagation）。

### 关键概念

- 标量（scalar）：单个数字。
- 向量（vector）：一维数字数组。
- 矩阵（matrix）：二维数字数组。
- 张量（tensor）：更一般的多维数字数组，是深度学习框架中的基本计算对象。

### 下一步

1. 继续回答问题：token id 和嵌入（embedding）的区别是什么。

## 2026-05-10：检查点，token id 和嵌入初学

### 今天做了什么

- 用问答方式学习了为什么模型不能直接吃字符串。
- 开始区分 token id、嵌入（embedding）、隐藏表示（hidden representation）和 logits。
- 暴露出当前卡点：形状（shape）变化、隐藏维度（hidden size）和词表大小（vocab size）的区别还不稳。

### 当前理解

- 大模型不能直接吃字符串，不是因为计算机不能存储字符串，而是因为神经网络需要对数值张量（tensor）做矩阵乘法、求导和反向传播（backpropagation）。
- token id 是离散编号，也就是词表（vocabulary）里的索引（index）。
- 嵌入（embedding）是可训练的连续向量（continuous vector），由 token id 查嵌入表（embedding table）得到。
- 如果词表大小（vocab size）是 `50000`，嵌入维度（embedding dimension）是 `768`，嵌入表（embedding table）的形状（shape）是 `[50000, 768]`。

### 混淆点

- 不能把 token id 当成普通数值特征（numeric feature）。`15339` 只是编号，不代表它比 `15338` 更大或更相似。
- 输入 token ids 的形状（shape）是 `[batch_size, sequence_length]`，经过嵌入（embedding）后会变成 `[batch_size, sequence_length, embedding_dimension]`。
- logits 是模型对词表里每个候选 token 的原始分数（raw scores），不是概率（probability）。
- 隐藏维度（hidden size）和词表大小（vocab size）不是一回事。隐藏表示常见形状是 `[batch_size, sequence_length, hidden_size]`，logits 常见形状是 `[batch_size, sequence_length, vocab_size]`。

### 学习节奏调整

- 从第二问重新开始，不急着推进到 logits。
- 每次只处理一个概念：先 token id，再嵌入（embedding），再形状（shape），最后再讲 logits。
- 每个概念都用一个小例子检验，而不是连续追问多个形状。

### 下一步

1. 重新回答：token id 和嵌入（embedding）有什么区别。
2. 用一个 5 个 token 的小词表手算嵌入表（embedding table）和查表过程。

## 日志模板

```text
## YYYY-MM-DD：标题

### 今天做了什么

- 

### 关键概念

- 

### 实验结果

- 

### 问题和待确认

- 

### 下一步

1. 
```
