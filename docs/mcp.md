# MCP

## What it is

- FortyGuard MCP is an interface that lets AI assistant use FortyGuard for me.
- I used Claude Code in VS Code.

## What I did
- Asked for my credit balance.
- Ran MCP Quick Start example.

```text
Get the environmental conditions for Phoenix, Arizona at latitude 33.4484 and longitude -112.074 for September 20, 2025, using a reference temperature of 35 °C.
```
- Tested for the same Phoenix heatmap I ran through the API, and the same Chicago area I mapped in the dashboard.

```text
Get the fortyguard heatmap for Phoenix, Arizona at corners (longitude, latitude): (-112.0783, 33.4448), (-112.0697, 33.4448), (-112.0697, 33.4520), (-112.0783, 33.4520) for 2026-07-10 at 14:00 time, single hour, 100 x 100 granularity.
```
```text
Get the fortyguard heatmap for Chicago, Illinois at corners (longitude, latitude): (-87.6300, 41.8700), (-87.6150, 41.8700), (-87.6150, 41.8850), (-87.6300, 41.8850) for 2026-07-10 at 14:00 time, single hour, 100 x 100 granularity.
```


## Results
- It told me the cost before spending credits.
- It gave the same Phoenix result as the API (40.87C).
- Chicago was refused again and cost nothing.


## Findings
- **Client Setup did not match the guide.** The `claude` command didn't work on my VS code terminal. I added the server manually in claude code chat.
- **The docs list 9 tools, I see 11.** The extra ones are credit_balance (read-only) and monitoring (destructive).
- **My credits were only visible here.** I could not find them in the dashboard or the API quick start.
- **I only get the lowest, highest and average temperature.**