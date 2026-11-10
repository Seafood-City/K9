# Data, logs, models and large files

Keep source, configuration, small fixtures and selected evidence in Git. Store raw ZED captures, ROS bags, telemetry dumps, training datasets, downloaded models and long videos in a team-controlled artifact location. Record stable access-controlled URLs and SHA-256 checksums in the manifests; never commit an expiring signed URL or embedded credential.

This repository's file check uses a **10 MiB per tracked file** project limit. That is a team policy for a lightweight repository, not GitHub's upload limit. A Git LFS pointer can be small even when the actual asset is large; LFS bandwidth and storage are separate from normal Git.

| Material | Default handling |
| --- | --- |
| Python/ROS source, YAML/JSON, Pixhawk .param | Normal Git |
| Altium source and selected small CAD exports | Normal Git as binary; agree on one editor at a time |
| Markdown, small PDFs and editable report/deck files | Normal Git within the project size limit |
| Selected evidence photographs | Normal Git, resized only when the original detail is unnecessary |
| Raw recordings, model weights and datasets | External artifact location plus manifest/checksum |
| Generated builds, caches and runtime logs | Ignore; preserve selected evidence through an indexed test record |

The .gitattributes file marks binary formats but does not enable Git LFS. If the team chooses LFS for large CAD or editable documents, install Git LFS on every contributor machine, agree on the organization's quota/budget, then explicitly track the chosen paths before their first commit. Review the resulting .gitattributes change. LFS does not remove assets already present in earlier Git history.

For an accidentally staged generated file, unstage it and correct its location or ignore rule. An ignore rule does not stop tracking a file that was already committed.

## Manifests

[data/artifacts.csv](../../data/artifacts.csv) tracks externally stored data and models. [The evidence index](../verification/evidence/index.csv) tracks test evidence and links it to existing test IDs, source commits and parameter snapshots. These are header-only templates, not claims that artifacts or tests already exist.

Use a shared location that teammates and reviewers can actually access; a local Windows path is not an evidence URL.

Official guidance: [Git LFS](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-git-large-file-storage) and [Git LFS usage and billing](https://docs.github.com/en/billing/concepts/product-billing/git-lfs).
