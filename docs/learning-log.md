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
- 完整 Whisper 的数据和算力规模很大，学习时应先推理、再微调、最后实现 mini 版本。

### 问题和待确认

- 本机 Python、PyTorch、torchaudio、transformers 等依赖是否已安装。
- `uv sync --extra dev` 是否能顺利安装 PyTorch 和音频相关依赖。
- 后续优先学习英文 ASR、中文 ASR，还是二者都做。
- 是否使用 GPU、Apple Silicon MPS，还是 CPU 先跑小模型。

### 下一步

1. 运行 `uv sync --extra dev` 安装依赖。
2. 运行 `uv run python scripts/check_env.py` 检查环境。
3. 准备一段 10 到 30 秒测试音频。
4. 跑通第一个 Whisper 推理实验。

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
