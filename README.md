# UniSpyServer (GeneralsX Official Online Server)

UniSpyServer is an open-source GameSpy v1 and v2 backend/server emulation adapted for **Command & Conquer: Generals** and **Generals: Zero Hour** (GeneralsX).

This repository features a unified and self-contained Docker stack designed for seamless server deployment.

> This project is a fork of [GameProgressive/UniSpyServer](https://github.com/GameProgressive/UniSpyServer). We express our sincere gratitude to the original creators and contributors for providing the foundational codebase.

---

## 🚀 How to Run the Server (Docker)

The project provides a self-contained unified Docker image (`fbraz3/unispy-python`), allowing you to launch the full server stack using Docker Compose.

Sample configuration files for local or production deployment are located in the [`docker/`](docker/) directory.

### 1. Copy Deployment Files
Copy the `docker/` folder or its contents to your target server environment:
```bash
cp -r docker /data/docker/gamespy-generals
cd /data/docker/gamespy-generals
```

### 2. Mandatory Configuration Steps ⚠️

Before launching the server, you must set up your environment configuration file, update default credentials, and set a unique server identifier:

1. **Create Environment File (`.env`)**:
   Copy [`docker/.env.example`](docker/.env.example) to `.env`:
   ```bash
   cp .env.example .env
   ```

2. **Update Passwords in `.env` and `config.json`**:
   Replace **all** instances of `CHANGEME_ASAP` with your secure custom passwords:
   - File `.env` (copied from [`docker/.env.example`](docker/.env.example)): Set `POSTGRES_PASSWORD` and `REDIS_PASSWORD`.
   - File [`config.json`](docker/config.json): Update password fields in the `postgresql`, `mongodb`, and `redis` sections.

3. **Generate a Unique Server UUID (`server_id`)**:
   - Open [`config.json`](docker/config.json).
   - Replace the `server_id` value across all listed services with a newly generated UUID v4 unique to your server instance (e.g., generated using `uuidgen` or `python3 -c "import uuid; print(uuid.uuid4())"`).

### 3. Launch the Docker Stack

To start all containers (PostgreSQL, Redis, Backends, and GameSpy protocol Frontends):

```bash
docker compose up -d
```

---

## 🛠️ Building the Docker Image Manually (Optional)

If you modify the Python source code and wish to build the container image manually, run the following command from the repository root:

```bash
docker build -f docker/Dockerfile -t fbraz3/unispy-python .
```

---

## 🌐 DNS Configuration (DNSmasq / Hosts)

To route in-game client traffic to your UniSpy server:
- The [`docker/dnsmasq.conf`](docker/dnsmasq.conf) file contains the configuration required to resolve `*.gamespy.com` domains to your server IP address.
- Alternatively, you can configure your authoritative DNS server or client `hosts` file to resolve GameSpy domains directly.

---

## 📁 Repository Structure

- **`docker/`**: Docker deployment assets (Compose file, `.env`, `Dockerfile`, configurations, and database initialization schema).
- **`src/`**: Python server source code (FastAPI backend routers, GameSpy protocol handlers, etc.).
- **`common/`**: Shared data structures and configuration loaders.
- **`log/`**: Server runtime logs directory.

---

## 🙏 Credits & Acknowledgments

This repository is built upon [GameProgressive/UniSpyServer](https://github.com/GameProgressive/UniSpyServer). Special thanks to the original authors and maintainers for their hard work and dedication to preserving classic GameSpy multiplayer services.

---

## 📝 License
Refer to the [LICENSE](LICENSE) file for usage and distribution details.
