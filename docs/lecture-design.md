

# Lecture Design: Modular Blocks

## Overview

Lecture content is designed around **modular 25-minute modules** slotted into **6 blocks per week** (~150 minutes total). A **block** is a time slot on the schedule. A **module** is the content that fills it. The same content is delivered regardless of schedule format, only the grouping changes.

| Format | Sessions/Week | Blocks/Session | Total Blocks |
|--------|:-------------:|:--------------:|:------------:|
| 2×75   | 2             | 3              | 6            |
| 3×50   | 3             | 2              | 6            |

Over 14 weeks, that yields **84 total blocks**. Three blocks per week are reserved for fixed recurring modules (Recall, Interactive, Bridge), leaving **42 blocks for instructional content**.

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

## Typical Weekly Layout

```
Block 1: recall        (fixed)
Block 2: concept | content | demo
Block 3: concept | content | demo
Block 4: interactive   (fixed)
Block 5: concept | content | demo
Block 6: bridge        (fixed)
```

## Module Types

Six module types, each with a distinct instructional purpose:

| Type | Shorthand | Frequency | Purpose |
|---|---|---|---|
| Recall + Code Reading | `recall` | Weekly, Block 1 | Retrieval practice and code comprehension |
| Concept | `concept` | ~2-3 per week | Teach a programming construct through explanation and live coding |
| Content | `content` | ~0-2 per week | Transfer knowledge about tools, practices, or frameworks |
| Demo | `demo` | As needed | Guided walkthrough of a tool or environment |
| Interactive | `interactive` | Weekly, rotating | Applied exercise in one of three rotating formats |
| Bridge + Reflection | `bridge` | Weekly, Block 6 | Review, forward connection, and student feedback |

> See `module-types.md` for detailed descriptions of each module type.

**Distinguishing Concept, Content, and Demo:**

- **Concept**: "Here is how a for loop works." Programming construct. Instructor live-codes. Students build a transferable skill.
- **Content**: "Here is how LLMs generate code and where they fail." Knowledge transfer. Slides, discussion, frameworks. Students build judgment.
- **Demo**: "Here is how to set up a virtual environment." Tool proficiency. Instructor shows, students follow along. Students build workflow.

## Module Files

Individual 25-minute modules live in `shared/modules/` and are referenced from each semester's schedule. Each module file should specify:

- **Module type** (`concept`, `content`, `demo`, `recall`, `interactive`, `bridge`)
- **Topic**
- **Learning outcome(s)** addressed
- **Content/activity description**
- **Materials needed** (slides, starter code, datasets, etc.)

> See `shared/modules/` for the module library.