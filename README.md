# Docker Network Simulator

A lightweight Docker-based environment that simulates a containerized network with two isolated nodes — **Station** and **Tester** — connected over a custom bridge network. Designed for experimenting docker inter-container communication.

---

## Technology Used

* Python
* Docker

---

## Project Overview

This project sets up a self-contained network environment inside Docker using Docker Compose. Two containers are placed on a custom subnet and can communicate with each other using either their static IP addresses or container names (via Docker's built-in DNS).

The setup mirrors a typical networking lab environment where:
- One container acts as a **server/station**
- Another acts as a **client/tester**
- Both share the same virtual network and can exchange data

---

## Docker Architecture

```
Host Computer
└── Docker Engine
    └── lab-network (192.168.100.0/24)
        ├── station  (192.168.100.2)
        │   └── python:3.11
        └── tester   (192.168.100.3)
            └── python:3.11
```

Both containers run `python:3.11` (Debian-based), giving access to a full Linux shell and Python out of the box — no Dockerfile required.

---


## Getting Started

### 1. Start the containers

```bash
docker compose up -d
```

### 2. Verify containers are running

```bash
docker ps
```

### 3. Open a shell into either container

```bash
bash connectStation.sh
bash connectTester.sh
```

### 4. Tear down

```bash
docker compose down
```

---
