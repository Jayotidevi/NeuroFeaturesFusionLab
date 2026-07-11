# NeuroFeaturesFusion

A modular, extensible, and dataset-independent deep learning framework for multimodal biomedical data harmonization, representation learning, fusion, and evaluation.
> NeuroFeaturesFusion is currently under active development. The framework architecture and core abstractions are being implemented incrementally following software engineering best practices. Documentation and implementation are updated together as each milestone is completed.
## Project Overview

NeuroFeaturesFusion is a research-oriented software framework designed to support multimodal biomedical machine learning. The framework provides a unified architecture for integrating heterogeneous datasets, harmonizing different data modalities, learning deep representations using modality-specific foundation models, performing multimodal fusion, and evaluating downstream prediction tasks.

Unlike dataset-specific implementations, NeuroFeaturesFusion is designed as a reusable framework that enables new datasets, modalities, encoders, and fusion strategies to be integrated with minimal modifications.

## Motivation

Biomedical datasets differ significantly in terms of data modalities, acquisition protocols, sampling frequencies, channel configurations, metadata, and storage formats. These differences often require researchers to build independent processing pipelines for every dataset, making reproducibility and cross-dataset learning difficult.

NeuroFeaturesFusion addresses this challenge by introducing a unified software architecture that faithfully reads heterogeneous datasets, harmonizes their modality representations, preserves raw signal information for deep learning, and provides common interfaces for representation learning, multimodal fusion, and evaluation.

## Research Objectives

The primary objectives of NeuroFeaturesFusion are:

- Support heterogeneous biomedical datasets.
- Preserve raw modality information for deep representation learning.
- Harmonize incompatible datasets into unified modality representations.
- Enable modality-specific foundation models.
- Support flexible multimodal fusion architectures.
- Provide reusable software components for research and experimentation.
![NeuroFeaturesFusion Framework Architecture](docs/images/framework_overview.png)

For more details, see:
[Current Architecture Documentation](docs/architecture/current_architecture.md)- Improve cross-dataset generalization.
