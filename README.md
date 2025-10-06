# DS223_HW1  

# Bass Model Analysis  

This project examines worldwide consumer spending on smart home technologies and applies the **Bass Diffusion Model** to explore adoption patterns and forecast future trends.  

## 📂 Project Contents  

**data/**  
- `statistic_id693303_consumer_smart_home_spending_worldwide_2015_2025.xlsx` – Dataset with global smart home spending from 2015–2025.  

**images/**  
- `bass_model_adopters.png` – Graph showing cumulative adopters over time.  
- `bass_model_plot.png` – Graph showing Bass Model fit vs. actual data.  

**report/**  
- `DS223_HW1_Zhora_Poghosyan.pdf` – Final project report.  
- `report.pdf` – Supporting documentation.  

**scripts/**  
- `helper_functions.py` – Data processing and model calculation functions.  

Other files:  
- `venv/` – Virtual environment folder (excluded from version control).  
- `README.md` – This file.  
- `requirements.txt` – Python dependencies to run the analysis.  
- `DS223_MA_Bass_modelHW_Zhora_Poghosyan.ipynb` – Jupyter Notebook containing the implementation.  

---

## ⚙️ Setup  

Create a virtual environment and install the requirements:  

```sh
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
