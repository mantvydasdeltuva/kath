---
title: Team Structure
description: Overview of the development team structure.
tags: 
    - Development
    - Front-End
    - Back-End
draft: false
date: 2025-01-24
---

> [!todo]
> Introduce and refactor Kath project team structure. Use `./README.md` as reference.

<!-- Team grid layout -->
<div class="team-grid">
    <!-- MANTVYDAS DELTUVA -->
    <!-- Member card -->
    <div class="member-card" style="--color: #44911B; --rotation: 15deg">
        <!-- Details container -->
        <div class="details-container">
            <!-- Avatar container -->
            <div class="avatar-container">
                <div class="avatar-wrapper">
                    <div class="avatar-border"></div>
                    <!-- Avatar -->
                    <img src="https://avatars.githubusercontent.com/u/128229836?v=4" als="Avatar" class="avatar"/>
                </div>
            </div>
            <!-- Text container -->
            <div class="text-container">
                <!-- Name -->
                <div class="name">Mantvydas</div>
                <!-- Surname -->
                <div class="surname">Deltuva</div>
                <!-- Role -->
                <div class="role">Lead Frontend Developer</div>
                <!-- Text -->
                <div class="text">It’s not a bug. It’s an undocumented feature. – Anonymous</div>
            </div>
        </div>
        <!-- Links container -->
        <div class="links-container">
            <!-- LinkedIn link -->
            <a href="https://www.linkedin.com/in/mantvydasdeltuva/" class="linkedin">
                <img src="../assets/linkedin.svg" alt="LinkedIn" class="linkedin-icon">
            </a>
            <!-- GitHub link -->
            <a href="https://github.com/mantvydasdeltuva" class="github">             
                <img src="../assets/github.svg" alt="GitHub" class="github-icon">
            </a>
        </div>
    </div>
    <!-- JUSTINAS TESELIS -->
    <div class="member-card" style="--color: #4E2A84; --rotation: 60deg">
        <div class="details-container">
            <div class="avatar-container">
                <div class="avatar-wrapper">
                    <div class="avatar-border"></div>
                    <img src="https://avatars.githubusercontent.com/u/156369263?v=4" als="Avatar" class="avatar"/>
                </div>
            </div>
            <div class="text-container">
                <div class="name">Justinas</div>
                <div class="surname">Teselis</div>
                <div class="role">Frontend Developer</div>
                <div class="text">Student. Software Developer. Graphic Designer.</div>
            </div>
        </div>
        <div class="links-container">
            <a href="https://www.linkedin.com/in/justinasteselis/" class="linkedin">
                <img src="../assets/linkedin.svg" alt="LinkedIn" class="linkedin-icon">
            </a>
            <a href="https://github.com/justinnas/" class="github">             
                <img src="../assets/github.svg" alt="GitHub" class="github-icon">
            </a>
        </div>
    </div>
</div>

<!-- CSS -->
<style>
    .team-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(24rem, 1fr));
        justify-items: center;
        gap: 1rem;
        width: 100%;
        margin: 0 auto;
    }

    .member-card {
        position: relative;
        width: 100%;
        max-width: 26rem;
        aspect-ratio: 2 / 1;
    }

    .details-container {
        position: absolute;
        display: flex;
        flex-direction: row;
        width: 100%;
        height: 100%;
        border-radius: 0.3rem;
        background-color: #161618;
        box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
    }

    .avatar-container {
        display: flex;
        justify-content: center;
        align-items: center;
        width: 50%;
    }

    .avatar-wrapper {
        position: relative;
        width: 80%;
        height: 80%;
        border-radius: 100%;
    }

    .avatar-border {
        position: absolute;
        width: 100%;
        height: 100%;
        rotate: var(--rotation);
        box-sizing: border-box;
        border: 0.3rem solid var(--color);
        border-radius: 100%;
        border-top-color: transparent;
        border-right-color: transparent;
    }

    .avatar {
        position: absolute;
        top: 7.5%;
        left: 7.5%;
        margin: 0;
        width: 85%;
        height: 85%;
        border-radius: 100%;
    }

    .text-container {
        display: flex;
        flex-direction: column;
        width: 45%;
        margin: 2rem 0;
    }

    .name,
    .surname {
        font-family: 'Gill Sans MT';
        font-size: 1.4rem;
        font-weight: bold;
        line-height: 1.4rem;
        color: #EBEBEC;
    }

    .role {
        font-family: 'Gill Sans MT';
        font-size: 0.9rem;
        font-weight: bold;
        line-height: 1.6rem;
        color: var(--color);
    }

    .text {
        margin-top: 0.4rem;
        font-size: 0.7rem;
    }

    .links-container {
        position: absolute;
        display: flex;
        flex-direction: row;
        width: 100%;
        height: 100%;
        transition: background-color 0.2s ease-in-out, backdrop-filter 0.2s ease-in-out;
    }

    .links-container:hover {
        background-color: rgba(22, 22, 24, 0.8);
        backdrop-filter: blur(2px);
    }

    .linkedin {
        display: flex;
        justify-content: center;
        align-items: center;
        width: 50%;
        height: 100%;
        visibility: hidden;
    }

    .linkedin-icon {
        width:42px;
        height:42px;
        transition: transform 0.3s ease-in-out;
    }

    .linkedin:hover .linkedin-icon {
        transform: scale(1.5)
    }

    .github {
        display: flex;
        justify-content: center;
        align-items: center;
        width: 50%;
        height: 100%;
        visibility: hidden;
    }

    .github-icon {
        width:42px;
        height:42px;
        transition: transform 0.3s ease-in-out;
    }

    .github:hover .github-icon {
        transform: scale(1.5)
    }

    .links-container:hover .linkedin {
        visibility: visible;
    }

    .links-container:hover .github {
        visibility: visible;
    }
</style>