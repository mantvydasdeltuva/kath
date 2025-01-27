---
title: Documentation
description: A guide to setting up the environment for kath project documentation development.
tags: 
    - Development
    - Front-End
    - Back-End
    - Setup
    - Guide
draft: false
date: 2025-01-24
---

This guide explains how to set up the environment and start contributing to the `documentation` branch of the GitHub repository using _Quartz v4_ static-site generator that simplifies Markdown-based documentation.

---

## Step 1 - Setup Instructions

1. **Clone the Repository**

    ```bash
    git clone https://github.com/mantvydasdeltuva/kath.git
    ```

2. **Switch to the `documentation` Branch**

    ```bash
    git checkout documentation
    ```

3. **Install Dependencies**

    Run the following command to install all necessary dependencies.

    ```bash
    npm install
    ```

4. **Run the Local Development Server**
   
    Start the _Quartz_ development server to preview changes locally.
   
    ```bash
    npx quartz build --serve
    ```

> [!info]
> This will launch documentation on http://localhost:8080/. To stop the development server, simply press `Ctrl+C` in the VS Code terminal.

---

## Step 2 - Writing Documentation

1. **Markdown File -> Page**
    
    All documentation files should be written in Markdown (`.md`) and placed in the `content` directory. File names stand as paths in deployment. `index.md` files provide documentation to directories landing pages.

2. **Frontmatter Format**
   
    Begin each Markdown file with a _Frontmatter_ block to define metadata.

    ```md
    ---
    title: [Title of the Page]
    description: [Short Description of the Page]
    tags: 
        - [Tag1]
        - [Tag2]
    draft: [true or false]
    date: YYYY-MM-DD
    ---
    ```

> [!tip]
> When _Frontmatter_ field `show` is set to `false`, it disables the pages metadata from being displayed. Use only for special occasions like landing pages.

3. **Content Guidelines**

    - Use only _Heading_ `##` to structure your document. Before each _Heading_ add _Horizontal Rule_ `---`.
    - Add _Callouts_ `> [!tip]` for tips or important notes.
    - Provide _Code Blocks_ with _Syntax Highlighting_ using triple backticks `` ``` ``.
    - To fully utilize the provided enhanced Markdown capabilities, visit the [Quartz v4 official website](https://quartz.jzhao.xyz/features/).

> [!example] Example - Callouts
> ```md
> > [!question]
> > If you encounter any issues, reach out to your team lead!
> ```
>
> The example question callout markdown content in page is shown like this:
> 
> > [!question]
> > If you encounter any issues, reach out to your team lead!
> 
> It can also become collapsible.
> 
> ```md
> > [!info]+
> > This will launch the React application using Vite.
> ```
>
> The result would look like this:
> 
> > [!info]+
> > This will launch the React application using Vite.
>
> For more details, visit [Quartz v4 official website - Callouts](https://quartz.jzhao.xyz/features/callouts).

> [!example] Example - Code Blocks with Syntax Highlighting
> ``````md
> ```js showLineNumbers{5} title="example.js" {4} /number/
> function checkEvenOrOdd(number) {
>     if (number % 2 === 0) {
>         return `${number} is even.`;
>     } else {
>         return `${number} is odd.`;
>     }
> }
> ```
> ``````
>
> The example code block with syntax highlighting markdown content in page is shown like this:
> 
> ```js showLineNumbers{5} title="example.js" {4} /number/ 
> function checkEvenOrOdd(number) {
>     if (number % 2 === 0) {
>         return `${number} is even.`;
>     } else {
>         return `${number} is odd.`;
>     }
> }
> ```
>
> For more details, visit [Quartz v4 official website - Syntax Highlighting](https://quartz.jzhao.xyz/features/syntax-highlighting).

---

## Step 3 - Committing Changes

1. **Create a New Branch from `documentation`**
   
    First, ensure you're working on a separate branch based on the `documentation` branch.

    ```bash
    git checkout -b documentation/[page-name] documentation
    ```

2. **Stage and Commit Your Changes** 
   
    After making the necessary changes, stage and commit them.

    ```bash
    git add .
    git commit -m "documentation/[page-name] new page for [specific feature or section]"
    ```
3. **Push Changes to Your Branch**
   
    Push your changes to your remote branch (not directly to the `documentation` branch).

    ```bash
    git push origin [documentation/page-name]
    ```

4. **Create a Pull Request**
   
    Once your changes are pushed, create a _Pull Request_ from your branch into the `documentation` branch. **Direct pushes to the `documentation` branch are not allowed.**

> [!tip]
> Make sure to provide a clear description of your changes in the pull request so that reviewers can easily understand the updates. Also follow _Pull Request_ guidelines in [[workflow-guidelines#Pull Request Description Format|Workflow Guidelines]].

---

## Step 4 - Publishing

Once the changes are approved and merged into `documentation` branch, the documentation will automatically be built and deployed using _Quartz's_ static-site generation, _GitHub Actions_ and _GitHub Pages_. You can access the updated documentation through the [Kath official documentation website](https://docs.kath.lt/).

> [!success]
> Congratulations on setting up the documentation workflow! This is a great step towards contributing to the Kath project. Happy documenting!

> [!question]
> If you encounter any issues or need guidance, feel free to reach out to your team lead!