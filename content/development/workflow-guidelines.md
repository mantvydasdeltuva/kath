---
title: Workflow Guidelines
description: This section outlines the workflow guidelines for development tasks, including Jira automation, story assignment, naming conventions, and pull request descriptions.
tags: 
    - Development
    - Front-End
    - Back-End
    - Guide
draft: false
date: 2025-01-27
---

This section provides a detailed overview of the workflow guidelines for the development team, ensuring a streamlined and efficient process for managing tasks, code, and collaboration. These guidelines cover Jira automation, story assignment, naming conventions, and pull request descriptions, all aimed at maintaining consistency and clarity throughout the development lifecycle.

---

## Assigning Stories

Before starting work on an story, **always assign it to yourself** in Jira to avoid conflicts with other team members. This prevents others from accidentally working on the same story. If you are not actively working on an story or do not have time to handle it, unassign yourself to make it available for others. This ensures that tasks are distributed efficiently and progress is not blocked unnecessarily.

> [!warning]
> **Do not hold a story** unless you are actively working on it!

---

## Automation in Jira

To streamline task management, _Jira Automation_ has been integrated to update story statuses based on branch and pull request activities. The automation process includes the following:

- When a **branch is created**, the corresponding story is automatically moved to _In Progress_.
- When a **pull request is created**, the story is moved to _In Review_.
- When a **pull request is merged**, the story is moved to _Done_.
- If a **pull request is declined**, the story is moved back to _In Progress_.

> [!tip] Benefits
> This automation ensures that the status of tasks in Jira always reflects their current state in the development process.

---

## Naming Conventions

To maintain consistency across the codebase and use _Jira Automation_, the following naming conventions must be followed:

- **Branch Name:** [Name First Letter][Surname First Two Letters]/[Story Label From Jira]

> [!example] Example of _Branch Name_ for Mantvydas Deltuva in Front-End Team
> ```bash
> git checkout -b MDE/KFE-57
> git push -u origin MDE/KFE-57
> ```

- **Commit Message:** [Name First Letter][Surname First Two Letters]/[Story Label From Jira] [Short Description]

> [!example] Example of _Commit Message_ for Mantvydas Deltuva in Front-End Team
> ```bash
> git commit -m "MDE/KFE-57 Implemented Download Button"
> ```

- **Pull Request Title:** [Name First Letter][Surname First Two Letters]/[Story Label From Jira]

> [!example] Example of _Pull Request Title_ for Mantvydas Deltuva in Front-End Team
> ```bash
> MDE/KFE-57
> ```

> [!warning]
> Front-End and Back-End story label prefixes are different. For Front-End it is `KFE` and for Back-End - `KBE`. 

---

## Pull Request Description Format

The pull request description must follow a specific format to ensure clarity and traceability of changes.

**Initial Pull Request Description:**
- Header: Initial (YYYY-MM-DD)
- Bullet points: List of commits that changed the code. Also provide a description of what this feature enables or changes.

> [!example Initial Pull Request Example]
> ```markdown
> # Initial (2025-01-25)
> - [MDE/KFE-57 Implemented Download Button](https://github.com/mantvydasdeltuva/kath/commit/
>   6c3abc9119e726370bb4fcdec02010119761c8b6) End users are able to download specified file.
> - [MDE/KFE-57 Refactored Button Layout](https://github.com/mantvydasdeltuva/kath/commit/
>   1c3fgjd896dh93370bb4fcdec02010119761c8b6) Button design is visually appealing. 
> ```

If changes are present, update the pull request description as follows.

**Updated Pull Request Description**:
- Header: Changes (YYYY-MM-DD)
- Bullet points: List of commits related to the changes. Also provide a description of what this feature enables or changes.

> [!example Updated Pull Request Example]
> ```markdown
> # Initial (2025-01-25)
> - [MDE/KFE-57 Implemented Download Button](https://github.com/mantvydasdeltuva/kath/commit/
>   6c3abc9119e726370bb4fcdec02010119761c8b6) End users are able to download specified file.
> - [MDE/KFE-57 Refactored Button Layout](https://github.com/mantvydasdeltuva/kath/commit/
>   1c3fgjd896dh93370bb4fcdec02010119761c8b6) Button design is visually appealing. 
> # Changes (2025-01-27)
> - [MDE/KFE-57 Fixed Colors](https://github.com/mantvydasdeltuva/kath/commit/
>   363abc9119e435370bb4f346c02010119761c8b6) Button has correct design colors.
> ```

---

## Questions and Concerns

If you have any questions regarding an story or how to implement it, please reach out to your teams **Lead Developer**. Open communication is key to resolving issues quickly and effectively.