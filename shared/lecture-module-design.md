# Lecture Design: Modular Blocks

## Overview
Lecture content is designed around **modular 25-minute blocks** rather than fixed session lengths. Each week consists of **6 blocks (~150 minutes total)**. The same content is delivered regardless of schedule format, only the grouping changes.

| Format | Sessions/Week | Blocks/Session | Total Blocks |
|--------|:-------------:|:--------------:|:------------:|
| 2×75   | 2             | 3              | 6            |
| 3×50   | 3             | 2              | 6            |

## Session Groupings

**2×75 Format:**
| Session | Blocks    |
|---------|-----------|
| A       | [1] [2] [3] |
| B       | [4] [5] [6] |

**3×50 Format:**
| Session | Blocks    |
|---------|-----------|
| A       | [1] [2]  |
| B       | [3] [4]  |
| C       | [5] [6]  |

The content is identical — only the packaging changes. Materials are written once.

---

## Block Structure: Pre-AI Weeks
These weeks focus on building foundational programming skills from scratch.

| Block | Purpose     | Description                                                        | Example                                                              |
|:-----:|-------------|--------------------------------------------------------------------|----------------------------------------------------------------------|
| 1     | **Concept** | Introduce the idea, why it matters, show briefly in another language | "Iteration lets you repeat operations across data without writing redundant code" |
| 2     | **Demo**    | Instructor live-codes in Python                                     | Build a for loop that computes cumulative load values                |
| 3     | **Practice**| Students try a small exercise                                       | "Write a loop that sums rainfall data from a list"                   |
| 4     | **Deepen**  | Engineering application, edge cases, common mistakes                | What happens with an empty list? Nested loops for 2D grid data?      |
| 5     | **Exercise**| Independent problem, slightly harder                                | More complex problem, less scaffolding                               |
| 6     | **Bridge**  | Review, connect to next topic, preview                              | "Next: functions — so you don't rewrite that loop every time"        |

## Block Structure: Post-AI Weeks
These weeks integrate AI tools into the workflow, shifting from writing-from-scratch to plan-prompt-evaluate cycles.

| Block | Purpose              | Description                                                   | Example                                                              |
|:-----:|----------------------|---------------------------------------------------------------|----------------------------------------------------------------------|
| 1     | **Concept**          | New concept or AI technique                                    | "How to specify requirements before prompting"                       |
| 2     | **Plan**             | Students write a spec/outline before touching AI               | "What inputs, outputs, edge cases, and constraints does this script need?" |
| 3     | **Prompt + Critique**| Live prompt, class evaluates output together                   | Instructor prompts, code goes on screen, class finds issues          |
| 4     | **Fix**              | Students make targeted corrections                             | "The AI missed the unit conversion — fix it"                         |
| 5     | **Apply**            | Engineering application with AI as tool                        | Full prompt-evaluate-fix cycle on a domain problem                   |
| 6     | **Bridge**           | Review, patterns observed, preview                             | "Notice how specifying output format upfront saved a re-prompt"      |

---

## Module Files
Individual 25-minute modules live in `shared/modules/` and are referenced from each semester's schedule. Each module file should specify:

- **Block type** (Concept, Demo, Practice, etc.)
- **Topic**
- **Learning outcome(s)** addressed
- **Content/activity description**
- **Materials needed** (slides, starter code, datasets, etc.)

See `shared/modules/` for the module library.
