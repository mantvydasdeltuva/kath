---
title: Kath Docs
description: Kath is a user-friendly GUI tool designed to streamline the in-depth analysis of gene variation data.
draft: false
date: 2025-01-28
show: false
---

<img src="assets/image/kath_banner_dark.png" alt="Kath Banner">

---

## Overview

**_Kath_ is a user-friendly GUI tool designed to streamline the in-depth analysis of gene variation data from LOVD, gnomAD, and ClinVar genetic databases**. By consolidating critical information into an accessible interface, _Kath_ empowers researchers, clinicians, and geneticists to uncover actionable insights with ease.

Built for efficiency and adaptability, it is ideal for tasks such as assessing pathogenicity or cross-referencing genetic variant data. It serves as a vital tool for advancing research, improving diagnostics, and supporting genomic studies.

<img src="assets/image/kath_design_dark.png" alt="Kath Design Dark" style="border-radius: 0.25rem;">

---

## Documentation

Comprehensive and detailed documentation is provided to support all users, developers, and system administrators throughout the _Kath_. Whether you’re a first-time user, a contributor to the project, or managing the deployment and maintenance of _Kath_, our resources are designed to guide you at every step.

### User Manual

![[manual/index.md#^summary]]

### System Deployment

![[deployment/index.md#^summary]]

### Project Development

![[development/index.md#^summary]]

---

## Advisors

We are honored to recognize the contributions of our advisors who **bring expertise, resources, and guidance to the development of _Kath_**. Their support is instrumental in ensuring the quality, innovation, and impact of our tool in the field of genetics.

<div class="grid-container">
    <div class="card">
        <a href="https://www.harvard.edu">
            <img src="assets/image/harvard_logo.png" alt="Harvard University">
            <div class="card-title">Harvard University</div>
        </a>
        <div class="card-description">
            Leading institution in education and research.
        </div>
    </div>
    <div class="card">
        <a href="https://genomika.lt">
            <img src="assets/image/genomika_logo.png" alt="Genomika Lietuva">
            <div class="card-title">Genomika Lietuva</div>
        </a>
        <div class="card-description">
            Innovative solutions in genomics and biotechnology.
        </div>
    </div>
</div>

<!-- CSS -->
<style>
    .grid-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(24rem, 1fr));
        justify-items: center;
        gap: 1rem;
        width: 100%;
        margin: 0 auto;
    }

    .card {
        display: flex;
        flex-direction: column;
        width: 100%;
        max-width: 26rem;
    }

    .card a {
        display: flex;
        flex-direction: column;
        align-items: center;
        text-decoration: none;
    }

    .card img {
        width: auto;
        height: 13rem;
        border-radius: 0.25rem;
    }

    .card-title {
        font-size: 1.4rem;
        font-weight: bold;
        line-height: 1.4rem;
        text-align: center;
    }

    .card-description {
        text-align: center;
        margin: 0.5rem 0;
    }
</style>
