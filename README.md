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

##Acknowledgement.
Atlassian for Startups. CoderdojoStPaul2, part of Mother Divine Seattle, an incorporated Non Profit Corporation, HQ in Seattle is a Non Profit partner of Microsoft Inc and Atlassian Inc, Twilio Inc.
