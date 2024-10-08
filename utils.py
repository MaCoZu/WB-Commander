import plotly.graph_objects as go
import wbgapi as wb

# rename region code to propper region name
country_code_dict = {
    "ABW": "Aruba",
    "AFE": "Africa Eastern and Southern",
    "AFG": "Afghanistan",
    "AFW": "Africa Western and Central",
    "AGO": "Angola",
    "ALB": "Albania",
    "AND": "Andorra",
    "ARB": "Arab World",
    "ARE": "United Arab Emirates",
    "ARG": "Argentina",
    "ARM": "Armenia",
    "ASM": "American Samoa",
    "ATG": "Antigua and Barbuda",
    "AUS": "Australia",
    "AUT": "Austria",
    "AZE": "Azerbaijan",
    "BDI": "Burundi",
    "BEL": "Belgium",
    "BEN": "Benin",
    "BFA": "Burkina Faso",
    "BGD": "Bangladesh",
    "BGR": "Bulgaria",
    "BHR": "Bahrain",
    "BHS": "Bahamas, The",
    "BIH": "Bosnia and Herzegovina",
    "BLR": "Belarus",
    "BLZ": "Belize",
    "BMU": "Bermuda",
    "BOL": "Bolivia",
    "BRA": "Brazil",
    "BRB": "Barbados",
    "BRN": "Brunei Darussalam",
    "BTN": "Bhutan",
    "BWA": "Botswana",
    "CAF": "Central African Republic",
    "CAN": "Canada",
    "CEB": "Central Europe and the Baltics",
    "CHE": "Switzerland",
    "CHI": "Channel Islands",
    "CHL": "Chile",
    "CHN": "China",
    "CIV": "Cote d'Ivoire",
    "CMR": "Cameroon",
    "COD": "Congo, Dem. Rep.",
    "COG": "Congo, Rep.",
    "COL": "Colombia",
    "COM": "Comoros",
    "CPV": "Cabo Verde",
    "CRI": "Costa Rica",
    "CSS": "Caribbean small states",
    "CUB": "Cuba",
    "CUW": "Curacao",
    "CYM": "Cayman Islands",
    "CYP": "Cyprus",
    "CZE": "Czechia",
    "DEU": "Germany",
    "DJI": "Djibouti",
    "DMA": "Dominica",
    "DNK": "Denmark",
    "DOM": "Dominican Republic",
    "DZA": "Algeria",
    "EAP": "East Asia & Pacific (excluding high income)",
    "EAR": "Early-demographic dividend",
    "EAS": "East Asia & Pacific",
    "ECA": "Europe & Central Asia (excluding high income)",
    "ECS": "Europe & Central Asia",
    "ECU": "Ecuador",
    "EGY": "Egypt, Arab Rep.",
    "EMU": "Euro area",
    "ERI": "Eritrea",
    "ESP": "Spain",
    "EST": "Estonia",
    "ETH": "Ethiopia",
    "EUU": "European Union",
    "FCS": "Fragile and conflict affected situations",
    "FIN": "Finland",
    "FJI": "Fiji",
    "FRA": "France",
    "FRO": "Faroe Islands",
    "FSM": "Micronesia, Fed. Sts.",
    "GAB": "Gabon",
    "GBR": "United Kingdom",
    "GEO": "Georgia",
    "GHA": "Ghana",
    "GIB": "Gibraltar",
    "GIN": "Guinea",
    "GMB": "Gambia, The",
    "GNB": "Guinea-Bissau",
    "GNQ": "Equatorial Guinea",
    "GRC": "Greece",
    "GRD": "Grenada",
    "GRL": "Greenland",
    "GTM": "Guatemala",
    "GUM": "Guam",
    "GUY": "Guyana",
    "HIC": "High income",
    "HKG": "Hong Kong SAR, China",
    "HND": "Honduras",
    "HPC": "Heavily indebted poor countries (HIPC)",
    "HRV": "Croatia",
    "HTI": "Haiti",
    "HUN": "Hungary",
    "IBD": "IBRD only",
    "IBT": "IDA & IBRD total",
    "IDA": "IDA total",
    "IDB": "IDA blend",
    "IDN": "Indonesia",
    "IDX": "IDA only",
    "IMN": "Isle of Man",
    "IND": "India",
    "INX": "Not classified",
    "IRL": "Ireland",
    "IRN": "Iran, Islamic Rep.",
    "IRQ": "Iraq",
    "ISL": "Iceland",
    "ISR": "Israel",
    "ITA": "Italy",
    "JAM": "Jamaica",
    "JOR": "Jordan",
    "JPN": "Japan",
    "KAZ": "Kazakhstan",
    "KEN": "Kenya",
    "KGZ": "Kyrgyz Republic",
    "KHM": "Cambodia",
    "KIR": "Kiribati",
    "KNA": "St. Kitts and Nevis",
    "KOR": "Korea, Rep.",
    "KWT": "Kuwait",
    "LAC": "Latin America & Caribbean (excluding high income)",
    "LAO": "Lao PDR",
    "LBN": "Lebanon",
    "LBR": "Liberia",
    "LBY": "Libya",
    "LCA": "St. Lucia",
    "LCN": "Latin America & Caribbean",
    "LDC": "Least developed countries: UN classification",
    "LIC": "Low income",
    "LIE": "Liechtenstein",
    "LKA": "Sri Lanka",
    "LMC": "Lower middle income",
    "LMY": "Low & middle income",
    "LSO": "Lesotho",
    "LTE": "Late-demographic dividend",
    "LTU": "Lithuania",
    "LUX": "Luxembourg",
    "LVA": "Latvia",
    "MAC": "Macao SAR, China",
    "MAF": "St. Martin (French part)",
    "MAR": "Morocco",
    "MCO": "Monaco",
    "MDA": "Moldova",
    "MDG": "Madagascar",
    "MDV": "Maldives",
    "MEA": "Middle East & North Africa",
    "MEX": "Mexico",
    "MHL": "Marshall Islands",
    "MIC": "Middle income",
    "MKD": "North Macedonia",
    "MLI": "Mali",
    "MLT": "Malta",
    "MMR": "Myanmar",
    "MNA": "Middle East & North Africa (excluding high income)",
    "MNE": "Montenegro",
    "MNG": "Mongolia",
    "MNP": "Northern Mariana Islands",
    "MOZ": "Mozambique",
    "MRT": "Mauritania",
    "MUS": "Mauritius",
    "MWI": "Malawi",
    "MYS": "Malaysia",
    "NAC": "North America",
    "NAM": "Namibia",
    "NCL": "New Caledonia",
    "NER": "Niger",
    "NGA": "Nigeria",
    "NIC": "Nicaragua",
    "NLD": "Netherlands",
    "NOR": "Norway",
    "NPL": "Nepal",
    "NRU": "Nauru",
    "NZL": "New Zealand",
    "OED": "OECD members",
    "OMN": "Oman",
    "OSS": "Other small states",
    "PAK": "Pakistan",
    "PAN": "Panama",
    "PER": "Peru",
    "PHL": "Philippines",
    "PLW": "Palau",
    "PNG": "Papua New Guinea",
    "POL": "Poland",
    "PRE": "Pre-demographic dividend",
    "PRI": "Puerto Rico",
    "PRK": "Korea, Dem. People's Rep.",
    "PRT": "Portugal",
    "PRY": "Paraguay",
    "PSE": "West Bank and Gaza",
    "PSS": "Pacific island small states",
    "PST": "Post-demographic dividend",
    "PYF": "French Polynesia",
    "QAT": "Qatar",
    "ROU": "Romania",
    "RUS": "Russian Federation",
    "RWA": "Rwanda",
    "SAS": "South Asia",
    "SAU": "Saudi Arabia",
    "SDN": "Sudan",
    "SEN": "Senegal",
    "SGP": "Singapore",
    "SLB": "Solomon Islands",
    "SLE": "Sierra Leone",
    "SLV": "El Salvador",
    "SMR": "San Marino",
    "SOM": "Somalia",
    "SRB": "Serbia",
    "SSA": "Sub-Saharan Africa (excluding high income)",
    "SSD": "South Sudan",
    "SSF": "Sub-Saharan Africa",
    "SST": "Small states",
    "STP": "Sao Tome and Principe",
    "SUR": "Suriname",
    "SVK": "Slovak Republic",
    "SVN": "Slovenia",
    "SWE": "Sweden",
    "SWZ": "Eswatini",
    "SXM": "Sint Maarten (Dutch part)",
    "SYC": "Seychelles",
    "SYR": "Syrian Arab Republic",
    "TCA": "Turks and Caicos Islands",
    "TCD": "Chad",
    "TEA": "East Asia & Pacific (IDA & IBRD countries)",
    "TEC": "Europe & Central Asia (IDA & IBRD countries)",
    "TGO": "Togo",
    "THA": "Thailand",
    "TJK": "Tajikistan",
    "TKM": "Turkmenistan",
    "TLA": "Latin America & the Caribbean (IDA & IBRD countries)",
    "TLS": "Timor-Leste",
    "TMN": "Middle East & North Africa (IDA & IBRD countries)",
    "TON": "Tonga",
    "TSA": "South Asia (IDA & IBRD)",
    "TSS": "Sub-Saharan Africa (IDA & IBRD countries)",
    "TTO": "Trinidad and Tobago",
    "TUN": "Tunisia",
    "TUR": "Turkiye",
    "TUV": "Tuvalu",
    "TZA": "Tanzania",
    "UGA": "Uganda",
    "UKR": "Ukraine",
    "UMC": "Upper middle income",
    "URY": "Uruguay",
    "USA": "United States",
    "UZB": "Uzbekistan",
    "VCT": "St. Vincent and the Grenadines",
    "VEN": "Venezuela, RB",
    "VGB": "British Virgin Islands",
    "VIR": "Virgin Islands (U.S.)",
    "VNM": "Viet Nam",
    "VUT": "Vanuatu",
    "WLD": "World",
    "WSM": "Samoa",
    "XKX": "Kosovo",
    "YEM": "Yemen, Rep.",
    "ZAF": "South Africa",
    "ZMB": "Zambia",
    "ZWE": "Zimbabwe",
}


def resolve_country_code(code):
    """resolve country code to country name"""
    region = country_code_dict[code]
    return region


def get_data_dict(indicator_code, country_list):
    try:
        data_dict = {}
        for item in wb.data.fetch(indicator_code, country_list, skipAggs=True, numericTimeKeys=True):
                country_code = item['economy']
                value = item['value']
                year = item['time']
                
                if country_code not in data_dict:
                    data_dict[country_code] = {"dates": [], "values": [], "first_value_found": False}
                    
                # Check if the value is a number
                if isinstance(value, (int, float)) and not isinstance(value, bool):
                    data_dict[country_code]["first_value_found"] = True

                # Append data only if the first valid value has been found and value is numeric
                if data_dict[country_code]["first_value_found"] and isinstance(value, (int, float)):
                    data_dict[country_code]["dates"].append(year)
                    data_dict[country_code]["values"].append(value)

                    
            # Sort the dates and values together
        for country_code, data in data_dict.items():
            sorted_data = sorted(zip(data["dates"], data["values"]))
            data_dict[country_code]["dates"], data_dict[country_code]["values"] = map(list, zip(*sorted_data))
        return data_dict
    except wb.APIResponseError as e:
        print(f"APIResponseError: {e}")
        return {}  # Return an empty dictionary or handle as needed
    except Exception as e:
        print(f"Unexpected error: {e}")
        return {}


def plot(indicator_code, country_list):
    data_dict = get_data_dict(indicator_code, country_list)
    indicator_name = wb.series.get(indicator_code)["value"]
    
    # Dynamically adjust font size based on the length of the indicator name
    base_font_size = 16
    if len(indicator_name) > 50:
        font_size = max(base_font_size - (len(indicator_name) // 10), 14)
    else:
        font_size = base_font_size

    # Wrap long indicator names by adding line breaks
    max_line_length = 50  # Define a maximum length before wrapping
    wrapped_indicator_name = "<br>".join([indicator_name[i:i+max_line_length] for i in range(0, len(indicator_name), max_line_length)])


    fig = go.Figure()

    # Add traces for each economy
    for economy, data in data_dict.items():
        fig.add_trace(
            go.Scatter(
                x=data["dates"], 
                y=data["values"], 
                mode="lines",
                name=resolve_country_code(economy),
                )
            )

    # Customize layout
    fig.update_layout(
        xaxis_title=None,  
        yaxis_title=None,  
        margin=dict(l=40, r=40, t=90, b=20),
        legend_title_text="",
            hovermode="closest",  # Change how the hover information is displayed
            showlegend=True,  # Show legend
            template="plotly_white",  # Set plot template to white background
            title=dict(
                text=wrapped_indicator_name,
                font=dict(size=font_size),
                x=0.5,
                y=0.9,
                xanchor='center',
                yanchor='top',
            ),
            legend=dict(
                orientation="h",
                xanchor="left",
                yanchor="bottom",
                x=0,
                y=1.01,
                bgcolor='rgba(0,0,0,0)',  # Transparent background
                bordercolor='rgba(0,0,0,0)',  # Transparent border
                groupclick="toggleitem",
                font=dict(family="Courier", size=14, color="black"),
            ),
            xaxis=dict(
                tickmode="linear",
                dtick=5,  # Show every fifth year
            ),
            modebar_orientation="v",
            modebar_remove=["zoom", "pan", "displaylogo"]
    )
    
    return fig