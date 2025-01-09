
# Olympics Analysis with Streamlit

This repository contains a Streamlit web application for analyzing Olympics data. The app provides insights into medal tallies, athlete performance, country-wise statistics, and trends over time. Users can explore the data interactively using visualizations powered by Plotly and Matplotlib.

## Features

- **Medal Tally**: View medal tallies by country and year.
- **Overall Analysis**: Explore trends such as the number of participating nations, athletes, and events over time.
- **Country-wise Analysis**: Analyze the performance of individual countries, their top athletes, and the sports they excel in.
- **Athlete-wise Analysis**: Visualize athlete statistics, such as age distribution, and analyze height vs. weight correlations for different sports.

## Technologies Used

- **Python**: Backend programming.
- **Streamlit**: Interactive web application framework.
- **Pandas**: Data manipulation and analysis.
- **Plotly**: Interactive plotting library.
- **Matplotlib** and **Seaborn**: Data visualization libraries.
- **Plotly Figure Factory**: Distribution plots for data analysis.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/olympics-analysis.git
   cd olympics-analysis
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:
   ```bash
   streamlit run app.py
   ```

4. Access the app in your browser at `http://localhost:8501`.

## File Structure

```
.
├── app.py                    # Main Streamlit app script
├── preprocessor.py           # Data preprocessing functions
├── helper.py                 # Utility functions for analysis
├── athlete_events.csv        # Dataset of athlete events
├── noc_regions.csv           # Dataset of NOC regions
├── requirements.txt          # Required Python packages
└── README.md                 # Project documentation
```

## Datasets

- **Athlete Events Dataset**: Contains data about athletes, events, and medals in the Olympics.
- **NOC Regions Dataset**: Maps National Olympic Committees (NOCs) to their respective regions.

## Visualizations

- **Medal Tally Table**: Displays medal counts for countries and years.
- **Line Charts**: Trends in participating nations, athletes, and events.
- **Heatmaps**: Event occurrences over time for each sport.
- **Distribution Plots**: Age distribution of athletes across different medal types and sports.
- **Scatterplots**: Height vs. weight correlation for athletes.

## Future Enhancements

- Add predictive analytics for medal tally predictions.
- Enable exporting analysis results as reports.
- Enhance interactivity with more filtering options.

## Contributing

Contributions are welcome! If you'd like to enhance the project, follow these steps:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Make your changes and commit them:
   ```bash
   git commit -m "Add new feature"
   ```
4. Push your branch:
   ```bash
   git push origin feature-name
   ```
5. Submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

---
