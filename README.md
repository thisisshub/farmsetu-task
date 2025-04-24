# FarmSetu Weather Data Analysis

A Django-based application for analyzing and managing weather data from the UK Met Office, focusing on temperature and rainfall patterns across different regions of the UK.

## Features

- **Data Collection**: Automated collection of weather data from the UK Met Office
- **Region-wise Analysis**: Support for multiple UK regions including England, Scotland, Wales, and Northern Ireland
- **Temporal Analysis**: 
  - Monthly temperature and rainfall data
  - Seasonal weather patterns
  - Annual trends
- **Parameter Tracking**:
  - Maximum temperature (Tmax)
  - Minimum temperature (Tmin)
  - Mean temperature (Tmean)
  - Sunshine hours
  - Rainfall measurements
  - Rain days (≥1mm)
  - Air frost days

## Project Structure

```
farmsetu/
├── api/
│   ├── admin.py          # Django admin interface configuration
│   ├── enum.py           # Enums for regions, parameters, months, and seasons
│   ├── models/           # Database models
│   └── views/            # API views and data processing
├── manage.py             # Django management script
└── requirements.txt      # Project dependencies
```

## Data Models

The application uses several key models to store and manage weather data:

1. **BaseDbModel**: Abstract base model with common fields
   - UUID primary key
   - Creation and update timestamps
   - Active status flag

2. **YearDbModel**: Stores year-specific data

3. **MonthWiseTempratureDbModel**: Monthly temperature data
   - Region
   - Month
   - Temperature
   - Year reference

4. **SeasonWiseTempratureDbModel**: Seasonal temperature data
   - Region
   - Season
   - Temperature
   - Year reference

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd farmsetu
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Usage

### Admin Interface

Access the admin interface at `http://localhost:8000/admin/` to:
- View and manage weather data
- Filter data by region, month/season, and year
- Search through historical records
- Monitor data collection status

### API Endpoints

The application provides RESTful API endpoints for:
- Fetching weather data by region
- Retrieving monthly/seasonal statistics
- Accessing historical weather patterns

## Data Sources

The application primarily uses data from the UK Met Office's climate datasets, including:
- Regional temperature records
- Rainfall measurements
- Sunshine duration
- Air frost occurrences

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

[Specify your license here]

## Acknowledgments

- UK Met Office for providing the climate datasets
- Django framework
- [Any other acknowledgments]
