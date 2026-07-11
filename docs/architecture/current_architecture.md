# NeuroFeaturesFusion Current Architecture

## Framework Data Flow



## Explanation

NeuroFeaturesFusion separates dataset loading, sample representation, modality handling, and deep representation learning.

Raw datasets are first converted into unified framework objects. Each sample can contain different combinations of modalities such as EEG, audio, clinical data, or future modalities.

The framework preserves raw modality information before applying deep encoders.
