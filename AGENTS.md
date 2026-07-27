# UniSpyServer Project Guidelines

UniSpyServer is an open-source GameSpy v1 and v2 backend and frontend protocol emulation server designed for **Command & Conquer: Generals** and **Generals: Zero Hour** (GeneralsX).

---

## Architecture

The project consists of a FastAPI backend core and multiple asyncio/socket-based frontend protocol emulators:

- **`docker/`**: Deployment assets (`docker-compose.yml`, `Dockerfile`, `.env.example`, `config.json`, `dnsmasq.conf`, database initialization scripts).
- **`src/backends/`**: FastAPI routers, SQLAlchemy ORM models, database repositories, and service business logic.
- **`src/frontends/gamespy/protocols/`**: GameSpy protocol frontends:
  - `chat`: IRC / GameSpy chat server (port `6667`)
  - `game_status`: Game status reporting service (port `29920`)
  - `presence_connection_manager` (`pcm`): Player authentication & connection management (port `29900`)
  - `presence_search_player` (`psp`): Player lookup service (port `29901`)
  - `query_report` (`qr`): Game server query & heartbeat listener over UDP (port `27900`)
  - `server_browser` (`sb`): Master server browser & server list queries (ports `28900`, `28910`)
  - `natneg`: UDP NAT negotiation service (port `27901`)
  - `game_traffic_relay` (`gtr`): Game traffic relay service
  - `web_services` (`web`): HTTP/REST endpoints for GameSpy web protocols (Sake, Auth, Racing) (port `8081`)
- **`common/`**: Shared configuration loaders (`config.json`), database initialization schemas (`UniSpy_pg.sql`), and certificates.

---

## Code Style & Guidelines

- **Python Version**: Python 3.12+
- **Frameworks & Libraries**: FastAPI, SQLAlchemy (v2.0+), Pydantic, Redis asyncio.
- **Testing Requirement**: Every feature or bug fix must include corresponding unit tests in `src/backends/tests/` or `src/frontends/tests/`.
- **Imports & Dependencies**: Keep imports organized and explicit. Ensure dependencies added to `src/requirements.txt` match runtime container requirements.

---

## Commit Message Conventions

This project strictly follows the **Conventional Commits specification (v1.0.0)** formatted as `[type]([scope]): [subject]`.

- **Types**: `feat`, `fix`, `perf`, `docs`, `style`, `refactor`, `test`, `build`, `ci`.
- **Scopes**:
  - `core`: Core libraries (`UniSpy.Server.Libraries.Core`)
  - `cdkey`: CDKey service (`UniSpy.Server.CDKey`)
  - `chat`: Chat protocol (`UniSpy.Server.Chat`)
  - `gs`: Game Status protocol (`UniSpy.Server.GameStatus`)
  - `gtr`: Game Traffic Relay (`UniSpy.Server.GameTrafficRelay`)
  - `nn`: NAT Negotiation (`UniSpy.Server.NatNegotiation`)
  - `pcm`: Presence Connection Manager (`UniSpy.Server.PresenceConnectionManager`)
  - `psp`: Presence Search Player (`UniSpy.Server.PresenceSearchPlayer`)
  - `qr`: Query Report (`UniSpy.Server.QueryReport`)
  - `sb`: Server Browser (`UniSpy.Server.ServerBrowser`)
  - `ws`: Web Services (`UniSpy.Server.WebServer`)
- **Subject Formatting**: Use imperative, present tense ("add", not "added"), lowercase, no trailing period.

---

## Build, Run & Test Commands

- **Local Docker Launch**:
  ```bash
  cd docker
  cp .env.example .env
  docker compose up -d
  ```
- **Build Docker Image Manually**:
  ```bash
  docker build -f docker/Dockerfile -t fbraz3/unispy-python .
  ```
- **Run Unit Tests**:
  ```bash
  python3 -m unittest discover -s src -p "*_tests.py"
  ```
