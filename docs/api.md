# API

## What it is
- The same temperature data, asked for with API instead of a map. I sent an area, a date and a time then waited and got the answer.

## What I did
- Tested quick start example (Manhattan): refused.
- Tested Chicago three times with different dates: refused.
- Tested Phoenix: worked in 50.1 seconds.

_NOTE: Refused requests don't cost credits as stated in the `quick start` and confirmed during testing._

## Findings
- **Quick start example was refused** using my API key.
- **The dashboard covers Chicago but the API does not.** I found no list of covered places.
- **Units differ.** The API gives Celsius, the dashboard gives Fahrenheit.
- **The heatmap of Phoenix is flat.** Only shows the same temperature (40.87C).