# Audio LLM Lab

这是一个用音频模型作为载体学习大模型的长期工程。Whisper 是后续重点案例，但学习顺序不是先学会调用 Whisper，而是先掌握大模型核心机制，再把这些机制迁移到音频输入和语音识别任务。

## 学习目标

1. 从零理解一个大模型训练闭环：数据、token、embedding、Transformer、loss、优化器、评估、推理。
2. 先实现一个极小文本语言模型，掌握 next-token prediction 和 decoder-only Transformer。
3. 再实现 encoder-decoder Transformer，理解 Whisper 这类模型为什么需要 encoder 和 decoder。
4. 接入音频特征：waveform、STFT、log-Mel，把音频变成模型可处理的序列。
5. 最后微调或复刻 mini-Whisper，学习真实大模型工程中的数据、训练、评估和推理问题。

## 工程结构

```text
audio-llm-lab/
  README.md
  pyproject.toml
  docs/
    roadmap.md          # 分阶段学习路线
    llm-knowledge-map.md # 大模型知识地图
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

之后进入第 1 阶段：从零实现一个最小文本语言模型，先学清楚大模型训练的基本闭环。

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
experiments/2026-05-10-tiny-lm/
```
