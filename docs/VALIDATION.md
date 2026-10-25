# Validation snapshot

Snapshot date: **October 25, 2026**.

## Private source application

The release candidate passed:

| Check | Result |
| --- | --- |
| Offline regression | 1,900 passed; 1 skipped; 4 network tests deselected |
| Compilation and imports | Passed |
| Server startup and health endpoint | Passed |
| Separate provider smoke | Historical AAPL data and native discovery returned results |
| Desktop workflow checks | Representative workflows exercised across all eight research modules |
| Updated robustness preview | Reviewed and accepted by the creator before release |

Production smoke checks subsequently confirmed app/navigation loading, a healthy endpoint, 751 AAPL daily bars loaded through OpenBB/yfinance, research discovery, 26 calculated rolling windows, and basic Play/Pause/timeline controls.

## Limits

- The test count concerns the private source application. The full suite is not included here and cannot be reproduced from this documentation-only showcase.
- The cloud verification browser lacked WebGL. Its control checks did not establish full 3D geometry, camera/hover, comparison-overlay smoothness, or rendering performance. Creator visual review is separate from those automated checks.
- Independent mobile visual coverage remains limited.
- Same-instance saved-record recovery was exercised. The free hosted filesystem does not establish durability across redeployments or replacement instances.
- Provider availability and historical coverage can change. An example's result is not a promise that every provider request will succeed.
- Passing software and accounting checks does not validate a profitable trading strategy.

## Public example

The standalone Python sample has four passing tests for completed outcomes, chronological stability, the final window, and invalid inputs. They validate only the sample. Run them with:

```bash
python -m unittest discover -s examples -p 'test_*.py' -v
```
