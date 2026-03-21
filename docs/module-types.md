# Block Types

## Overview

All course content is delivered through **25-minute modules** slotted into **6 blocks per week** (~150 minutes total). Three blocks are fixed each week (Recall, Interactive, Bridge). The remaining three are filled from a pool of content-oriented types (Concept, Content, Demo) depending on the week's topics.

| Block Type | Shorthand | Frequency | Purpose |
|---|---|---|---|
| Recall + Code Reading | `recall` | Weekly, Block 1 | Retrieval practice and code comprehension |
| Concept | `concept` | ~2-3 per week | Teach a programming construct through explanation and live coding |
| Content | `content` | ~0-2 per week | Transfer knowledge about tools, practices, or frameworks |
| Demo | `demo` | As needed | Guided walkthrough of a tool or environment |
| Interactive | `interactive` | Weekly, rotating | Applied exercise in one of three rotating formats |
| Bridge + Reflection | `bridge` | Weekly, Block 6 | Review, forward connection, and student feedback |

### Typical Weekly Layout

```
Block 1: recall
Block 2: concept | content | demo
Block 3: concept | content | demo
Block 4: interactive
Block 5: concept | content | demo
Block 6: bridge
```

### Distinguishing Concept, Content, and Demo

- **Concept**: "Here is how a for loop works." Programming construct. Instructor live-codes. Students build a transferable skill.
- **Content**: "Here is how LLMs generate code and where they fail." Knowledge transfer. Slides, discussion, frameworks. Students build judgment.
- **Demo**: "Here is how to set up a virtual environment." Tool proficiency. Instructor shows, students follow along. Students build workflow.

## Recall + Code Reading

Retrieval practice followed by a code comprehension exercise. Runs every week as Block 1.

| Activity | Time | Description |
|---|---|---|
| Quiz | 8 min | 5 questions such as: predict the output, spot the error, fill the blank, conceptual choice. No question exceeds 90 seconds. Covers previous week's material. |
| Transition | 2 min | Code snippet goes on the projector. |
| Individual Trace | 5 min | Students trace variable values, predict the final output, and write a one-sentence summary of what the code does. No running the code. |
| Discussion | 3 min | Students compare predictions and reconcile differences. |
| Reveal + Debrief | 7 min | Instructor walks through the correct trace, reveals output, discusses surprises or common misreadings. |

**Notes**: Code snippets can be Python, pseudocode, or another language (JavaScript, MATLAB) to reinforce that concepts are language-agnostic.

## Concept

Introduce a programming construct, demonstrate it live, and let students try it briefly. The repeatable core teaching unit.

| Activity | Time | Description |
|---|---|---|
| Introduce | 8 min | What is this construct? Why does it matter? Where does it appear across languages? Brief visual or pseudocode example. |
| Live Code | 10 min | Instructor builds a working example in Python from scratch. Engineering context where possible. Narrate decisions aloud. |
| Mini-Exercise | 5 min | Students attempt a small, tightly scoped variation of what was just demonstrated. |
| Connect | 2 min | Tie this construct to what came before and what comes next. Surface one common mistake or misconception. |

**Notes**: A single topic (e.g., "looping") may span multiple Concept modules: one on `for`, one on `while`, one on advanced patterns. Each follows the same internal structure. The Introduce segment should reference at least one non-Python representation (pseudocode, flowchart, or another language).

## Content

Transfer knowledge that is conceptual, strategic, or framework-oriented rather than syntax-oriented. More slides and discussion, less live coding.

| Activity | Time | Description |
|---|---|---|
| Context | 3 min | Why this topic matters. Situate it in the course arc or in professional practice. |
| Core Material | 15 min | Instructor-led presentation: frameworks, mental models, examples, case studies. Slides, diagrams, or worked examples on the projector. |
| Discussion | 5 min | Instructor poses a concrete question or scenario. Students respond via open discussion, think-pair-share, or quick poll. |
| Takeaways | 2 min | Summarize 2-3 key points. Provide a reference or resource for further reading. |

## Demo

Guided walkthrough of a tool, environment, or workflow. Instructor demonstrates, students follow along on their own machines.

| Activity | Time | Description |
|---|---|---|
| Context | 3 min | What is this tool? What problem does it solve? When would you reach for it? |
| Instructor Walkthrough | 10 min | Step-by-step demonstration on the projector. Deliberate pacing. Narrate what you are clicking/typing and why. |
| Student Follow-Along | 10 min | Students replicate the same steps on their own machines. Instructor circulates. |
| Troubleshoot | 2 min | Address common issues surfaced during follow-along. Provide a cheat sheet or reference link. |

**Notes**: Demo modules appear infrequently and cluster near the beginning and end of the semester. Provide written step-by-step instructions so students who fall behind can catch up outside class.

## Interactive

Applied exercise in one of three rotating formats. Runs every week, cycling on a 3-week rotation.

### Format A: Bug Hunt

| Activity | Time | Description |
|---|---|---|
| Setup | 3 min | Distribute the script and expected output. Rules: no AI tools, no print-debugging for the first 5 minutes. |
| Read + Diagnose | 10 min | Students read the code and identify logic error(s). After 5 min, they may run and test. |
| Debrief | 10 min | Instructor reveals the bug(s), discusses why they are easy to miss, connects to broader patterns. |
| Wrap | 2 min | One-sentence takeaway. |

### Format B: Refactor

| Activity | Time | Description |
|---|---|---|
| Setup | 3 min | Distribute working but poorly written code. Provide constraints. |
| Refactor | 12 min | Students improve the code without changing its behavior. |
| Share + Compare | 8 min | 2-3 students show their version. Class discusses tradeoffs. |
| Wrap | 2 min | One-sentence takeaway on code quality. |

### Format C: Engineering Scenario Discussion

| Activity | Time | Description |
|---|---|---|
| Setup | 3 min | Project an engineering scenario on screen. Form groups of 3-4. No IDE. |
| Decompose | 12 min | Groups answer 5 fixed guiding questions: (1) What are the inputs? (2) What are the outputs? (3) What are the steps? (4) What could go wrong? (5) What would you ask AI to help with? |
| Present | 8 min | 1-2 groups share their decomposition. Class compares approaches. |
| Wrap | 2 min | Instructor connects the decomposition to upcoming programming topics. |

**Notes**: Bug Hunt and Refactor exercises should use engineering-relevant code rather than abstract puzzles.

## Bridge + Reflection

Review the week's material, connect forward to the next topic, and collect structured student feedback. Runs every week as Block 6.

| Activity | Time | Description |
|---|---|---|
| Review | 8 min | Summarize the week's key concepts. Highlight connections between modules. |
| Preview | 5 min | Introduce next week's topic at a high level. Frame it as a question or problem. |
| Reflection | 10 min | Students complete a fixed 3-question form: (1) One thing that clicked this week. (2) One thing that is still fuzzy. (3) One thing you would do differently on this week's exercises. |
| Dismiss | 2 min | Closing remarks. |

**Notes**: Reflection uses the same form every week. Read responses before the next week. Open Block 1 with "Several of you mentioned X was unclear - let's revisit that" to close the feedback loop visibly. The Preview segment should create mild anticipation, not front-load complexity.