# DS223_HW1  

# Bass Model Analysis  

This project analyzes how global consumer spending on smart home technologies has evolved from 2015 to 2025 and uses the **Bass Diffusion Model** to understand and forecast the adoption behavior of such technologies over time.

The **Bass model** is a widely used tool in marketing and innovation research. It helps us estimate how many people will adopt a new product based on two types of adopters:  
- **Innovators** who adopt early based on external influence (parameter **p**)  
- **Imitators** who adopt based on interactions with others (parameter **q**)  

By fitting the model to real consumer spending data, we can predict future trends and visualize the speed and saturation of adoption in the market.

---
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
