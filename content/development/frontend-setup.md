---
title: Front-End Setup
description: A guide to setting up the front-end environment for kath project development.
tags: 
    - Development
    - Front-End
    - Setup
    - Guide
draft: false
date: 2025-01-22
---

This guide walks you through the process of setting up and running a Front-End development environment using **Vite**, a fast and lean tool, alongside **React** for building the user interface, and **TypeScript** for adding static typing to your application.

---

## Step 1 - Install Node.js and npm

1. **Check Node.js Version**
    
    Ensure that you have Node.js installed. Run the following command to check Node.js version.

    ```bash
    node -v
    ```

2. **Check npm Version**

    Run the following command to check npm version.

    ```bash
    npm -v
    ```

>[!info]
>If Node.js is not installed, you can download it from [Node.js official website](https://nodejs.org/). Node Package Manager will come bundled with Node.js.

---

## Step 2 - Set Up Your Development Environment

1. **Open VS Code**

    If you haven't already installed Visual Studio Code, you can download it from [Visual Studio Code official website](https://code.visualstudio.com/).

2. **Open Project Folder**
   
   In the VS Code window, open the _Command Palette_ `Ctrl+Shift+P`. Type `>File: Open Folder...` and navigate to your project folder located on your system. Open whole GitHub repository (root).

3. **Navigate to Front-End Application**

    Open the _New Terminal_ `` Ctrl+Shift+` `` and navigate Front-End application directory.

    ```bash
    cd app/front_end
    ```

4. **Install Dependencies**

    Run the following command to install all necessary packages.

    ```bash
    npm install
    ```

    Wait for the dependencies to be installed.

---

## Step 3 - Start the Development Server

Once your dependencies are installed, start the development server with the following command.

```bash
npm run dev
```

> [!info]
> This will launch the React application using Vite on http://localhost:5173/. To stop the development server, simply press `Ctrl+C` in the VS Code terminal.

> [!success]
> Congratulations on starting the Front-End development server! This is a great step towards contributing to the Kath project. Happy coding and development! Remember to keep your code organized, break down tasks into manageable parts, and continuously test your components.

> [!question]
> If you encounter any issues or need guidance, feel free to reach out to your team lead!