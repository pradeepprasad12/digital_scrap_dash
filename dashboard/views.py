
import pandas as pd
from django.shortcuts import render
from .data import scrape_data  # Import the scraping function

def dashboard_view(request):
    # Call the scrape_data function to fetch the data
    df = scrape_data()

    # If data is available, convert it to dictionary format for rendering
    if df is not None:
        table_data = df.to_dict(orient='records')
    else:
        table_data = []  # Handle case where no data is returned

    # Render the HTML template with the scraped data
    return render(request, 'dashboard/dashboard.html', {'products': table_data})
