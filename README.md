+16
Lines changed: 16 additions & 0 deletions


Original file line number	Original file line	Diff line number	Diff line change
@@ -1,2 +1,18 @@
# design-patterns
A collection of design patterns, invented by me, marketed by the Trio(TM), on CoreDump.
Per-Observer
State Pattern
ParaGenerator
Generator
Iterator
Reactor
Imploder
Disassembler
Parser
CAS
Balancer
Positifier
Repl
Optimism
Wall
Query

# Perobserver Pattern

![Perobserver UML](perobserver.png)

## Intent

**Perobserver** is a behavioral persistence pattern in which the state of an
observed object is **automatically persisted** whenever that state changes.

Persistence is triggered by events or value changes and may target JSON,
serialization formats, databases, or other data structures.

---

## Motivation

In many systems, persistence is handled by:
- explicit `save()` calls,
- embedded database logic inside domain objects, or
- ad-hoc checkpoints scattered throughout code.

These approaches tightly couple business logic to storage concerns and make
state consistency fragile.

The **Perobserver Pattern** decouples **state mutation** from **state
persistence** while ensuring that persistence happens *automatically and
deterministically*.

---

## Definition

> **Perobserver** is a design pattern where an observer automatically persists
> the state of an observed object whenever its state changes, without embedding
> persistence logic directly into the object’s domain behavior.

---

## Structure

The pattern consists of:

### Subject
- Owns and mutates state
- Emits change events
- May optionally trigger persistence internally (variant)

### PerObserver
- Listens for state changes
- Persists the subject’s state
- Encapsulates storage and serialization logic

### ConcretePerObserver
- Implements persistence to a specific medium:
  - JSON
  - Serialized objects
  - Relational or NoSQL databases
  - In-memory data structures
  - Event logs

---

```markdown
## Acknowledgements

We gratefully acknowledge **Atlassian for Startups** for providing tools and
resources that support early-stage development and collaborative innovation.

**CoderdojoStPaul2**, part of **Mother Divine Seattle**, an
incorporated non-profit corporation headquartered in Seattle.  
CoderdojoStPaul2, Mother Divine Seattle is a non-profit partner of **Microsoft Inc.**,
**Atlassian Inc.**, and **Twilio Inc.**, supporting education, community learning,
and technology empowerment.
```
