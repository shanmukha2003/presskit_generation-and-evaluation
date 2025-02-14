# 📰 AI-Powered Press Kit Generation & Evaluation  

This project presents an AI-driven system for generating and evaluating press kits with minimal manual effort. It leverages a LLaMA 3 model, downloaded from LM Studio, to produce professional-quality content based on user inputs. The system also provides actionable feedback to improve the generated content, ensuring that the final press kit meets the desired quality standards.  

---

## 🛠️ Problem Statement  

Creating press kits manually is time-consuming, labor-intensive, and often inconsistent. Traditional processes require domain experts to gather information, craft narratives, and refine content repeatedly. The goal of this project is to build an AI-assisted solution that:  

- **Simplifies Press Kit Creation**: Users provide key inputs, and the system generates draft content automatically.  
- **Ensures Content Quality**: Evaluates generated content and suggests improvements.  
- **Improves Efficiency**: Reduces the time and effort required for content creation.  
- **Allows Dynamic Adjustments**: Users can modify content priorities and model parameters if unsatisfied with the output.  

---

## ⚙️ Core Functionality  

The system follows a structured pipeline:  

1. **User Input Collection**:  
   - Users provide relevant details such as event information, target audience, and key messages.  

2. **Priority Adjustment**:  
   - Users can modify the relative importance of different content elements.  

3. **Press Kit Generation**:  
   - The LLaMA 3 model generates draft content based on the provided inputs and adjusted priorities.  

4. **Content Evaluation**:  
   - The system analyzes the generated text, providing feedback on readability, clarity, and relevance.  

5. **Model Adjustments**:  
   - If needed, users can adjust model settings for better results.  

---

## 🧠 AI Model Details  

- **Model Used**: LLaMA 3 (downloaded from LM Studio)  
- **Task**: Text generation for press kit content creation  
  

---


## 🚀 Installation & Usage  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/shanmukha2003/presskit_generation-and-evaluation.git  
cd presskit_generation-and-evaluation  
2️⃣ Set Up Environment

pip install -r requirements.txt  
3️⃣ Run the Application

python llama_model.py



result screen shots :

https://drive.google.com/drive/folders/1uzAXpd6UHKlJBU0jtboTVmLdR_paoZ8O?usp=sharing

