# NeuroFeaturesFusion Architecture

## 1. Project Vision:
NeuroFeaturesFusion is a modular, reusable, and dataset-independent
framework for multimodal biomedical machine learning.

The framework is designed to support heterogeneous biomedical datasets,
preserve raw modality information, harmonize incompatible data
representations, learn modality-specific representations, perform
multimodal fusion, and evaluate downstream predictive tasks.

## 2. Framework Design Principles:
## Framework Design Principles

The framework follows several software engineering principles.

- Single Responsibility Principle
- Dataset independence
- Modality independence
- Reusable software components
- Separation between data representation and learning
- Extensible architecture for future modalities

## 3. Current Architecture:

External Dataset
        │
   BaseAdapter
        │
   BaseDataset
        │
   BaseSample
        │
Dictionary[str, BaseModality]

## 4. Framework Data Flow:
## Framework Data Flow

Raw biomedical datasets are first converted into a unified internal
representation through dataset adapters.

Each dataset consists of multiple samples.

Each sample maintains a collection of modalities using a dictionary,
allowing different datasets to contain arbitrary combinations of
modalities such as EEG, audio, video, MRI, ECG, or clinical data.

The framework preserves the original modality information before
performing harmonization, deep representation learning, multimodal
fusion, and downstream prediction.

## 5. Core Components:
## Core Components

### BaseComponent

Purpose

Provides the common interface shared by all framework components.

Responsibilities

- Configuration
- Validation
- Initialization
- Summary

---

### BaseDataset

Purpose

Represents one biomedical dataset.

Responsibilities

- Store samples
- Dataset metadata

---

### BaseSample

Purpose

Represents one participant/sample.

Responsibilities

- Sample information
- Label
- Metadata
- Collection of modalities

---

### BaseModality

Purpose

Represents a single modality.

Responsibilities

- Raw modality data
- Metadata
- Modality description

---

### BaseAdapter

Purpose

Converts heterogeneous external datasets into framework objects.

Responsibilities

- Load datasets
- Parse structure
- Create samples

## 6. Milestone Progress:
## Milestone Progress

### Milestone 1

Core framework abstraction

Status

Completed

---

### Milestone 2

Generic dataset representation

Status

Completed

---

### Milestone 3

Generic modality architecture

Status

Completed

---

### Milestone 4

Dataset adapter architecture

Status

In Progress

## 7. Current Status:
## Current Status

Core Framework

[x] BaseComponent

[x] BaseDataset

[x] BaseSample

[x] BaseModality

[x] BaseAdapter

[ ] BaseHarmonizer

[ ] BaseEncoder

[ ] BaseFusion

[ ] BaseTrainer

[ ] BaseEvaluator

## 8. Next Development Phase:
## Next Development Phase

The next stage of development focuses on:

- Building dataset-specific adapters
- Designing harmonization interfaces
- Developing modality-specific encoders
- Constructing multimodal fusion strategies
- Integrating the training pipeline
