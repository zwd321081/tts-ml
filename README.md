# Audio LLM Lab

这是一个从 Whisper 入手学习音频大模型的长期工程。目标不是一开始复刻完整 Whisper，而是按阶段把自动语音识别、大模型训练、数据处理、评估和推理部署逐步跑通。

## 学习目标

1. 跑通现成 Whisper 模型，理解音频转文字的完整链路。
2. 掌握 ASR 基础：采样率、waveform、STFT、log-Mel、tokenizer、WER/CER。
3. 微调一个小型 Whisper 模型，熟悉数据集、训练循环、评估和 checkpoint。
4. 从零实现一个 mini-Whisper，理解 encoder-decoder Transformer 的关键细节。
5. 逐步扩展到长音频、时间戳、多语言、噪声鲁棒性和推理优化。

## 工程结构

```text
audio-llm-lab/
  README.md
  pyproject.toml
  docs/
    roadmap.md          # 分阶段学习路线
    learning-log.md     # 每次学习和实验记录
    resources.md        # 论文、课程、数据集、代码资源
  src/audio_llm_lab/
    __init__.py
  scripts/
    check_env.py        # 检查 Python 和常用依赖
  experiments/          # 每次实验的脚本、notebook 或结果记录
  data/
    raw/                # 原始数据，本地使用，不提交大文件
    processed/          # 处理后的特征或样本，本地使用
```

## 当前阶段

当前处于第 0 阶段：建立工程、保存路线、准备第一个环境检查脚本。

下一步建议：

```bash
cd audio-llm-lab
uv sync --extra dev
uv run python scripts/check_env.py
```

之后再进入第 1 阶段：安装 Whisper，拿一段音频跑通第一次转写。

## Python 环境

本工程使用 `uv` 管理 Python 环境和依赖，并固定使用 Python 3.11。

常用命令：

```bash
uv sync --extra dev
uv run python scripts/check_env.py
uv add <package>
uv run pytest
```

## 记录约定

每次学习或实验都更新 `docs/learning-log.md`，至少记录：

- 日期
- 今天做了什么
- 关键概念
- 遇到的问题
- 下一步

每个较完整的实验可以在 `experiments/` 下新建一个目录，例如：

```text
experiments/2026-05-10-run-whisper-inference/
```
