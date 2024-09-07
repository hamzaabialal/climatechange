import os

from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from climate_change.forms import ClimateForm, ClimateGraphForm
from climate_change.models import ClimateData, CLimateGraphs
from djangoProject3 import settings


# Create your views here.

class IndexPageView(TemplateView):
    template_name = 'index.html'


class ElementsPageView(TemplateView):
    template_name = 'elements.html'


class GenericPageView(TemplateView):
    template_name = 'generic.html'
    
    
class GenericPageView(TemplateView):
    template_name = 'documentation.html'

import json
import random

landlocked_countries = [
    "Afghanistan", "Andorra", "Armenia", "Austria", "Azerbaijan", "Belarus", "Bhutan",
    "Bolivia", "Botswana", "Burkina Faso", "Burundi", "Central African Republic", "Chad",
    "Czech Republic", "Eswatini", "Ethiopia", "Hungary", "Kazakhstan", "Kosovo", "Kyrgyzstan",
    "Laos", "Lesotho", "Liechtenstein", "Luxembourg", "Malawi", "Mali", "Moldova", "Mongolia",
    "Nepal", "North Macedonia", "Paraguay", "Rwanda", "San Marino", "Serbia", "Slovakia",
    "South Sudan", "Switzerland", "Tajikistan", "Turkmenistan", "Uganda", "Uzbekistan",
    "Vatican City", "Zambia", "Zimbabwe", "Niger", "South Sudan", "Burkina Faso", "Malawi",
    "Ethiopia"
]

def generate_yearly_data(country, start_year, end_year):
    data = {"countries": {country: {}}}

    # Define temperature profiles and other data based on regions
    if country in ["USA", "Canada", "Australia", "Norway", "Sweden", "Finland", "Russia", "Iceland", "Greenland", "Svalbard and Jan Mayen", "Mongolia", "Norway", "Heard Island and McDonald Islands", "Finland", "Kyrgyzstan", "Sweden", "Tajikistan", "French Southern and Antarctic Lands", "Saint Pierre and Miquelon", "Estonia", "Switzerland", "Faroe Islands", "Latvia", "North Korea", "Kazakhstan", "Lithuania", "Austria", "Belarus", "Liechtenstein", "Armenia", "Andorra", "Czech Republic", "Poland", "Slovakia", "Georgia", "United Kingdom", "Ukraine", "Chile", "Isle of Man", "Ireland", "Slovenia", "Montenegro", "Luxembourg", "Kosovo", "Romania", "Bosnia and Herzegovina", "Bhutan", "New Zealand", "Netherlands", "Belgium", "North Macedonia", "Moldova", "Bulgaria", "Serbia", "Hungary", "France", "Turkey", "Japan", "Croatia", "Guernsey", "South Korea", "Jersey", "Lesotho", "Albania", "San Marino"]:
        temperature_avg = 10.0
        temperature_min = -10
        temperature_max = 35
        total_precipitation = 1100
        co2_total_tonnes = 5100000
        co2_per_capita = 15.3
        sea_level_rise_mm = 3.5
        temp_increase_prediction = 0.6
        sea_level_rise_prediction = 4.2
        climate_risk_index = 5.5
        policy_effectiveness_score = 7.9

    elif country in ["Brazil", "South Africa", "New Zealand", "Chile", "Argentina", "Colombia", "Venezuela", "Ecuador", "Bolivia", "Paraguay", "Uruguay", "Panama", "Belize", "Venezuela", "Yemen", "Cuba", "Nicaragua", "Central African Republic", "Liberia", "El Salvador", "Gabon", "Kenya", "Puerto Rico"]:
        temperature_avg = 25.0
        temperature_min = 15
        temperature_max = 45
        total_precipitation = 1200
        co2_total_tonnes = 6000000
        co2_per_capita = 16.0
        sea_level_rise_mm = 3.8
        temp_increase_prediction = 0.8
        sea_level_rise_prediction = 4.5
        climate_risk_index = 6.0
        policy_effectiveness_score = 7.5

    elif country in ["India", "Pakistan", "Afghanistan", "Iran", "Iraq", "Saudi Arabia", "Oman", "United Arab Emirates", "Kuwait", "Morocco", "Tunisia", "Libya", "Egypt", "Israel", "Jordan", "Qatar", "Burkina Faso", "Mali", "Aruba", "Senegal", "Mauritania", "Tokelau", "Tuvalu", "Djibouti", "Curacao", "Gambia", "Maldives", "Niger", "Benin", "Marshall Islands", "Guinea Bissau", "South Sudan", "Sudan", "Palau", "Nauru", "Cayman Islands", "Guam", "Kiribati", "Anguilla", "Saint Martin", "Sint Maarten", "Bahrain", "Singapore", "Ghana", "Oman", "Chad"]:
        temperature_avg = 30.0
        temperature_min = 20
        temperature_max = 50
        total_precipitation = 1400
        co2_total_tonnes = 7000000
        co2_per_capita = 18.0
        sea_level_rise_mm = 4.0
        temp_increase_prediction = 0.9
        sea_level_rise_prediction = 5.0
        climate_risk_index = 6.5
        policy_effectiveness_score = 7.0

    elif country in ["Germany", "France", "Spain", "Italy", "United Kingdom", "Netherlands", "Belgium", "Switzerland", "Austria", "Denmark", "Poland", "Czech Republic", "Slovakia", "Hungary", "Romania", "Bulgaria", "Greece", "Portugal", "Ireland", "Australia", "Finland", "Norway", "Iceland", "Turkey", "Chile", "Peru"]:
        temperature_avg = 8.0
        temperature_min = -5
        temperature_max = 30
        total_precipitation = 1000
        co2_total_tonnes = 4500000
        co2_per_capita = 12.0
        sea_level_rise_mm = 3.0
        temp_increase_prediction = 0.5
        sea_level_rise_prediction = 3.8
        climate_risk_index = 5.0
        policy_effectiveness_score = 8.0

    else:
        temperature_avg = 18.0
        temperature_min = 8
        temperature_max = 40
        total_precipitation = 1150
        co2_total_tonnes = 5500000
        co2_per_capita = 15.8
        sea_level_rise_mm = 3.7
        temp_increase_prediction = 0.7
        sea_level_rise_prediction = 4.4
        climate_risk_index = 5.8
        policy_effectiveness_score = 7.7

    # Check if the country is landlocked, set sea level rise to 0

    for year in range(start_year, end_year + 1):
        # Random slight changes for each year
        temperature_avg += round(random.uniform(0.01, 0.05), 2)
        temperature_min += round(random.uniform(0.01, 0.1), 2)
        temperature_max += round(random.uniform(0.01, 0.1), 2)
        total_precipitation += round(random.uniform(1, 5), 2)
        co2_total_tonnes += random.randint(10000, 50000)
        co2_per_capita += round(random.uniform(0.01, 0.05), 2)
        sea_level_rise_mm += round(random.uniform(0.01, 0.05), 2)
        temp_increase_prediction += round(random.uniform(0.01, 0.05), 2)
        sea_level_rise_prediction += round(random.uniform(0.01, 0.05), 2)
        climate_risk_index += round(random.uniform(0.01, 0.05), 2)
        policy_effectiveness_score += round(random.uniform(-0.05, 0.05), 2)

        if country in landlocked_countries:
            sea_level_rise_mm = 0
            sea_level_rise_prediction = 0

        data["countries"][country][str(year)] = {
            "temperature": {
                "avg": temperature_avg,
                "min": temperature_min,
                "max": temperature_max
            },
            "precipitation": {
                "total_mm": total_precipitation,
                "avg_mm": round(total_precipitation / 12, 2)
            },
            "CO2_emissions": {
                "total_tonnes": co2_total_tonnes,
                "per_capita_tonnes": co2_per_capita
            },
            "sea_level_rise": {
                "mm": sea_level_rise_mm
            },
            "prediction": {
                "temperature_increase": temp_increase_prediction,
                "sea_level_rise": sea_level_rise_prediction
            },
            "status": {
                "climate_risk_index": climate_risk_index,
                "policy_effectiveness_score": policy_effectiveness_score
            }
        }

    return data


import pandas as pd

# Example method, replace this with your actual method logic
from groq import Groq

# Configure the API keys and model
grok_api = "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"
client = Groq(api_key=grok_api)

def generate_climate_summary(country, year, year_data):
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": f"""
You are an AI bot, and your task is to generate a detailed and concise paragraph summarizing the climate change impacts for a specific country and year that I will provide.
The summary should be data-driven, focusing on key climate indicators and trends.
The information provided will include:
{year_data}

Your response should be well-structured, weaving these elements into a coherent narrative that reflects both current conditions and future projections for the country.
Emphasize any significant patterns or trends specific to the region and provide context where necessary.
Here is the country: {country} and the year: {year}.
Do not return any extra words, such as "Here is your output" or similar. Just return the description as requested, nothing more.
Ensure the description accurately reflects all the provided data and does not include any additional text or incorrect information.
                    """
                }
            ],
            model="llama3-70b-8192"
        )
        description = chat_completion.choices[0].message.content.strip()
        return description
    except Exception as e:
        print("E", e)
        return "None"

def predict_climate(request):
    year_data = None
    filename = None
    climate_text=None

    if request.method == 'POST':
        form = ClimateForm(request.POST)  # Replace ClimateForm with your actual form class
        if form.is_valid():
            country = form.cleaned_data['country']
            year = form.cleaned_data['year']

            # Generate climate data
            data = generate_yearly_data(country, 2024, 2100)
            print(data)
            filename = f"climate_data_{country}.json"
            file_path = os.path.join(settings.MEDIA_ROOT, filename)

            # Ensure the directory exists
            media_dir = os.path.dirname(file_path)
            if not os.path.exists(media_dir):
                os.makedirs(media_dir)

            # Save the JSON data to the file
            with open(file_path, 'w') as f:
                json.dump(data, f, indent=4)

            # Create a new entry in the database
            ClimateData.objects.create(
                country=country,
                file=filename
            )

            # Load the JSON data from the file
            with open(file_path, 'r') as f:
                file_data = json.load(f)

            # Extract year-specific data
            country_data = file_data.get('countries', {}).get(country, {})
            year_data = country_data.get(str(year), 'No data available for this year.')
            climate_text = generate_climate_summary(country, year, year_data)

    else:
        form = ClimateForm()  # Replace with your actual form class

    return render(request, 'add_detail.html', {
        'form': form,
        'year_data': year_data,
        'filename': filename,
        'climate_text':climate_text
    })


# views.py
from django.shortcuts import render
from .models import ClimateData
import json
import os
import pandas as pd
import matplotlib.pyplot as plt
from django.conf import settings
from .forms import ClimateForm  # Make sure to import your form class


def climate_data_graphs(filename, country):
    # Load JSON data from file
    file_path = os.path.join(settings.MEDIA_ROOT, filename)
    with open(file_path) as f:
        data = json.load(f)

    # Extract the climate data
    country_data = data['countries'][country]

    # Prepare lists for plotting
    years = []
    avg_temperature = []
    min_temperature = []
    max_temperature = []
    total_precipitation_mm = []
    co2_emissions_tonnes = []
    sea_level_rise_mm = []
    temperature_increase_prediction = []
    sea_level_rise_prediction = []
    climate_risk_index = []
    policy_effectiveness_score = []

    for year, details in country_data.items():
        years.append(int(year))
        avg_temperature.append(details['temperature']['avg'])
        min_temperature.append(details['temperature']['min'])
        max_temperature.append(details['temperature']['max'])
        total_precipitation_mm.append(details['precipitation']['total_mm'])
        co2_emissions_tonnes.append(details['CO2_emissions']['total_tonnes'])
        sea_level_rise_mm.append(details['sea_level_rise']['mm'])
        temperature_increase_prediction.append(details['prediction']['temperature_increase'])
        sea_level_rise_prediction.append(details['prediction']['sea_level_rise'])
        climate_risk_index.append(details['status']['climate_risk_index'])
        policy_effectiveness_score.append(details['status']['policy_effectiveness_score'])

    # Create DataFrame
    df = pd.DataFrame({
        'Year': years,
        'Avg_Temperature': avg_temperature,
        'Min_Temperature': min_temperature,
        'Max_Temperature': max_temperature,
        'Total_Precipitation_mm': total_precipitation_mm,
        'CO2_Emissions_Tonnes': co2_emissions_tonnes,
        'Sea_Level_Rise_mm': sea_level_rise_mm,
        'Temperature_Increase_Prediction': temperature_increase_prediction,
        'Sea_Level_Rise_Prediction': sea_level_rise_prediction,
        'Climate_Risk_Index': climate_risk_index,
        'Policy_Effectiveness_Score': policy_effectiveness_score
    })

    # Directory to save images
    graph_dir = os.path.join(settings.MEDIA_ROOT, 'graphs')
    if not os.path.exists(graph_dir):
        os.makedirs(graph_dir)

    # Plotting
    fig, axs = plt.subplots(6, 1, figsize=(10, 20))

    axs[0].plot(df['Year'], df['Avg_Temperature'], label='Average Temperature')
    axs[0].plot(df['Year'], df['Min_Temperature'], label='Min Temperature')
    axs[0].plot(df['Year'], df['Max_Temperature'], label='Max Temperature')
    axs[0].set_title('Temperature Trends')
    axs[0].set_ylabel('Temperature (°C)')
    axs[0].legend()

    axs[1].bar(df['Year'], df['Total_Precipitation_mm'], color='skyblue')
    axs[1].set_title('Total Annual Precipitation')
    axs[1].set_ylabel('Precipitation (mm)')

    axs[2].bar(df['Year'], df['CO2_Emissions_Tonnes'], color='green')
    axs[2].set_title('CO2 Emissions')
    axs[2].set_ylabel('Emissions (Tonnes)')

    axs[3].plot(df['Year'], df['Sea_Level_Rise_mm'])
    axs[3].set_title('Sea Level Rise')
    axs[3].set_ylabel('Sea Level Rise (mm)')

    axs[4].plot(df['Year'], df['Temperature_Increase_Prediction'], label='Temperature Increase')
    axs[4].plot(df['Year'], df['Sea_Level_Rise_Prediction'], label='Sea Level Rise')
    axs[4].set_title('Climate Predictions')
    axs[4].set_ylabel('Prediction Units')
    axs[4].legend()

    axs[5].scatter(df['Year'], df['Climate_Risk_Index'], color='red', label='Climate Risk Index')
    axs[5].scatter(df['Year'], df['Policy_Effectiveness_Score'], color='blue', label='Policy Effectiveness')
    axs[5].set_title('Status Indicators')
    axs[5].set_ylabel('Score')
    axs[5].legend()

    fig.tight_layout()
    graph_file_name = 'climate_data_graphs.png'
    graph_file_path = os.path.join(graph_dir, graph_file_name)
    plt.savefig(graph_file_path)
    plt.close(fig)

    return os.path.join('graphs', graph_file_name)  # Return relative path

def predict_climate_graphs(request):
    graphs = None
    filename = None

    if request.method == 'POST':
        form = ClimateGraphForm(request.POST)
        if form.is_valid():
            country = form.cleaned_data['country']
            start_year = form.cleaned_data['start_year']
            end_year = form.cleaned_data['end_year']
            filename_record = ClimateData.objects.filter(country=country).first()

            if filename_record:
                filename = filename_record.file.name
            else:
                # Generate and save climate data
                data = generate_yearly_data(country, start_year, end_year)
                filename = f"climate_data_{country}.json"
                file_path = os.path.join(settings.MEDIA_ROOT, filename)

                if not os.path.exists(os.path.dirname(file_path)):
                    os.makedirs(os.path.dirname(file_path))

                with open(file_path, 'w') as f:
                    json.dump(data, f, indent=4)

                ClimateData.objects.create(country=country, file=filename)

            # Generate and save graphs
            graphs = climate_data_graphs(filename, country)
            graphs = CLimateGraphs.objects.create(country=country, file=graphs)

            print(graphs.file)

    else:
        form = ClimateGraphForm()

    return render(request, 'climate_graphs.html', {
        'form': form,
        'graphs': graphs,
        'filename': filename
    })


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login after successful signup
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'signup_form': form})


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('index_page')  # Redirect to home or another page after login
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'login_form': form})


def logout(request):
    auth_logout(request)
    return redirect('login')  # Redirect to login page after logout
