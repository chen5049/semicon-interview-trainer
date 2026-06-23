# Contributing

Thank you for helping improve Semicon Interview Trainer.

## Good contribution types

- Add technically accurate questions
- Improve Traditional Chinese terminology
- Add references to reliable semiconductor textbooks or vendor documentation
- Add tests
- Improve accessibility and usability
- Add new process modules

## Development setup

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e .
python -m pip install pytest
pytest
```

On Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -e .
python -m pip install pytest
pytest
```

## Pull requests

1. Keep changes focused.
2. Add or update tests when changing behaviour.
3. Verify Traditional Chinese terminology.
4. Do not include confidential company process parameters.
5. Do not include proprietary interview questions copied from employers.
