# 🌍 World Bank Commander (WBC)
WBC is a dashboard of world bank indicators displayed on a 2x2 grid.
You can reach WBC here: https://data.worldbank.org/indicator

Simplicity was my goal. I wanted different indicators of various countries shown
in an overview to explore relations not normally considered. Something like illegal mining and drug trade in neighbouring countries, for example.

The indicators are fetched using the [wbgapi](https://pypi.org/project/wbgapi/) python library.
Graphs are build with [plotly.graph_objects](https://plotly.com/python/).

I've considered rebuilding it with html and D3 charts to address long indicator names, legends and spacing.

# Install and utilize
You can take this project as a base for your own dashboard.
- clone the repo `git clone git@github.com:MaCoZu/WB-Commander.git`
- navigate in the repo and create a new virtual environment (venv)
    - there are many options for virtual environments I use micromamba and my commaands are 
    - `micromamaba create -n env_name -f requirements.txt -c conda-forge`
- once installed and in the right folder app.py ran be run with `python app.py`
- the dashboard should run on a specified server adress or better still it opens in a browser tab, if you've a Server **Extension like Five Server** installed.


# 🤝 Contributing
Feel free to open issues or submit pull requests if you find any bugs or have suggestions for improvements.

# 📝 License
This project is licensed under the MIT License - see the LICENSE file for details.