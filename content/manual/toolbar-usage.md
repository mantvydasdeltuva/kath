---
title: Tool Bar Usage
description: This guide explains how to use each tool bar sections.
tags: 
    - End-User
    - Guide
date: 2025-01-30
draft: false
---

The **Tool Bar** is located at the top of the Kath application and is divided into three main sections: **Download**, **Merge**, and **Apply**. Each section has specific parameters and actions to help you manage and process your databases. This guide will walk you through how to use each section step by step.

---

## Download

The _Download_ section allows you to download specific databases into your workspace. You can choose which gene to download and where to save the data.

### Parameters

**`Gene`** - choose the gene to download.

**`Save To`** - specify an existing file in your workspace to save the database. The default option `New file...` creates a new file.

**`Override`** - appears when saving to an existing file. If checked, the file will be overwritten; otherwise, new data will be appended.

> [!info]
> Gene parameter currently supports only _eys_ gene.

### Actions

**`Download All`** - downloads all available databases (LOVD, ClinVar and gnomAD).

**`LOVD`** - downloads the LOVD database.

**`ClinVar`** - downloads the ClinVar database.

**`gnomAD`** - downloads the gnomAD database.

### How To Use

![](../assets/video/manual_toolbar_download.mp4)

1. **Select Gene**: Choose _eys_ from the _Gene_ dropdown.
2. **Choose Save Location**:
    - Select an existing file or choose _New File..._ to create a new one.
    - If using an existing file, decide whether to override or append data using the _Override Checkbox_.
3. **Click an Action**: Choose one of the actions (_LOVD_, _ClinVar_, _gnomAD_ or _Download All_) to start the download.
4. **Check Console**: Real-time feedback will appear in the _console_.
5. **View Results**: Once the download is complete, the new database files will appear in the _File Tree_.

---

## Merge

The _Merge_ section allows you to combine multiple databases into a single file for easier analysis.

### Parameters

**`Lovd File`** - choose a previously downloaded LOVD database file.

**`ClinVar File`** - choose a previously downloaded ClinVar database file.

**`gnomAD File`** - choose a previously downloaded gnomAD database file.

**`Custom File`** - select a predefined custom database file from Harvard University.

**`Save To`** - specify an existing file in your workspace to save the database. The default option `New file...` creates a new file.

**`Override`** - appears when saving to an existing file. If checked, the file will be overwritten; otherwise, new data will be appended.

> [!info]
> Custom File parameter is optional.

### Actions

**`Merge All`** - merges all selected databases. If a Custom File is specified, it is also merged.

**`Merge LOVD & gnomAD`** - merges only the LOVD and gnomAD databases.

**`Merge LOVD & ClinVar`** - merges only the LOVD and ClinVar databases.

### How To Use

![](../assets/video/manual_toolbar_merge.mp4)

1. **Select Databases**:
    - Choose the _LOVD_, _ClinVar_, and _gnomAD_ files you want to merge.
    - Optionally, select the _Custom File_ if needed.
2. **Choose Save Location**:
    - Select an existing file or choose _New File..._ to create a new one.
    - If using an existing file, decide whether to override or append data using the _Override Checkbox_.
3. **Click an Action**: Choose one of the merge actions (_Merge All_, _Merge LOVD & gnomAD_ or _Merge LOVD & ClinVar_).
4. **Check Console**: Real-time feedback will appear in the _console_.
5. **View Results**: Once the merge is complete, the merged file will appear in the _File Tree_.

---

## Apply

The _Apply_ section allows you to run algorithms on your databases to analyze, process, or enhance the data.

### Parameters

**`Apply To`** - select the database file on which you want to apply the algorithm.

**`Save To`** - specify an existing file in your workspace to save the database. The default option `New file...` creates a new file.

**`Override`** - appears when saving to an existing file. If checked, the file will be overwritten; otherwise, new data will be appended.

### Actions

**`Apply SpliceAI`** - predicts the impact of genetic variants on RNA splicing in the selected database.

**`Apply CADD`** - scores genetic variants based on their likelihood of being deleterious using multiple annotations.

**`Apply REVEL`** - assesses missense variant pathogenicity by combining multiple prediction scores.

> [!info]
> These algorithms are designed to work on merged databases.

### How To Use

![](../assets/video/manual_toolbar_apply.mp4)

1. **Select Database**: Choose the database file you want to process from the _Apply To_ dropdown.
2. **Choose Save Location**:
    - Select an existing file or choose _New File..._ to create a new one.
    - If using an existing file, decide whether to override or append data using the _Override Checkbox_.
3. **Click an Action**: Choose one of the algorithms (_Apply SpliceAI_, _Apply CADD_ or _Apply REVEL_).
4. **Check Console**: Real-time feedback will appear in the _console_.
5. **View Results**: Once algorithm is applied, the processed file will appear in the _File Tree_.