# NFL Pick'em Prediction

Advanced NFL game predictions using EPA (Expected Points Added) and custom WinScore calculations.

## Setup

1. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure environment variables in `.env`

4. Run the application:
```bash
python run.py
```

Visit: http://localhost:5000

## Features

- Team statistics visualization
- Matchup predictions with win probabilities
- Integration with nflfastR data
- Google Sheets integration

## Data Sources

- nflfastR: https://nflfastr.com/
- Custom Google Sheets calculations
