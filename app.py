import base64
from pydoc import classname

import dash_bootstrap_components as dbc
import utils
from dash import Dash, Input, Output, State, callback, dcc, html

app = Dash(
    __name__,
    suppress_callback_exceptions=True,
    external_stylesheets=[dbc.themes.LUX],
)

# Declare server for Heroku deployment. Needed for Procfile.
server = app.server

country_list = [
    {
        "label": html.Span(
            ["COUNTRIES", html.Hr()], style={"color": "green", "font-size": 20}
        ),
        "value": "COUNTRIES",
        "search": "Countries",
    },
    {"label": "Aruba", "value": "ABW", "search": "Aruba"},
    {"label": "Afghanistan", "value": "AFG", "search": "Afghanistan"},
    {"label": "Angola", "value": "AGO", "search": "Angola"},
    {"label": "Albania", "value": "ALB", "search": "Albania"},
    {"label": "Andorra", "value": "AND", "search": "Andorra"},
    {"label": "United Arab Emirates", "value": "ARE", "search": "United Arab Emirates"},
    {"label": "Argentina", "value": "ARG", "search": "Argentina"},
    {"label": "Armenia", "value": "ARM", "search": "Armenia"},
    {"label": "American Samoa", "value": "ASM", "search": "American Samoa"},
    {"label": "Antigua and Barbuda", "value": "ATG", "search": "Antigua and Barbuda"},
    {"label": "Australia", "value": "AUS", "search": "Australia"},
    {"label": "Austria", "value": "AUT", "search": "Austria"},
    {"label": "Azerbaijan", "value": "AZE", "search": "Azerbaijan"},
    {"label": "Burundi", "value": "BDI", "search": "Burundi"},
    {"label": "Belgium", "value": "BEL", "search": "Belgium"},
    {"label": "Benin", "value": "BEN", "search": "Benin"},
    {"label": "Burkina Faso", "value": "BFA", "search": "Burkina Faso"},
    {"label": "Bangladesh", "value": "BGD", "search": "Bangladesh"},
    {"label": "Bulgaria", "value": "BGR", "search": "Bulgaria"},
    {"label": "Bahrain", "value": "BHR", "search": "Bahrain"},
    {"label": "Bahamas, The", "value": "BHS", "search": "Bahamas, The"},
    {
        "label": "Bosnia and Herzegovina",
        "value": "BIH",
        "search": "Bosnia and Herzegovina",
    },
    {"label": "Belarus", "value": "BLR", "search": "Belarus"},
    {"label": "Belize", "value": "BLZ", "search": "Belize"},
    {"label": "Bermuda", "value": "BMU", "search": "Bermuda"},
    {"label": "Bolivia", "value": "BOL", "search": "Bolivia"},
    {"label": "Brazil", "value": "BRA", "search": "Brazil"},
    {"label": "Barbados", "value": "BRB", "search": "Barbados"},
    {"label": "Brunei Darussalam", "value": "BRN", "search": "Brunei Darussalam"},
    {"label": "Bhutan", "value": "BTN", "search": "Bhutan"},
    {"label": "Botswana", "value": "BWA", "search": "Botswana"},
    {
        "label": "Central African Republic",
        "value": "CAF",
        "search": "Central African Republic",
    },
    {"label": "Canada", "value": "CAN", "search": "Canada"},
    {"label": "Switzerland", "value": "CHE", "search": "Switzerland"},
    {"label": "Channel Islands", "value": "CHI", "search": "Channel Islands"},
    {"label": "Chile", "value": "CHL", "search": "Chile"},
    {"label": "China", "value": "CHN", "search": "China"},
    {"label": "Cote d'Ivoire", "value": "CIV", "search": "Cote d'Ivoire"},
    {"label": "Cameroon", "value": "CMR", "search": "Cameroon"},
    {"label": "Congo, Dem. Rep.", "value": "COD", "search": "Congo, Dem. Rep."},
    {"label": "Congo, Rep.", "value": "COG", "search": "Congo, Rep."},
    {"label": "Colombia", "value": "COL", "search": "Colombia"},
    {"label": "Comoros", "value": "COM", "search": "Comoros"},
    {"label": "Cabo Verde", "value": "CPV", "search": "Cabo Verde"},
    {"label": "Costa Rica", "value": "CRI", "search": "Costa Rica"},
    {"label": "Cuba", "value": "CUB", "search": "Cuba"},
    {"label": "Curacao", "value": "CUW", "search": "Curacao"},
    {"label": "Cayman Islands", "value": "CYM", "search": "Cayman Islands"},
    {"label": "Cyprus", "value": "CYP", "search": "Cyprus"},
    {"label": "Czechia", "value": "CZE", "search": "Czechia"},
    {"label": "Germany", "value": "DEU", "search": "Germany"},
    {"label": "Djibouti", "value": "DJI", "search": "Djibouti"},
    {"label": "Dominica", "value": "DMA", "search": "Dominica"},
    {"label": "Denmark", "value": "DNK", "search": "Denmark"},
    {"label": "Dominican Republic", "value": "DOM", "search": "Dominican Republic"},
    {"label": "Algeria", "value": "DZA", "search": "Algeria"},
    {"label": "Ecuador", "value": "ECU", "search": "Ecuador"},
    {"label": "Egypt, Arab Rep.", "value": "EGY", "search": "Egypt, Arab Rep."},
    {"label": "Eritrea", "value": "ERI", "search": "Eritrea"},
    {"label": "Spain", "value": "ESP", "search": "Spain"},
    {"label": "Estonia", "value": "EST", "search": "Estonia"},
    {"label": "Ethiopia", "value": "ETH", "search": "Ethiopia"},
    {"label": "Finland", "value": "FIN", "search": "Finland"},
    {"label": "Fiji", "value": "FJI", "search": "Fiji"},
    {"label": "France", "value": "FRA", "search": "France"},
    {"label": "Faroe Islands", "value": "FRO", "search": "Faroe Islands"},
    {
        "label": "Micronesia, Fed. Sts.",
        "value": "FSM",
        "search": "Micronesia, Fed. Sts.",
    },
    {"label": "Gabon", "value": "GAB", "search": "Gabon"},
    {"label": "United Kingdom", "value": "GBR", "search": "United Kingdom"},
    {"label": "Georgia", "value": "GEO", "search": "Georgia"},
    {"label": "Ghana", "value": "GHA", "search": "Ghana"},
    {"label": "Gibraltar", "value": "GIB", "search": "Gibraltar"},
    {"label": "Guinea", "value": "GIN", "search": "Guinea"},
    {"label": "Gambia, The", "value": "GMB", "search": "Gambia, The"},
    {"label": "Guinea-Bissau", "value": "GNB", "search": "Guinea-Bissau"},
    {"label": "Equatorial Guinea", "value": "GNQ", "search": "Equatorial Guinea"},
    {"label": "Greece", "value": "GRC", "search": "Greece"},
    {"label": "Grenada", "value": "GRD", "search": "Grenada"},
    {"label": "Greenland", "value": "GRL", "search": "Greenland"},
    {"label": "Guatemala", "value": "GTM", "search": "Guatemala"},
    {"label": "Guam", "value": "GUM", "search": "Guam"},
    {"label": "Guyana", "value": "GUY", "search": "Guyana"},
    {"label": "Hong Kong SAR, China", "value": "HKG", "search": "Hong Kong SAR, China"},
    {"label": "Honduras", "value": "HND", "search": "Honduras"},
    {"label": "Croatia", "value": "HRV", "search": "Croatia"},
    {"label": "Haiti", "value": "HTI", "search": "Haiti"},
    {"label": "Hungary", "value": "HUN", "search": "Hungary"},
    {"label": "Indonesia", "value": "IDN", "search": "Indonesia"},
    {"label": "Isle of Man", "value": "IMN", "search": "Isle of Man"},
    {"label": "India", "value": "IND", "search": "India"},
    {"label": "Ireland", "value": "IRL", "search": "Ireland"},
    {"label": "Iran, Islamic Rep.", "value": "IRN", "search": "Iran, Islamic Rep."},
    {"label": "Iraq", "value": "IRQ", "search": "Iraq"},
    {"label": "Iceland", "value": "ISL", "search": "Iceland"},
    {"label": "Israel", "value": "ISR", "search": "Israel"},
    {"label": "Italy", "value": "ITA", "search": "Italy"},
    {"label": "Jamaica", "value": "JAM", "search": "Jamaica"},
    {"label": "Jordan", "value": "JOR", "search": "Jordan"},
    {"label": "Japan", "value": "JPN", "search": "Japan"},
    {"label": "Kazakhstan", "value": "KAZ", "search": "Kazakhstan"},
    {"label": "Kenya", "value": "KEN", "search": "Kenya"},
    {"label": "Kyrgyz Republic", "value": "KGZ", "search": "Kyrgyz Republic"},
    {"label": "Cambodia", "value": "KHM", "search": "Cambodia"},
    {"label": "Kiribati", "value": "KIR", "search": "Kiribati"},
    {"label": "St. Kitts and Nevis", "value": "KNA", "search": "St. Kitts and Nevis"},
    {"label": "Korea, Rep.", "value": "KOR", "search": "Korea, Rep."},
    {"label": "Kuwait", "value": "KWT", "search": "Kuwait"},
    {"label": "Lao PDR", "value": "LAO", "search": "Lao PDR"},
    {"label": "Lebanon", "value": "LBN", "search": "Lebanon"},
    {"label": "Liberia", "value": "LBR", "search": "Liberia"},
    {"label": "Libya", "value": "LBY", "search": "Libya"},
    {"label": "St. Lucia", "value": "LCA", "search": "St. Lucia"},
    {"label": "Liechtenstein", "value": "LIE", "search": "Liechtenstein"},
    {"label": "Sri Lanka", "value": "LKA", "search": "Sri Lanka"},
    {"label": "Lesotho", "value": "LSO", "search": "Lesotho"},
    {"label": "Lithuania", "value": "LTU", "search": "Lithuania"},
    {"label": "Luxembourg", "value": "LUX", "search": "Luxembourg"},
    {"label": "Latvia", "value": "LVA", "search": "Latvia"},
    {"label": "Macao SAR, China", "value": "MAC", "search": "Macao SAR, China"},
    {
        "label": "St. Martin (French part)",
        "value": "MAF",
        "search": "St. Martin (French part)",
    },
    {"label": "Morocco", "value": "MAR", "search": "Morocco"},
    {"label": "Monaco", "value": "MCO", "search": "Monaco"},
    {"label": "Moldova", "value": "MDA", "search": "Moldova"},
    {"label": "Madagascar", "value": "MDG", "search": "Madagascar"},
    {"label": "Maldives", "value": "MDV", "search": "Maldives"},
    {"label": "Mexico", "value": "MEX", "search": "Mexico"},
    {"label": "Marshall Islands", "value": "MHL", "search": "Marshall Islands"},
    {"label": "North Macedonia", "value": "MKD", "search": "North Macedonia"},
    {"label": "Mali", "value": "MLI", "search": "Mali"},
    {"label": "Malta", "value": "MLT", "search": "Malta"},
    {"label": "Myanmar", "value": "MMR", "search": "Myanmar"},
    {"label": "Montenegro", "value": "MNE", "search": "Montenegro"},
    {"label": "Mongolia", "value": "MNG", "search": "Mongolia"},
    {
        "label": "Northern Mariana Islands",
        "value": "MNP",
        "search": "Northern Mariana Islands",
    },
    {"label": "Mozambique", "value": "MOZ", "search": "Mozambique"},
    {"label": "Mauritania", "value": "MRT", "search": "Mauritania"},
    {"label": "Mauritius", "value": "MUS", "search": "Mauritius"},
    {"label": "Malawi", "value": "MWI", "search": "Malawi"},
    {"label": "Malaysia", "value": "MYS", "search": "Malaysia"},
    {"label": "Namibia", "value": "NAM", "search": "Namibia"},
    {"label": "New Caledonia", "value": "NCL", "search": "New Caledonia"},
    {"label": "Niger", "value": "NER", "search": "Niger"},
    {"label": "Nigeria", "value": "NGA", "search": "Nigeria"},
    {"label": "Nicaragua", "value": "NIC", "search": "Nicaragua"},
    {"label": "Netherlands", "value": "NLD", "search": "Netherlands"},
    {"label": "Norway", "value": "NOR", "search": "Norway"},
    {"label": "Nepal", "value": "NPL", "search": "Nepal"},
    {"label": "Nauru", "value": "NRU", "search": "Nauru"},
    {"label": "New Zealand", "value": "NZL", "search": "New Zealand"},
    {"label": "Oman", "value": "OMN", "search": "Oman"},
    {"label": "Pakistan", "value": "PAK", "search": "Pakistan"},
    {"label": "Panama", "value": "PAN", "search": "Panama"},
    {"label": "Peru", "value": "PER", "search": "Peru"},
    {"label": "Philippines", "value": "PHL", "search": "Philippines"},
    {"label": "Palau", "value": "PLW", "search": "Palau"},
    {"label": "Papua New Guinea", "value": "PNG", "search": "Papua New Guinea"},
    {"label": "Poland", "value": "POL", "search": "Poland"},
    {"label": "Puerto Rico", "value": "PRI", "search": "Puerto Rico"},
    {
        "label": "Korea, Dem. People's Rep.",
        "value": "PRK",
        "search": "Korea, Dem. People's Rep.",
    },
    {"label": "Portugal", "value": "PRT", "search": "Portugal"},
    {"label": "Paraguay", "value": "PRY", "search": "Paraguay"},
    {"label": "West Bank and Gaza", "value": "PSE", "search": "West Bank and Gaza"},
    {"label": "French Polynesia", "value": "PYF", "search": "French Polynesia"},
    {"label": "Qatar", "value": "QAT", "search": "Qatar"},
    {"label": "Romania", "value": "ROU", "search": "Romania"},
    {"label": "Russian Federation", "value": "RUS", "search": "Russian Federation"},
    {"label": "Rwanda", "value": "RWA", "search": "Rwanda"},
    {"label": "Saudi Arabia", "value": "SAU", "search": "Saudi Arabia"},
    {"label": "Sudan", "value": "SDN", "search": "Sudan"},
    {"label": "Senegal", "value": "SEN", "search": "Senegal"},
    {"label": "Singapore", "value": "SGP", "search": "Singapore"},
    {"label": "Solomon Islands", "value": "SLB", "search": "Solomon Islands"},
    {"label": "Sierra Leone", "value": "SLE", "search": "Sierra Leone"},
    {"label": "El Salvador", "value": "SLV", "search": "El Salvador"},
    {"label": "San Marino", "value": "SMR", "search": "San Marino"},
    {"label": "Somalia", "value": "SOM", "search": "Somalia"},
    {"label": "Serbia", "value": "SRB", "search": "Serbia"},
    {"label": "South Sudan", "value": "SSD", "search": "South Sudan"},
    {
        "label": "Sao Tome and Principe",
        "value": "STP",
        "search": "Sao Tome and Principe",
    },
    {"label": "Suriname", "value": "SUR", "search": "Suriname"},
    {"label": "Slovak Republic", "value": "SVK", "search": "Slovak Republic"},
    {"label": "Slovenia", "value": "SVN", "search": "Slovenia"},
    {"label": "Sweden", "value": "SWE", "search": "Sweden"},
    {"label": "Eswatini", "value": "SWZ", "search": "Eswatini"},
    {
        "label": "Sint Maarten (Dutch part)",
        "value": "SXM",
        "search": "Sint Maarten (Dutch part)",
    },
    {"label": "Seychelles", "value": "SYC", "search": "Seychelles"},
    {"label": "Syrian Arab Republic", "value": "SYR", "search": "Syrian Arab Republic"},
    {
        "label": "Turks and Caicos Islands",
        "value": "TCA",
        "search": "Turks and Caicos Islands",
    },
    {"label": "Chad", "value": "TCD", "search": "Chad"},
    {"label": "Togo", "value": "TGO", "search": "Togo"},
    {"label": "Thailand", "value": "THA", "search": "Thailand"},
    {"label": "Tajikistan", "value": "TJK", "search": "Tajikistan"},
    {"label": "Turkmenistan", "value": "TKM", "search": "Turkmenistan"},
    {"label": "Timor-Leste", "value": "TLS", "search": "Timor-Leste"},
    {"label": "Tonga", "value": "TON", "search": "Tonga"},
    {"label": "Trinidad and Tobago", "value": "TTO", "search": "Trinidad and Tobago"},
    {"label": "Tunisia", "value": "TUN", "search": "Tunisia"},
    {"label": "Turkiye", "value": "TUR", "search": "Turkiye"},
    {"label": "Tuvalu", "value": "TUV", "search": "Tuvalu"},
    {"label": "Tanzania", "value": "TZA", "search": "Tanzania"},
    {"label": "Uganda", "value": "UGA", "search": "Uganda"},
    {"label": "Ukraine", "value": "UKR", "search": "Ukraine"},
    {"label": "Uruguay", "value": "URY", "search": "Uruguay"},
    {"label": "United States", "value": "USA", "search": "United States"},
    {"label": "Uzbekistan", "value": "UZB", "search": "Uzbekistan"},
    {
        "label": "St. Vincent and the Grenadines",
        "value": "VCT",
        "search": "St. Vincent and the Grenadines",
    },
    {"label": "Venezuela, RB", "value": "VEN", "search": "Venezuela, RB"},
    {
        "label": "British Virgin Islands",
        "value": "VGB",
        "search": "British Virgin Islands",
    },
    {
        "label": "Virgin Islands (U.S.)",
        "value": "VIR",
        "search": "Virgin Islands (U.S.)",
    },
    {"label": "Viet Nam", "value": "VNM", "search": "Viet Nam"},
    {"label": "Vanuatu", "value": "VUT", "search": "Vanuatu"},
    {"label": "Samoa", "value": "WSM", "search": "Samoa"},
    {"label": "Kosovo", "value": "XKX", "search": "Kosovo"},
    {"label": "Yemen, Rep.", "value": "YEM", "search": "Yemen, Rep."},
    {"label": "South Africa", "value": "ZAF", "search": "South Africa"},
    {"label": "Zambia", "value": "ZMB", "search": "Zambia"},
    {"label": "Zimbabwe", "value": "ZWE", "search": "Zimbabwe"},
    
    {"label": "", "value": ""},
    
    {
        "label": html.Span(
            ["REGIONS", html.Hr()], style={"color": "green", "font-size": 20}
        ),
        "value": "REGIONS",
        "search": "Regions",
    },
    {
        "label": "Africa Eastern and Southern",
        "value": "AFE",
        "search": "Africa Eastern and Southern",
    },
    {"label": "Africa", "value": "AFR", "search": "Africa"},
    {
        "label": "Africa Western and Central",
        "value": "AFW",
        "search": "Africa Western and Central",
    },
    {"label": "Arab World", "value": "ARB", "search": "Arab World"},
    {
        "label": "Sub-Saharan Africa (IFC classification)",
        "value": "CAA",
        "search": "Sub-Saharan Africa (IFC classification)",
    },
    {
        "label": "East Asia and the Pacific (IFC classification)",
        "value": "CEA",
        "search": "East Asia and the Pacific (IFC classification)",
    },
    {
        "label": "Central Europe and the Baltics",
        "value": "CEB",
        "search": "Central Europe and the Baltics",
    },
    {
        "label": "Europe and Central Asia (IFC classification)",
        "value": "CEU",
        "search": "Europe and Central Asia (IFC classification)",
    },
    {
        "label": "Latin America and the Caribbean (IFC classification)",
        "value": "CLA",
        "search": "Latin America and the Caribbean (IFC classification)",
    },
    {
        "label": "Middle East and North Africa (IFC classification)",
        "value": "CME",
        "search": "Middle East and North Africa (IFC classification)",
    },
    {
        "label": "South Asia (IFC classification)",
        "value": "CSA",
        "search": "South Asia (IFC classification)",
    },
    {
        "label": "Caribbean small states",
        "value": "CSS",
        "search": "Caribbean small states",
    },
    {
        "label": "East Asia & Pacific (excluding high income)",
        "value": "EAP",
        "search": "East Asia & Pacific (excluding high income)",
    },
    {
        "label": "Early-demographic dividend",
        "value": "EAR",
        "search": "Early-demographic dividend",
    },
    {"label": "East Asia & Pacific", "value": "EAS", "search": "East Asia & Pacific"},
    {
        "label": "Europe & Central Asia (excluding high income)",
        "value": "ECA",
        "search": "Europe & Central Asia (excluding high income)",
    },
    {
        "label": "Europe & Central Asia",
        "value": "ECS",
        "search": "Europe & Central Asia",
    },
    {"label": "Euro area", "value": "EMU", "search": "Euro area"},
    {"label": "European Union", "value": "EUU", "search": "European Union"},
    {
        "label": "Fragile and conflict affected situations",
        "value": "FCS",
        "search": "Fragile and conflict affected situations",
    },
    {
        "label": "Heavily indebted poor countries (HIPC)",
        "value": "HPC",
        "search": "Heavily indebted poor countries (HIPC)",
    },
    {
        "label": "Latin America & Caribbean (excluding high income)",
        "value": "LAC",
        "search": "Latin America & Caribbean (excluding high income)",
    },
    {
        "label": "Latin America & Caribbean ",
        "value": "LCN",
        "search": "Latin America & Caribbean ",
    },
    {
        "label": "Least developed countries: UN classification",
        "value": "LDC",
        "search": "Least developed countries: UN classification",
    },
    {
        "label": "Late-demographic dividend",
        "value": "LTE",
        "search": "Late-demographic dividend",
    },
    {
        "label": "Middle East (developing only)",
        "value": "MDE",
        "search": "Middle East (developing only)",
    },
    {
        "label": "Middle East & North Africa",
        "value": "MEA",
        "search": "Middle East & North Africa",
    },
    {
        "label": "Middle East & North Africa (excluding high income)",
        "value": "MNA",
        "search": "Middle East & North Africa (excluding high income)",
    },
    {"label": "North America", "value": "NAC", "search": "North America"},
    {"label": "North Africa", "value": "NAF", "search": "North Africa"},
    {
        "label": "Non-resource rich Sub-Saharan Africa countries",
        "value": "NRS",
        "search": "Non-resource rich Sub-Saharan Africa countries",
    },
    {"label": "OECD members", "value": "OED", "search": "OECD members"},
    {"label": "Other small states", "value": "OSS", "search": "Other small states"},
    {
        "label": "Pre-demographic dividend",
        "value": "PRE",
        "search": "Pre-demographic dividend",
    },
    {
        "label": "Pacific island small states",
        "value": "PSS",
        "search": "Pacific island small states",
    },
    {
        "label": "Post-demographic dividend",
        "value": "PST",
        "search": "Post-demographic dividend",
    },
    {
        "label": "Resource rich Sub-Saharan Africa countries",
        "value": "RRS",
        "search": "Resource rich Sub-Saharan Africa countries",
    },
    {"label": "South Asia", "value": "SAS", "search": "South Asia"},
    {
        "label": "Sub-Saharan Africa (excluding high income)",
        "value": "SSA",
        "search": "Sub-Saharan Africa (excluding high income)",
    },
    {"label": "Sub-Saharan Africa ", "value": "SSF", "search": "Sub-Saharan Africa "},
    {"label": "Small states", "value": "SST", "search": "Small states"},
    {
        "label": "Sub-Saharan Africa excluding South Africa",
        "value": "SXZ",
        "search": "Sub-Saharan Africa excluding South Africa",
    },
    {"label": "World", "value": "WLD", "search": "World"},
    {
        "label": "Sub-Saharan Africa excluding South Africa and Nigeria",
        "value": "XZN",
        "search": "Sub-Saharan Africa excluding South Africa and Nigeria",
    },
]

indicator_list = [
    {
        "label": "Agricultural machinery, tractors",
        "value": "AG.AGR.TRAC.NO",
    },
    {
        "label": "Fertilizer consumption (% of fertilizer production)",
        "value": "AG.CON.FERT.PT.ZS",
    },
    {
        "label": "Fertilizer consumption (kilograms per hectare of arable land)",
        "value": "AG.CON.FERT.ZS",
    },
    {"label": "Agricultural land (sq. km)", "value": "AG.LND.AGRI.K2"},
    {
        "label": "Agricultural land (% of land area)",
        "value": "AG.LND.AGRI.ZS",
    },
    {"label": "Arable land (hectares)", "value": "AG.LND.ARBL.HA"},
    {
        "label": "Arable land (hectares per person)",
        "value": "AG.LND.ARBL.HA.PC",
    },
    {
        "label": "Arable land (% of land area)",
        "value": "AG.LND.ARBL.ZS",
    },
    {
        "label": "Land under cereal production (hectares)",
        "value": "AG.LND.CREL.HA",
    },
    {
        "label": "Permanent cropland (% of land area)",
        "value": "AG.LND.CROP.ZS",
    },
    {
        "label": "Rural land area where elevation is below 5 meters (sq. km)",
        "value": "AG.LND.EL5M.RU.K2",
    },
    {
        "label": "Rural land area where elevation is below 5 meters (% of total land area)",
        "value": "AG.LND.EL5M.RU.ZS",
    },
    {
        "label": "Urban land area where elevation is below 5 meters (sq. km)",
        "value": "AG.LND.EL5M.UR.K2",
    },
    {
        "label": "Urban land area where elevation is below 5 meters (% of total land area)",
        "value": "AG.LND.EL5M.UR.ZS",
    },
    {
        "label": "Land area where elevation is below 5 meters (% of total land area)",
        "value": "AG.LND.EL5M.ZS",
    },
    {"label": "Forest area (sq. km)", "value": "AG.LND.FRST.K2"},
    {
        "label": "Forest area (% of land area)",
        "value": "AG.LND.FRST.ZS",
    },
    {
        "label": "Agricultural irrigated land (% of total agricultural land)",
        "value": "AG.LND.IRIG.AG.ZS",
    },
    {
        "label": "Average precipitation in depth (mm per year)",
        "value": "AG.LND.PRCP.MM",
    },
    {"label": "Land area (sq. km)", "value": "AG.LND.TOTL.K2"},
    {"label": "Rural land area (sq. km)", "value": "AG.LND.TOTL.RU.K2"},
    {"label": "Urban land area (sq. km)", "value": "AG.LND.TOTL.UR.K2"},
    {
        "label": "Agricultural machinery, tractors per 100 sq. km of arable land",
        "value": "AG.LND.TRAC.ZS",
    },
    {
        "label": "Cereal production (metric tons)",
        "value": "AG.PRD.CREL.MT",
    },
    {
        "label": "Crop production index (2014-2016 = 100)",
        "value": "AG.PRD.CROP.XD",
    },
    {
        "label": "Food production index (2014-2016 = 100)",
        "value": "AG.PRD.FOOD.XD",
    },
    {
        "label": "Livestock production index (2014-2016 = 100)",
        "value": "AG.PRD.LVSK.XD",
    },
    {"label": "Surface area (sq. km)", "value": "AG.SRF.TOTL.K2"},
    {
        "label": "Cereal yield (kg per hectare)",
        "value": "AG.YLD.CREL.KG",
    },
    {
        "label": "Trade in services (% of GDP)",
        "value": "BG.GSR.NFSV.GD.ZS",
    },
    {
        "label": "Communications, computer, etc. (% of service imports, BoP)",
        "value": "BM.GSR.CMCP.ZS",
    },
    {
        "label": "Primary income payments (BoP, current US$)",
        "value": "BM.GSR.FCTY.CD",
    },
    {
        "label": "Imports of goods and services (BoP, current US$)",
        "value": "BM.GSR.GNFS.CD",
    },
    {
        "label": "Insurance and financial services (% of service imports, BoP)",
        "value": "BM.GSR.INSF.ZS",
    },
    {
        "label": "Goods imports (BoP, current US$)",
        "value": "BM.GSR.MRCH.CD",
    },
    {
        "label": "Service imports (BoP, current US$)",
        "value": "BM.GSR.NFSV.CD",
    },
    {
        "label": "Charges for the use of intellectual property, payments (BoP, current US$)",
        "value": "BM.GSR.ROYL.CD",
    },
    {
        "label": "Imports of goods, services and primary income (BoP, current US$)",
        "value": "BM.GSR.TOTL.CD",
    },
    {
        "label": "Transport services (% of service imports, BoP)",
        "value": "BM.GSR.TRAN.ZS",
    },
    {
        "label": "Travel services (% of service imports, BoP)",
        "value": "BM.GSR.TRVL.ZS",
    },
    {
        "label": "Foreign direct investment, net outflows (BoP, current US$)",
        "value": "BM.KLT.DINV.CD.WD",
    },
    {
        "label": "Foreign direct investment, net outflows (% of GDP)",
        "value": "BM.KLT.DINV.WD.GD.ZS",
    },
    {
        "label": "Secondary income, other sectors, payments (BoP, current US$)",
        "value": "BM.TRF.PRVT.CD",
    },
    {
        "label": "Personal remittances, paid (current US$)",
        "value": "BM.TRF.PWKR.CD.DT",
    },
    {
        "label": "Current account balance (BoP, current US$)",
        "value": "BN.CAB.XOKA.CD",
    },
    {
        "label": "Current account balance (% of GDP)",
        "value": "BN.CAB.XOKA.GD.ZS",
    },
    {
        "label": "Net financial account (BoP, current US$)",
        "value": "BN.FIN.TOTL.CD",
    },
    {
        "label": "Net primary income (BoP, current US$)",
        "value": "BN.GSR.FCTY.CD",
    },
    {
        "label": "Net trade in goods and services (BoP, current US$)",
        "value": "BN.GSR.GNFS.CD",
    },
    {
        "label": "Net trade in goods (BoP, current US$)",
        "value": "BN.GSR.MRCH.CD",
    },
    {
        "label": "Net errors and omissions (BoP, current US$)",
        "value": "BN.KAC.EOMS.CD",
    },
    {
        "label": "Foreign direct investment, net (BoP, current US$)",
        "value": "BN.KLT.DINV.CD",
    },
    {
        "label": "Portfolio investment, net (BoP, current US$)",
        "value": "BN.KLT.PTXL.CD",
    },
    {
        "label": "Reserves and related items (BoP, current US$)",
        "value": "BN.RES.INCL.CD",
    },
    {
        "label": "Net secondary income (BoP, current US$)",
        "value": "BN.TRF.CURR.CD",
    },
    {
        "label": "Net capital account (BoP, current US$)",
        "value": "BN.TRF.KOGT.CD",
    },
    {
        "label": "Grants, excluding technical cooperation (BoP, current US$)",
        "value": "BX.GRT.EXTA.CD.WD",
    },
    {
        "label": "Technical cooperation grants (BoP, current US$)",
        "value": "BX.GRT.TECH.CD.WD",
    },
    {
        "label": "ICT service exports (BoP, current US$)",
        "value": "BX.GSR.CCIS.CD",
    },
    {
        "label": "ICT service exports (% of service exports, BoP)",
        "value": "BX.GSR.CCIS.ZS",
    },
    {
        "label": "Communications, computer, etc. (% of service exports, BoP)",
        "value": "BX.GSR.CMCP.ZS",
    },
    {
        "label": "Primary income receipts (BoP, current US$)",
        "value": "BX.GSR.FCTY.CD",
    },
    {
        "label": "Exports of goods and services (BoP, current US$)",
        "value": "BX.GSR.GNFS.CD",
    },
    {
        "label": "Insurance and financial services (% of service exports, BoP)",
        "value": "BX.GSR.INSF.ZS",
    },
    {
        "label": "Goods exports (BoP, current US$)",
        "value": "BX.GSR.MRCH.CD",
    },
    {
        "label": "Service exports (BoP, current US$)",
        "value": "BX.GSR.NFSV.CD",
    },
    {
        "label": "Charges for the use of intellectual property, receipts (BoP, current US$)",
        "value": "BX.GSR.ROYL.CD",
    },
    {
        "label": "Exports of goods, services and primary income (BoP, current US$)",
        "value": "BX.GSR.TOTL.CD",
    },
    {
        "label": "Transport services (% of service exports, BoP)",
        "value": "BX.GSR.TRAN.ZS",
    },
    {
        "label": "Travel services (% of service exports, BoP)",
        "value": "BX.GSR.TRVL.ZS",
    },
    {
        "label": "Foreign direct investment, net inflows (BoP, current US$)",
        "value": "BX.KLT.DINV.CD.WD",
    },
    {
        "label": "Foreign direct investment, net inflows (% of GDP)",
        "value": "BX.KLT.DINV.WD.GD.ZS",
    },
    {
        "label": "Portfolio equity, net inflows (BoP, current US$)",
        "value": "BX.PEF.TOTL.CD.WD",
    },
    {
        "label": "Secondary income receipts (BoP, current US$)",
        "value": "BX.TRF.CURR.CD",
    },
    {
        "label": "Personal transfers, receipts (BoP, current US$)",
        "value": "BX.TRF.PWKR.CD",
    },
    {
        "label": "Personal remittances, received (current US$)",
        "value": "BX.TRF.PWKR.CD.DT",
    },
    {
        "label": "Personal remittances, received (% of GDP)",
        "value": "BX.TRF.PWKR.DT.GD.ZS",
    },
    {"label": "Control of Corruption: Estimate", "value": "CC.EST"},
    {
        "label": "Control of Corruption: Number of Sources",
        "value": "CC.NO.SRC",
    },
    {
        "label": "Control of Corruption: Percentile Rank",
        "value": "CC.PER.RNK",
    },
    {
        "label": "Control of Corruption: Percentile Rank, Lower Bound of 90% Confidence Interval",
        "value": "CC.PER.RNK.LOWER",
    },
    {
        "label": "Control of Corruption: Percentile Rank, Upper Bound of 90% Confidence Interval",
        "value": "CC.PER.RNK.UPPER",
    },
    {
        "label": "Control of Corruption: Standard Error",
        "value": "CC.STD.ERR",
    },
    {
        "label": "S&P Global Equity Indices (annual % change)",
        "value": "CM.MKT.INDX.ZG",
    },
    {
        "label": "Market capitalization of listed domestic companies (current US$)",
        "value": "CM.MKT.LCAP.CD",
    },
    {
        "label": "Market capitalization of listed domestic companies (% of GDP)",
        "value": "CM.MKT.LCAP.GD.ZS",
    },
    {
        "label": "Listed domestic companies, total",
        "value": "CM.MKT.LDOM.NO",
    },
    {
        "label": "Stocks traded, total value (current US$)",
        "value": "CM.MKT.TRAD.CD",
    },
    {
        "label": "Stocks traded, total value (% of GDP)",
        "value": "CM.MKT.TRAD.GD.ZS",
    },
    {
        "label": "Stocks traded, turnover ratio of domestic shares (%)",
        "value": "CM.MKT.TRNR",
    },
    {
        "label": "Net bilateral aid flows from DAC donors, Australia (current US$)",
        "value": "DC.DAC.AUSL.CD",
    },
    {
        "label": "Net bilateral aid flows from DAC donors, Austria (current US$)",
        "value": "DC.DAC.AUTL.CD",
    },
    {
        "label": "Net bilateral aid flows from DAC donors, Belgium (current US$)",
        "value": "DC.DAC.BELL.CD",
    },
    {
        "label": "Net bilateral aid flows from DAC donors, Canada (current US$)",
        "value": "DC.DAC.CANL.CD",
    },
    {
        "label": "Net bilateral aid flows from DAC donors, European Union institutions (current US$)",
        "value": "DC.DAC.CECL.CD",
    },
    {
        "label": "Net bilateral aid flows from DAC donors, Switzerland (current US$)",
        "value": "DC.DAC.CHEL.CD",
    },
    {
        "label": "Net bilateral aid flows from DAC donors, Czechia (current US$)",
        "value": "DC.DAC.CZEL.CD",
    },
    {
        "label": "Net bilateral aid flows from DAC donors, Germany (current US$)",
        "value": "DC.DAC.DEUL.CD",
    },
    {
        "label": "Net bilateral aid flows from DAC donors, Denmark (current US$)",
        "value": "DC.DAC.DNKL.CD",
    },
    {
        "label": "Net bilateral aid flows from DAC donors, Spain (current US$)",
        "value": "DC.DAC.ESPL.CD",
    },
    {
        "label": "Net bilateral aid flows from DAC donors, Estonia (current US$)",
        "value": "DC.DAC.ESTL.CD",
    },
    {
        "label": "Net bilateral aid flows from DAC donors, Finland (current US$)",
        "value": "DC.DAC.FINL.CD",
    },
    {
        "label": "Net bilateral aid flows from DAC donors, France (current US$)",
        "value": "DC.DAC.FRAL.CD",
    },
    {
        "label": "Net bilateral aid flows from DAC donors, United Kingdom (current US$)",
        "value": "DC.DAC.GBRL.CD",
    },
    {
        "label": "Net bilateral aid flows from DAC donors, Greece (current US$)",
        "value": "DC.DAC.GRCL.CD",
    },
    {
        "label": "Net bilateral aid flows from DAC donors, Hungary (current US$)",
        "value": "DC.DAC.HUNL.CD",
    },
    {
        "label": "Net bilateral aid flows from DAC donors, Ireland (current US$)",
        "value": "DC.DAC.IRLL.CD",
    },
    {
        "label": "Net bilateral aid flows from DAC donors, Iceland (current US$)",
        "value": "DC.DAC.ISLL.CD",
    },
    {
        "label": "Net bilateral aid flows from DAC donors, Italy (current US$)",
        "value": "DC.DAC.ITAL.CD",
    },
    {
        "label": "Net bilateral aid flows from DAC donors, Japan (current US$)",
        "value": "DC.DAC.JPNL.CD",
    },
    {
        "label": "Net bilateral aid flows from DAC donors, Korea, Rep. (current US$)",
        "value": "DC.DAC.KORL.CD",
    },
    {
        "label": "Net bilateral aid flows from DAC donors, Lithuania (current US$)",
        "value": "DC.DAC.LTUL.CD",
    },
    {
        "label": "Net bilateral aid flows from DAC donors, Luxembourg (current US$)",
        "value": "DC.DAC.LUXL.CD",
    },
    {
        "label": "Net bilateral aid flows from DAC donors, Netherlands (current US$)",
        "value": "DC.DAC.NLDL.CD",
    },
    {
        "label": "Net bilateral aid flows from DAC donors, Norway (current US$)",
        "value": "DC.DAC.NORL.CD",
    },
    {
        "label": "Net bilateral aid flows from DAC donors, New Zealand (current US$)",
        "value": "DC.DAC.NZLL.CD",
    },
    {
        "label": "Net bilateral aid flows from DAC donors, Poland (current US$)",
        "value": "DC.DAC.POLL.CD",
    },
    {
        "label": "Net bilateral aid flows from DAC donors, Portugal (current US$)",
        "value": "DC.DAC.PRTL.CD",
    },
    {
        "label": "Net bilateral aid flows from DAC donors, Slovak Republic (current US$)",
        "value": "DC.DAC.SVKL.CD",
    },
    {
        "label": "Net bilateral aid flows from DAC donors, Slovenia (current US$)",
        "value": "DC.DAC.SVNL.CD",
    },
    {
        "label": "Net bilateral aid flows from DAC donors, Sweden (current US$)",
        "value": "DC.DAC.SWEL.CD",
    },
    {
        "label": "Net bilateral aid flows from DAC donors, Total (current US$)",
        "value": "DC.DAC.TOTL.CD",
    },
    {
        "label": "Net bilateral aid flows from DAC donors, United States (current US$)",
        "value": "DC.DAC.USAL.CD",
    },
    {
        "label": "Net ODA provided, to the least developed countries (current US$)",
        "value": "DC.ODA.TLDC.CD",
    },
    {
        "label": "Net ODA provided to the least developed countries (% of GNI)",
        "value": "DC.ODA.TLDC.GN.ZS",
    },
    {
        "label": "Net ODA provided, total (current US$)",
        "value": "DC.ODA.TOTL.CD",
    },
    {
        "label": "Net ODA provided, total (% of GNI)",
        "value": "DC.ODA.TOTL.GN.ZS",
    },
    {
        "label": "Net ODA provided, total (constant 2021 US$)",
        "value": "DC.ODA.TOTL.KD",
    },
    {
        "label": "External debt stocks, total (DOD, current US$)",
        "value": "DT.DOD.DECT.CD",
    },
    {
        "label": "External debt stocks (% of GNI)",
        "value": "DT.DOD.DECT.GN.ZS",
    },
    {
        "label": "Use of IMF credit (DOD, current US$)",
        "value": "DT.DOD.DIMF.CD",
    },
    {
        "label": "External debt stocks, long-term (DOD, current US$)",
        "value": "DT.DOD.DLXF.CD",
    },
    {
        "label": "External debt stocks, private nonguaranteed (PNG) (DOD, current US$)",
        "value": "DT.DOD.DPNG.CD",
    },
    {
        "label": "External debt stocks, public and publicly guaranteed (PPG) (DOD, current US$)",
        "value": "DT.DOD.DPPG.CD",
    },
    {
        "label": "External debt stocks, short-term (DOD, current US$)",
        "value": "DT.DOD.DSTC.CD",
    },
    {
        "label": "Short-term debt (% of total reserves)",
        "value": "DT.DOD.DSTC.IR.ZS",
    },
    {
        "label": "Short-term debt (% of exports of goods, services and primary income)",
        "value": "DT.DOD.DSTC.XP.ZS",
    },
    {
        "label": "Short-term debt (% of total external debt)",
        "value": "DT.DOD.DSTC.ZS",
    },
    {
        "label": "PPG, IBRD (DOD, current US$)",
        "value": "DT.DOD.MIBR.CD",
    },
    {"label": "PPG, IDA (DOD, current US$)", "value": "DT.DOD.MIDA.CD"},
    {
        "label": "IBRD loans and IDA credits (DOD, current US$)",
        "value": "DT.DOD.MWBG.CD",
    },
    {
        "label": "Present value of external debt (current US$)",
        "value": "DT.DOD.PVLX.CD",
    },
    {
        "label": "Present value of external debt (% of exports of goods, services and primary income)",
        "value": "DT.DOD.PVLX.EX.ZS",
    },
    {
        "label": "Present value of external debt (% of GNI)",
        "value": "DT.DOD.PVLX.GN.ZS",
    },
    {
        "label": "Net financial flows, bilateral (NFL, current US$)",
        "value": "DT.NFL.BLAT.CD",
    },
    {
        "label": "Portfolio investment, bonds (PPG + PNG) (NFL, current US$)",
        "value": "DT.NFL.BOND.CD",
    },
    {
        "label": "Net official flows from UN agencies, CERF (current US$)",
        "value": "DT.NFL.CERF.CD",
    },
    {
        "label": "Net flows on external debt, private nonguaranteed (PNG) (NFL, current US$)",
        "value": "DT.NFL.DPNG.CD",
    },
    {
        "label": "Net official flows from UN agencies, FAO (current US$)",
        "value": "DT.NFL.FAOG.CD",
    },
    {
        "label": "Net official flows from UN agencies, IAEA (current US$)",
        "value": "DT.NFL.IAEA.CD",
    },
    {
        "label": "Net official flows from UN agencies, IFAD (current US$)",
        "value": "DT.NFL.IFAD.CD",
    },
    {
        "label": "Net official flows from UN agencies, ILO (current US$)",
        "value": "DT.NFL.ILOG.CD",
    },
    {
        "label": "Net financial flows, IMF concessional (NFL, current US$)",
        "value": "DT.NFL.IMFC.CD",
    },
    {
        "label": "Net financial flows, IMF nonconcessional (NFL, current US$)",
        "value": "DT.NFL.IMFN.CD",
    },
    {
        "label": "Net financial flows, IBRD (NFL, current US$)",
        "value": "DT.NFL.MIBR.CD",
    },
    {
        "label": "Net financial flows, IDA (NFL, current US$)",
        "value": "DT.NFL.MIDA.CD",
    },
    {
        "label": "Net financial flows, multilateral (NFL, current US$)",
        "value": "DT.NFL.MLAT.CD",
    },
    {
        "label": "Net financial flows, others (NFL, current US$)",
        "value": "DT.NFL.MOTH.CD",
    },
    {
        "label": "IFC, private nonguaranteed (NFL, US$)",
        "value": "DT.NFL.NIFC.CD",
    },
    {
        "label": "PPG, official creditors (NFL, US$)",
        "value": "DT.NFL.OFFT.CD",
    },
    {
        "label": "PPG, bonds (NFL, current US$)",
        "value": "DT.NFL.PBND.CD",
    },
    {
        "label": "PPG, commercial banks (NFL, current US$)",
        "value": "DT.NFL.PCBK.CD",
    },
    {
        "label": "Commercial banks and other lending (PPG + PNG) (NFL, current US$)",
        "value": "DT.NFL.PCBO.CD",
    },
    {
        "label": "PNG, bonds (NFL, current US$)",
        "value": "DT.NFL.PNGB.CD",
    },
    {
        "label": "PNG, commercial banks and other creditors (NFL, current US$)",
        "value": "DT.NFL.PNGC.CD",
    },
    {
        "label": "PPG, other private creditors (NFL, current US$)",
        "value": "DT.NFL.PROP.CD",
    },
    {
        "label": "PPG, private creditors (NFL, US$)",
        "value": "DT.NFL.PRVT.CD",
    },
    {
        "label": "Net financial flows, RDB concessional (NFL, current US$)",
        "value": "DT.NFL.RDBC.CD",
    },
    {
        "label": "Net financial flows, RDB nonconcessional (NFL, current US$)",
        "value": "DT.NFL.RDBN.CD",
    },
    {
        "label": "Net official flows from UN agencies, SDGFUND (current US$)",
        "value": "DT.NFL.SDGF.CD",
    },
    {
        "label": "Net official flows from UN agencies, SPRP (current US$)",
        "value": "DT.NFL.SPRP.CD",
    },
    {
        "label": "Net official flows from UN agencies, UNAIDS (current US$)",
        "value": "DT.NFL.UNAI.CD",
    },
    {
        "label": "Net official flows from UN agencies, UNCDF (current US$)",
        "value": "DT.NFL.UNCD.CD",
    },
    {
        "label": "Net official flows from UN agencies, UNICEF (current US$)",
        "value": "DT.NFL.UNCF.CD",
    },
    {
        "label": "Net official flows from UN agencies, UNHCR (current US$)",
        "value": "DT.NFL.UNCR.CD",
    },
    {
        "label": "Net official flows from UN agencies, UNCTAD (current US$)",
        "value": "DT.NFL.UNCTAD.CD",
    },
    {
        "label": "Net official flows from UN agencies, UNCOVID (current US$)",
        "value": "DT.NFL.UNCV.CD",
    },
    {
        "label": "Net official flows from UN agencies, UNDP (current US$)",
        "value": "DT.NFL.UNDP.CD",
    },
    {
        "label": "Net official flows from UN agencies, UNECE (current US$)",
        "value": "DT.NFL.UNEC.CD",
    },
    {
        "label": "Net official flows from UN agencies, UNEP (current US$)",
        "value": "DT.NFL.UNEP.CD",
    },
    {
        "label": "Net official flows from UN agencies, UNFPA (current US$)",
        "value": "DT.NFL.UNFP.CD",
    },
    {
        "label": "Net official flows from UN agencies, UNIDIR (current US$)",
        "value": "DT.NFL.UNID.CD",
    },
    {
        "label": "Net official flows from UN agencies, UNIDO (current US$)",
        "value": "DT.NFL.UNIDO.CD",
    },
    {
        "label": "Net official flows from UN agencies, UNPBF (current US$)",
        "value": "DT.NFL.UNPB.CD",
    },
    {
        "label": "Net official flows from UN agencies, UNRWA (current US$)",
        "value": "DT.NFL.UNRW.CD",
    },
    {
        "label": "Net official flows from UN agencies, UNTA (current US$)",
        "value": "DT.NFL.UNTA.CD",
    },
    {
        "label": "Net official flows from UN agencies, UNWOMEN (current US$)",
        "value": "DT.NFL.UNWN.CD",
    },
    {
        "label": "Net official flows from UN agencies, UNWTO (current US$)",
        "value": "DT.NFL.UNWT.CD",
    },
    {
        "label": "Net official flows from UN agencies, WFP (current US$)",
        "value": "DT.NFL.WFPG.CD",
    },
    {
        "label": "Net official flows from UN agencies, WHO (current US$)",
        "value": "DT.NFL.WHOL.CD",
    },
    {
        "label": "Net official flows from UN agencies, WTO-ITC (current US$)",
        "value": "DT.NFL.WITC.CD",
    },
    {
        "label": "Net official development assistance and official aid received (current US$)",
        "value": "DT.ODA.ALLD.CD",
    },
    {
        "label": "Net official development assistance and official aid received (constant 2021 US$)",
        "value": "DT.ODA.ALLD.KD",
    },
    {
        "label": "Net official aid received (current US$)",
        "value": "DT.ODA.OATL.CD",
    },
    {
        "label": "Net official aid received (constant 2021 US$)",
        "value": "DT.ODA.OATL.KD",
    },
    {
        "label": "Net official development assistance received (current US$)",
        "value": "DT.ODA.ODAT.CD",
    },
    {
        "label": "Net ODA received (% of gross capital formation)",
        "value": "DT.ODA.ODAT.GI.ZS",
    },
    {
        "label": "Net ODA received (% of GNI)",
        "value": "DT.ODA.ODAT.GN.ZS",
    },
    {
        "label": "Net official development assistance received (constant 2021 US$)",
        "value": "DT.ODA.ODAT.KD",
    },
    {
        "label": "Net ODA received (% of imports of goods, services and primary income)",
        "value": "DT.ODA.ODAT.MP.ZS",
    },
    {
        "label": "Net ODA received per capita (current US$)",
        "value": "DT.ODA.ODAT.PC.ZS",
    },
    {
        "label": "Net ODA received (% of central government expense)",
        "value": "DT.ODA.ODAT.XP.ZS",
    },
    {
        "label": "Debt service on external debt, total (TDS, current US$)",
        "value": "DT.TDS.DECT.CD",
    },
    {
        "label": "Total debt service (% of exports of goods, services and primary income)",
        "value": "DT.TDS.DECT.EX.ZS",
    },
    {
        "label": "Total debt service (% of GNI)",
        "value": "DT.TDS.DECT.GN.ZS",
    },
    {
        "label": "IMF repurchases and charges (TDS, current US$)",
        "value": "DT.TDS.DIMF.CD",
    },
    {
        "label": "Debt service (PPG and IMF only, % of exports of goods, services and primary income)",
        "value": "DT.TDS.DPPF.XP.ZS",
    },
    {
        "label": "Debt service on external debt, public and publicly guaranteed (PPG) (TDS, current US$)",
        "value": "DT.TDS.DPPG.CD",
    },
    {
        "label": "Public and publicly guaranteed debt service (% of GNI)",
        "value": "DT.TDS.DPPG.GN.ZS",
    },
    {
        "label": "Public and publicly guaranteed debt service (% of exports of goods, services and primary income)",
        "value": "DT.TDS.DPPG.XP.ZS",
    },
    {
        "label": "Multilateral debt service (TDS, current US$)",
        "value": "DT.TDS.MLAT.CD",
    },
    {
        "label": "Multilateral debt service (% of public and publicly guaranteed debt service)",
        "value": "DT.TDS.MLAT.PG.ZS",
    },
    {
        "label": "Access to clean fuels and technologies for cooking, rural (% of rural population)",
        "value": "EG.CFT.ACCS.RU.ZS",
    },
    {
        "label": "Access to clean fuels and technologies for cooking, urban (% of urban population)",
        "value": "EG.CFT.ACCS.UR.ZS",
    },
    {
        "label": "Access to clean fuels and technologies for cooking (% of population)",
        "value": "EG.CFT.ACCS.ZS",
    },
    {
        "label": "Energy intensity level of primary energy (MJ/$2017 PPP GDP)",
        "value": "EG.EGY.PRIM.PP.KD",
    },
    {
        "label": "Access to electricity, rural (% of rural population)",
        "value": "EG.ELC.ACCS.RU.ZS",
    },
    {
        "label": "Access to electricity, urban (% of urban population)",
        "value": "EG.ELC.ACCS.UR.ZS",
    },
    {
        "label": "Access to electricity (% of population)",
        "value": "EG.ELC.ACCS.ZS",
    },
    {
        "label": "Electricity production from coal sources (% of total)",
        "value": "EG.ELC.COAL.ZS",
    },
    {
        "label": "Electricity production from oil, gas and coal sources (% of total)",
        "value": "EG.ELC.FOSL.ZS",
    },
    {
        "label": "Electricity production from hydroelectric sources (% of total)",
        "value": "EG.ELC.HYRO.ZS",
    },
    {
        "label": "Electric power transmission and distribution losses (% of output)",
        "value": "EG.ELC.LOSS.ZS",
    },
    {
        "label": "Electricity production from natural gas sources (% of total)",
        "value": "EG.ELC.NGAS.ZS",
    },
    {
        "label": "Electricity production from nuclear sources (% of total)",
        "value": "EG.ELC.NUCL.ZS",
    },
    {
        "label": "Electricity production from oil sources (% of total)",
        "value": "EG.ELC.PETR.ZS",
    },
    {
        "label": "Renewable electricity output (% of total electricity output)",
        "value": "EG.ELC.RNEW.ZS",
    },
    {
        "label": "Electricity production from renewable sources, excluding hydroelectric (kWh)",
        "value": "EG.ELC.RNWX.KH",
    },
    {
        "label": "Electricity production from renewable sources, excluding hydroelectric (% of total)",
        "value": "EG.ELC.RNWX.ZS",
    },
    {
        "label": "Renewable energy consumption (% of total final energy consumption)",
        "value": "EG.FEC.RNEW.ZS",
    },
    {
        "label": "GDP per unit of energy use (PPP $ per kg of oil equivalent)",
        "value": "EG.GDP.PUSE.KO.PP",
    },
    {
        "label": "GDP per unit of energy use (constant 2017 PPP $ per kg of oil equivalent)",
        "value": "EG.GDP.PUSE.KO.PP.KD",
    },
    {
        "label": "Energy imports, net (% of energy use)",
        "value": "EG.IMP.CONS.ZS",
    },
    {
        "label": "Alternative and nuclear energy (% of total energy use)",
        "value": "EG.USE.COMM.CL.ZS",
    },
    {
        "label": "Fossil fuel energy consumption (% of total)",
        "value": "EG.USE.COMM.FO.ZS",
    },
    {
        "label": "Energy use (kg of oil equivalent) per $1,000 GDP (constant 2017 PPP)",
        "value": "EG.USE.COMM.GD.PP.KD",
    },
    {
        "label": "Combustible renewables and waste (% of total energy)",
        "value": "EG.USE.CRNW.ZS",
    },
    {
        "label": "Electric power consumption (kWh per capita)",
        "value": "EG.USE.ELEC.KH.PC",
    },
    {
        "label": "Energy use (kg of oil equivalent per capita)",
        "value": "EG.USE.PCAP.KG.OE",
    },
    {
        "label": "CO2 intensity (kg per kg of oil equivalent energy use)",
        "value": "EN.ATM.CO2E.EG.ZS",
    },
    {
        "label": "CO2 emissions from gaseous fuel consumption (kt)",
        "value": "EN.ATM.CO2E.GF.KT",
    },
    {
        "label": "CO2 emissions from gaseous fuel consumption (% of total)",
        "value": "EN.ATM.CO2E.GF.ZS",
    },
    {
        "label": "CO2 emissions (kg per 2015 US$ of GDP)",
        "value": "EN.ATM.CO2E.KD.GD",
    },
    {"label": "CO2 emissions (kt)", "value": "EN.ATM.CO2E.KT"},
    {
        "label": "CO2 emissions from liquid fuel consumption (kt)",
        "value": "EN.ATM.CO2E.LF.KT",
    },
    {
        "label": "CO2 emissions from liquid fuel consumption (% of total)",
        "value": "EN.ATM.CO2E.LF.ZS",
    },
    {
        "label": "CO2 emissions (metric tons per capita)",
        "value": "EN.ATM.CO2E.PC",
    },
    {
        "label": "CO2 emissions (kg per PPP $ of GDP)",
        "value": "EN.ATM.CO2E.PP.GD",
    },
    {
        "label": "CO2 emissions (kg per 2017 PPP $ of GDP)",
        "value": "EN.ATM.CO2E.PP.GD.KD",
    },
    {
        "label": "CO2 emissions from solid fuel consumption (kt)",
        "value": "EN.ATM.CO2E.SF.KT",
    },
    {
        "label": "CO2 emissions from solid fuel consumption (% of total)",
        "value": "EN.ATM.CO2E.SF.ZS",
    },
    {
        "label": "Other greenhouse gas emissions, HFC, PFC and SF6 (thousand metric tons of CO2 equivalent)",
        "value": "EN.ATM.GHGO.KT.CE",
    },
    {
        "label": "Other greenhouse gas emissions (% change from 1990)",
        "value": "EN.ATM.GHGO.ZG",
    },
    {
        "label": "Total greenhouse gas emissions (kt of CO2 equivalent)",
        "value": "EN.ATM.GHGT.KT.CE",
    },
    {
        "label": "Total greenhouse gas emissions (% change from 1990)",
        "value": "EN.ATM.GHGT.ZG",
    },
    {
        "label": "HFC gas emissions (thousand metric tons of CO2 equivalent)",
        "value": "EN.ATM.HFCG.KT.CE",
    },
    {
        "label": "Agricultural methane emissions (thousand metric tons of CO2 equivalent)",
        "value": "EN.ATM.METH.AG.KT.CE",
    },
    {
        "label": "Agricultural methane emissions (% of total)",
        "value": "EN.ATM.METH.AG.ZS",
    },
    {
        "label": "Methane emissions in energy sector (thousand metric tons of CO2 equivalent)",
        "value": "EN.ATM.METH.EG.KT.CE",
    },
    {
        "label": "Energy related methane emissions (% of total)",
        "value": "EN.ATM.METH.EG.ZS",
    },
    {
        "label": "Methane emissions (kt of CO2 equivalent)",
        "value": "EN.ATM.METH.KT.CE",
    },
    {
        "label": "Methane emissions (% change from 1990)",
        "value": "EN.ATM.METH.ZG",
    },
    {
        "label": "Agricultural nitrous oxide emissions (thousand metric tons of CO2 equivalent)",
        "value": "EN.ATM.NOXE.AG.KT.CE",
    },
    {
        "label": "Agricultural nitrous oxide emissions (% of total)",
        "value": "EN.ATM.NOXE.AG.ZS",
    },
    {
        "label": "Nitrous oxide emissions in energy sector (thousand metric tons of CO2 equivalent)",
        "value": "EN.ATM.NOXE.EG.KT.CE",
    },
    {
        "label": "Nitrous oxide emissions in energy sector (% of total)",
        "value": "EN.ATM.NOXE.EG.ZS",
    },
    {
        "label": "Nitrous oxide emissions (thousand metric tons of CO2 equivalent)",
        "value": "EN.ATM.NOXE.KT.CE",
    },
    {
        "label": "Nitrous oxide emissions (% change from 1990)",
        "value": "EN.ATM.NOXE.ZG",
    },
    {
        "label": "PFC gas emissions (thousand metric tons of CO2 equivalent)",
        "value": "EN.ATM.PFCG.KT.CE",
    },
    {
        "label": "PM2.5 air pollution, mean annual exposure (micrograms per cubic meter)",
        "value": "EN.ATM.PM25.MC.M3",
    },
    {
        "label": "PM2.5 pollution, population exposed to levels exceeding WHO Interim Target-1 value (% of total)",
        "value": "EN.ATM.PM25.MC.T1.ZS",
    },
    {
        "label": "PM2.5 pollution, population exposed to levels exceeding WHO Interim Target-2 value (% of total)",
        "value": "EN.ATM.PM25.MC.T2.ZS",
    },
    {
        "label": "PM2.5 pollution, population exposed to levels exceeding WHO Interim Target-3 value (% of total)",
        "value": "EN.ATM.PM25.MC.T3.ZS",
    },
    {
        "label": "PM2.5 air pollution, population exposed to levels exceeding WHO guideline value (% of total)",
        "value": "EN.ATM.PM25.MC.ZS",
    },
    {
        "label": "SF6 gas emissions (thousand metric tons of CO2 equivalent)",
        "value": "EN.ATM.SF6G.KT.CE",
    },
    {"label": "Bird species, threatened", "value": "EN.BIR.THRD.NO"},
    {
        "label": "Disaster risk reduction progress score (1-5 scale; 5=best)",
        "value": "EN.CLC.DRSK.XQ",
    },
    {
        "label": "GHG net emissions/removals by LUCF (Mt of CO2 equivalent)",
        "value": "EN.CLC.GHGR.MT.CE",
    },
    {
        "label": "Droughts, floods, extreme temperatures (% of population, average 1990-2009)",
        "value": "EN.CLC.MDAT.ZS",
    },
    {
        "label": "CO2 emissions from residential buildings and commercial and public services (% of total fuel combustion)",
        "value": "EN.CO2.BLDG.ZS",
    },
    {
        "label": "CO2 emissions from electricity and heat production, total (% of total fuel combustion)",
        "value": "EN.CO2.ETOT.ZS",
    },
    {
        "label": "CO2 emissions from manufacturing industries and construction (% of total fuel combustion)",
        "value": "EN.CO2.MANF.ZS",
    },
    {
        "label": "CO2 emissions from other sectors, excluding residential buildings and commercial and public services (% of total fuel combustion)",
        "value": "EN.CO2.OTHX.ZS",
    },
    {
        "label": "CO2 emissions from transport (% of total fuel combustion)",
        "value": "EN.CO2.TRAN.ZS",
    },
    {"label": "Fish species, threatened", "value": "EN.FSH.THRD.NO"},
    {
        "label": "Plant species (higher), threatened",
        "value": "EN.HPT.THRD.NO",
    },
    {"label": "Mammal species, threatened", "value": "EN.MAM.THRD.NO"},
    {
        "label": "Population density (people per sq. km of land area)",
        "value": "EN.POP.DNST",
    },
    {
        "label": "Rural population living in areas where elevation is below 5 meters (% of total population)",
        "value": "EN.POP.EL5M.RU.ZS",
    },
    {
        "label": "Urban population living in areas where elevation is below 5 meters (% of total population)",
        "value": "EN.POP.EL5M.UR.ZS",
    },
    {
        "label": "Population living in areas where elevation is below 5 meters (% of total population)",
        "value": "EN.POP.EL5M.ZS",
    },
    {
        "label": "Population living in slums (% of urban population)",
        "value": "EN.POP.SLUM.UR.ZS",
    },
    {"label": "Population in largest city", "value": "EN.URB.LCTY"},
    {
        "label": "Population in the largest city (% of urban population)",
        "value": "EN.URB.LCTY.UR.ZS",
    },
    {
        "label": "Population in urban agglomerations of more than 1 million",
        "value": "EN.URB.MCTY",
    },
    {
        "label": "Population in urban agglomerations of more than 1 million (% of total population)",
        "value": "EN.URB.MCTY.TL.ZS",
    },
    {
        "label": "Pump price for diesel fuel (US$ per liter)",
        "value": "EP.PMP.DESL.CD",
    },
    {
        "label": "Pump price for gasoline (US$ per liter)",
        "value": "EP.PMP.SGAS.CD",
    },
    {
        "label": "Aquaculture production (metric tons)",
        "value": "ER.FSH.AQUA.MT",
    },
    {
        "label": "Capture fisheries production (metric tons)",
        "value": "ER.FSH.CAPT.MT",
    },
    {
        "label": "Total fisheries production (metric tons)",
        "value": "ER.FSH.PROD.MT",
    },
    {
        "label": "Water productivity, total (constant 2015 US$ GDP per cubic meter of total freshwater withdrawal)",
        "value": "ER.GDP.FWTL.M3.KD",
    },
    {
        "label": "Annual freshwater withdrawals, agriculture (% of total freshwater withdrawal)",
        "value": "ER.H2O.FWAG.ZS",
    },
    {
        "label": "Annual freshwater withdrawals, domestic (% of total freshwater withdrawal)",
        "value": "ER.H2O.FWDM.ZS",
    },
    {
        "label": "Annual freshwater withdrawals, industry (% of total freshwater withdrawal)",
        "value": "ER.H2O.FWIN.ZS",
    },
    {
        "label": "Level of water stress: freshwater withdrawal as a proportion of available freshwater resources",
        "value": "ER.H2O.FWST.ZS",
    },
    {
        "label": "Annual freshwater withdrawals, total (billion cubic meters)",
        "value": "ER.H2O.FWTL.K3",
    },
    {
        "label": "Annual freshwater withdrawals, total (% of internal resources)",
        "value": "ER.H2O.FWTL.ZS",
    },
    {
        "label": "Renewable internal freshwater resources, total (billion cubic meters)",
        "value": "ER.H2O.INTR.K3",
    },
    {
        "label": "Renewable internal freshwater resources per capita (cubic meters)",
        "value": "ER.H2O.INTR.PC",
    },
    {
        "label": "Terrestrial protected areas (% of total land area)",
        "value": "ER.LND.PTLD.ZS",
    },
    {
        "label": "Marine protected areas (% of territorial waters)",
        "value": "ER.MRN.PTMR.ZS",
    },
    {
        "label": "Terrestrial and marine protected areas (% of total territorial area)",
        "value": "ER.PTD.TOTL.ZS",
    },
    {
        "label": "Bank nonperforming loans to total gross loans (%)",
        "value": "FB.AST.NPER.ZS",
    },
    {
        "label": "Automated teller machines (ATMs) (per 100,000 adults)",
        "value": "FB.ATM.TOTL.P5",
    },
    {
        "label": "Bank capital to assets ratio (%)",
        "value": "FB.BNK.CAPA.ZS",
    },
    {
        "label": "Commercial bank branches (per 100,000 adults)",
        "value": "FB.CBK.BRCH.P5",
    },
    {
        "label": "Borrowers from commercial banks (per 1,000 adults)",
        "value": "FB.CBK.BRWR.P3",
    },
    {
        "label": "Depositors with commercial banks (per 1,000 adults)",
        "value": "FB.CBK.DPTR.P3",
    },
    {
        "label": "Domestic credit to private sector by banks (% of GDP)",
        "value": "FD.AST.PRVT.GD.ZS",
    },
    {
        "label": "Bank liquid reserves to bank assets ratio (%)",
        "value": "FD.RES.LIQU.AS.ZS",
    },
    {
        "label": "Total reserves (includes gold, current US$)",
        "value": "FI.RES.TOTL.CD",
    },
    {
        "label": "Total reserves (% of total external debt)",
        "value": "FI.RES.TOTL.DT.ZS",
    },
    {
        "label": "Total reserves in months of imports",
        "value": "FI.RES.TOTL.MO",
    },
    {
        "label": "Total reserves minus gold (current US$)",
        "value": "FI.RES.XGLD.CD",
    },
    {
        "label": "Claims on central government (annual growth as % of broad money)",
        "value": "FM.AST.CGOV.ZG.M3",
    },
    {
        "label": "Claims on other sectors of the domestic economy (annual growth as % of broad money)",
        "value": "FM.AST.DOMO.ZG.M3",
    },
    {
        "label": "Net domestic credit (current LCU)",
        "value": "FM.AST.DOMS.CN",
    },
    {
        "label": "Net foreign assets (current LCU)",
        "value": "FM.AST.NFRG.CN",
    },
    {
        "label": "Monetary Sector credit to private sector (% GDP)",
        "value": "FM.AST.PRVT.GD.ZS",
    },
    {
        "label": "Claims on private sector (annual growth as % of broad money)",
        "value": "FM.AST.PRVT.ZG.M3",
    },
    {"label": "Broad money (current LCU)", "value": "FM.LBL.BMNY.CN"},
    {"label": "Broad money (% of GDP)", "value": "FM.LBL.BMNY.GD.ZS"},
    {
        "label": "Broad money to total reserves ratio",
        "value": "FM.LBL.BMNY.IR.ZS",
    },
    {
        "label": "Broad money growth (annual %)",
        "value": "FM.LBL.BMNY.ZG",
    },
    {
        "label": "Consumer price index (2010 = 100)",
        "value": "FP.CPI.TOTL",
    },
    {
        "label": "Inflation, consumer prices (annual %)",
        "value": "FP.CPI.TOTL.ZG",
    },
    {
        "label": "Wholesale price index (2010 = 100)",
        "value": "FP.WPI.TOTL",
    },
    {"label": "Deposit interest rate (%)", "value": "FR.INR.DPST"},
    {"label": "Lending interest rate (%)", "value": "FR.INR.LEND"},
    {
        "label": "Interest rate spread (lending rate minus deposit rate, %)",
        "value": "FR.INR.LNDP",
    },
    {"label": "Real interest rate (%)", "value": "FR.INR.RINR"},
    {
        "label": "Risk premium on lending (lending rate minus treasury bill rate, %)",
        "value": "FR.INR.RISK",
    },
    {
        "label": "Claims on central government, etc. (% GDP)",
        "value": "FS.AST.CGOV.GD.ZS",
    },
    {
        "label": "Claims on other sectors of the domestic economy (% of GDP)",
        "value": "FS.AST.DOMO.GD.ZS",
    },
    {
        "label": "Domestic credit provided by financial sector (% of GDP)",
        "value": "FS.AST.DOMS.GD.ZS",
    },
    {
        "label": "Domestic credit to private sector (% of GDP)",
        "value": "FS.AST.PRVT.GD.ZS",
    },
    {
        "label": "Account ownership at a financial institution or with a mobile-money-service provider, poorest 40% (% of population ages 15+)",
        "value": "FX.OWN.TOTL.40.ZS",
    },
    {
        "label": "Account ownership at a financial institution or with a mobile-money-service provider, richest 60% (% of population ages 15+)",
        "value": "FX.OWN.TOTL.60.ZS",
    },
    {
        "label": "Account ownership at a financial institution or with a mobile-money-service provider, female (% of population ages 15+)",
        "value": "FX.OWN.TOTL.FE.ZS",
    },
    {
        "label": "Account ownership at a financial institution or with a mobile-money-service provider, male (% of population ages 15+)",
        "value": "FX.OWN.TOTL.MA.ZS",
    },
    {
        "label": "Account ownership at a financial institution or with a mobile-money-service provider, older adults (% of population ages 25+)",
        "value": "FX.OWN.TOTL.OL.ZS",
    },
    {
        "label": "Account ownership at a financial institution or with a mobile-money-service provider, primary education or less (% of population ages 15+)",
        "value": "FX.OWN.TOTL.PL.ZS",
    },
    {
        "label": "Account ownership at a financial institution or with a mobile-money-service provider, secondary education or more (% of population ages 15+)",
        "value": "FX.OWN.TOTL.SO.ZS",
    },
    {
        "label": "Account ownership at a financial institution or with a mobile-money-service provider, young adults (% of population ages 15-24)",
        "value": "FX.OWN.TOTL.YG.ZS",
    },
    {
        "label": "Account ownership at a financial institution or with a mobile-money-service provider (% of population ages 15+)",
        "value": "FX.OWN.TOTL.ZS",
    },
    {
        "label": "Research and development expenditure (% of GDP)",
        "value": "GB.XPD.RSDV.GD.ZS",
    },
    {
        "label": "Net acquisition of financial assets (current LCU)",
        "value": "GC.AST.TOTL.CN",
    },
    {
        "label": "Net acquisition of financial assets (% of GDP)",
        "value": "GC.AST.TOTL.GD.ZS",
    },
    {
        "label": "Central government debt, total (current LCU)",
        "value": "GC.DOD.TOTL.CN",
    },
    {
        "label": "Central government debt, total (% of GDP)",
        "value": "GC.DOD.TOTL.GD.ZS",
    },
    {
        "label": "Net incurrence of liabilities, total (current LCU)",
        "value": "GC.LBL.TOTL.CN",
    },
    {
        "label": "Net incurrence of liabilities, total (% of GDP)",
        "value": "GC.LBL.TOTL.GD.ZS",
    },
    {
        "label": "Net investment in nonfinancial assets (current LCU)",
        "value": "GC.NFN.TOTL.CN",
    },
    {
        "label": "Net investment in nonfinancial assets (% of GDP)",
        "value": "GC.NFN.TOTL.GD.ZS",
    },
    {
        "label": "Net lending (+) / net borrowing (-) (current LCU)",
        "value": "GC.NLD.TOTL.CN",
    },
    {
        "label": "Net lending (+) / net borrowing (-) (% of GDP)",
        "value": "GC.NLD.TOTL.GD.ZS",
    },
    {
        "label": "Grants and other revenue (current LCU)",
        "value": "GC.REV.GOTR.CN",
    },
    {
        "label": "Grants and other revenue (% of revenue)",
        "value": "GC.REV.GOTR.ZS",
    },
    {
        "label": "Social contributions (current LCU)",
        "value": "GC.REV.SOCL.CN",
    },
    {
        "label": "Social contributions (% of revenue)",
        "value": "GC.REV.SOCL.ZS",
    },
    {
        "label": "Revenue, excluding grants (current LCU)",
        "value": "GC.REV.XGRT.CN",
    },
    {
        "label": "Revenue, excluding grants (% of GDP)",
        "value": "GC.REV.XGRT.GD.ZS",
    },
    {
        "label": "Taxes on exports (current LCU)",
        "value": "GC.TAX.EXPT.CN",
    },
    {
        "label": "Taxes on exports (% of tax revenue)",
        "value": "GC.TAX.EXPT.ZS",
    },
    {
        "label": "Taxes on goods and services (current LCU)",
        "value": "GC.TAX.GSRV.CN",
    },
    {
        "label": "Taxes on goods and services (% of revenue)",
        "value": "GC.TAX.GSRV.RV.ZS",
    },
    {
        "label": "Taxes on goods and services (% value added of industry and services)",
        "value": "GC.TAX.GSRV.VA.ZS",
    },
    {
        "label": "Customs and other import duties (current LCU)",
        "value": "GC.TAX.IMPT.CN",
    },
    {
        "label": "Customs and other import duties (% of tax revenue)",
        "value": "GC.TAX.IMPT.ZS",
    },
    {
        "label": "Taxes on international trade (current LCU)",
        "value": "GC.TAX.INTT.CN",
    },
    {
        "label": "Taxes on international trade (% of revenue)",
        "value": "GC.TAX.INTT.RV.ZS",
    },
    {"label": "Other taxes (current LCU)", "value": "GC.TAX.OTHR.CN"},
    {
        "label": "Other taxes (% of revenue)",
        "value": "GC.TAX.OTHR.RV.ZS",
    },
    {"label": "Tax revenue (current LCU)", "value": "GC.TAX.TOTL.CN"},
    {"label": "Tax revenue (% of GDP)", "value": "GC.TAX.TOTL.GD.ZS"},
    {
        "label": "Taxes on income, profits and capital gains (current LCU)",
        "value": "GC.TAX.YPKG.CN",
    },
    {
        "label": "Taxes on income, profits and capital gains (% of revenue)",
        "value": "GC.TAX.YPKG.RV.ZS",
    },
    {
        "label": "Taxes on income, profits and capital gains (% of total taxes)",
        "value": "GC.TAX.YPKG.ZS",
    },
    {
        "label": "Compensation of employees (current LCU)",
        "value": "GC.XPN.COMP.CN",
    },
    {
        "label": "Compensation of employees (% of expense)",
        "value": "GC.XPN.COMP.ZS",
    },
    {
        "label": "Goods and services expense (current LCU)",
        "value": "GC.XPN.GSRV.CN",
    },
    {
        "label": "Goods and services expense (% of expense)",
        "value": "GC.XPN.GSRV.ZS",
    },
    {
        "label": "Interest payments (current LCU)",
        "value": "GC.XPN.INTP.CN",
    },
    {
        "label": "Interest payments (% of revenue)",
        "value": "GC.XPN.INTP.RV.ZS",
    },
    {
        "label": "Interest payments (% of expense)",
        "value": "GC.XPN.INTP.ZS",
    },
    {"label": "Other expense (current LCU)", "value": "GC.XPN.OTHR.CN"},
    {
        "label": "Other expense (% of expense)",
        "value": "GC.XPN.OTHR.ZS",
    },
    {"label": "Expense (current LCU)", "value": "GC.XPN.TOTL.CN"},
    {"label": "Expense (% of GDP)", "value": "GC.XPN.TOTL.GD.ZS"},
    {
        "label": "Subsidies and other transfers (current LCU)",
        "value": "GC.XPN.TRFT.CN",
    },
    {
        "label": "Subsidies and other transfers (% of expense)",
        "value": "GC.XPN.TRFT.ZS",
    },
    {"label": "Government Effectiveness: Estimate", "value": "GE.EST"},
    {
        "label": "Government Effectiveness: Number of Sources",
        "value": "GE.NO.SRC",
    },
    {
        "label": "Government Effectiveness: Percentile Rank",
        "value": "GE.PER.RNK",
    },
    {
        "label": "Government Effectiveness: Percentile Rank, Lower Bound of 90% Confidence Interval",
        "value": "GE.PER.RNK.LOWER",
    },
    {
        "label": "Government Effectiveness: Percentile Rank, Upper Bound of 90% Confidence Interval",
        "value": "GE.PER.RNK.UPPER",
    },
    {
        "label": "Government Effectiveness: Standard Error",
        "value": "GE.STD.ERR",
    },
    {
        "label": "Primary government expenditures as a proportion of original approved budget (%)",
        "value": "GF.XPD.BUDG.ZS",
    },
    {
        "label": "Human capital index (HCI) (scale 0-1)",
        "value": "HD.HCI.OVRL",
    },
    {
        "label": "Human capital index (HCI), female (scale 0-1)",
        "value": "HD.HCI.OVRL.FE",
    },
    {
        "label": "Human capital index (HCI), lower bound (scale 0-1)",
        "value": "HD.HCI.OVRL.LB",
    },
    {
        "label": "Human capital index (HCI), female, lower bound (scale 0-1)",
        "value": "HD.HCI.OVRL.LB.FE",
    },
    {
        "label": "Human capital index (HCI), male, lower bound (scale 0-1)",
        "value": "HD.HCI.OVRL.LB.MA",
    },
    {
        "label": "Human capital index (HCI), male (scale 0-1)",
        "value": "HD.HCI.OVRL.MA",
    },
    {
        "label": "Human capital index (HCI), upper bound (scale 0-1)",
        "value": "HD.HCI.OVRL.UB",
    },
    {
        "label": "Human capital index (HCI), female, upper bound (scale 0-1)",
        "value": "HD.HCI.OVRL.UB.FE",
    },
    {
        "label": "Human capital index (HCI), male, upper bound (scale 0-1)",
        "value": "HD.HCI.OVRL.UB.MA",
    },
    {
        "label": "Ease of doing business score (0 = lowest performance to 100 = best performance)",
        "value": "IC.BUS.DFRN.XQ",
    },
    {
        "label": "Business extent of disclosure index (0=less disclosure to 10=more disclosure)",
        "value": "IC.BUS.DISC.XQ",
    },
    {
        "label": "Ease of doing business rank (1=most business-friendly regulations)",
        "value": "IC.BUS.EASE.XQ",
    },
    {
        "label": "New business density (new registrations per 1,000 people ages 15-64)",
        "value": "IC.BUS.NDNS.ZS",
    },
    {
        "label": "New businesses registered (number)",
        "value": "IC.BUS.NREG",
    },
    {
        "label": "Depth of credit information index (0=low to 8=high)",
        "value": "IC.CRD.INFO.XQ",
    },
    {
        "label": "Private credit bureau coverage (% of adults)",
        "value": "IC.CRD.PRVT.ZS",
    },
    {
        "label": "Public credit registry coverage (% of adults)",
        "value": "IC.CRD.PUBL.ZS",
    },
    {
        "label": "Average time to clear exports through customs (days)",
        "value": "IC.CUS.DURS.EX",
    },
    {
        "label": "Time to obtain an electrical connection (days)",
        "value": "IC.ELC.DURS",
    },
    {
        "label": "Power outages in firms in a typical month (number)",
        "value": "IC.ELC.OUTG",
    },
    {
        "label": "Firms experiencing electrical outages (% of firms)",
        "value": "IC.ELC.OUTG.ZS",
    },
    {
        "label": "Time required to get electricity (days)",
        "value": "IC.ELC.TIME",
    },
    {
        "label": "Cost to export, border compliance (US$)",
        "value": "IC.EXP.CSBC.CD",
    },
    {
        "label": "Cost to export, documentary compliance (US$)",
        "value": "IC.EXP.CSDC.CD",
    },
    {
        "label": "Time to export, border compliance (hours)",
        "value": "IC.EXP.TMBC",
    },
    {
        "label": "Time to export, documentary compliance (hours)",
        "value": "IC.EXP.TMDC",
    },
    {
        "label": "Firms using banks to finance working capital (% of firms)",
        "value": "IC.FRM.BKWC.ZS",
    },
    {
        "label": "Firms using banks to finance investment (% of firms)",
        "value": "IC.FRM.BNKS.ZS",
    },
    {
        "label": "Bribery incidence (% of firms experiencing at least one bribe payment request)",
        "value": "IC.FRM.BRIB.ZS",
    },
    {
        "label": "Firms competing against unregistered firms (% of firms)",
        "value": "IC.FRM.CMPU.ZS",
    },
    {
        "label": "Informal payments to public officials (% of firms)",
        "value": "IC.FRM.CORR.ZS",
    },
    {
        "label": "Losses due to theft and vandalism (% of annual sales for affected firms)",
        "value": "IC.FRM.CRIM.ZS",
    },
    {
        "label": "Time required to obtain an operating license (days)",
        "value": "IC.FRM.DURS",
    },
    {
        "label": "Firms with female top manager (% of firms)",
        "value": "IC.FRM.FEMM.ZS",
    },
    {
        "label": "Firms with female participation in ownership (% of firms)",
        "value": "IC.FRM.FEMO.ZS",
    },
    {
        "label": "Firms formally registered when operations started (% of firms)",
        "value": "IC.FRM.FREG.ZS",
    },
    {
        "label": "Firms that do not report all sales for tax purposes (% of firms)",
        "value": "IC.FRM.INFM.ZS",
    },
    {
        "label": "Firms visited or required meetings with tax officials (% of firms)",
        "value": "IC.FRM.METG.ZS",
    },
    {
        "label": "Value lost due to electrical outages (% of sales for affected firms)",
        "value": "IC.FRM.OUTG.ZS",
    },
    {
        "label": "Firms that spend on R&D (% of firms)",
        "value": "IC.FRM.RSDV.ZS",
    },
    {
        "label": "Firms experiencing losses due to theft and vandalism (% of firms)",
        "value": "IC.FRM.THEV.ZS",
    },
    {
        "label": "Firms offering formal training (% of firms)",
        "value": "IC.FRM.TRNG.ZS",
    },
    {
        "label": "Time spent dealing with the requirements of government regulations (% of senior management time)",
        "value": "IC.GOV.DURS.ZS",
    },
    {
        "label": "Cost to import, border compliance (US$)",
        "value": "IC.IMP.CSBC.CD",
    },
    {
        "label": "Cost to import, documentary compliance (US$)",
        "value": "IC.IMP.CSDC.CD",
    },
    {
        "label": "Time to import, border compliance (hours)",
        "value": "IC.IMP.TMBC",
    },
    {
        "label": "Time to import, documentary compliance (hours)",
        "value": "IC.IMP.TMDC",
    },
    {
        "label": "Time to resolve insolvency (years)",
        "value": "IC.ISV.DURS",
    },
    {
        "label": "Strength of legal rights index (0=weak to 12=strong)",
        "value": "IC.LGL.CRED.XQ",
    },
    {
        "label": "Time required to enforce a contract (days)",
        "value": "IC.LGL.DURS",
    },
    {
        "label": "Time required to register property (days)",
        "value": "IC.PRP.DURS",
    },
    {
        "label": "Procedures to register property (number)",
        "value": "IC.PRP.PROC",
    },
    {
        "label": "Cost of business start-up procedures, female (% of GNI per capita)",
        "value": "IC.REG.COST.PC.FE.ZS",
    },
    {
        "label": "Cost of business start-up procedures, male (% of GNI per capita)",
        "value": "IC.REG.COST.PC.MA.ZS",
    },
    {
        "label": "Cost of business start-up procedures (% of GNI per capita)",
        "value": "IC.REG.COST.PC.ZS",
    },
    {
        "label": "Time required to start a business (days)",
        "value": "IC.REG.DURS",
    },
    {
        "label": "Time required to start a business, female (days)",
        "value": "IC.REG.DURS.FE",
    },
    {
        "label": "Time required to start a business, male (days)",
        "value": "IC.REG.DURS.MA",
    },
    {
        "label": "Start-up procedures to register a business (number)",
        "value": "IC.REG.PROC",
    },
    {
        "label": "Start-up procedures to register a business, female (number)",
        "value": "IC.REG.PROC.FE",
    },
    {
        "label": "Start-up procedures to register a business, male (number)",
        "value": "IC.REG.PROC.MA",
    },
    {
        "label": "Time to prepare and pay taxes (hours)",
        "value": "IC.TAX.DURS",
    },
    {
        "label": "Firms expected to give gifts in meetings with tax officials (% of firms)",
        "value": "IC.TAX.GIFT.ZS",
    },
    {
        "label": "Labor tax and contributions (% of commercial profits)",
        "value": "IC.TAX.LABR.CP.ZS",
    },
    {
        "label": "Number of visits or required meetings with tax officials (average for affected firms)",
        "value": "IC.TAX.METG",
    },
    {
        "label": "Other taxes payable by businesses (% of commercial profits)",
        "value": "IC.TAX.OTHR.CP.ZS",
    },
    {"label": "Tax payments (number)", "value": "IC.TAX.PAYM"},
    {
        "label": "Profit tax (% of commercial profits)",
        "value": "IC.TAX.PRFT.CP.ZS",
    },
    {
        "label": "Total tax and contribution rate (% of profit)",
        "value": "IC.TAX.TOTL.CP.ZS",
    },
    {
        "label": "Time required to build a warehouse (days)",
        "value": "IC.WRH.DURS",
    },
    {
        "label": "Procedures to build a warehouse (number)",
        "value": "IC.WRH.PROC",
    },
    {
        "label": "Investment in energy with private participation (current US$)",
        "value": "IE.PPI.ENGY.CD",
    },
    {
        "label": "Investment in ICT with private participation (current US$)",
        "value": "IE.PPI.ICTI.CD",
    },
    {
        "label": "Investment in transport with private participation (current US$)",
        "value": "IE.PPI.TRAN.CD",
    },
    {
        "label": "Investment in water and sanitation with private participation (current US$)",
        "value": "IE.PPI.WATR.CD",
    },
    {
        "label": "Public private partnerships investment in energy (current US$)",
        "value": "IE.PPN.ENGY.CD",
    },
    {
        "label": "Public private partnerships investment in ICT (current US$)",
        "value": "IE.PPN.ICTI.CD",
    },
    {
        "label": "Public private partnerships investment in transport (current US$)",
        "value": "IE.PPN.TRAN.CD",
    },
    {
        "label": "Public private partnerships investment in water and sanitation (current US$)",
        "value": "IE.PPN.WATR.CD",
    },
    {
        "label": "Industrial design applications, nonresident, by count",
        "value": "IP.IDS.NRCT",
    },
    {
        "label": "Industrial design applications, resident, by count",
        "value": "IP.IDS.RSCT",
    },
    {
        "label": "Scientific and technical journal articles",
        "value": "IP.JRN.ARTC.SC",
    },
    {
        "label": "Patent applications, nonresidents",
        "value": "IP.PAT.NRES",
    },
    {"label": "Patent applications, residents", "value": "IP.PAT.RESD"},
    {
        "label": "Trademark applications, nonresident, by count",
        "value": "IP.TMK.NRCT",
    },
    {
        "label": "Trademark applications, resident, by count",
        "value": "IP.TMK.RSCT",
    },
    {
        "label": "CPIA business regulatory environment rating (1=low to 6=high)",
        "value": "IQ.CPA.BREG.XQ",
    },
    {
        "label": "CPIA debt policy rating (1=low to 6=high)",
        "value": "IQ.CPA.DEBT.XQ",
    },
    {
        "label": "CPIA economic management cluster average (1=low to 6=high)",
        "value": "IQ.CPA.ECON.XQ",
    },
    {
        "label": "CPIA policy and institutions for environmental sustainability rating (1=low to 6=high)",
        "value": "IQ.CPA.ENVR.XQ",
    },
    {
        "label": "CPIA quality of budgetary and financial management rating (1=low to 6=high)",
        "value": "IQ.CPA.FINQ.XQ",
    },
    {
        "label": "CPIA financial sector rating (1=low to 6=high)",
        "value": "IQ.CPA.FINS.XQ",
    },
    {
        "label": "CPIA fiscal policy rating (1=low to 6=high)",
        "value": "IQ.CPA.FISP.XQ",
    },
    {
        "label": "CPIA gender equality rating (1=low to 6=high)",
        "value": "IQ.CPA.GNDR.XQ",
    },
    {
        "label": "CPIA building human resources rating (1=low to 6=high)",
        "value": "IQ.CPA.HRES.XQ",
    },
    {
        "label": "IDA resource allocation index (1=low to 6=high)",
        "value": "IQ.CPA.IRAI.XQ",
    },
    {
        "label": "CPIA macroeconomic management rating (1=low to 6=high)",
        "value": "IQ.CPA.MACR.XQ",
    },
    {
        "label": "CPIA quality of public administration rating (1=low to 6=high)",
        "value": "IQ.CPA.PADM.XQ",
    },
    {
        "label": "CPIA equity of public resource use rating (1=low to 6=high)",
        "value": "IQ.CPA.PRES.XQ",
    },
    {
        "label": "CPIA property rights and rule-based governance rating (1=low to 6=high)",
        "value": "IQ.CPA.PROP.XQ",
    },
    {
        "label": "CPIA social protection rating (1=low to 6=high)",
        "value": "IQ.CPA.PROT.XQ",
    },
    {
        "label": "CPIA public sector management and institutions cluster average (1=low to 6=high)",
        "value": "IQ.CPA.PUBS.XQ",
    },
    {
        "label": "CPIA efficiency of revenue mobilization rating (1=low to 6=high)",
        "value": "IQ.CPA.REVN.XQ",
    },
    {
        "label": "CPIA policies for social inclusion/equity cluster average (1=low to 6=high)",
        "value": "IQ.CPA.SOCI.XQ",
    },
    {
        "label": "CPIA structural policies cluster average (1=low to 6=high)",
        "value": "IQ.CPA.STRC.XQ",
    },
    {
        "label": "CPIA trade rating (1=low to 6=high)",
        "value": "IQ.CPA.TRAD.XQ",
    },
    {
        "label": "CPIA transparency, accountability, and corruption in the public sector rating (1=low to 6=high)",
        "value": "IQ.CPA.TRAN.XQ",
    },
    {
        "label": "Methodology assessment of statistical capacity (scale 0 - 100)",
        "value": "IQ.SCI.MTHD",
    },
    {
        "label": "Statistical Capacity Score (Overall Average) (scale 0 - 100)",
        "value": "IQ.SCI.OVRL",
    },
    {
        "label": "Periodicity and timeliness assessment of statistical capacity (scale 0 - 100)",
        "value": "IQ.SCI.PRDC",
    },
    {
        "label": "Source data assessment of statistical capacity (scale 0 - 100)",
        "value": "IQ.SCI.SRCE",
    },
    {
        "label": "Statistical performance indicators (SPI): Overall score (scale 0-100)",
        "value": "IQ.SPI.OVRL",
    },
    {
        "label": "Statistical performance indicators (SPI): Pillar 1 data use score (scale 0-100)",
        "value": "IQ.SPI.PIL1",
    },
    {
        "label": "Statistical performance indicators (SPI): Pillar 2 data services score (scale 0-100)",
        "value": "IQ.SPI.PIL2",
    },
    {
        "label": "Statistical performance indicators (SPI): Pillar 3 data products score  (scale 0-100)",
        "value": "IQ.SPI.PIL3",
    },
    {
        "label": "Statistical performance indicators (SPI): Pillar 4 data sources score (scale 0-100)",
        "value": "IQ.SPI.PIL4",
    },
    {
        "label": "Statistical performance indicators (SPI): Pillar 5 data infrastructure score (scale 0-100)",
        "value": "IQ.SPI.PIL5",
    },
    {
        "label": "Air transport, registered carrier departures worldwide",
        "value": "IS.AIR.DPRT",
    },
    {
        "label": "Air transport, freight (million ton-km)",
        "value": "IS.AIR.GOOD.MT.K1",
    },
    {
        "label": "Air transport, passengers carried",
        "value": "IS.AIR.PSGR",
    },
    {
        "label": "Railways, goods transported (million ton-km)",
        "value": "IS.RRS.GOOD.MT.K6",
    },
    {
        "label": "Railways, passengers carried (million passenger-km)",
        "value": "IS.RRS.PASG.KM",
    },
    {"label": "Rail lines (total route-km)", "value": "IS.RRS.TOTL.KM"},
    {
        "label": "Liner shipping connectivity index (maximum value in 2004 = 100)",
        "value": "IS.SHP.GCNW.XQ",
    },
    {
        "label": "Container port traffic (TEU: 20 foot equivalent units)",
        "value": "IS.SHP.GOOD.TU",
    },
    {"label": "Mobile cellular subscriptions", "value": "IT.CEL.SETS"},
    {
        "label": "Mobile cellular subscriptions (per 100 people)",
        "value": "IT.CEL.SETS.P2",
    },
    {"label": "Fixed telephone subscriptions", "value": "IT.MLT.MAIN"},
    {
        "label": "Fixed telephone subscriptions (per 100 people)",
        "value": "IT.MLT.MAIN.P2",
    },
    {"label": "Fixed broadband subscriptions", "value": "IT.NET.BBND"},
    {
        "label": "Fixed broadband subscriptions (per 100 people)",
        "value": "IT.NET.BBND.P2",
    },
    {"label": "Secure Internet servers", "value": "IT.NET.SECR"},
    {
        "label": "Secure Internet servers (per 1 million people)",
        "value": "IT.NET.SECR.P6",
    },
    {
        "label": "Individuals using the Internet (% of population)",
        "value": "IT.NET.USER.ZS",
    },
    {
        "label": "Lead time to export, median case (days)",
        "value": "LP.EXP.DURS.MD",
    },
    {
        "label": "Lead time to import, median case (days)",
        "value": "LP.IMP.DURS.MD",
    },
    {
        "label": "Logistics performance index: Efficiency of customs clearance process (1=low to 5=high)",
        "value": "LP.LPI.CUST.XQ",
    },
    {
        "label": "Logistics performance index: Quality of trade and transport-related infrastructure (1=low to 5=high)",
        "value": "LP.LPI.INFR.XQ",
    },
    {
        "label": "Logistics performance index: Ease of arranging competitively priced shipments (1=low to 5=high)",
        "value": "LP.LPI.ITRN.XQ",
    },
    {
        "label": "Logistics performance index: Competence and quality of logistics services (1=low to 5=high)",
        "value": "LP.LPI.LOGS.XQ",
    },
    {
        "label": "Logistics performance index: Overall (1=low to 5=high)",
        "value": "LP.LPI.OVRL.XQ",
    },
    {
        "label": "Logistics performance index: Frequency with which shipments reach consignee within scheduled or expected time (1=low to 5=high)",
        "value": "LP.LPI.TIME.XQ",
    },
    {
        "label": "Logistics performance index: Ability to track and trace consignments (1=low to 5=high)",
        "value": "LP.LPI.TRAC.XQ",
    },
    {
        "label": "Arms imports (SIPRI trend indicator values)",
        "value": "MS.MIL.MPRT.KD",
    },
    {
        "label": "Armed forces personnel, total",
        "value": "MS.MIL.TOTL.P1",
    },
    {
        "label": "Armed forces personnel (% of total labor force)",
        "value": "MS.MIL.TOTL.TF.ZS",
    },
    {
        "label": "Military expenditure (current USD)",
        "value": "MS.MIL.XPND.CD",
    },
    {
        "label": "Military expenditure (current LCU)",
        "value": "MS.MIL.XPND.CN",
    },
    {
        "label": "Military expenditure (% of GDP)",
        "value": "MS.MIL.XPND.GD.ZS",
    },
    {
        "label": "Military expenditure (% of general government expenditure)",
        "value": "MS.MIL.XPND.ZS",
    },
    {
        "label": "Arms exports (SIPRI trend indicator values)",
        "value": "MS.MIL.XPRT.KD",
    },
    {
        "label": "General government final consumption expenditure (current US$)",
        "value": "NE.CON.GOVT.CD",
    },
    {
        "label": "General government final consumption expenditure (current LCU)",
        "value": "NE.CON.GOVT.CN",
    },
    {
        "label": "General government final consumption expenditure (constant 2015 US$)",
        "value": "NE.CON.GOVT.KD",
    },
    {
        "label": "General government final consumption expenditure (annual % growth)",
        "value": "NE.CON.GOVT.KD.ZG",
    },
    {
        "label": "General government final consumption expenditure (constant LCU)",
        "value": "NE.CON.GOVT.KN",
    },
    {
        "label": "General government final consumption expenditure (% of GDP)",
        "value": "NE.CON.GOVT.ZS",
    },
    {
        "label": "Households and NPISHs Final consumption expenditure (current US$)",
        "value": "NE.CON.PRVT.CD",
    },
    {
        "label": "Households and NPISHs Final consumption expenditure (current LCU)",
        "value": "NE.CON.PRVT.CN",
    },
    {
        "label": "Households and NPISHs final consumption expenditure: linked series (current LCU)",
        "value": "NE.CON.PRVT.CN.AD",
    },
    {
        "label": "Households and NPISHs Final consumption expenditure (constant 2015 US$)",
        "value": "NE.CON.PRVT.KD",
    },
    {
        "label": "Households and NPISHs Final consumption expenditure (annual % growth)",
        "value": "NE.CON.PRVT.KD.ZG",
    },
    {
        "label": "Households and NPISHs Final consumption expenditure (constant LCU)",
        "value": "NE.CON.PRVT.KN",
    },
    {
        "label": "Households and NPISHs Final consumption expenditure per capita (constant 2015 US$)",
        "value": "NE.CON.PRVT.PC.KD",
    },
    {
        "label": "Households and NPISHs Final consumption expenditure per capita growth (annual %)",
        "value": "NE.CON.PRVT.PC.KD.ZG",
    },
    {
        "label": "Households and NPISHs Final consumption expenditure, PPP (current international $)",
        "value": "NE.CON.PRVT.PP.CD",
    },
    {
        "label": "Households and NPISHs Final consumption expenditure, PPP (constant 2017 international $)",
        "value": "NE.CON.PRVT.PP.KD",
    },
    {
        "label": "Households and NPISHs final consumption expenditure (% of GDP)",
        "value": "NE.CON.PRVT.ZS",
    },
    {
        "label": "Final consumption expenditure (current US$)",
        "value": "NE.CON.TOTL.CD",
    },
    {
        "label": "Final consumption expenditure (current LCU)",
        "value": "NE.CON.TOTL.CN",
    },
    {
        "label": "Final consumption expenditure (constant 2015 US$)",
        "value": "NE.CON.TOTL.KD",
    },
    {
        "label": "Final consumption expenditure (annual % growth)",
        "value": "NE.CON.TOTL.KD.ZG",
    },
    {
        "label": "Final consumption expenditure (constant LCU)",
        "value": "NE.CON.TOTL.KN",
    },
    {
        "label": "Final consumption expenditure (% of GDP)",
        "value": "NE.CON.TOTL.ZS",
    },
    {
        "label": "Gross national expenditure deflator (base year varies by country)",
        "value": "NE.DAB.DEFL.ZS",
    },
    {
        "label": "Gross national expenditure (current US$)",
        "value": "NE.DAB.TOTL.CD",
    },
    {
        "label": "Gross national expenditure (current LCU)",
        "value": "NE.DAB.TOTL.CN",
    },
    {
        "label": "Gross national expenditure (constant 2015 US$)",
        "value": "NE.DAB.TOTL.KD",
    },
    {
        "label": "Gross national expenditure (constant LCU)",
        "value": "NE.DAB.TOTL.KN",
    },
    {
        "label": "Gross national expenditure (% of GDP)",
        "value": "NE.DAB.TOTL.ZS",
    },
    {
        "label": "Exports of goods and services (current US$)",
        "value": "NE.EXP.GNFS.CD",
    },
    {
        "label": "Exports of goods and services (current LCU)",
        "value": "NE.EXP.GNFS.CN",
    },
    {
        "label": "Exports of goods and services (constant 2015 US$)",
        "value": "NE.EXP.GNFS.KD",
    },
    {
        "label": "Exports of goods and services (annual % growth)",
        "value": "NE.EXP.GNFS.KD.ZG",
    },
    {
        "label": "Exports of goods and services (constant LCU)",
        "value": "NE.EXP.GNFS.KN",
    },
    {
        "label": "Exports of goods and services (% of GDP)",
        "value": "NE.EXP.GNFS.ZS",
    },
    {
        "label": "Gross fixed capital formation, private sector (current LCU)",
        "value": "NE.GDI.FPRV.CN",
    },
    {
        "label": "Gross fixed capital formation, private sector (% of GDP)",
        "value": "NE.GDI.FPRV.ZS",
    },
    {
        "label": "Gross fixed capital formation (current US$)",
        "value": "NE.GDI.FTOT.CD",
    },
    {
        "label": "Gross fixed capital formation (current LCU)",
        "value": "NE.GDI.FTOT.CN",
    },
    {
        "label": "Gross fixed capital formation (constant 2015 US$)",
        "value": "NE.GDI.FTOT.KD",
    },
    {
        "label": "Gross fixed capital formation (annual % growth)",
        "value": "NE.GDI.FTOT.KD.ZG",
    },
    {
        "label": "Gross fixed capital formation (constant LCU)",
        "value": "NE.GDI.FTOT.KN",
    },
    {
        "label": "Gross fixed capital formation (% of GDP)",
        "value": "NE.GDI.FTOT.ZS",
    },
    {
        "label": "Changes in inventories (current US$)",
        "value": "NE.GDI.STKB.CD",
    },
    {
        "label": "Changes in inventories (current LCU)",
        "value": "NE.GDI.STKB.CN",
    },
    {
        "label": "Changes in inventories (constant LCU)",
        "value": "NE.GDI.STKB.KN",
    },
    {
        "label": "Gross capital formation (current US$)",
        "value": "NE.GDI.TOTL.CD",
    },
    {
        "label": "Gross capital formation (current LCU)",
        "value": "NE.GDI.TOTL.CN",
    },
    {
        "label": "Gross capital formation (constant 2015 US$)",
        "value": "NE.GDI.TOTL.KD",
    },
    {
        "label": "Gross capital formation (annual % growth)",
        "value": "NE.GDI.TOTL.KD.ZG",
    },
    {
        "label": "Gross capital formation (constant LCU)",
        "value": "NE.GDI.TOTL.KN",
    },
    {
        "label": "Gross capital formation (% of GDP)",
        "value": "NE.GDI.TOTL.ZS",
    },
    {
        "label": "Imports of goods and services (current US$)",
        "value": "NE.IMP.GNFS.CD",
    },
    {
        "label": "Imports of goods and services (current LCU)",
        "value": "NE.IMP.GNFS.CN",
    },
    {
        "label": "Imports of goods and services (constant 2015 US$)",
        "value": "NE.IMP.GNFS.KD",
    },
    {
        "label": "Imports of goods and services (annual % growth)",
        "value": "NE.IMP.GNFS.KD.ZG",
    },
    {
        "label": "Imports of goods and services (constant LCU)",
        "value": "NE.IMP.GNFS.KN",
    },
    {
        "label": "Imports of goods and services (% of GDP)",
        "value": "NE.IMP.GNFS.ZS",
    },
    {
        "label": "External balance on goods and services (current US$)",
        "value": "NE.RSB.GNFS.CD",
    },
    {
        "label": "External balance on goods and services (current LCU)",
        "value": "NE.RSB.GNFS.CN",
    },
    {
        "label": "External balance on goods and services (constant LCU)",
        "value": "NE.RSB.GNFS.KN",
    },
    {
        "label": "External balance on goods and services (% of GDP)",
        "value": "NE.RSB.GNFS.ZS",
    },
    {"label": "Trade (% of GDP)", "value": "NE.TRD.GNFS.ZS"},
    {
        "label": "Agriculture, forestry, and fishing, value added per worker (constant 2015 US$)",
        "value": "NV.AGR.EMPL.KD",
    },
    {
        "label": "Agriculture, forestry, and fishing, value added (current US$)",
        "value": "NV.AGR.TOTL.CD",
    },
    {
        "label": "Agriculture, forestry, and fishing, value added (current LCU)",
        "value": "NV.AGR.TOTL.CN",
    },
    {
        "label": "Agriculture, forestry, and fishing, value added (constant 2015 US$)",
        "value": "NV.AGR.TOTL.KD",
    },
    {
        "label": "Agriculture, forestry, and fishing, value added (annual % growth)",
        "value": "NV.AGR.TOTL.KD.ZG",
    },
    {
        "label": "Agriculture, forestry, and fishing, value added (constant LCU)",
        "value": "NV.AGR.TOTL.KN",
    },
    {
        "label": "Agriculture, forestry, and fishing, value added (% of GDP)",
        "value": "NV.AGR.TOTL.ZS",
    },
    {
        "label": "Financial intermediary services indirectly Measured (FISIM) (current LCU)",
        "value": "NV.FSM.TOTL.CN",
    },
    {
        "label": "Financial intermediary services indirectly Measured (FISIM) (constant LCU)",
        "value": "NV.FSM.TOTL.KN",
    },
    {
        "label": "Industry (including construction), value added per worker (constant 2015 US$)",
        "value": "NV.IND.EMPL.KD",
    },
    {
        "label": "Manufacturing, value added (current US$)",
        "value": "NV.IND.MANF.CD",
    },
    {
        "label": "Manufacturing, value added (current LCU)",
        "value": "NV.IND.MANF.CN",
    },
    {
        "label": "Manufacturing, value added (constant 2015 US$)",
        "value": "NV.IND.MANF.KD",
    },
    {
        "label": "Manufacturing, value added (annual % growth)",
        "value": "NV.IND.MANF.KD.ZG",
    },
    {
        "label": "Manufacturing, value added (constant LCU)",
        "value": "NV.IND.MANF.KN",
    },
    {
        "label": "Manufacturing, value added (% of GDP)",
        "value": "NV.IND.MANF.ZS",
    },
    {
        "label": "Industry (including construction), value added (current US$)",
        "value": "NV.IND.TOTL.CD",
    },
    {
        "label": "Industry (including construction), value added (current LCU)",
        "value": "NV.IND.TOTL.CN",
    },
    {
        "label": "Industry (including construction), value added (constant 2015 US$)",
        "value": "NV.IND.TOTL.KD",
    },
    {
        "label": "Industry (including construction), value added (annual % growth)",
        "value": "NV.IND.TOTL.KD.ZG",
    },
    {
        "label": "Industry (including construction), value added (constant LCU)",
        "value": "NV.IND.TOTL.KN",
    },
    {
        "label": "Industry (including construction), value added (% of GDP)",
        "value": "NV.IND.TOTL.ZS",
    },
    {
        "label": "Chemicals (% of value added in manufacturing)",
        "value": "NV.MNF.CHEM.ZS.UN",
    },
    {
        "label": "Food, beverages and tobacco (% of value added in manufacturing)",
        "value": "NV.MNF.FBTO.ZS.UN",
    },
    {
        "label": "Machinery and transport equipment (% of value added in manufacturing)",
        "value": "NV.MNF.MTRN.ZS.UN",
    },
    {
        "label": "Other manufacturing (% of value added in manufacturing)",
        "value": "NV.MNF.OTHR.ZS.UN",
    },
    {
        "label": "Medium and high-tech manufacturing value added (% manufacturing value added)",
        "value": "NV.MNF.TECH.ZS.UN",
    },
    {
        "label": "Textiles and clothing (% of value added in manufacturing)",
        "value": "NV.MNF.TXTL.ZS.UN",
    },
    {
        "label": "Services, value added per worker (constant 2015 US$)",
        "value": "NV.SRV.EMPL.KD",
    },
    {
        "label": "Services, value added (current US$)",
        "value": "NV.SRV.TOTL.CD",
    },
    {
        "label": "Services, value added (current LCU)",
        "value": "NV.SRV.TOTL.CN",
    },
    {
        "label": "Services, value added (constant 2015 US$)",
        "value": "NV.SRV.TOTL.KD",
    },
    {
        "label": "Services, value added (annual % growth)",
        "value": "NV.SRV.TOTL.KD.ZG",
    },
    {
        "label": "Services, value added (constant LCU)",
        "value": "NV.SRV.TOTL.KN",
    },
    {
        "label": "Services, value added (% of GDP)",
        "value": "NV.SRV.TOTL.ZS",
    },
    {
        "label": "Adjusted savings: education expenditure (current US$)",
        "value": "NY.ADJ.AEDU.CD",
    },
    {
        "label": "Adjusted savings: education expenditure (% of GNI)",
        "value": "NY.ADJ.AEDU.GN.ZS",
    },
    {
        "label": "Adjusted savings: carbon dioxide damage (current US$)",
        "value": "NY.ADJ.DCO2.CD",
    },
    {
        "label": "Adjusted savings: carbon dioxide damage (% of GNI)",
        "value": "NY.ADJ.DCO2.GN.ZS",
    },
    {
        "label": "Adjusted savings: net forest depletion (current US$)",
        "value": "NY.ADJ.DFOR.CD",
    },
    {
        "label": "Adjusted savings: net forest depletion (% of GNI)",
        "value": "NY.ADJ.DFOR.GN.ZS",
    },
    {
        "label": "Adjusted savings: consumption of fixed capital (current US$)",
        "value": "NY.ADJ.DKAP.CD",
    },
    {
        "label": "Adjusted savings: consumption of fixed capital (% of GNI)",
        "value": "NY.ADJ.DKAP.GN.ZS",
    },
    {
        "label": "Adjusted savings: mineral depletion (current US$)",
        "value": "NY.ADJ.DMIN.CD",
    },
    {
        "label": "Adjusted savings: mineral depletion (% of GNI)",
        "value": "NY.ADJ.DMIN.GN.ZS",
    },
    {
        "label": "Adjusted savings: energy depletion (current US$)",
        "value": "NY.ADJ.DNGY.CD",
    },
    {
        "label": "Adjusted savings: energy depletion (% of GNI)",
        "value": "NY.ADJ.DNGY.GN.ZS",
    },
    {
        "label": "Adjusted savings: particulate emission damage (current US$)",
        "value": "NY.ADJ.DPEM.CD",
    },
    {
        "label": "Adjusted savings: particulate emission damage (% of GNI)",
        "value": "NY.ADJ.DPEM.GN.ZS",
    },
    {
        "label": "Adjusted savings: natural resources depletion (% of GNI)",
        "value": "NY.ADJ.DRES.GN.ZS",
    },
    {
        "label": "Adjusted savings: gross savings (% of GNI)",
        "value": "NY.ADJ.ICTR.GN.ZS",
    },
    {
        "label": "Adjusted savings: net national savings (current US$)",
        "value": "NY.ADJ.NNAT.CD",
    },
    {
        "label": "Adjusted savings: net national savings (% of GNI)",
        "value": "NY.ADJ.NNAT.GN.ZS",
    },
    {
        "label": "Adjusted net national income (current US$)",
        "value": "NY.ADJ.NNTY.CD",
    },
    {
        "label": "Adjusted net national income (constant 2015 US$)",
        "value": "NY.ADJ.NNTY.KD",
    },
    {
        "label": "Adjusted net national income (annual % growth)",
        "value": "NY.ADJ.NNTY.KD.ZG",
    },
    {
        "label": "Adjusted net national income per capita (current US$)",
        "value": "NY.ADJ.NNTY.PC.CD",
    },
    {
        "label": "Adjusted net national income per capita (constant 2015 US$)",
        "value": "NY.ADJ.NNTY.PC.KD",
    },
    {
        "label": "Adjusted net national income per capita (annual % growth)",
        "value": "NY.ADJ.NNTY.PC.KD.ZG",
    },
    {
        "label": "Adjusted net savings, including particulate emission damage (current US$)",
        "value": "NY.ADJ.SVNG.CD",
    },
    {
        "label": "Adjusted net savings, including particulate emission damage (% of GNI)",
        "value": "NY.ADJ.SVNG.GN.ZS",
    },
    {
        "label": "Adjusted net savings, excluding particulate emission damage (current US$)",
        "value": "NY.ADJ.SVNX.CD",
    },
    {
        "label": "Adjusted net savings, excluding particulate emission damage (% of GNI)",
        "value": "NY.ADJ.SVNX.GN.ZS",
    },
    {
        "label": "Exports as a capacity to import (constant LCU)",
        "value": "NY.EXP.CAPM.KN",
    },
    {"label": "Coal rents (% of GDP)", "value": "NY.GDP.COAL.RT.ZS"},
    {
        "label": "Inflation, GDP deflator (annual %)",
        "value": "NY.GDP.DEFL.KD.ZG",
    },
    {
        "label": "Inflation, GDP deflator: linked series (annual %)",
        "value": "NY.GDP.DEFL.KD.ZG.AD",
    },
    {
        "label": "GDP deflator (base year varies by country)",
        "value": "NY.GDP.DEFL.ZS",
    },
    {
        "label": "GDP deflator: linked series (base year varies by country)",
        "value": "NY.GDP.DEFL.ZS.AD",
    },
    {
        "label": "Discrepancy in expenditure estimate of GDP (current LCU)",
        "value": "NY.GDP.DISC.CN",
    },
    {
        "label": "Discrepancy in expenditure estimate of GDP (constant LCU)",
        "value": "NY.GDP.DISC.KN",
    },
    {
        "label": "Gross value added at basic prices (GVA) (current US$)",
        "value": "NY.GDP.FCST.CD",
    },
    {
        "label": "Gross value added at basic prices (GVA) (current LCU)",
        "value": "NY.GDP.FCST.CN",
    },
    {
        "label": "Gross value added at basic prices (GVA) (constant 2015 US$)",
        "value": "NY.GDP.FCST.KD",
    },
    {
        "label": "Gross value added at basic prices (GVA) (constant LCU)",
        "value": "NY.GDP.FCST.KN",
    },
    {"label": "Forest rents (% of GDP)", "value": "NY.GDP.FRST.RT.ZS"},
    {"label": "Mineral rents (% of GDP)", "value": "NY.GDP.MINR.RT.ZS"},
    {"label": "GDP (current US$)", "value": "NY.GDP.MKTP.CD"},
    {"label": "GDP (current LCU)", "value": "NY.GDP.MKTP.CN"},
    {
        "label": "GDP: linked series (current LCU)",
        "value": "NY.GDP.MKTP.CN.AD",
    },
    {"label": "GDP (constant 2015 US$)", "value": "NY.GDP.MKTP.KD"},
    {"label": "GDP growth (annual %)", "value": "NY.GDP.MKTP.KD.ZG"},
    {"label": "GDP (constant LCU)", "value": "NY.GDP.MKTP.KN"},
    {
        "label": "GDP, PPP (current international $)",
        "value": "NY.GDP.MKTP.PP.CD",
    },
    {
        "label": "GDP, PPP (constant 2017 international $)",
        "value": "NY.GDP.MKTP.PP.KD",
    },
    {
        "label": "Natural gas rents (% of GDP)",
        "value": "NY.GDP.NGAS.RT.ZS",
    },
    {
        "label": "GDP per capita (current US$)",
        "value": "NY.GDP.PCAP.CD",
    },
    {
        "label": "GDP per capita (current LCU)",
        "value": "NY.GDP.PCAP.CN",
    },
    {
        "label": "GDP per capita (constant 2015 US$)",
        "value": "NY.GDP.PCAP.KD",
    },
    {
        "label": "GDP per capita growth (annual %)",
        "value": "NY.GDP.PCAP.KD.ZG",
    },
    {
        "label": "GDP per capita (constant LCU)",
        "value": "NY.GDP.PCAP.KN",
    },
    {
        "label": "GDP per capita, PPP (current international $)",
        "value": "NY.GDP.PCAP.PP.CD",
    },
    {
        "label": "GDP per capita, PPP (constant 2017 international $)",
        "value": "NY.GDP.PCAP.PP.KD",
    },
    {"label": "Oil rents (% of GDP)", "value": "NY.GDP.PETR.RT.ZS"},
    {
        "label": "Total natural resources rents (% of GDP)",
        "value": "NY.GDP.TOTL.RT.ZS",
    },
    {
        "label": "Gross domestic savings (current US$)",
        "value": "NY.GDS.TOTL.CD",
    },
    {
        "label": "Gross domestic savings (current LCU)",
        "value": "NY.GDS.TOTL.CN",
    },
    {
        "label": "Gross domestic savings (% of GDP)",
        "value": "NY.GDS.TOTL.ZS",
    },
    {
        "label": "Gross domestic income (constant LCU)",
        "value": "NY.GDY.TOTL.KN",
    },
    {
        "label": "GNI, Atlas method (current US$)",
        "value": "NY.GNP.ATLS.CD",
    },
    {"label": "GNI (current US$)", "value": "NY.GNP.MKTP.CD"},
    {"label": "GNI (current LCU)", "value": "NY.GNP.MKTP.CN"},
    {
        "label": "GNI: linked series (current LCU)",
        "value": "NY.GNP.MKTP.CN.AD",
    },
    {"label": "GNI (constant 2015 US$)", "value": "NY.GNP.MKTP.KD"},
    {"label": "GNI growth (annual %)", "value": "NY.GNP.MKTP.KD.ZG"},
    {"label": "GNI (constant LCU)", "value": "NY.GNP.MKTP.KN"},
    {
        "label": "GNI, PPP (current international $)",
        "value": "NY.GNP.MKTP.PP.CD",
    },
    {
        "label": "GNI, PPP (constant 2017 international $)",
        "value": "NY.GNP.MKTP.PP.KD",
    },
    {
        "label": "GNI per capita, Atlas method (current US$)",
        "value": "NY.GNP.PCAP.CD",
    },
    {
        "label": "GNI per capita (current LCU)",
        "value": "NY.GNP.PCAP.CN",
    },
    {
        "label": "GNI per capita (constant 2015 US$)",
        "value": "NY.GNP.PCAP.KD",
    },
    {
        "label": "GNI per capita growth (annual %)",
        "value": "NY.GNP.PCAP.KD.ZG",
    },
    {
        "label": "GNI per capita (constant LCU)",
        "value": "NY.GNP.PCAP.KN",
    },
    {
        "label": "GNI per capita, PPP (current international $)",
        "value": "NY.GNP.PCAP.PP.CD",
    },
    {
        "label": "GNI per capita, PPP (constant 2017 international $)",
        "value": "NY.GNP.PCAP.PP.KD",
    },
    {"label": "Gross savings (current US$)", "value": "NY.GNS.ICTR.CD"},
    {"label": "Gross savings (current LCU)", "value": "NY.GNS.ICTR.CN"},
    {"label": "Gross savings (% of GNI)", "value": "NY.GNS.ICTR.GN.ZS"},
    {"label": "Gross savings (% of GDP)", "value": "NY.GNS.ICTR.ZS"},
    {
        "label": "Net primary income (Net income from abroad) (current US$)",
        "value": "NY.GSR.NFCY.CD",
    },
    {
        "label": "Net primary income (Net income from abroad) (current LCU)",
        "value": "NY.GSR.NFCY.CN",
    },
    {
        "label": "Net primary income (Net income from abroad) (constant LCU)",
        "value": "NY.GSR.NFCY.KN",
    },
    {
        "label": "Taxes less subsidies on products (current US$)",
        "value": "NY.TAX.NIND.CD",
    },
    {
        "label": "Taxes less subsidies on products (current LCU)",
        "value": "NY.TAX.NIND.CN",
    },
    {
        "label": "Taxes less subsidies on products (constant LCU)",
        "value": "NY.TAX.NIND.KN",
    },
    {
        "label": "Net secondary income (Net current transfers from abroad) (current US$)",
        "value": "NY.TRF.NCTR.CD",
    },
    {
        "label": "Net secondary income (Net current transfers from abroad) (current LCU)",
        "value": "NY.TRF.NCTR.CN",
    },
    {
        "label": "Net secondary income (Net current transfers from abroad) (constant LCU)",
        "value": "NY.TRF.NCTR.KN",
    },
    {
        "label": "Terms of trade adjustment (constant LCU)",
        "value": "NY.TTF.GNFS.KN",
    },
    {
        "label": "DEC alternative conversion factor (LCU per US$)",
        "value": "PA.NUS.ATLS",
    },
    {
        "label": "Official exchange rate (LCU per US$, period average)",
        "value": "PA.NUS.FCRF",
    },
    {
        "label": "PPP conversion factor, GDP (LCU per international $)",
        "value": "PA.NUS.PPP",
    },
    {
        "label": "Price level ratio of PPP conversion factor (GDP) to market exchange rate",
        "value": "PA.NUS.PPPC.RF",
    },
    {
        "label": "PPP conversion factor, private consumption (LCU per international $)",
        "value": "PA.NUS.PRVT.PP",
    },
    {
        "label": "Adequacy of social protection and labor programs (% of total welfare of beneficiary households)",
        "value": "per_allsp.adq_pop_tot",
    },
    {
        "label": "Benefit incidence of social protection and labor programs to poorest quintile (% of total SPL benefits)",
        "value": "per_allsp.ben_q1_tot",
    },
    {
        "label": "Coverage of social protection and labor programs (% of population)",
        "value": "per_allsp.cov_pop_tot",
    },
    {
        "label": "Adequacy of unemployment benefits and ALMP (% of total welfare of beneficiary households)",
        "value": "per_lm_alllm.adq_pop_tot",
    },
    {
        "label": "Benefit incidence of unemployment benefits and ALMP to poorest quintile (% of total U/ALMP benefits)",
        "value": "per_lm_alllm.ben_q1_tot",
    },
    {
        "label": "Coverage of unemployment benefits and ALMP (% of population)",
        "value": "per_lm_alllm.cov_pop_tot",
    },
    {
        "label": "Coverage of unemployment benefits and ALMP in poorest quintile (% of population)",
        "value": "per_lm_alllm.cov_q1_tot",
    },
    {
        "label": "Coverage of unemployment benefits and ALMP in 2nd quintile (% of population)",
        "value": "per_lm_alllm.cov_q2_tot",
    },
    {
        "label": "Coverage of unemployment benefits and ALMP in 3rd quintile (% of population)",
        "value": "per_lm_alllm.cov_q3_tot",
    },
    {
        "label": "Coverage of unemployment benefits and ALMP in 4th quintile (% of population)",
        "value": "per_lm_alllm.cov_q4_tot",
    },
    {
        "label": "Coverage of unemployment benefits and ALMP in richest quintile (% of population)",
        "value": "per_lm_alllm.cov_q5_tot",
    },
    {
        "label": "Adequacy of social safety net programs (% of total welfare of beneficiary households)",
        "value": "per_sa_allsa.adq_pop_tot",
    },
    {
        "label": "Benefit incidence of social safety net programs to poorest quintile (% of total safety net benefits)",
        "value": "per_sa_allsa.ben_q1_tot",
    },
    {
        "label": "Coverage of social safety net programs (% of population)",
        "value": "per_sa_allsa.cov_pop_tot",
    },
    {
        "label": "Coverage of social safety net programs in poorest quintile (% of population)",
        "value": "per_sa_allsa.cov_q1_tot",
    },
    {
        "label": "Coverage of social safety net programs in 2nd quintile (% of population)",
        "value": "per_sa_allsa.cov_q2_tot",
    },
    {
        "label": "Coverage of social safety net programs in 3rd quintile (% of population)",
        "value": "per_sa_allsa.cov_q3_tot",
    },
    {
        "label": "Coverage of social safety net programs in 4th quintile (% of population)",
        "value": "per_sa_allsa.cov_q4_tot",
    },
    {
        "label": "Coverage of social safety net programs in richest quintile (% of population)",
        "value": "per_sa_allsa.cov_q5_tot",
    },
    {
        "label": "Adequacy of social insurance programs (% of total welfare of beneficiary households)",
        "value": "per_si_allsi.adq_pop_tot",
    },
    {
        "label": "Benefit incidence of social insurance programs to poorest quintile (% of total social insurance benefits)",
        "value": "per_si_allsi.ben_q1_tot",
    },
    {
        "label": "Coverage of social insurance programs (% of population)",
        "value": "per_si_allsi.cov_pop_tot",
    },
    {
        "label": "Coverage of social insurance programs in poorest quintile (% of population)",
        "value": "per_si_allsi.cov_q1_tot",
    },
    {
        "label": "Coverage of social insurance programs in 2nd quintile (% of population)",
        "value": "per_si_allsi.cov_q2_tot",
    },
    {
        "label": "Coverage of social insurance programs in 3rd quintile (% of population)",
        "value": "per_si_allsi.cov_q3_tot",
    },
    {
        "label": "Coverage of social insurance programs in 4th quintile (% of population)",
        "value": "per_si_allsi.cov_q4_tot",
    },
    {
        "label": "Coverage of social insurance programs in richest quintile (% of population)",
        "value": "per_si_allsi.cov_q5_tot",
    },
    {
        "label": "Political Stability and Absence of Violence/Terrorism: Estimate",
        "value": "PV.EST",
    },
    {
        "label": "Political Stability and Absence of Violence/Terrorism: Number of Sources",
        "value": "PV.NO.SRC",
    },
    {
        "label": "Political Stability and Absence of Violence/Terrorism: Percentile Rank",
        "value": "PV.PER.RNK",
    },
    {
        "label": "Political Stability and Absence of Violence/Terrorism: Percentile Rank, Lower Bound of 90% Confidence Interval",
        "value": "PV.PER.RNK.LOWER",
    },
    {
        "label": "Political Stability and Absence of Violence/Terrorism: Percentile Rank, Upper Bound of 90% Confidence Interval",
        "value": "PV.PER.RNK.UPPER",
    },
    {
        "label": "Political Stability and Absence of Violence/Terrorism: Standard Error",
        "value": "PV.STD.ERR",
    },
    {
        "label": "Real effective exchange rate index (2010 = 100)",
        "value": "PX.REX.REER",
    },
    {"label": "Rule of Law: Estimate", "value": "RL.EST"},
    {"label": "Rule of Law: Number of Sources", "value": "RL.NO.SRC"},
    {"label": "Rule of Law: Percentile Rank", "value": "RL.PER.RNK"},
    {
        "label": "Rule of Law: Percentile Rank, Lower Bound of 90% Confidence Interval",
        "value": "RL.PER.RNK.LOWER",
    },
    {
        "label": "Rule of Law: Percentile Rank, Upper Bound of 90% Confidence Interval",
        "value": "RL.PER.RNK.UPPER",
    },
    {"label": "Rule of Law: Standard Error", "value": "RL.STD.ERR"},
    {"label": "Regulatory Quality: Estimate", "value": "RQ.EST"},
    {
        "label": "Regulatory Quality: Number of Sources",
        "value": "RQ.NO.SRC",
    },
    {
        "label": "Regulatory Quality: Percentile Rank",
        "value": "RQ.PER.RNK",
    },
    {
        "label": "Regulatory Quality: Percentile Rank, Lower Bound of 90% Confidence Interval",
        "value": "RQ.PER.RNK.LOWER",
    },
    {
        "label": "Regulatory Quality: Percentile Rank, Upper Bound of 90% Confidence Interval",
        "value": "RQ.PER.RNK.UPPER",
    },
    {
        "label": "Regulatory Quality: Standard Error",
        "value": "RQ.STD.ERR",
    },
    {
        "label": "Literacy rate, youth female (% of females ages 15-24)",
        "value": "SE.ADT.1524.LT.FE.ZS",
    },
    {
        "label": "Literacy rate, youth (ages 15-24), gender parity index (GPI)",
        "value": "SE.ADT.1524.LT.FM.ZS",
    },
    {
        "label": "Literacy rate, youth male (% of males ages 15-24)",
        "value": "SE.ADT.1524.LT.MA.ZS",
    },
    {
        "label": "Literacy rate, youth total (% of people ages 15-24)",
        "value": "SE.ADT.1524.LT.ZS",
    },
    {
        "label": "Literacy rate, adult female (% of females ages 15 and above)",
        "value": "SE.ADT.LITR.FE.ZS",
    },
    {
        "label": "Literacy rate, adult male (% of males ages 15 and above)",
        "value": "SE.ADT.LITR.MA.ZS",
    },
    {
        "label": "Literacy rate, adult total (% of people ages 15 and above)",
        "value": "SE.ADT.LITR.ZS",
    },
    {
        "label": "Compulsory education, duration (years)",
        "value": "SE.COM.DURS",
    },
    {
        "label": "School enrollment, primary (gross), gender parity index (GPI)",
        "value": "SE.ENR.PRIM.FM.ZS",
    },
    {
        "label": "School enrollment, primary and secondary (gross), gender parity index (GPI)",
        "value": "SE.ENR.PRSC.FM.ZS",
    },
    {
        "label": "School enrollment, secondary (gross), gender parity index (GPI)",
        "value": "SE.ENR.SECO.FM.ZS",
    },
    {
        "label": "School enrollment, tertiary (gross), gender parity index (GPI)",
        "value": "SE.ENR.TERT.FM.ZS",
    },
    {
        "label": "Learning poverty: Share of Children at the End-of-Primary age below minimum reading proficiency adjusted by Out-of-School Children (%)",
        "value": "SE.LPV.PRIM",
    },
    {
        "label": "Learning poverty: Share of Female Children at the End-of-Primary age below minimum reading proficiency adjusted by Out-of-School Children (%)",
        "value": "SE.LPV.PRIM.FE",
    },
    {
        "label": "Pupils below minimum reading proficiency at end of primary (%). Low GAML threshold",
        "value": "SE.LPV.PRIM.LD",
    },
    {
        "label": "Female pupils below minimum reading proficiency at end of primary (%). Low GAML threshold",
        "value": "SE.LPV.PRIM.LD.FE",
    },
    {
        "label": "Male pupils below minimum reading proficiency at end of primary (%). Low GAML threshold",
        "value": "SE.LPV.PRIM.LD.MA",
    },
    {
        "label": "Learning poverty: Share of Male Children at the End-of-Primary age below minimum reading proficiency adjusted by Out-of-School Children (%)",
        "value": "SE.LPV.PRIM.MA",
    },
    {
        "label": "Primary school age children out-of-school (%)",
        "value": "SE.LPV.PRIM.SD",
    },
    {
        "label": "Female primary school age children out-of-school (%)",
        "value": "SE.LPV.PRIM.SD.FE",
    },
    {
        "label": "Male primary school age children out-of-school (%)",
        "value": "SE.LPV.PRIM.SD.MA",
    },
    {
        "label": "Preprimary education, duration (years)",
        "value": "SE.PRE.DURS",
    },
    {
        "label": "Pupil-teacher ratio, preprimary",
        "value": "SE.PRE.ENRL.TC.ZS",
    },
    {
        "label": "School enrollment, preprimary (% gross)",
        "value": "SE.PRE.ENRR",
    },
    {
        "label": "School enrollment, preprimary, female (% gross)",
        "value": "SE.PRE.ENRR.FE",
    },
    {
        "label": "School enrollment, preprimary, male (% gross)",
        "value": "SE.PRE.ENRR.MA",
    },
    {
        "label": "Trained teachers in preprimary education, female (% of female teachers)",
        "value": "SE.PRE.TCAQ.FE.ZS",
    },
    {
        "label": "Trained teachers in preprimary education, male (% of male teachers)",
        "value": "SE.PRE.TCAQ.MA.ZS",
    },
    {
        "label": "Trained teachers in preprimary education (% of total teachers)",
        "value": "SE.PRE.TCAQ.ZS",
    },
    {
        "label": "Primary school starting age (years)",
        "value": "SE.PRM.AGES",
    },
    {
        "label": "Primary completion rate, female (% of relevant age group)",
        "value": "SE.PRM.CMPT.FE.ZS",
    },
    {
        "label": "Primary completion rate, male (% of relevant age group)",
        "value": "SE.PRM.CMPT.MA.ZS",
    },
    {
        "label": "Primary completion rate, total (% of relevant age group)",
        "value": "SE.PRM.CMPT.ZS",
    },
    {
        "label": "Educational attainment, at least completed primary, population 25+ years, female (%) (cumulative)",
        "value": "SE.PRM.CUAT.FE.ZS",
    },
    {
        "label": "Educational attainment, at least completed primary, population 25+ years, male (%) (cumulative)",
        "value": "SE.PRM.CUAT.MA.ZS",
    },
    {
        "label": "Educational attainment, at least completed primary, population 25+ years, total (%) (cumulative)",
        "value": "SE.PRM.CUAT.ZS",
    },
    {
        "label": "Primary education, duration (years)",
        "value": "SE.PRM.DURS",
    },
    {"label": "Primary education, pupils", "value": "SE.PRM.ENRL"},
    {
        "label": "Primary education, pupils (% female)",
        "value": "SE.PRM.ENRL.FE.ZS",
    },
    {
        "label": "Pupil-teacher ratio, primary",
        "value": "SE.PRM.ENRL.TC.ZS",
    },
    {
        "label": "School enrollment, primary (% gross)",
        "value": "SE.PRM.ENRR",
    },
    {
        "label": "School enrollment, primary, female (% gross)",
        "value": "SE.PRM.ENRR.FE",
    },
    {
        "label": "School enrollment, primary, male (% gross)",
        "value": "SE.PRM.ENRR.MA",
    },
    {
        "label": "Gross intake ratio in first grade of primary education, female (% of relevant age group)",
        "value": "SE.PRM.GINT.FE.ZS",
    },
    {
        "label": "Gross intake ratio in first grade of primary education, male (% of relevant age group)",
        "value": "SE.PRM.GINT.MA.ZS",
    },
    {
        "label": "Gross intake ratio in first grade of primary education, total (% of relevant age group)",
        "value": "SE.PRM.GINT.ZS",
    },
    {
        "label": "School enrollment, primary (% net)",
        "value": "SE.PRM.NENR",
    },
    {
        "label": "School enrollment, primary, female (% net)",
        "value": "SE.PRM.NENR.FE",
    },
    {
        "label": "School enrollment, primary, male (% net)",
        "value": "SE.PRM.NENR.MA",
    },
    {
        "label": "Net intake rate in grade 1, female (% of official school-age population)",
        "value": "SE.PRM.NINT.FE.ZS",
    },
    {
        "label": "Net intake rate in grade 1, male (% of official school-age population)",
        "value": "SE.PRM.NINT.MA.ZS",
    },
    {
        "label": "Net intake rate in grade 1 (% of official school-age population)",
        "value": "SE.PRM.NINT.ZS",
    },
    {
        "label": "Over-age students, primary, female (% of female enrollment)",
        "value": "SE.PRM.OENR.FE.ZS",
    },
    {
        "label": "Over-age students, primary, male (% of male enrollment)",
        "value": "SE.PRM.OENR.MA.ZS",
    },
    {
        "label": "Over-age students, primary (% of enrollment)",
        "value": "SE.PRM.OENR.ZS",
    },
    {
        "label": "School enrollment, primary, private (% of total primary)",
        "value": "SE.PRM.PRIV.ZS",
    },
    {
        "label": "Persistence to grade 5, female (% of cohort)",
        "value": "SE.PRM.PRS5.FE.ZS",
    },
    {
        "label": "Persistence to grade 5, male (% of cohort)",
        "value": "SE.PRM.PRS5.MA.ZS",
    },
    {
        "label": "Persistence to grade 5, total (% of cohort)",
        "value": "SE.PRM.PRS5.ZS",
    },
    {
        "label": "Persistence to last grade of primary, female (% of cohort)",
        "value": "SE.PRM.PRSL.FE.ZS",
    },
    {
        "label": "Persistence to last grade of primary, male (% of cohort)",
        "value": "SE.PRM.PRSL.MA.ZS",
    },
    {
        "label": "Persistence to last grade of primary, total (% of cohort)",
        "value": "SE.PRM.PRSL.ZS",
    },
    {
        "label": "Repeaters, primary, female (% of female enrollment)",
        "value": "SE.PRM.REPT.FE.ZS",
    },
    {
        "label": "Repeaters, primary, male (% of male enrollment)",
        "value": "SE.PRM.REPT.MA.ZS",
    },
    {
        "label": "Repeaters, primary, total (% of total enrollment)",
        "value": "SE.PRM.REPT.ZS",
    },
    {
        "label": "Trained teachers in primary education, female (% of female teachers)",
        "value": "SE.PRM.TCAQ.FE.ZS",
    },
    {
        "label": "Trained teachers in primary education, male (% of male teachers)",
        "value": "SE.PRM.TCAQ.MA.ZS",
    },
    {
        "label": "Trained teachers in primary education (% of total teachers)",
        "value": "SE.PRM.TCAQ.ZS",
    },
    {"label": "Primary education, teachers", "value": "SE.PRM.TCHR"},
    {
        "label": "Primary education, teachers (% female)",
        "value": "SE.PRM.TCHR.FE.ZS",
    },
    {
        "label": "Adjusted net enrollment rate, primary (% of primary school age children)",
        "value": "SE.PRM.TENR",
    },
    {
        "label": "Adjusted net enrollment rate, primary, female (% of primary school age children)",
        "value": "SE.PRM.TENR.FE",
    },
    {
        "label": "Adjusted net enrollment rate, primary, male (% of primary school age children)",
        "value": "SE.PRM.TENR.MA",
    },
    {
        "label": "Children out of school, primary",
        "value": "SE.PRM.UNER",
    },
    {
        "label": "Children out of school, primary, female",
        "value": "SE.PRM.UNER.FE",
    },
    {
        "label": "Children out of school, female (% of female primary school age)",
        "value": "SE.PRM.UNER.FE.ZS",
    },
    {
        "label": "Children out of school, primary, male",
        "value": "SE.PRM.UNER.MA",
    },
    {
        "label": "Children out of school, male (% of male primary school age)",
        "value": "SE.PRM.UNER.MA.ZS",
    },
    {
        "label": "Children out of school (% of primary school age)",
        "value": "SE.PRM.UNER.ZS",
    },
    {
        "label": "Lower secondary school starting age (years)",
        "value": "SE.SEC.AGES",
    },
    {
        "label": "Lower secondary completion rate, female (% of relevant age group)",
        "value": "SE.SEC.CMPT.LO.FE.ZS",
    },
    {
        "label": "Lower secondary completion rate, male (% of relevant age group)",
        "value": "SE.SEC.CMPT.LO.MA.ZS",
    },
    {
        "label": "Lower secondary completion rate, total (% of relevant age group)",
        "value": "SE.SEC.CMPT.LO.ZS",
    },
    {
        "label": "Educational attainment, at least completed lower secondary, population 25+, female (%) (cumulative)",
        "value": "SE.SEC.CUAT.LO.FE.ZS",
    },
    {
        "label": "Educational attainment, at least completed lower secondary, population 25+, male (%) (cumulative)",
        "value": "SE.SEC.CUAT.LO.MA.ZS",
    },
    {
        "label": "Educational attainment, at least completed lower secondary, population 25+, total (%) (cumulative)",
        "value": "SE.SEC.CUAT.LO.ZS",
    },
    {
        "label": "Educational attainment, at least completed post-secondary, population 25+, female (%) (cumulative)",
        "value": "SE.SEC.CUAT.PO.FE.ZS",
    },
    {
        "label": "Educational attainment, at least completed post-secondary, population 25+, male (%) (cumulative)",
        "value": "SE.SEC.CUAT.PO.MA.ZS",
    },
    {
        "label": "Educational attainment, at least completed post-secondary, population 25+, total (%) (cumulative)",
        "value": "SE.SEC.CUAT.PO.ZS",
    },
    {
        "label": "Educational attainment, at least completed upper secondary, population 25+, female (%) (cumulative)",
        "value": "SE.SEC.CUAT.UP.FE.ZS",
    },
    {
        "label": "Educational attainment, at least completed upper secondary, population 25+, male (%) (cumulative)",
        "value": "SE.SEC.CUAT.UP.MA.ZS",
    },
    {
        "label": "Educational attainment, at least completed upper secondary, population 25+, total (%) (cumulative)",
        "value": "SE.SEC.CUAT.UP.ZS",
    },
    {
        "label": "Secondary education, duration (years)",
        "value": "SE.SEC.DURS",
    },
    {"label": "Secondary education, pupils", "value": "SE.SEC.ENRL"},
    {
        "label": "Secondary education, pupils (% female)",
        "value": "SE.SEC.ENRL.FE.ZS",
    },
    {
        "label": "Secondary education, general pupils",
        "value": "SE.SEC.ENRL.GC",
    },
    {
        "label": "Secondary education, general pupils (% female)",
        "value": "SE.SEC.ENRL.GC.FE.ZS",
    },
    {
        "label": "Pupil-teacher ratio, lower secondary",
        "value": "SE.SEC.ENRL.LO.TC.ZS",
    },
    {
        "label": "Pupil-teacher ratio, secondary",
        "value": "SE.SEC.ENRL.TC.ZS",
    },
    {
        "label": "Pupil-teacher ratio, upper secondary",
        "value": "SE.SEC.ENRL.UP.TC.ZS",
    },
    {
        "label": "Secondary education, vocational pupils",
        "value": "SE.SEC.ENRL.VO",
    },
    {
        "label": "Secondary education, vocational pupils (% female)",
        "value": "SE.SEC.ENRL.VO.FE.ZS",
    },
    {
        "label": "School enrollment, secondary (% gross)",
        "value": "SE.SEC.ENRR",
    },
    {
        "label": "School enrollment, secondary, female (% gross)",
        "value": "SE.SEC.ENRR.FE",
    },
    {
        "label": "School enrollment, secondary, male (% gross)",
        "value": "SE.SEC.ENRR.MA",
    },
    {
        "label": "School enrollment, secondary (% net)",
        "value": "SE.SEC.NENR",
    },
    {
        "label": "School enrollment, secondary, female (% net)",
        "value": "SE.SEC.NENR.FE",
    },
    {
        "label": "School enrollment, secondary, male (% net)",
        "value": "SE.SEC.NENR.MA",
    },
    {
        "label": "School enrollment, secondary, private (% of total secondary)",
        "value": "SE.SEC.PRIV.ZS",
    },
    {
        "label": "Progression to secondary school, female (%)",
        "value": "SE.SEC.PROG.FE.ZS",
    },
    {
        "label": "Progression to secondary school, male (%)",
        "value": "SE.SEC.PROG.MA.ZS",
    },
    {
        "label": "Progression to secondary school (%)",
        "value": "SE.SEC.PROG.ZS",
    },
    {
        "label": "Trained teachers in secondary education, female (% of female teachers)",
        "value": "SE.SEC.TCAQ.FE.ZS",
    },
    {
        "label": "Trained teachers in lower secondary education, female (% of female teachers)",
        "value": "SE.SEC.TCAQ.LO.FE.ZS",
    },
    {
        "label": "Trained teachers in lower secondary education, male (% of male teachers)",
        "value": "SE.SEC.TCAQ.LO.MA.ZS",
    },
    {
        "label": "Trained teachers in lower secondary education (% of total teachers)",
        "value": "SE.SEC.TCAQ.LO.ZS",
    },
    {
        "label": "Trained teachers in secondary education, male (% of male teachers)",
        "value": "SE.SEC.TCAQ.MA.ZS",
    },
    {
        "label": "Trained teachers in upper secondary education, female (% of female teachers)",
        "value": "SE.SEC.TCAQ.UP.FE.ZS",
    },
    {
        "label": "Trained teachers in upper secondary education, male (% of male teachers)",
        "value": "SE.SEC.TCAQ.UP.MA.ZS",
    },
    {
        "label": "Trained teachers in upper secondary education (% of total teachers)",
        "value": "SE.SEC.TCAQ.UP.ZS",
    },
    {
        "label": "Trained teachers in secondary education (% of total teachers)",
        "value": "SE.SEC.TCAQ.ZS",
    },
    {"label": "Secondary education, teachers", "value": "SE.SEC.TCHR"},
    {
        "label": "Secondary education, teachers, female",
        "value": "SE.SEC.TCHR.FE",
    },
    {
        "label": "Secondary education, teachers (% female)",
        "value": "SE.SEC.TCHR.FE.ZS",
    },
    {
        "label": "Adolescents out of school, female (% of female lower secondary school age)",
        "value": "SE.SEC.UNER.LO.FE.ZS",
    },
    {
        "label": "Adolescents out of school, male (% of male lower secondary school age)",
        "value": "SE.SEC.UNER.LO.MA.ZS",
    },
    {
        "label": "Adolescents out of school (% of lower secondary school age)",
        "value": "SE.SEC.UNER.LO.ZS",
    },
    {
        "label": "Educational attainment, at least Bachelor's or equivalent, population 25+, female (%) (cumulative)",
        "value": "SE.TER.CUAT.BA.FE.ZS",
    },
    {
        "label": "Educational attainment, at least Bachelor's or equivalent, population 25+, male (%) (cumulative)",
        "value": "SE.TER.CUAT.BA.MA.ZS",
    },
    {
        "label": "Educational attainment, at least Bachelor's or equivalent, population 25+, total (%) (cumulative)",
        "value": "SE.TER.CUAT.BA.ZS",
    },
    {
        "label": "Educational attainment, Doctoral or equivalent, population 25+, female (%) (cumulative)",
        "value": "SE.TER.CUAT.DO.FE.ZS",
    },
    {
        "label": "Educational attainment, Doctoral or equivalent, population 25+, male (%) (cumulative)",
        "value": "SE.TER.CUAT.DO.MA.ZS",
    },
    {
        "label": "Educational attainment, Doctoral or equivalent, population 25+, total (%) (cumulative)",
        "value": "SE.TER.CUAT.DO.ZS",
    },
    {
        "label": "Educational attainment, at least Master's or equivalent, population 25+, female (%) (cumulative)",
        "value": "SE.TER.CUAT.MS.FE.ZS",
    },
    {
        "label": "Educational attainment, at least Master's or equivalent, population 25+, male (%) (cumulative)",
        "value": "SE.TER.CUAT.MS.MA.ZS",
    },
    {
        "label": "Educational attainment, at least Master's or equivalent, population 25+, total (%) (cumulative)",
        "value": "SE.TER.CUAT.MS.ZS",
    },
    {
        "label": "Educational attainment, at least completed short-cycle tertiary, population 25+, female (%) (cumulative)",
        "value": "SE.TER.CUAT.ST.FE.ZS",
    },
    {
        "label": "Educational attainment, at least completed short-cycle tertiary, population 25+, male (%) (cumulative)",
        "value": "SE.TER.CUAT.ST.MA.ZS",
    },
    {
        "label": "Educational attainment, at least completed short-cycle tertiary, population 25+, total (%) (cumulative)",
        "value": "SE.TER.CUAT.ST.ZS",
    },
    {
        "label": "Pupil-teacher ratio, tertiary",
        "value": "SE.TER.ENRL.TC.ZS",
    },
    {
        "label": "School enrollment, tertiary (% gross)",
        "value": "SE.TER.ENRR",
    },
    {
        "label": "School enrollment, tertiary, female (% gross)",
        "value": "SE.TER.ENRR.FE",
    },
    {
        "label": "School enrollment, tertiary, male (% gross)",
        "value": "SE.TER.ENRR.MA",
    },
    {
        "label": "Tertiary education, academic staff (% female)",
        "value": "SE.TER.TCHR.FE.ZS",
    },
    {
        "label": "Current education expenditure, primary (% of total expenditure in primary public institutions)",
        "value": "SE.XPD.CPRM.ZS",
    },
    {
        "label": "Current education expenditure, secondary (% of total expenditure in secondary public institutions)",
        "value": "SE.XPD.CSEC.ZS",
    },
    {
        "label": "Current education expenditure, tertiary (% of total expenditure in tertiary public institutions)",
        "value": "SE.XPD.CTER.ZS",
    },
    {
        "label": "Current education expenditure, total (% of total expenditure in public institutions)",
        "value": "SE.XPD.CTOT.ZS",
    },
    {
        "label": "Government expenditure per student, primary (% of GDP per capita)",
        "value": "SE.XPD.PRIM.PC.ZS",
    },
    {
        "label": "Expenditure on primary education (% of government expenditure on education)",
        "value": "SE.XPD.PRIM.ZS",
    },
    {
        "label": "Government expenditure per student, secondary (% of GDP per capita)",
        "value": "SE.XPD.SECO.PC.ZS",
    },
    {
        "label": "Expenditure on secondary education (% of government expenditure on education)",
        "value": "SE.XPD.SECO.ZS",
    },
    {
        "label": "Government expenditure per student, tertiary (% of GDP per capita)",
        "value": "SE.XPD.TERT.PC.ZS",
    },
    {
        "label": "Expenditure on tertiary education (% of government expenditure on education)",
        "value": "SE.XPD.TERT.ZS",
    },
    {
        "label": "Government expenditure on education, total (% of government expenditure)",
        "value": "SE.XPD.TOTL.GB.ZS",
    },
    {
        "label": "Government expenditure on education, total (% of GDP)",
        "value": "SE.XPD.TOTL.GD.ZS",
    },
    {
        "label": "Women participating in the three decisions (own health care, major household purchases, and visiting family) (% of women age 15-49)",
        "value": "SG.DMK.ALLD.FN.ZS",
    },
    {
        "label": "Women making their own informed decisions regarding sexual relations, contraceptive use and reproductive health care (% of women age 15-49)",
        "value": "SG.DMK.SRCR.FN.ZS",
    },
    {
        "label": "Proportion of seats held by women in national parliaments (%)",
        "value": "SG.GEN.PARL.ZS",
    },
    {
        "label": "Women Business and the Law Index Score (scale 1-100)",
        "value": "SG.LAW.INDX",
    },
    {
        "label": "Proportion of time spent on unpaid domestic and care work, female (% of 24 hour day)",
        "value": "SG.TIM.UWRK.FE",
    },
    {
        "label": "Proportion of time spent on unpaid domestic and care work, male (% of 24 hour day)",
        "value": "SG.TIM.UWRK.MA",
    },
    {
        "label": "Proportion of women subjected to physical and/or sexual violence in the last 12 months (% of ever-partnered women ages 15-49)",
        "value": "SG.VAW.1549.ZS",
    },
    {
        "label": "Women who believe a husband is justified in beating his wife when she argues with him (%)",
        "value": "SG.VAW.ARGU.ZS",
    },
    {
        "label": "Women who believe a husband is justified in beating his wife when she burns the food (%)",
        "value": "SG.VAW.BURN.ZS",
    },
    {
        "label": "Women who believe a husband is justified in beating his wife when she goes out without telling him (%)",
        "value": "SG.VAW.GOES.ZS",
    },
    {
        "label": "Women who believe a husband is justified in beating his wife when she neglects the children (%)",
        "value": "SG.VAW.NEGL.ZS",
    },
    {
        "label": "Women who believe a husband is justified in beating his wife (any of five reasons) (%)",
        "value": "SG.VAW.REAS.ZS",
    },
    {
        "label": "Women who believe a husband is justified in beating his wife when she refuses sex with him (%)",
        "value": "SG.VAW.REFU.ZS",
    },
    {
        "label": "Total alcohol consumption per capita, female (liters of pure alcohol, projected estimates, female 15+ years of age)",
        "value": "SH.ALC.PCAP.FE.LI",
    },
    {
        "label": "Total alcohol consumption per capita (liters of pure alcohol, projected estimates, 15+ years of age)",
        "value": "SH.ALC.PCAP.LI",
    },
    {
        "label": "Total alcohol consumption per capita, male (liters of pure alcohol, projected estimates, male 15+ years of age)",
        "value": "SH.ALC.PCAP.MA.LI",
    },
    {
        "label": "Prevalence of anemia among women of reproductive age (% of women ages 15-49)",
        "value": "SH.ANM.ALLW.ZS",
    },
    {
        "label": "Prevalence of anemia among children (% of children ages 6-59 months)",
        "value": "SH.ANM.CHLD.ZS",
    },
    {
        "label": "Prevalence of anemia among non-pregnant women (% of women ages 15-49)",
        "value": "SH.ANM.NPRG.ZS",
    },
    {
        "label": "Condom use, population ages 15-24, female (% of females ages 15-24)",
        "value": "SH.CON.1524.FE.ZS",
    },
    {
        "label": "Condom use, population ages 15-24, male (% of males ages 15-24)",
        "value": "SH.CON.1524.MA.ZS",
    },
    {
        "label": "Number of deaths ages 5-9 years",
        "value": "SH.DTH.0509",
    },
    {
        "label": "Number of deaths ages 10-14 years",
        "value": "SH.DTH.1014",
    },
    {
        "label": "Number of deaths ages 15-19 years",
        "value": "SH.DTH.1519",
    },
    {
        "label": "Number of deaths ages 20-24 years",
        "value": "SH.DTH.2024",
    },
    {
        "label": "Cause of death, by communicable diseases and maternal, prenatal and nutrition conditions (% of total)",
        "value": "SH.DTH.COMM.ZS",
    },
    {"label": "Number of infant deaths", "value": "SH.DTH.IMRT"},
    {
        "label": "Cause of death, by injury (% of total)",
        "value": "SH.DTH.INJR.ZS",
    },
    {"label": "Number of under-five deaths", "value": "SH.DTH.MORT"},
    {
        "label": "Cause of death, by non-communicable diseases (% of total)",
        "value": "SH.DTH.NCOM.ZS",
    },
    {"label": "Number of neonatal deaths", "value": "SH.DTH.NMRT"},
    {
        "label": "Probability of dying among children ages 5-9 years (per 1,000)",
        "value": "SH.DYN.0509",
    },
    {
        "label": "Probability of dying among adolescents ages 10-14 years (per 1,000)",
        "value": "SH.DYN.1014",
    },
    {
        "label": "Probability of dying among adolescents ages 15-19 years (per 1,000)",
        "value": "SH.DYN.1519",
    },
    {
        "label": "Probability of dying among youth ages 20-24 years (per 1,000)",
        "value": "SH.DYN.2024",
    },
    {
        "label": "Women's share of population ages 15+ living with HIV (%)",
        "value": "SH.DYN.AIDS.FE.ZS",
    },
    {
        "label": "Prevalence of HIV, total (% of population ages 15-49)",
        "value": "SH.DYN.AIDS.ZS",
    },
    {
        "label": "Mortality rate, under-5 (per 1,000 live births)",
        "value": "SH.DYN.MORT",
    },
    {
        "label": "Mortality rate, under-5, female (per 1,000 live births)",
        "value": "SH.DYN.MORT.FE",
    },
    {
        "label": "Mortality rate, under-5, male (per 1,000 live births)",
        "value": "SH.DYN.MORT.MA",
    },
    {
        "label": "Mortality from CVD, cancer, diabetes or CRD between exact ages 30 and 70, female (%)",
        "value": "SH.DYN.NCOM.FE.ZS",
    },
    {
        "label": "Mortality from CVD, cancer, diabetes or CRD between exact ages 30 and 70, male (%)",
        "value": "SH.DYN.NCOM.MA.ZS",
    },
    {
        "label": "Mortality from CVD, cancer, diabetes or CRD between exact ages 30 and 70 (%)",
        "value": "SH.DYN.NCOM.ZS",
    },
    {
        "label": "Mortality rate, neonatal (per 1,000 live births)",
        "value": "SH.DYN.NMRT",
    },
    {
        "label": "Demand for family planning satisfied by modern methods (% of married women with demand for family planning)",
        "value": "SH.FPL.SATM.ZS",
    },
    {
        "label": "People using at least basic drinking water services, rural (% of rural population)",
        "value": "SH.H2O.BASW.RU.ZS",
    },
    {
        "label": "People using at least basic drinking water services, urban (% of urban population)",
        "value": "SH.H2O.BASW.UR.ZS",
    },
    {
        "label": "People using at least basic drinking water services (% of population)",
        "value": "SH.H2O.BASW.ZS",
    },
    {
        "label": "People using safely managed drinking water services, rural (% of rural population)",
        "value": "SH.H2O.SMDW.RU.ZS",
    },
    {
        "label": "People using safely managed drinking water services, urban (% of urban population)",
        "value": "SH.H2O.SMDW.UR.ZS",
    },
    {
        "label": "People using safely managed drinking water services (% of population)",
        "value": "SH.H2O.SMDW.ZS",
    },
    {
        "label": "Children (0-14) living with HIV",
        "value": "SH.HIV.0014",
    },
    {
        "label": "Prevalence of HIV, female (% ages 15-24)",
        "value": "SH.HIV.1524.FE.ZS",
    },
    {
        "label": "Prevalence of HIV, male (% ages 15-24)",
        "value": "SH.HIV.1524.MA.ZS",
    },
    {
        "label": "Antiretroviral therapy coverage (% of people living with HIV)",
        "value": "SH.HIV.ARTC.ZS",
    },
    {
        "label": "Adults (ages 15-49) newly infected with HIV",
        "value": "SH.HIV.INCD",
    },
    {
        "label": "Children (ages 0-14) newly infected with HIV",
        "value": "SH.HIV.INCD.14",
    },
    {
        "label": "Adults (ages 15+) and children (ages 0-14) newly infected with HIV",
        "value": "SH.HIV.INCD.TL",
    },
    {
        "label": "Incidence of HIV, all (per 1,000 uninfected population)",
        "value": "SH.HIV.INCD.TL.P3",
    },
    {
        "label": "Young people (ages 15-24) newly infected with HIV",
        "value": "SH.HIV.INCD.YG",
    },
    {
        "label": "Incidence of HIV, ages 15-24 (per 1,000 uninfected population ages 15-24)",
        "value": "SH.HIV.INCD.YG.P3",
    },
    {
        "label": "Incidence of HIV, ages 15-49 (per 1,000 uninfected population ages 15-49)",
        "value": "SH.HIV.INCD.ZS",
    },
    {
        "label": "Antiretroviral therapy coverage for PMTCT (% of pregnant women living with HIV)",
        "value": "SH.HIV.PMTC.ZS",
    },
    {
        "label": "Immunization, HepB3 (% of one-year-old children)",
        "value": "SH.IMM.HEPB",
    },
    {
        "label": "Immunization, DPT (% of children ages 12-23 months)",
        "value": "SH.IMM.IDPT",
    },
    {
        "label": "Immunization, measles (% of children ages 12-23 months)",
        "value": "SH.IMM.MEAS",
    },
    {
        "label": "Hospital beds (per 1,000 people)",
        "value": "SH.MED.BEDS.ZS",
    },
    {
        "label": "Community health workers (per 1,000 people)",
        "value": "SH.MED.CMHW.P3",
    },
    {
        "label": "Nurses and midwives (per 1,000 people)",
        "value": "SH.MED.NUMW.P3",
    },
    {
        "label": "Physicians (per 1,000 people)",
        "value": "SH.MED.PHYS.ZS",
    },
    {
        "label": "Specialist surgical workforce (per 100,000 population)",
        "value": "SH.MED.SAOP.P5",
    },
    {
        "label": "Incidence of malaria (per 1,000 population at risk)",
        "value": "SH.MLR.INCD.P3",
    },
    {
        "label": "Use of insecticide-treated bed nets (% of under-5 population)",
        "value": "SH.MLR.NETS.ZS",
    },
    {
        "label": "Children with fever receiving antimalarial drugs (% of children under age 5 with fever)",
        "value": "SH.MLR.TRET.ZS",
    },
    {"label": "Number of maternal deaths", "value": "SH.MMR.DTHS"},
    {
        "label": "Lifetime risk of maternal death (1 in: rate varies by country)",
        "value": "SH.MMR.RISK",
    },
    {
        "label": "Lifetime risk of maternal death (%)",
        "value": "SH.MMR.RISK.ZS",
    },
    {
        "label": "Prevalence of anemia among pregnant women (%)",
        "value": "SH.PRG.ANEM",
    },
    {
        "label": "Prevalence of current tobacco use (% of adults)",
        "value": "SH.PRV.SMOK",
    },
    {
        "label": "Prevalence of current tobacco use, females (% of female adults)",
        "value": "SH.PRV.SMOK.FE",
    },
    {
        "label": "Prevalence of current tobacco use, males (% of male adults)",
        "value": "SH.PRV.SMOK.MA",
    },
    {
        "label": "Risk of catastrophic expenditure for surgical care (% of people at risk)",
        "value": "SH.SGR.CRSK.ZS",
    },
    {
        "label": "Risk of impoverishing expenditure for surgical care (% of people at risk)",
        "value": "SH.SGR.IRSK.ZS",
    },
    {
        "label": "Number of surgical procedures (per 100,000 population)",
        "value": "SH.SGR.PROC.P5",
    },
    {
        "label": "Mortality rate attributed to household and ambient air pollution, age-standardized, female (per 100,000 female population)",
        "value": "SH.STA.AIRP.FE.P5",
    },
    {
        "label": "Mortality rate attributed to household and ambient air pollution, age-standardized, male (per 100,000 male population)",
        "value": "SH.STA.AIRP.MA.P5",
    },
    {
        "label": "Mortality rate attributed to household and ambient air pollution, age-standardized (per 100,000 population)",
        "value": "SH.STA.AIRP.P5",
    },
    {
        "label": "Pregnant women receiving prenatal care (%)",
        "value": "SH.STA.ANVC.ZS",
    },
    {
        "label": "ARI treatment (% of children under 5 taken to a health provider)",
        "value": "SH.STA.ARIC.ZS",
    },
    {
        "label": "People using at least basic sanitation services, rural (% of rural population)",
        "value": "SH.STA.BASS.RU.ZS",
    },
    {
        "label": "People using at least basic sanitation services, urban (% of urban population)",
        "value": "SH.STA.BASS.UR.ZS",
    },
    {
        "label": "People using at least basic sanitation services (% of population)",
        "value": "SH.STA.BASS.ZS",
    },
    {
        "label": "Exclusive breastfeeding (% of children under 6 months)",
        "value": "SH.STA.BFED.ZS",
    },
    {
        "label": "Births attended by skilled health staff (% of total)",
        "value": "SH.STA.BRTC.ZS",
    },
    {
        "label": "Low-birthweight babies (% of births)",
        "value": "SH.STA.BRTW.ZS",
    },
    {
        "label": "Diabetes prevalence (% of population ages 20 to 79)",
        "value": "SH.STA.DIAB.ZS",
    },
    {
        "label": "Female genital mutilation prevalence (%)",
        "value": "SH.STA.FGMS.ZS",
    },
    {
        "label": "People with basic handwashing facilities including soap and water, rural (% of rural population)",
        "value": "SH.STA.HYGN.RU.ZS",
    },
    {
        "label": "People with basic handwashing facilities including soap and water, urban (% of urban population)",
        "value": "SH.STA.HYGN.UR.ZS",
    },
    {
        "label": "People with basic handwashing facilities including soap and water (% of population)",
        "value": "SH.STA.HYGN.ZS",
    },
    {
        "label": "Prevalence of underweight, weight for age, female (% of children under 5)",
        "value": "SH.STA.MALN.FE.ZS",
    },
    {
        "label": "Prevalence of underweight, weight for age, male (% of children under 5)",
        "value": "SH.STA.MALN.MA.ZS",
    },
    {
        "label": "Prevalence of underweight, weight for age (% of children under 5)",
        "value": "SH.STA.MALN.ZS",
    },
    {
        "label": "Maternal mortality ratio (modeled estimate, per 100,000 live births)",
        "value": "SH.STA.MMRT",
    },
    {
        "label": "Maternal mortality ratio (national estimate, per 100,000 live births)",
        "value": "SH.STA.MMRT.NE",
    },
    {
        "label": "People practicing open defecation, rural (% of rural population)",
        "value": "SH.STA.ODFC.RU.ZS",
    },
    {
        "label": "People practicing open defecation, urban (% of urban population)",
        "value": "SH.STA.ODFC.UR.ZS",
    },
    {
        "label": "People practicing open defecation (% of population)",
        "value": "SH.STA.ODFC.ZS",
    },
    {
        "label": "Diarrhea treatment (% of children under 5 receiving oral rehydration and continued feeding)",
        "value": "SH.STA.ORCF.ZS",
    },
    {
        "label": "Diarrhea treatment (% of children under 5 who received ORS packet)",
        "value": "SH.STA.ORTH",
    },
    {
        "label": "Prevalence of overweight, weight for height, female (% of children under 5)",
        "value": "SH.STA.OWGH.FE.ZS",
    },
    {
        "label": "Prevalence of overweight, weight for height, male (% of children under 5)",
        "value": "SH.STA.OWGH.MA.ZS",
    },
    {
        "label": "Prevalence of overweight (modeled estimate, % of children under 5)",
        "value": "SH.STA.OWGH.ME.ZS",
    },
    {
        "label": "Prevalence of overweight, weight for height (% of children under 5)",
        "value": "SH.STA.OWGH.ZS",
    },
    {
        "label": "Mortality rate attributed to unintentional poisoning (per 100,000 population)",
        "value": "SH.STA.POIS.P5",
    },
    {
        "label": "Mortality rate attributed to unintentional poisoning, female (per 100,000 female population)",
        "value": "SH.STA.POIS.P5.FE",
    },
    {
        "label": "Mortality rate attributed to unintentional poisoning, male (per 100,000 male population)",
        "value": "SH.STA.POIS.P5.MA",
    },
    {
        "label": "People using safely managed sanitation services, rural (% of rural population)",
        "value": "SH.STA.SMSS.RU.ZS",
    },
    {
        "label": "People using safely managed sanitation services, urban (% of urban population)",
        "value": "SH.STA.SMSS.UR.ZS",
    },
    {
        "label": "People using safely managed sanitation services (% of population)",
        "value": "SH.STA.SMSS.ZS",
    },
    {
        "label": "Prevalence of stunting, height for age, female (% of children under 5)",
        "value": "SH.STA.STNT.FE.ZS",
    },
    {
        "label": "Prevalence of stunting, height for age, male (% of children under 5)",
        "value": "SH.STA.STNT.MA.ZS",
    },
    {
        "label": "Prevalence of stunting, height for age (modeled estimate, % of children under 5)",
        "value": "SH.STA.STNT.ME.ZS",
    },
    {
        "label": "Prevalence of stunting, height for age (% of children under 5)",
        "value": "SH.STA.STNT.ZS",
    },
    {
        "label": "Suicide mortality rate, female (per 100,000 female population)",
        "value": "SH.STA.SUIC.FE.P5",
    },
    {
        "label": "Suicide mortality rate, male (per 100,000 male population)",
        "value": "SH.STA.SUIC.MA.P5",
    },
    {
        "label": "Suicide mortality rate (per 100,000 population)",
        "value": "SH.STA.SUIC.P5",
    },
    {
        "label": "Mortality caused by road traffic injury (per 100,000 population)",
        "value": "SH.STA.TRAF.P5",
    },
    {
        "label": "Mortality rate attributed to unsafe water, unsafe sanitation and lack of hygiene (per 100,000 population)",
        "value": "SH.STA.WASH.P5",
    },
    {
        "label": "Prevalence of wasting, weight for height, female (% of children under 5)",
        "value": "SH.STA.WAST.FE.ZS",
    },
    {
        "label": "Prevalence of wasting, weight for height, male (% of children under 5)",
        "value": "SH.STA.WAST.MA.ZS",
    },
    {
        "label": "Prevalence of wasting, weight for height (% of children under 5)",
        "value": "SH.STA.WAST.ZS",
    },
    {
        "label": "Prevalence of severe wasting, weight for height, female (% of children under 5)",
        "value": "SH.SVR.WAST.FE.ZS",
    },
    {
        "label": "Prevalence of severe wasting, weight for height, male (% of children under 5)",
        "value": "SH.SVR.WAST.MA.ZS",
    },
    {
        "label": "Prevalence of severe wasting, weight for height (% of children under 5)",
        "value": "SH.SVR.WAST.ZS",
    },
    {
        "label": "Tuberculosis treatment success rate (% of new cases)",
        "value": "SH.TBS.CURE.ZS",
    },
    {
        "label": "Tuberculosis case detection rate (%, all forms)",
        "value": "SH.TBS.DTEC.ZS",
    },
    {
        "label": "Incidence of tuberculosis (per 100,000 people)",
        "value": "SH.TBS.INCD",
    },
    {
        "label": "Proportion of population pushed further below the $2.15 ($ 2017 PPP) poverty line by out-of-pocket health care expenditure (%)",
        "value": "SH.UHC.FBP1.ZS",
    },
    {
        "label": "Proportion of population pushed further below the $3.65 ($ 2017 PPP) poverty line by out-of-pocket health care expenditure (%)",
        "value": "SH.UHC.FBP2.ZS",
    },
    {
        "label": "Proportion of population pushed further below the 60% median consumption poverty line by out-of-pocket health care expenditure (%)",
        "value": "SH.UHC.FBPR.ZS",
    },
    {
        "label": "Proportion of population pushed below the $2.15 ($ 2017 PPP) poverty line by out-of-pocket health care expenditure (%)",
        "value": "SH.UHC.NOP1.ZS",
    },
    {
        "label": "Proportion of population pushed below the $3.65 ($ 2017 PPP) poverty line by out-of-pocket health care expenditure (%)",
        "value": "SH.UHC.NOP2.ZS",
    },
    {
        "label": "Proportion of population pushed below the 60% median consumption poverty line by out-of-pocket health expenditure (%)",
        "value": "SH.UHC.NOPR.ZS",
    },
    {
        "label": "Proportion of population spending more than 10% of household consumption or income on out-of-pocket health care expenditure (%)",
        "value": "SH.UHC.OOPC.10.ZS",
    },
    {
        "label": "Proportion of population spending more than 25% of household consumption or income on out-of-pocket health care expenditure (%)",
        "value": "SH.UHC.OOPC.25.ZS",
    },
    {
        "label": "UHC service coverage index",
        "value": "SH.UHC.SRVS.CV.XD",
    },
    {
        "label": "Proportion of population pushed or further pushed below the $2.15 ($ 2017 PPP) poverty line by out-of-pocket health care expenditure (%)",
        "value": "SH.UHC.TOT1.ZS",
    },
    {
        "label": "Proportion of population pushed or further pushed below the $3.65 ($ 2017 PPP) poverty line by out-of-pocket health care expenditure (%)",
        "value": "SH.UHC.TOT2.ZS",
    },
    {
        "label": "Proportion of population pushed or further pushed below the 60% median consumption poverty line by out-of-pocket health expenditure (%)",
        "value": "SH.UHC.TOTR.ZS",
    },
    {
        "label": "Newborns protected against tetanus (%)",
        "value": "SH.VAC.TTNS.ZS",
    },
    {
        "label": "Current health expenditure (% of GDP)",
        "value": "SH.XPD.CHEX.GD.ZS",
    },
    {
        "label": "Current health expenditure per capita (current US$)",
        "value": "SH.XPD.CHEX.PC.CD",
    },
    {
        "label": "Current health expenditure per capita, PPP (current international $)",
        "value": "SH.XPD.CHEX.PP.CD",
    },
    {
        "label": "External health expenditure (% of current health expenditure)",
        "value": "SH.XPD.EHEX.CH.ZS",
    },
    {
        "label": "External health expenditure per capita (current US$)",
        "value": "SH.XPD.EHEX.PC.CD",
    },
    {
        "label": "External health expenditure per capita, PPP (current international $)",
        "value": "SH.XPD.EHEX.PP.CD",
    },
    {
        "label": "Domestic general government health expenditure (% of current health expenditure)",
        "value": "SH.XPD.GHED.CH.ZS",
    },
    {
        "label": "Domestic general government health expenditure (% of GDP)",
        "value": "SH.XPD.GHED.GD.ZS",
    },
    {
        "label": "Domestic general government health expenditure (% of general government expenditure)",
        "value": "SH.XPD.GHED.GE.ZS",
    },
    {
        "label": "Domestic general government health expenditure per capita (current US$)",
        "value": "SH.XPD.GHED.PC.CD",
    },
    {
        "label": "Domestic general government health expenditure per capita, PPP (current international $)",
        "value": "SH.XPD.GHED.PP.CD",
    },
    {
        "label": "Out-of-pocket expenditure (% of current health expenditure)",
        "value": "SH.XPD.OOPC.CH.ZS",
    },
    {
        "label": "Out-of-pocket expenditure per capita (current US$)",
        "value": "SH.XPD.OOPC.PC.CD",
    },
    {
        "label": "Out-of-pocket expenditure per capita, PPP (current international $)",
        "value": "SH.XPD.OOPC.PP.CD",
    },
    {
        "label": "Domestic private health expenditure (% of current health expenditure)",
        "value": "SH.XPD.PVTD.CH.ZS",
    },
    {
        "label": "Domestic private health expenditure per capita (current US$)",
        "value": "SH.XPD.PVTD.PC.CD",
    },
    {
        "label": "Domestic private health expenditure per capita, PPP (current international $)",
        "value": "SH.XPD.PVTD.PP.CD",
    },
    {
        "label": "Income share held by second 20%",
        "value": "SI.DST.02ND.20",
    },
    {
        "label": "Income share held by third 20%",
        "value": "SI.DST.03RD.20",
    },
    {
        "label": "Income share held by fourth 20%",
        "value": "SI.DST.04TH.20",
    },
    {
        "label": "Income share held by highest 20%",
        "value": "SI.DST.05TH.20",
    },
    {
        "label": "Income share held by highest 10%",
        "value": "SI.DST.10TH.10",
    },
    {
        "label": "Proportion of people living below 50 percent of median income (%)",
        "value": "SI.DST.50MD",
    },
    {
        "label": "Income share held by lowest 10%",
        "value": "SI.DST.FRST.10",
    },
    {
        "label": "Income share held by lowest 20%",
        "value": "SI.DST.FRST.20",
    },
    {
        "label": "Poverty headcount ratio at $2.15 a day (2017 PPP) (% of population)",
        "value": "SI.POV.DDAY",
    },
    {
        "label": "Poverty gap at $2.15 a day (2017 PPP) (%)",
        "value": "SI.POV.GAPS",
    },
    {"label": "Gini index", "value": "SI.POV.GINI"},
    {
        "label": "Poverty headcount ratio at $3.65 a day (2017 PPP) (% of population)",
        "value": "SI.POV.LMIC",
    },
    {
        "label": "Poverty gap at $3.65 a day (2017 PPP) (%)",
        "value": "SI.POV.LMIC.GP",
    },
    {
        "label": "Multidimensional poverty headcount ratio (UNDP) (% of population)",
        "value": "SI.POV.MPUN",
    },
    {
        "label": "Multidimensional poverty headcount ratio (World Bank) (% of population)",
        "value": "SI.POV.MPWB",
    },
    {
        "label": "Poverty headcount ratio at national poverty lines (% of population)",
        "value": "SI.POV.NAHC",
    },
    {
        "label": "Poverty headcount ratio at societal poverty line (% of population)",
        "value": "SI.POV.SOPO",
    },
    {
        "label": "Poverty headcount ratio at $6.85 a day (2017 PPP) (% of population)",
        "value": "SI.POV.UMIC",
    },
    {
        "label": "Poverty gap at $6.85 a day (2017 PPP) (%)",
        "value": "SI.POV.UMIC.GP",
    },
    {
        "label": "Average transaction cost of sending remittances to a specific country (%)",
        "value": "SI.RMT.COST.IB.ZS",
    },
    {
        "label": "Average transaction cost of sending remittances from a specific country (%)",
        "value": "SI.RMT.COST.OB.ZS",
    },
    {
        "label": "Survey mean consumption or income per capita, bottom 40% of population (2017 PPP $ per day)",
        "value": "SI.SPR.PC40",
    },
    {
        "label": "Annualized average growth rate in per capita real survey mean consumption or income, bottom 40% of population (%)",
        "value": "SI.SPR.PC40.ZG",
    },
    {
        "label": "Survey mean consumption or income per capita, total population (2017 PPP $ per day)",
        "value": "SI.SPR.PCAP",
    },
    {
        "label": "Annualized average growth rate in per capita real survey mean consumption or income, total population (%)",
        "value": "SI.SPR.PCAP.ZG",
    },
    {
        "label": "Child employment in agriculture, female (% of female economically active children ages 7-14)",
        "value": "SL.AGR.0714.FE.ZS",
    },
    {
        "label": "Child employment in agriculture, male (% of male economically active children ages 7-14)",
        "value": "SL.AGR.0714.MA.ZS",
    },
    {
        "label": "Child employment in agriculture (% of economically active children ages 7-14)",
        "value": "SL.AGR.0714.ZS",
    },
    {
        "label": "Employment in agriculture, female (% of female employment) (modeled ILO estimate)",
        "value": "SL.AGR.EMPL.FE.ZS",
    },
    {
        "label": "Employment in agriculture, male (% of male employment) (modeled ILO estimate)",
        "value": "SL.AGR.EMPL.MA.ZS",
    },
    {
        "label": "Employment in agriculture (% of total employment) (modeled ILO estimate)",
        "value": "SL.AGR.EMPL.ZS",
    },
    {
        "label": "Employment to population ratio, ages 15-24, female (%) (national estimate)",
        "value": "SL.EMP.1524.SP.FE.NE.ZS",
    },
    {
        "label": "Employment to population ratio, ages 15-24, female (%) (modeled ILO estimate)",
        "value": "SL.EMP.1524.SP.FE.ZS",
    },
    {
        "label": "Employment to population ratio, ages 15-24, male (%) (national estimate)",
        "value": "SL.EMP.1524.SP.MA.NE.ZS",
    },
    {
        "label": "Employment to population ratio, ages 15-24, male (%) (modeled ILO estimate)",
        "value": "SL.EMP.1524.SP.MA.ZS",
    },
    {
        "label": "Employment to population ratio, ages 15-24, total (%) (national estimate)",
        "value": "SL.EMP.1524.SP.NE.ZS",
    },
    {
        "label": "Employment to population ratio, ages 15-24, total (%) (modeled ILO estimate)",
        "value": "SL.EMP.1524.SP.ZS",
    },
    {
        "label": "Employers, female (% of female employment) (modeled ILO estimate)",
        "value": "SL.EMP.MPYR.FE.ZS",
    },
    {
        "label": "Employers, male (% of male employment) (modeled ILO estimate)",
        "value": "SL.EMP.MPYR.MA.ZS",
    },
    {
        "label": "Employers, total (% of total employment) (modeled ILO estimate)",
        "value": "SL.EMP.MPYR.ZS",
    },
    {
        "label": "Self-employed, female (% of female employment) (modeled ILO estimate)",
        "value": "SL.EMP.SELF.FE.ZS",
    },
    {
        "label": "Self-employed, male (% of male employment) (modeled ILO estimate)",
        "value": "SL.EMP.SELF.MA.ZS",
    },
    {
        "label": "Self-employed, total (% of total employment) (modeled ILO estimate)",
        "value": "SL.EMP.SELF.ZS",
    },
    {
        "label": "Female share of employment in senior and middle management (%)",
        "value": "SL.EMP.SMGT.FE.ZS",
    },
    {
        "label": "Employment to population ratio, 15+, female (%) (national estimate)",
        "value": "SL.EMP.TOTL.SP.FE.NE.ZS",
    },
    {
        "label": "Employment to population ratio, 15+, female (%) (modeled ILO estimate)",
        "value": "SL.EMP.TOTL.SP.FE.ZS",
    },
    {
        "label": "Employment to population ratio, 15+, male (%) (national estimate)",
        "value": "SL.EMP.TOTL.SP.MA.NE.ZS",
    },
    {
        "label": "Employment to population ratio, 15+, male (%) (modeled ILO estimate)",
        "value": "SL.EMP.TOTL.SP.MA.ZS",
    },
    {
        "label": "Employment to population ratio, 15+, total (%) (national estimate)",
        "value": "SL.EMP.TOTL.SP.NE.ZS",
    },
    {
        "label": "Employment to population ratio, 15+, total (%) (modeled ILO estimate)",
        "value": "SL.EMP.TOTL.SP.ZS",
    },
    {
        "label": "Vulnerable employment, female (% of female employment) (modeled ILO estimate)",
        "value": "SL.EMP.VULN.FE.ZS",
    },
    {
        "label": "Vulnerable employment, male (% of male employment) (modeled ILO estimate)",
        "value": "SL.EMP.VULN.MA.ZS",
    },
    {
        "label": "Vulnerable employment, total (% of total employment) (modeled ILO estimate)",
        "value": "SL.EMP.VULN.ZS",
    },
    {
        "label": "Wage and salaried workers, female (% of female employment) (modeled ILO estimate)",
        "value": "SL.EMP.WORK.FE.ZS",
    },
    {
        "label": "Wage and salaried workers, male (% of male employment) (modeled ILO estimate)",
        "value": "SL.EMP.WORK.MA.ZS",
    },
    {
        "label": "Wage and salaried workers, total (% of total employment) (modeled ILO estimate)",
        "value": "SL.EMP.WORK.ZS",
    },
    {
        "label": "Children in employment, unpaid family workers, female (% of female children in employment, ages 7-14)",
        "value": "SL.FAM.0714.FE.ZS",
    },
    {
        "label": "Children in employment, unpaid family workers, male (% of male children in employment, ages 7-14)",
        "value": "SL.FAM.0714.MA.ZS",
    },
    {
        "label": "Children in employment, unpaid family workers (% of children in employment, ages 7-14)",
        "value": "SL.FAM.0714.ZS",
    },
    {
        "label": "Contributing family workers, female (% of female employment) (modeled ILO estimate)",
        "value": "SL.FAM.WORK.FE.ZS",
    },
    {
        "label": "Contributing family workers, male (% of male employment) (modeled ILO estimate)",
        "value": "SL.FAM.WORK.MA.ZS",
    },
    {
        "label": "Contributing family workers, total (% of total employment) (modeled ILO estimate)",
        "value": "SL.FAM.WORK.ZS",
    },
    {
        "label": "GDP per person employed (constant 2017 PPP $)",
        "value": "SL.GDP.PCAP.EM.KD",
    },
    {
        "label": "Employment in industry, female (% of female employment) (modeled ILO estimate)",
        "value": "SL.IND.EMPL.FE.ZS",
    },
    {
        "label": "Employment in industry, male (% of male employment) (modeled ILO estimate)",
        "value": "SL.IND.EMPL.MA.ZS",
    },
    {
        "label": "Employment in industry (% of total employment) (modeled ILO estimate)",
        "value": "SL.IND.EMPL.ZS",
    },
    {
        "label": "Child employment in manufacturing, female (% of female economically active children ages 7-14)",
        "value": "SL.MNF.0714.FE.ZS",
    },
    {
        "label": "Child employment in manufacturing, male (% of male economically active children ages 7-14)",
        "value": "SL.MNF.0714.MA.ZS",
    },
    {
        "label": "Child employment in manufacturing (% of economically active children ages 7-14)",
        "value": "SL.MNF.0714.ZS",
    },
    {
        "label": "Children in employment, self-employed, female (% of female children in employment, ages 7-14)",
        "value": "SL.SLF.0714.FE.ZS",
    },
    {
        "label": "Children in employment, self-employed, male (% of male children in employment, ages 7-14)",
        "value": "SL.SLF.0714.MA.ZS",
    },
    {
        "label": "Children in employment, self-employed (% of children in employment, ages 7-14)",
        "value": "SL.SLF.0714.ZS",
    },
    {
        "label": "Child employment in services, female (% of female economically active children ages 7-14)",
        "value": "SL.SRV.0714.FE.ZS",
    },
    {
        "label": "Child employment in services, male (% of male economically active children ages 7-14)",
        "value": "SL.SRV.0714.MA.ZS",
    },
    {
        "label": "Child employment in services (% of economically active children ages 7-14)",
        "value": "SL.SRV.0714.ZS",
    },
    {
        "label": "Employment in services, female (% of female employment) (modeled ILO estimate)",
        "value": "SL.SRV.EMPL.FE.ZS",
    },
    {
        "label": "Employment in services, male (% of male employment) (modeled ILO estimate)",
        "value": "SL.SRV.EMPL.MA.ZS",
    },
    {
        "label": "Employment in services (% of total employment) (modeled ILO estimate)",
        "value": "SL.SRV.EMPL.ZS",
    },
    {
        "label": "Children in employment, female (% of female children ages 7-14)",
        "value": "SL.TLF.0714.FE.ZS",
    },
    {
        "label": "Children in employment, male (% of male children ages 7-14)",
        "value": "SL.TLF.0714.MA.ZS",
    },
    {
        "label": "Average working hours of children, study and work, female, ages 7-14 (hours per week)",
        "value": "SL.TLF.0714.SW.FE.TM",
    },
    {
        "label": "Children in employment, study and work, female (% of female children in employment, ages 7-14)",
        "value": "SL.TLF.0714.SW.FE.ZS",
    },
    {
        "label": "Average working hours of children, study and work, male, ages 7-14 (hours per week)",
        "value": "SL.TLF.0714.SW.MA.TM",
    },
    {
        "label": "Children in employment, study and work, male (% of male children in employment, ages 7-14)",
        "value": "SL.TLF.0714.SW.MA.ZS",
    },
    {
        "label": "Average working hours of children, study and work, ages 7-14 (hours per week)",
        "value": "SL.TLF.0714.SW.TM",
    },
    {
        "label": "Children in employment, study and work (% of children in employment, ages 7-14)",
        "value": "SL.TLF.0714.SW.ZS",
    },
    {
        "label": "Average working hours of children, working only, female, ages 7-14 (hours per week)",
        "value": "SL.TLF.0714.WK.FE.TM",
    },
    {
        "label": "Children in employment, work only, female (% of female children in employment, ages 7-14)",
        "value": "SL.TLF.0714.WK.FE.ZS",
    },
    {
        "label": "Average working hours of children, working only, male, ages 7-14 (hours per week)",
        "value": "SL.TLF.0714.WK.MA.TM",
    },
    {
        "label": "Children in employment, work only, male (% of male children in employment, ages 7-14)",
        "value": "SL.TLF.0714.WK.MA.ZS",
    },
    {
        "label": "Average working hours of children, working only, ages 7-14 (hours per week)",
        "value": "SL.TLF.0714.WK.TM",
    },
    {
        "label": "Children in employment, work only (% of children in employment, ages 7-14)",
        "value": "SL.TLF.0714.WK.ZS",
    },
    {
        "label": "Children in employment, total (% of children ages 7-14)",
        "value": "SL.TLF.0714.ZS",
    },
    {
        "label": "Labor force participation rate for ages 15-24, female (%) (national estimate)",
        "value": "SL.TLF.ACTI.1524.FE.NE.ZS",
    },
    {
        "label": "Labor force participation rate for ages 15-24, female (%) (modeled ILO estimate)",
        "value": "SL.TLF.ACTI.1524.FE.ZS",
    },
    {
        "label": "Labor force participation rate for ages 15-24, male (%) (national estimate)",
        "value": "SL.TLF.ACTI.1524.MA.NE.ZS",
    },
    {
        "label": "Labor force participation rate for ages 15-24, male (%) (modeled ILO estimate)",
        "value": "SL.TLF.ACTI.1524.MA.ZS",
    },
    {
        "label": "Labor force participation rate for ages 15-24, total (%) (national estimate)",
        "value": "SL.TLF.ACTI.1524.NE.ZS",
    },
    {
        "label": "Labor force participation rate for ages 15-24, total (%) (modeled ILO estimate)",
        "value": "SL.TLF.ACTI.1524.ZS",
    },
    {
        "label": "Labor force participation rate, female (% of female population ages 15-64) (modeled ILO estimate)",
        "value": "SL.TLF.ACTI.FE.ZS",
    },
    {
        "label": "Labor force participation rate, male (% of male population ages 15-64) (modeled ILO estimate)",
        "value": "SL.TLF.ACTI.MA.ZS",
    },
    {
        "label": "Labor force participation rate, total (% of total population ages 15-64) (modeled ILO estimate)",
        "value": "SL.TLF.ACTI.ZS",
    },
    {
        "label": "Labor force with advanced education, female (% of female working-age population with advanced education)",
        "value": "SL.TLF.ADVN.FE.ZS",
    },
    {
        "label": "Labor force with advanced education, male (% of male working-age population with advanced education)",
        "value": "SL.TLF.ADVN.MA.ZS",
    },
    {
        "label": "Labor force with advanced education (% of total working-age population with advanced education)",
        "value": "SL.TLF.ADVN.ZS",
    },
    {
        "label": "Labor force with basic education, female (% of female working-age population with basic education)",
        "value": "SL.TLF.BASC.FE.ZS",
    },
    {
        "label": "Labor force with basic education, male (% of male working-age population with basic education)",
        "value": "SL.TLF.BASC.MA.ZS",
    },
    {
        "label": "Labor force with basic education (% of total working-age population with basic education)",
        "value": "SL.TLF.BASC.ZS",
    },
    {
        "label": "Labor force participation rate, female (% of female population ages 15+) (national estimate)",
        "value": "SL.TLF.CACT.FE.NE.ZS",
    },
    {
        "label": "Labor force participation rate, female (% of female population ages 15+) (modeled ILO estimate)",
        "value": "SL.TLF.CACT.FE.ZS",
    },
    {
        "label": "Ratio of female to male labor force participation rate (%) (national estimate)",
        "value": "SL.TLF.CACT.FM.NE.ZS",
    },
    {
        "label": "Ratio of female to male labor force participation rate (%) (modeled ILO estimate)",
        "value": "SL.TLF.CACT.FM.ZS",
    },
    {
        "label": "Labor force participation rate, male (% of male population ages 15+) (national estimate)",
        "value": "SL.TLF.CACT.MA.NE.ZS",
    },
    {
        "label": "Labor force participation rate, male (% of male population ages 15+) (modeled ILO estimate)",
        "value": "SL.TLF.CACT.MA.ZS",
    },
    {
        "label": "Labor force participation rate, total (% of total population ages 15+) (national estimate)",
        "value": "SL.TLF.CACT.NE.ZS",
    },
    {
        "label": "Labor force participation rate, total (% of total population ages 15+) (modeled ILO estimate)",
        "value": "SL.TLF.CACT.ZS",
    },
    {
        "label": "Labor force with intermediate education, female (% of female working-age population with intermediate education)",
        "value": "SL.TLF.INTM.FE.ZS",
    },
    {
        "label": "Labor force with intermediate education, male (% of male working-age population with intermediate education)",
        "value": "SL.TLF.INTM.MA.ZS",
    },
    {
        "label": "Labor force with intermediate education (% of total working-age population with intermediate education)",
        "value": "SL.TLF.INTM.ZS",
    },
    {
        "label": "Part time employment, female (% of total female employment)",
        "value": "SL.TLF.PART.FE.ZS",
    },
    {
        "label": "Part time employment, male (% of total male employment)",
        "value": "SL.TLF.PART.MA.ZS",
    },
    {
        "label": "Part time employment, total (% of total employment)",
        "value": "SL.TLF.PART.ZS",
    },
    {
        "label": "Labor force, female (% of total labor force)",
        "value": "SL.TLF.TOTL.FE.ZS",
    },
    {"label": "Labor force, total", "value": "SL.TLF.TOTL.IN"},
    {
        "label": "Unemployment, youth female (% of female labor force ages 15-24) (national estimate)",
        "value": "SL.UEM.1524.FE.NE.ZS",
    },
    {
        "label": "Unemployment, youth female (% of female labor force ages 15-24) (modeled ILO estimate)",
        "value": "SL.UEM.1524.FE.ZS",
    },
    {
        "label": "Unemployment, youth male (% of male labor force ages 15-24) (national estimate)",
        "value": "SL.UEM.1524.MA.NE.ZS",
    },
    {
        "label": "Unemployment, youth male (% of male labor force ages 15-24) (modeled ILO estimate)",
        "value": "SL.UEM.1524.MA.ZS",
    },
    {
        "label": "Unemployment, youth total (% of total labor force ages 15-24) (national estimate)",
        "value": "SL.UEM.1524.NE.ZS",
    },
    {
        "label": "Unemployment, youth total (% of total labor force ages 15-24) (modeled ILO estimate)",
        "value": "SL.UEM.1524.ZS",
    },
    {
        "label": "Unemployment with advanced education, female (% of female labor force with advanced education)",
        "value": "SL.UEM.ADVN.FE.ZS",
    },
    {
        "label": "Unemployment with advanced education, male (% of male labor force with advanced education)",
        "value": "SL.UEM.ADVN.MA.ZS",
    },
    {
        "label": "Unemployment with advanced education (% of total labor force with advanced education)",
        "value": "SL.UEM.ADVN.ZS",
    },
    {
        "label": "Unemployment with basic education, female (% of female labor force with basic education)",
        "value": "SL.UEM.BASC.FE.ZS",
    },
    {
        "label": "Unemployment with basic education, male (% of male labor force with basic education)",
        "value": "SL.UEM.BASC.MA.ZS",
    },
    {
        "label": "Unemployment with basic education (% of total labor force with basic education)",
        "value": "SL.UEM.BASC.ZS",
    },
    {
        "label": "Unemployment with intermediate education, female (% of female labor force with intermediate education)",
        "value": "SL.UEM.INTM.FE.ZS",
    },
    {
        "label": "Unemployment with intermediate education, male (% of male labor force with intermediate education)",
        "value": "SL.UEM.INTM.MA.ZS",
    },
    {
        "label": "Unemployment with intermediate education (% of total labor force with intermediate education)",
        "value": "SL.UEM.INTM.ZS",
    },
    {
        "label": "Share of youth not in education, employment or training, female (% of female youth population)",
        "value": "SL.UEM.NEET.FE.ZS",
    },
    {
        "label": "Share of youth not in education, employment or training, male (% of male youth population)",
        "value": "SL.UEM.NEET.MA.ZS",
    },
    {
        "label": "Share of youth not in education, employment or training, total (% of youth population)",
        "value": "SL.UEM.NEET.ZS",
    },
    {
        "label": "Unemployment, female (% of female labor force) (national estimate)",
        "value": "SL.UEM.TOTL.FE.NE.ZS",
    },
    {
        "label": "Unemployment, female (% of female labor force) (modeled ILO estimate)",
        "value": "SL.UEM.TOTL.FE.ZS",
    },
    {
        "label": "Unemployment, male (% of male labor force) (national estimate)",
        "value": "SL.UEM.TOTL.MA.NE.ZS",
    },
    {
        "label": "Unemployment, male (% of male labor force) (modeled ILO estimate)",
        "value": "SL.UEM.TOTL.MA.ZS",
    },
    {
        "label": "Unemployment, total (% of total labor force) (national estimate)",
        "value": "SL.UEM.TOTL.NE.ZS",
    },
    {
        "label": "Unemployment, total (% of total labor force) (modeled ILO estimate)",
        "value": "SL.UEM.TOTL.ZS",
    },
    {
        "label": "Children in employment, wage workers, female (% of female children in employment, ages 7-14)",
        "value": "SL.WAG.0714.FE.ZS",
    },
    {
        "label": "Children in employment, wage workers, male (% of male children in employment, ages 7-14)",
        "value": "SL.WAG.0714.MA.ZS",
    },
    {
        "label": "Children in employment, wage workers (% of children in employment, ages 7-14)",
        "value": "SL.WAG.0714.ZS",
    },
    {"label": "Net migration", "value": "SM.POP.NETM"},
    {
        "label": "Refugee population by country or territory of asylum",
        "value": "SM.POP.REFG",
    },
    {
        "label": "Refugee population by country or territory of origin",
        "value": "SM.POP.REFG.OR",
    },
    {
        "label": "International migrant stock, total",
        "value": "SM.POP.TOTL",
    },
    {
        "label": "International migrant stock (% of population)",
        "value": "SM.POP.TOTL.ZS",
    },
    {
        "label": "Prevalence of undernourishment (% of population)",
        "value": "SN.ITK.DEFC.ZS",
    },
    {
        "label": "Prevalence of moderate or severe food insecurity in the population (%)",
        "value": "SN.ITK.MSFI.ZS",
    },
    {
        "label": "Consumption of iodized salt (% of households)",
        "value": "SN.ITK.SALT.ZS",
    },
    {
        "label": "Prevalence of severe food insecurity in the population (%)",
        "value": "SN.ITK.SVFI.ZS",
    },
    {
        "label": "Vitamin A supplementation coverage rate (% of children ages 6-59 months)",
        "value": "SN.ITK.VITA.ZS",
    },
    {
        "label": "Adolescent fertility rate (births per 1,000 women ages 15-19)",
        "value": "SP.ADO.TFRT",
    },
    {
        "label": "Mortality rate, adult, female (per 1,000 female adults)",
        "value": "SP.DYN.AMRT.FE",
    },
    {
        "label": "Mortality rate, adult, male (per 1,000 male adults)",
        "value": "SP.DYN.AMRT.MA",
    },
    {
        "label": "Birth rate, crude (per 1,000 people)",
        "value": "SP.DYN.CBRT.IN",
    },
    {
        "label": "Death rate, crude (per 1,000 people)",
        "value": "SP.DYN.CDRT.IN",
    },
    {
        "label": "Contraceptive prevalence, any modern method (% of married women ages 15-49)",
        "value": "SP.DYN.CONM.ZS",
    },
    {
        "label": "Contraceptive prevalence, any method (% of married women ages 15-49)",
        "value": "SP.DYN.CONU.ZS",
    },
    {
        "label": "Mortality rate, infant, female (per 1,000 live births)",
        "value": "SP.DYN.IMRT.FE.IN",
    },
    {
        "label": "Mortality rate, infant (per 1,000 live births)",
        "value": "SP.DYN.IMRT.IN",
    },
    {
        "label": "Mortality rate, infant, male (per 1,000 live births)",
        "value": "SP.DYN.IMRT.MA.IN",
    },
    {
        "label": "Life expectancy at birth, female (years)",
        "value": "SP.DYN.LE00.FE.IN",
    },
    {
        "label": "Life expectancy at birth, total (years)",
        "value": "SP.DYN.LE00.IN",
    },
    {
        "label": "Life expectancy at birth, male (years)",
        "value": "SP.DYN.LE00.MA.IN",
    },
    {
        "label": "Fertility rate, total (births per woman)",
        "value": "SP.DYN.TFRT.IN",
    },
    {
        "label": "Survival to age 65, female (% of cohort)",
        "value": "SP.DYN.TO65.FE.ZS",
    },
    {
        "label": "Survival to age 65, male (% of cohort)",
        "value": "SP.DYN.TO65.MA.ZS",
    },
    {
        "label": "Wanted fertility rate (births per woman)",
        "value": "SP.DYN.WFRT",
    },
    {
        "label": "Female headed households (% of households with a female head)",
        "value": "SP.HOU.FEMA.ZS",
    },
    {
        "label": "Women who were first married by age 15 (% of women ages 20-24)",
        "value": "SP.M15.2024.FE.ZS",
    },
    {
        "label": "Women who were first married by age 18 (% of women ages 20-24)",
        "value": "SP.M18.2024.FE.ZS",
    },
    {
        "label": "Teenage mothers (% of women ages 15-19 who have had children or are currently pregnant)",
        "value": "SP.MTR.1519.ZS",
    },
    {
        "label": "Population ages 00-04, female (% of female population)",
        "value": "SP.POP.0004.FE.5Y",
    },
    {
        "label": "Population ages 00-04, male (% of male population)",
        "value": "SP.POP.0004.MA.5Y",
    },
    {
        "label": "Population ages 0-14, female",
        "value": "SP.POP.0014.FE.IN",
    },
    {
        "label": "Population ages 0-14, female (% of female population)",
        "value": "SP.POP.0014.FE.ZS",
    },
    {
        "label": "Population ages 0-14, male",
        "value": "SP.POP.0014.MA.IN",
    },
    {
        "label": "Population ages 0-14, male (% of male population)",
        "value": "SP.POP.0014.MA.ZS",
    },
    {"label": "Population ages 0-14, total", "value": "SP.POP.0014.TO"},
    {
        "label": "Population ages 0-14 (% of total population)",
        "value": "SP.POP.0014.TO.ZS",
    },
    {
        "label": "Population ages 05-09, female (% of female population)",
        "value": "SP.POP.0509.FE.5Y",
    },
    {
        "label": "Population ages 05-09, male (% of male population)",
        "value": "SP.POP.0509.MA.5Y",
    },
    {
        "label": "Population ages 10-14, female (% of female population)",
        "value": "SP.POP.1014.FE.5Y",
    },
    {
        "label": "Population ages 10-14, male (% of male population)",
        "value": "SP.POP.1014.MA.5Y",
    },
    {
        "label": "Population ages 15-19, female (% of female population)",
        "value": "SP.POP.1519.FE.5Y",
    },
    {
        "label": "Population ages 15-19, male (% of male population)",
        "value": "SP.POP.1519.MA.5Y",
    },
    {
        "label": "Population ages 15-64, female",
        "value": "SP.POP.1564.FE.IN",
    },
    {
        "label": "Population ages 15-64, female (% of female population)",
        "value": "SP.POP.1564.FE.ZS",
    },
    {
        "label": "Population ages 15-64, male",
        "value": "SP.POP.1564.MA.IN",
    },
    {
        "label": "Population ages 15-64, male (% of male population)",
        "value": "SP.POP.1564.MA.ZS",
    },
    {
        "label": "Population ages 15-64, total",
        "value": "SP.POP.1564.TO",
    },
    {
        "label": "Population ages 15-64 (% of total population)",
        "value": "SP.POP.1564.TO.ZS",
    },
    {
        "label": "Population ages 20-24, female (% of female population)",
        "value": "SP.POP.2024.FE.5Y",
    },
    {
        "label": "Population ages 20-24, male (% of male population)",
        "value": "SP.POP.2024.MA.5Y",
    },
    {
        "label": "Population ages 25-29, female (% of female population)",
        "value": "SP.POP.2529.FE.5Y",
    },
    {
        "label": "Population ages 25-29, male (% of male population)",
        "value": "SP.POP.2529.MA.5Y",
    },
    {
        "label": "Population ages 30-34, female (% of female population)",
        "value": "SP.POP.3034.FE.5Y",
    },
    {
        "label": "Population ages 30-34, male (% of male population)",
        "value": "SP.POP.3034.MA.5Y",
    },
    {
        "label": "Population ages 35-39, female (% of female population)",
        "value": "SP.POP.3539.FE.5Y",
    },
    {
        "label": "Population ages 35-39, male (% of male population)",
        "value": "SP.POP.3539.MA.5Y",
    },
    {
        "label": "Population ages 40-44, female (% of female population)",
        "value": "SP.POP.4044.FE.5Y",
    },
    {
        "label": "Population ages 40-44, male (% of male population)",
        "value": "SP.POP.4044.MA.5Y",
    },
    {
        "label": "Population ages 45-49, female (% of female population)",
        "value": "SP.POP.4549.FE.5Y",
    },
    {
        "label": "Population ages 45-49, male (% of male population)",
        "value": "SP.POP.4549.MA.5Y",
    },
    {
        "label": "Population ages 50-54, female (% of female population)",
        "value": "SP.POP.5054.FE.5Y",
    },
    {
        "label": "Population ages 50-54, male (% of male population)",
        "value": "SP.POP.5054.MA.5Y",
    },
    {
        "label": "Population ages 55-59, female (% of female population)",
        "value": "SP.POP.5559.FE.5Y",
    },
    {
        "label": "Population ages 55-59, male (% of male population)",
        "value": "SP.POP.5559.MA.5Y",
    },
    {
        "label": "Population ages 60-64, female (% of female population)",
        "value": "SP.POP.6064.FE.5Y",
    },
    {
        "label": "Population ages 60-64, male (% of male population)",
        "value": "SP.POP.6064.MA.5Y",
    },
    {
        "label": "Population ages 65-69, female (% of female population)",
        "value": "SP.POP.6569.FE.5Y",
    },
    {
        "label": "Population ages 65-69, male (% of male population)",
        "value": "SP.POP.6569.MA.5Y",
    },
    {
        "label": "Population ages 65 and above, female",
        "value": "SP.POP.65UP.FE.IN",
    },
    {
        "label": "Population ages 65 and above, female (% of female population)",
        "value": "SP.POP.65UP.FE.ZS",
    },
    {
        "label": "Population ages 65 and above, male",
        "value": "SP.POP.65UP.MA.IN",
    },
    {
        "label": "Population ages 65 and above, male (% of male population)",
        "value": "SP.POP.65UP.MA.ZS",
    },
    {
        "label": "Population ages 65 and above, total",
        "value": "SP.POP.65UP.TO",
    },
    {
        "label": "Population ages 65 and above (% of total population)",
        "value": "SP.POP.65UP.TO.ZS",
    },
    {
        "label": "Population ages 70-74, female (% of female population)",
        "value": "SP.POP.7074.FE.5Y",
    },
    {
        "label": "Population ages 70-74, male (% of male population)",
        "value": "SP.POP.7074.MA.5Y",
    },
    {
        "label": "Population ages 75-79, female (% of female population)",
        "value": "SP.POP.7579.FE.5Y",
    },
    {
        "label": "Population ages 75-79, male (% of male population)",
        "value": "SP.POP.7579.MA.5Y",
    },
    {
        "label": "Population ages 80 and above, female (% of female population)",
        "value": "SP.POP.80UP.FE.5Y",
    },
    {
        "label": "Population ages 80 and above, male (% of male population)",
        "value": "SP.POP.80UP.MA.5Y",
    },
    {
        "label": "Sex ratio at birth (male births per female births)",
        "value": "SP.POP.BRTH.MF",
    },
    {
        "label": "Age dependency ratio (% of working-age population)",
        "value": "SP.POP.DPND",
    },
    {
        "label": "Age dependency ratio, old (% of working-age population)",
        "value": "SP.POP.DPND.OL",
    },
    {
        "label": "Age dependency ratio, young (% of working-age population)",
        "value": "SP.POP.DPND.YG",
    },
    {"label": "Population growth (annual %)", "value": "SP.POP.GROW"},
    {
        "label": "Researchers in R&D (per million people)",
        "value": "SP.POP.SCIE.RD.P6",
    },
    {
        "label": "Technicians in R&D (per million people)",
        "value": "SP.POP.TECH.RD.P6",
    },
    {"label": "Population, total", "value": "SP.POP.TOTL"},
    {"label": "Population, female", "value": "SP.POP.TOTL.FE.IN"},
    {
        "label": "Population, female (% of total population)",
        "value": "SP.POP.TOTL.FE.ZS",
    },
    {"label": "Population, male", "value": "SP.POP.TOTL.MA.IN"},
    {
        "label": "Population, male (% of total population)",
        "value": "SP.POP.TOTL.MA.ZS",
    },
    {
        "label": "Completeness of birth registration, female (%)",
        "value": "SP.REG.BRTH.FE.ZS",
    },
    {
        "label": "Completeness of birth registration, male (%)",
        "value": "SP.REG.BRTH.MA.ZS",
    },
    {
        "label": "Completeness of birth registration, rural (%)",
        "value": "SP.REG.BRTH.RU.ZS",
    },
    {
        "label": "Completeness of birth registration, urban (%)",
        "value": "SP.REG.BRTH.UR.ZS",
    },
    {
        "label": "Completeness of birth registration (%)",
        "value": "SP.REG.BRTH.ZS",
    },
    {
        "label": "Completeness of death registration with cause-of-death information (%)",
        "value": "SP.REG.DTHS.ZS",
    },
    {"label": "Rural population", "value": "SP.RUR.TOTL"},
    {
        "label": "Rural population growth (annual %)",
        "value": "SP.RUR.TOTL.ZG",
    },
    {
        "label": "Rural population (% of total population)",
        "value": "SP.RUR.TOTL.ZS",
    },
    {
        "label": "Urban population growth (annual %)",
        "value": "SP.URB.GROW",
    },
    {"label": "Urban population", "value": "SP.URB.TOTL"},
    {
        "label": "Urban population (% of total population)",
        "value": "SP.URB.TOTL.IN.ZS",
    },
    {
        "label": "Unmet need for contraception (% of married women ages 15-49)",
        "value": "SP.UWT.TFRT",
    },
    {
        "label": "International tourism, number of arrivals",
        "value": "ST.INT.ARVL",
    },
    {
        "label": "International tourism, number of departures",
        "value": "ST.INT.DPRT",
    },
    {
        "label": "International tourism, receipts (current US$)",
        "value": "ST.INT.RCPT.CD",
    },
    {
        "label": "International tourism, receipts (% of total exports)",
        "value": "ST.INT.RCPT.XP.ZS",
    },
    {
        "label": "International tourism, receipts for passenger transport items (current US$)",
        "value": "ST.INT.TRNR.CD",
    },
    {
        "label": "International tourism, expenditures for passenger transport items (current US$)",
        "value": "ST.INT.TRNX.CD",
    },
    {
        "label": "International tourism, receipts for travel items (current US$)",
        "value": "ST.INT.TVLR.CD",
    },
    {
        "label": "International tourism, expenditures for travel items (current US$)",
        "value": "ST.INT.TVLX.CD",
    },
    {
        "label": "International tourism, expenditures (current US$)",
        "value": "ST.INT.XPND.CD",
    },
    {
        "label": "International tourism, expenditures (% of total imports)",
        "value": "ST.INT.XPND.MP.ZS",
    },
    {
        "label": "Merchandise trade (% of GDP)",
        "value": "TG.VAL.TOTL.GD.ZS",
    },
    {
        "label": "Import volume index (2015 = 100)",
        "value": "TM.QTY.MRCH.XD.WD",
    },
    {
        "label": "Binding coverage, manufactured products (%)",
        "value": "TM.TAX.MANF.BC.ZS",
    },
    {
        "label": "Bound rate, simple mean, manufactured products (%)",
        "value": "TM.TAX.MANF.BR.ZS",
    },
    {
        "label": "Share of tariff lines with international peaks, manufactured products (%)",
        "value": "TM.TAX.MANF.IP.ZS",
    },
    {
        "label": "Tariff rate, applied, simple mean, manufactured products (%)",
        "value": "TM.TAX.MANF.SM.AR.ZS",
    },
    {
        "label": "Tariff rate, most favored nation, simple mean, manufactured products (%)",
        "value": "TM.TAX.MANF.SM.FN.ZS",
    },
    {
        "label": "Share of tariff lines with specific rates, manufactured products (%)",
        "value": "TM.TAX.MANF.SR.ZS",
    },
    {
        "label": "Tariff rate, applied, weighted mean, manufactured products (%)",
        "value": "TM.TAX.MANF.WM.AR.ZS",
    },
    {
        "label": "Tariff rate, most favored nation, weighted mean, manufactured products (%)",
        "value": "TM.TAX.MANF.WM.FN.ZS",
    },
    {
        "label": "Binding coverage, all products (%)",
        "value": "TM.TAX.MRCH.BC.ZS",
    },
    {
        "label": "Bound rate, simple mean, all products (%)",
        "value": "TM.TAX.MRCH.BR.ZS",
    },
    {
        "label": "Share of tariff lines with international peaks, all products (%)",
        "value": "TM.TAX.MRCH.IP.ZS",
    },
    {
        "label": "Tariff rate, applied, simple mean, all products (%)",
        "value": "TM.TAX.MRCH.SM.AR.ZS",
    },
    {
        "label": "Tariff rate, most favored nation, simple mean, all products (%)",
        "value": "TM.TAX.MRCH.SM.FN.ZS",
    },
    {
        "label": "Share of tariff lines with specific rates, all products (%)",
        "value": "TM.TAX.MRCH.SR.ZS",
    },
    {
        "label": "Tariff rate, applied, weighted mean, all products (%)",
        "value": "TM.TAX.MRCH.WM.AR.ZS",
    },
    {
        "label": "Tariff rate, most favored nation, weighted mean, all products (%)",
        "value": "TM.TAX.MRCH.WM.FN.ZS",
    },
    {
        "label": "Binding coverage, primary products (%)",
        "value": "TM.TAX.TCOM.BC.ZS",
    },
    {
        "label": "Bound rate, simple mean, primary products (%)",
        "value": "TM.TAX.TCOM.BR.ZS",
    },
    {
        "label": "Share of tariff lines with international peaks, primary products (%)",
        "value": "TM.TAX.TCOM.IP.ZS",
    },
    {
        "label": "Tariff rate, applied, simple mean, primary products (%)",
        "value": "TM.TAX.TCOM.SM.AR.ZS",
    },
    {
        "label": "Tariff rate, most favored nation, simple mean, primary products (%)",
        "value": "TM.TAX.TCOM.SM.FN.ZS",
    },
    {
        "label": "Share of tariff lines with specific rates, primary products (%)",
        "value": "TM.TAX.TCOM.SR.ZS",
    },
    {
        "label": "Tariff rate, applied, weighted mean, primary products (%)",
        "value": "TM.TAX.TCOM.WM.AR.ZS",
    },
    {
        "label": "Tariff rate, most favored nation, weighted mean, primary products (%)",
        "value": "TM.TAX.TCOM.WM.FN.ZS",
    },
    {
        "label": "Import unit value index (2015 = 100)",
        "value": "TM.UVI.MRCH.XD.WD",
    },
    {
        "label": "Agricultural raw materials imports (% of merchandise imports)",
        "value": "TM.VAL.AGRI.ZS.UN",
    },
    {
        "label": "Food imports (% of merchandise imports)",
        "value": "TM.VAL.FOOD.ZS.UN",
    },
    {
        "label": "Fuel imports (% of merchandise imports)",
        "value": "TM.VAL.FUEL.ZS.UN",
    },
    {
        "label": "ICT goods imports (% total goods imports)",
        "value": "TM.VAL.ICTG.ZS.UN",
    },
    {
        "label": "Insurance and financial services (% of commercial service imports)",
        "value": "TM.VAL.INSF.ZS.WT",
    },
    {
        "label": "Manufactures imports (% of merchandise imports)",
        "value": "TM.VAL.MANF.ZS.UN",
    },
    {
        "label": "Ores and metals imports (% of merchandise imports)",
        "value": "TM.VAL.MMTL.ZS.UN",
    },
    {
        "label": "Merchandise imports from economies in the Arab World (% of total merchandise imports)",
        "value": "TM.VAL.MRCH.AL.ZS",
    },
    {
        "label": "Merchandise imports (current US$)",
        "value": "TM.VAL.MRCH.CD.WT",
    },
    {
        "label": "Merchandise imports from high-income economies (% of total merchandise imports)",
        "value": "TM.VAL.MRCH.HI.ZS",
    },
    {
        "label": "Merchandise imports from low- and middle-income economies outside region (% of total merchandise imports)",
        "value": "TM.VAL.MRCH.OR.ZS",
    },
    {
        "label": "Merchandise imports from low- and middle-income economies in East Asia & Pacific (% of total merchandise imports)",
        "value": "TM.VAL.MRCH.R1.ZS",
    },
    {
        "label": "Merchandise imports from low- and middle-income economies in Europe & Central Asia (% of total merchandise imports)",
        "value": "TM.VAL.MRCH.R2.ZS",
    },
    {
        "label": "Merchandise imports from low- and middle-income economies in Latin America & the Caribbean (% of total merchandise imports)",
        "value": "TM.VAL.MRCH.R3.ZS",
    },
    {
        "label": "Merchandise imports from low- and middle-income economies in Middle East & North Africa (% of total merchandise imports)",
        "value": "TM.VAL.MRCH.R4.ZS",
    },
    {
        "label": "Merchandise imports from low- and middle-income economies in South Asia (% of total merchandise imports)",
        "value": "TM.VAL.MRCH.R5.ZS",
    },
    {
        "label": "Merchandise imports from low- and middle-income economies in Sub-Saharan Africa (% of total merchandise imports)",
        "value": "TM.VAL.MRCH.R6.ZS",
    },
    {
        "label": "Merchandise imports by the reporting economy, residual (% of total merchandise imports)",
        "value": "TM.VAL.MRCH.RS.ZS",
    },
    {
        "label": "Merchandise imports by the reporting economy (current US$)",
        "value": "TM.VAL.MRCH.WL.CD",
    },
    {
        "label": "Merchandise imports from low- and middle-income economies within region (% of total merchandise imports)",
        "value": "TM.VAL.MRCH.WR.ZS",
    },
    {
        "label": "Import value index (2015 = 100)",
        "value": "TM.VAL.MRCH.XD.WD",
    },
    {
        "label": "Computer, communications and other services (% of commercial service imports)",
        "value": "TM.VAL.OTHR.ZS.WT",
    },
    {
        "label": "Commercial service imports (current US$)",
        "value": "TM.VAL.SERV.CD.WT",
    },
    {
        "label": "Transport services (% of commercial service imports)",
        "value": "TM.VAL.TRAN.ZS.WT",
    },
    {
        "label": "Travel services (% of commercial service imports)",
        "value": "TM.VAL.TRVL.ZS.WT",
    },
    {
        "label": "Net barter terms of trade index (2015 = 100)",
        "value": "TT.PRI.MRCH.XD.WD",
    },
    {
        "label": "Medium and high-tech exports (% manufactured exports)",
        "value": "TX.MNF.TECH.ZS.UN",
    },
    {
        "label": "Export volume index (2015 = 100)",
        "value": "TX.QTY.MRCH.XD.WD",
    },
    {
        "label": "Export unit value index (2015 = 100)",
        "value": "TX.UVI.MRCH.XD.WD",
    },
    {
        "label": "Agricultural raw materials exports (% of merchandise exports)",
        "value": "TX.VAL.AGRI.ZS.UN",
    },
    {
        "label": "Food exports (% of merchandise exports)",
        "value": "TX.VAL.FOOD.ZS.UN",
    },
    {
        "label": "Fuel exports (% of merchandise exports)",
        "value": "TX.VAL.FUEL.ZS.UN",
    },
    {
        "label": "ICT goods exports (% of total goods exports)",
        "value": "TX.VAL.ICTG.ZS.UN",
    },
    {
        "label": "Insurance and financial services (% of commercial service exports)",
        "value": "TX.VAL.INSF.ZS.WT",
    },
    {
        "label": "Manufactures exports (% of merchandise exports)",
        "value": "TX.VAL.MANF.ZS.UN",
    },
    {
        "label": "Ores and metals exports (% of merchandise exports)",
        "value": "TX.VAL.MMTL.ZS.UN",
    },
    {
        "label": "Merchandise exports to economies in the Arab World (% of total merchandise exports)",
        "value": "TX.VAL.MRCH.AL.ZS",
    },
    {
        "label": "Merchandise exports (current US$)",
        "value": "TX.VAL.MRCH.CD.WT",
    },
    {
        "label": "Merchandise exports to high-income economies (% of total merchandise exports)",
        "value": "TX.VAL.MRCH.HI.ZS",
    },
    {
        "label": "Merchandise exports to low- and middle-income economies outside region (% of total merchandise exports)",
        "value": "TX.VAL.MRCH.OR.ZS",
    },
    {
        "label": "Merchandise exports to low- and middle-income economies in East Asia & Pacific (% of total merchandise exports)",
        "value": "TX.VAL.MRCH.R1.ZS",
    },
    {
        "label": "Merchandise exports to low- and middle-income economies in Europe & Central Asia (% of total merchandise exports)",
        "value": "TX.VAL.MRCH.R2.ZS",
    },
    {
        "label": "Merchandise exports to low- and middle-income economies in Latin America & the Caribbean (% of total merchandise exports)",
        "value": "TX.VAL.MRCH.R3.ZS",
    },
    {
        "label": "Merchandise exports to low- and middle-income economies in Middle East & North Africa (% of total merchandise exports)",
        "value": "TX.VAL.MRCH.R4.ZS",
    },
    {
        "label": "Merchandise exports to low- and middle-income economies in South Asia (% of total merchandise exports)",
        "value": "TX.VAL.MRCH.R5.ZS",
    },
    {
        "label": "Merchandise exports to low- and middle-income economies in Sub-Saharan Africa (% of total merchandise exports)",
        "value": "TX.VAL.MRCH.R6.ZS",
    },
    {
        "label": "Merchandise exports by the reporting economy, residual (% of total merchandise exports)",
        "value": "TX.VAL.MRCH.RS.ZS",
    },
    {
        "label": "Merchandise exports by the reporting economy (current US$)",
        "value": "TX.VAL.MRCH.WL.CD",
    },
    {
        "label": "Merchandise exports to low- and middle-income economies within region (% of total merchandise exports)",
        "value": "TX.VAL.MRCH.WR.ZS",
    },
    {
        "label": "Export value index (2015 = 100)",
        "value": "TX.VAL.MRCH.XD.WD",
    },
    {
        "label": "Computer, communications and other services (% of commercial service exports)",
        "value": "TX.VAL.OTHR.ZS.WT",
    },
    {
        "label": "Commercial service exports (current US$)",
        "value": "TX.VAL.SERV.CD.WT",
    },
    {
        "label": "High-technology exports (current US$)",
        "value": "TX.VAL.TECH.CD",
    },
    {
        "label": "High-technology exports (% of manufactured exports)",
        "value": "TX.VAL.TECH.MF.ZS",
    },
    {
        "label": "Transport services (% of commercial service exports)",
        "value": "TX.VAL.TRAN.ZS.WT",
    },
    {
        "label": "Travel services (% of commercial service exports)",
        "value": "TX.VAL.TRVL.ZS.WT",
    },
    {"label": "Voice and Accountability: Estimate", "value": "VA.EST"},
    {
        "label": "Voice and Accountability: Number of Sources",
        "value": "VA.NO.SRC",
    },
    {
        "label": "Voice and Accountability: Percentile Rank",
        "value": "VA.PER.RNK",
    },
    {
        "label": "Voice and Accountability: Percentile Rank, Lower Bound of 90% Confidence Interval",
        "value": "VA.PER.RNK.LOWER",
    },
    {
        "label": "Voice and Accountability: Percentile Rank, Upper Bound of 90% Confidence Interval",
        "value": "VA.PER.RNK.UPPER",
    },
    {
        "label": "Voice and Accountability: Standard Error",
        "value": "VA.STD.ERR",
    },
    {
        "label": "Battle-related deaths (number of people)",
        "value": "VC.BTL.DETH",
    },
    {
        "label": "Internally displaced persons, new displacement associated with conflict and violence (number of cases)",
        "value": "VC.IDP.NWCV",
    },
    {
        "label": "Internally displaced persons, new displacement associated with disasters (number of cases)",
        "value": "VC.IDP.NWDS",
    },
    {
        "label": "Internally displaced persons, total displaced by conflict and violence (number of people)",
        "value": "VC.IDP.TOCV",
    },
    {
        "label": "Intentional homicides, female (per 100,000 female)",
        "value": "VC.IHR.PSRC.FE.P5",
    },
    {
        "label": "Intentional homicides, male (per 100,000 male)",
        "value": "VC.IHR.PSRC.MA.P5",
    },
    {
        "label": "Intentional homicides (per 100,000 people)",
        "value": "VC.IHR.PSRC.P5",
    },
]

country1 = html.Div(
    [
        dbc.Label("COUNTRY", html_for="country"),
        dcc.Dropdown(
            id="country-id1",
            options=country_list,
            multi=True,
            placeholder="Select a county or region",
            searchable=True,
            clearable=True,
            maxHeight=400,
            optionHeight=60,
        ),
    ],
    className="mt-2",
)

indicator1 = html.Div(
    [
        dbc.Label("INDICATOR", html_for="n_bins"),
        dcc.Dropdown(
            id="indicator-id1",
            options=indicator_list,
            multi=False,
            placeholder="Select an Indicator",
            searchable=True,
            clearable=True,
            maxHeight=400,
            optionHeight=60,
        ),
    ],
    className="mt-2",
)

control_panel1 = dbc.Card(
    dbc.CardBody(
        [country1, indicator1],
        className="control-panel",
    ),
)

graph1 = (
    dbc.Card(
        [html.Div(id="error_msg1", className="text-danger"), 
        dcc.Graph(id="graph-id1", config= {'displaylogo': False}, 
        className='graph-container')],
        className="graph-card"
    )
)


country2 = html.Div(
    [
        dbc.Label("COUNTRY", html_for="country"),
        dcc.Dropdown(
            id="country-id2",
            options=country_list,
            multi=True,
            placeholder="Select a county or region",
            searchable=True,
            clearable=True,
            maxHeight=400,
            optionHeight=60,
        ),
    ],
    className="mt-2",
)

indicator2 = html.Div(
    [
        dbc.Label("INDICATOR", html_for="n_bins"),
        dcc.Dropdown(
            id="indicator-id2",
            options=indicator_list,
            multi=False,
            placeholder="Select an Indicator",
            searchable=True,
            clearable=True,
            maxHeight=400,
            optionHeight=60,
        ),
    ],
    className="mt-2",
)

control_panel2 = dbc.Card(
    dbc.CardBody(
        [country2, indicator2],
        className="control-panel",
    ),
)

graph2 = dbc.Card(
    [html.Div(id="error_msg2", className="text-danger"), 
     dcc.Graph(id="graph-id2", config= {'displaylogo': False}, 
    className='graph-container')], 
    className="graph-card"
    
)

country3 = html.Div(
    [
        dbc.Label("COUNTRY", html_for="country"),
        dcc.Dropdown(
            id="country-id3",
            options=country_list,
            multi=True,
            placeholder="Select a county or region",
            searchable=True,
            clearable=True,
            maxHeight=400,
            optionHeight=60,
        ),
    ],
    className="mt-2",
)

indicator3 = html.Div(
    [
        dbc.Label("INDICATOR", html_for="n_bins"),
        dcc.Dropdown(
            id="indicator-id3",
            options=indicator_list,
            multi=False,
            placeholder="Select an Indicator",
            searchable=True,
            clearable=True,
            maxHeight=400,
            optionHeight=60,
        ),
    ],
    className="mt-2",
)

control_panel3 = dbc.Card(
    dbc.CardBody(
        [country3, indicator3],
        className="control-panel",
    ),
)

graph3 = dbc.Card(
    [html.Div(id="error_msg3", className="text-danger"), dcc.Graph(id="graph-id3", config= {'displaylogo': False}, className='graph-container')],
    className="graph-card"
)

country4 = html.Div(
    [
        dbc.Label("COUNTRY", html_for="country"),
        dcc.Dropdown(
            id="country-id4",
            options=country_list,
            multi=True,
            placeholder="Select a county or region",
            searchable=True,
            clearable=True,
            maxHeight=400,
            optionHeight=60,
        ),
    ],
    className="mt-2",
)

indicator4 = html.Div(
    [
        dbc.Label("INDICATOR", html_for="n_bins"),
        dcc.Dropdown(
            id="indicator-id4",
            options=indicator_list,
            multi=False,
            placeholder="Select an Indicator",
            searchable=True,
            clearable=True,
            maxHeight=400,
            optionHeight=60,
        ),
    ],
    className="mt-2",
)

control_panel4 = dbc.Card(
    dbc.CardBody(
        [country4, indicator4],
        className="control-panel",
    ),
)

graph4 = dbc.Card(
    [html.Div(id="error_msg4", className="text-danger"), dcc.Graph(id="graph-id4", config= {'displaylogo': False}, className='graph-container')],
    className="graph-card"
)

stack1 = dbc.Stack(
    [
        html.Div(control_panel1),
        html.Div(control_panel2),
    ],
    gap=4,
)

stack2 = dbc.Stack(
    [
        html.Div(control_panel3),
        html.Div(control_panel4),
    ],
    gap=4,
    
)


accordion = html.Div(
    dbc.Accordion(
        [
            dbc.AccordionItem(
                html.Div(
                    [
                        html.P(
                            "You can choose multiply countries and one indicator from the vast world bank database per graph."
                        ),
                        html.P(
                            "Use the search function to select countries and indicators."
                        ),
                        html.P(
                            "Graphs are interactive: you can download them as png file or click the legend items to toggle countries."
                        ),
                        html.P(
                            "Sometimes you will encounter gaps in the graphs, then the world bank has no data for this time, indicator, country or combination of them."
                        ),
                        html.P(
                            "If your graph is a straight line the indciator is probably a single number (constant) that doesn't change over the years."
                        ),
                    ]
                ),
                title="Information",
            ),
            dbc.AccordionItem(control_panel1, title="Graph 1   (top-left)"),
            dbc.AccordionItem(control_panel2, title="Graph 2   (top-right)"),
            dbc.AccordionItem(control_panel3, title="Graph 3   (bottom-left)"),
            dbc.AccordionItem(control_panel4, title="Graph 4   (bottom-right)"),
        ],
        start_collapsed=True,
    ),
)


offcanvas = html.Div(
    [
        dbc.Button("Choose your Data", id="open-offcanvas", n_clicks=0),
        dbc.Offcanvas(
            [accordion],
            id="offcanvas",
            style={"maxHeight": "100vh", "overflowY": "auto"},
            title="Choose what you want to plot.",
            placement="end",
            is_open=False,
            scrollable=True,
        ), 
    ], 
)


logo_base64 = base64.b64encode(open("./img/logo_.png", "rb").read()).decode("ascii")


navbar = dbc.Nav(
    [
        html.A(
            html.Img(src="data:image/png;base64,{}".format(logo_base64), id='logo'),
            href="https://macozu.github.io/index.html",  
            target="_blank",  
        ),
        dbc.NavItem(
            html.H2("World Bank Commander", id="title"), class_name="text-center pt-2 mx-1"
        ),
        dbc.NavItem(offcanvas, class_name="text-end mx-2", id="offcanvas-nav"),
    ],
    class_name="navbar",
)


app.layout = dbc.Container(
    [
        navbar,
        dbc.Row(
            [
                dbc.Col(graph1, xs=12, sm=12, md=6),
                dbc.Col(graph2, xs=12, sm=12, md=6),
            ],
            className="px-2 py-2",
        ),
        dbc.Row(
            [
                dbc.Col(graph3, xs=12, sm=12, md=6),
                dbc.Col(graph4, xs=12, sm=12, md=6),
            ],
            className="p-2",
        ),
    ],
    fluid=True,
    style={'height': '100vh'}
)


@app.callback(
    Output("offcanvas", "is_open"),
    Input("open-offcanvas", "n_clicks"),
    [State("offcanvas", "is_open")],
)
def toggle_offcanvas(n1, is_open):
    if n1:
        return not is_open
    return is_open


# callback for graph 1
@callback(
    Output("graph-id1", "figure"),
    Input("country-id1", "value"), 
    Input("indicator-id1", "value")
)
def make_graph1(indicator_code, country_list):
    if country_list is None or len(country_list) == 0 or indicator_code is None:
        return {}
    else:
        return utils.plot(country_list, indicator_code)


# callback for graph 2
@callback(
    Output("graph-id2", "figure"),
    Input("country-id2", "value"), Input("indicator-id2", "value")
)
def make_graph2(indicator_code, country_list):
    if country_list is None or len(country_list) == 0 or indicator_code is None:
        return {}
    else:
        return utils.plot(country_list, indicator_code)


# callback for graph 3
@callback(
    Output("graph-id3", "figure"),
    Input("country-id3", "value"), 
    Input("indicator-id3", "value")
)
def make_graph2(indicator_code, country_list):
    if country_list is None or len(country_list) == 0 or indicator_code is None:
        return {}
    else:
        return utils.plot(country_list, indicator_code)


# callback for graph 4
@callback(
    Output("graph-id4", "figure"),
    Input("country-id4", "value"), 
    Input("indicator-id4", "value")
)
def make_graph2(indicator_code, country_list):
    if country_list is None or len(country_list) == 0 or indicator_code is None:
        return {}
    else:
        return utils.plot(country_list, indicator_code)


if __name__ == "__main__":
    #  app.run_server(debug=True)
     app.run_server(host='127.0.0.1', port=8050, debug=True)
